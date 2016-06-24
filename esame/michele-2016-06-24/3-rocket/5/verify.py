# directories
molib_dir = "../../molib"
pylib_dir = "../../pylib"

#script vars
model_name = "ClosedSystem"

files = [
        "../model/controller.mo",
        "../model/closed_system.mo",
        "../model/rocket.mo",
        "../model/monitor.mo",
]

domains = {
        'r.h_start' : [50000, 55000],
        'r.v_start' : [-900, -1100],
}

end_time = 400

plot_variables = [
        "r.h",
        "r.v",
        "r.a",
        "c.u",
        "c.h_d",
        "c.v_d",
        "m.landed",
        "m.err",
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

if not montecarlo(model, domains, M, end_time, 0, continuous=True, monitor_name="m.controller_err", inspect_vars = plot_variables):
    print "Error found."
else:
    print "No error found with confidence {}% and margin {}%".format((1 - confidence) * 100.0, margin * 100.0)

