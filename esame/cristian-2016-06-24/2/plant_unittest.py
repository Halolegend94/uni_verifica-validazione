# Script utlizzato per laciare i modelli
# Autore: Cristian Di Pietrantonio

# import necessari
from pymodelica import compile_fmu
from pyfmi import load_fmu
import numpy as N
import os
import sys
sys.path.append("../PyLib")
from PlotData import plotData


model_name="Plant"

#sono caricati tutti i file ".mo" nella cartella
model_files = [f for f in os.listdir(".") if ".mo" in f]

#input_object = (['noise', 'failures'], input_function)

model_comp = compile_fmu(model_name, model_files)
model = load_fmu(model_comp)
maxt = 1000
res = model.simulate(start_time=0, final_time=maxt, options={'ncp':1000})

plt.plotData(2, 2, ['i_L', 'v_D'], res)
