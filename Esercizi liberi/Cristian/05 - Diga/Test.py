from pymodelica import compile_fmu
from pyfmi import load_fmu
import sys
import os

#compile

model_files = [f for f in os.listdir(".") if ".mo" in f]
fmu = compile_fmu('ClosedSystem', model_files)
model = load_fmu(fmu)
opts = model.simulate_options()
opts['result_handling'] = 'memory'
opts['CVode_options']['verbosity'] = 50 # No output
opts['initialize'] = False # No output
for i in range(5):
    model.reset()
    model.set('ec.quantX0', 550)
    model.set('e.riverLoad0', 7)
    model.initialize()
    model.simulate(start_time=i,final_time= i+1, options=opts)
