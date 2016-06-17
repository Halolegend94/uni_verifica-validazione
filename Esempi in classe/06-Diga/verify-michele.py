import sys
sys.path.append("../../model_checking/dfs-michele")

from search import montecarlo
from search import mc2

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu('System', ['system.mo', 'ad.mo', 'controller.mo', 'lake.mo', 'constants.mo', 'monitor.mo'])
model = load_fmu(fmu_path)

inputs = {
        'p'   : [1, 10]
}

inspect_vars = [
        'lake.x',
        'lake.u',
]

confidence = 0.01
margin = 0.01

M = mc2.trials_number(confidence, margin)

print "Running {} trials.".format(M)

if not montecarlo(model, inputs, M, 1000, 10, continuous=False, monitor_name="monitor.y", inspect_vars = inspect_vars):
    print "Error found."
else:
    print "No error found with confidence {}% and margin {}%".format(confidence * 100.0, margin * 100.0)

