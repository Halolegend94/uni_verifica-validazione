# directories
molib_dir = "../../molib"
pylib_dir = "../../pylib"

#script vars
model_name = "Validazione"

files = [
        "../model/rocket.mo",
        "../model/monitor.mo",
        "validazione_1.mo",
]

end_time = 100

plot_variables = [
        'r.h',
        'r.v',
        'r.a',
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

h = model.get('r.h')[0]

if h > 0.0:
    print "Missile ancora in volo."
else:
    print "ERRORE: missile non in volo."

