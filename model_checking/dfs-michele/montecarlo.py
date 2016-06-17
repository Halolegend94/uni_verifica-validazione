from search import montecarlo
from search import mc2

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu("ClosedSystem", ['closed-system.mo', 'system.mo', 'monitor.mo', 'environment.mo', 'dictionary.mo', 'state.mo'])
model = load_fmu(fmu_path)

inputs = {
        'env.d.noise'   : [-1, 0, 1],
        'env.d.failures': [0],
}

confidence = 0.1
margin = 0.1

M = mc2.trials_number(confidence, margin)

print "Running {} trials.".format(M)

if not montecarlo(model, inputs, M, 10, 10, False):
    print "Error found."
else:
    print "No error found with confidence {}% and margin {}%".format(confidence * 100.0, margin * 100.0)

