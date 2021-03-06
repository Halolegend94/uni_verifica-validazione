# Script utlizzato per laciare i modelli
# Autore: Cristian Di Pietrantonio


# import necessari
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys
sys.path.append("../../../Utilities")
import os
import PlotData as plt
model_name="ClosedSystem"

#sono caricati tutti i file ".mo" nella cartella
model_files = [f for f in os.listdir(".") if ".mo" in f]

#input_object = (['noise', 'failures'], input_function)

model_comp = compile_fmu(model_name, model_files)
model = load_fmu(model_comp)
maxt = 50
opts = model.simulate_options()
#opts['CVode_options']['maxh'] = 1.0e-4
res = model.simulate(start_time=0, final_time=maxt, options=opts)

plt.plotData(3, 2, ['proc1.myState', 'proc2.myState', 'proc1.ptime', 'proc2.ptime', 'mem.kr', 'm.y'], res)
