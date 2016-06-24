# directories
molib_dir = "../../molib"
pylib_dir = "../../pylib"

#script vars
model_name = "ClosedSystem"

files = [
        "../model/controller.mo",
        "closed_system.mo",
        "../model/plant.mo",
]

domains = {
        'p.i_L_start' : [0, 2],
        'p.v_O_start' : [0, 8],
}

end_time = 0.02

plot_variables = [
        "p.y",
        "p.u",
        "p.i_L",
        "p.v_O",
]

# don't touch after this point
import sys
sys.path.append(pylib_dir)

from search import *

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu(model_name, files, compiler_options = { 'extra_lib_dirs': molib_dir })
model = load_fmu(fmu_path)

confidence = 0.2
margin = 0.2

M = mc2.trials_number(confidence, margin)

print "Running {} trials.".format(M)

if not montecarlo(model, domains, M, end_time, 0, continuous=True, monitor_name="err", inspect_vars = plot_variables):
    print "Error found."
else:
    print "No error found with confidence {}% and margin {}%".format((1 - confidence) * 100.0, margin * 100.0)

