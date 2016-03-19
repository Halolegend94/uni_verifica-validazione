# Script utlizzato per laciare i modelli
# Autore: Cristian Di Pietrantonio

from pymodelica import compile_fmu
from pyfmi import load_fmu
import sys
import os

model_name="FullAdder"

#sono caricati tutti i file ".mo" nella cartella
model_files = [f for f in os.listdir(".") if ".mo" in f]

model_comp = compile_fmu(model_name, model_files)
model = load_fmu(model_comp)

#Simulazione: simuliamo tante volte quante sono le entries in params

for x1 in range(0, 2):
	for x2 in range(0, 2):
		for c in range(0, 2):
			model.set('x1', x1)
			model.set('x2', x2)
			model.set('c', c) 
			res = model.simulate(options={'ncp':1000})
			print("x1: " + `x1` + ", x2: " + `x2` +", c: " + `c` + " -->" +
				" y: " + `model.get('y')[0]` + ", co: " + `model.get('co')[0]`)
			model.reset()



