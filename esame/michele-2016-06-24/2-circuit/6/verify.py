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

end_time = 0.1

plot_variables = [
        "p.i_L",
        "p.v_O",
        "p.v_D",
        "p.i_D",
        "p.v_C",
        "p.i_C",
        "p.i_u",
        "p.v_u",
        "p.i_R",
        "p.v_L",
        "p.y",
        "p.u",
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

err = model.get("err")[0]

if err:
    print "ERROR: specifica non rispettata"
else:
    print "Specifica rispettata"

