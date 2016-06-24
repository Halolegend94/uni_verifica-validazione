# directories
molib_dir = "../../molib"
pylib_dir = "../../pylib"

#script vars
model_name = "ClosedSystem"

files = [
        "../model/rocket.mo",
        "../model/monitor.mo",
        "../model/controller.mo",
        "../model/closed_system.mo",
]

end_time = 300

plot_variables = [
        'r.h',
        'r.v',
        'c.v_d',
        'r.a',
        'r.m',
        'r.u',
        'c.h_d',
        'c.pre_h_d',
        'm.err',
]

# don't touch after this point
import sys
sys.path.append(pylib_dir)

from search import *

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu(model_name, files, compiler_options = { 'extra_lib_dirs': molib_dir })
model = load_fmu(fmu_path)

res = model.simulate(0, end_time)

display_variables(res, plot_variables)

err = model.get('m.err')[0]
h = model.get('r.h')[0]

if err:
    print "ERROR: missile schiantato"
elif h > 0.0:
    print "ERROR: missile ancora in volo."
else:
    print "missile atterrato correttamente"

