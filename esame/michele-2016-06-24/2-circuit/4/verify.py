# directories
molib_dir = "../../molib"
pylib_dir = "../../pylib"

#script vars
model_name = "ClosedSystem"

files = [
        "closed_system.mo",
        "../model/plant.mo",
]

end_time = 0.001

plot_variables = [
        "p.i_L",
        "p.v_O",
        "p.y",
        "p.u",
        "err",
]

# don't touch after this point
import sys
sys.path.append(pylib_dir)

from search import *

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu(model_name, files, compiler_options = { 'extra_lib_dirs': molib_dir })
model = load_fmu(fmu_path)

opts = model.simulate_options()
opts['result_handling'] = 'memory'

res = model.simulate(0, end_time, options = opts)

display_variables(res, plot_variables)

err = model.get('err')[0]

if err:
    print "ERROR: specifica non rispettata"
else:
    print "Specifica rispettata"

