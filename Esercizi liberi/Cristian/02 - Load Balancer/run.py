# Script utlizzato per laciare i modelli
# Autore: Cristian Di Pietrantonio

from pymodelica import compile_fmu
from pyfmi import load_fmu
import sys
import os

model_name="ClosedSystem"

#sono caricati tutti i file ".mo" nella cartella
model_files = [f for f in os.listdir(".") if ".mo" in f]

model_comp = compile_fmu(model_name, model_files)
model = load_fmu(model_comp)

res = model.simulate(options={'ncp':1000})



