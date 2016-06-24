# directories
molib_dir = "../../molib"
pylib_dir = "../../pylib"

#script vars
model_name = "Validazione"

files = [
        "../model/rocket.mo",
        "../model/monitor.mo",
        "validazione_0.mo",
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

err = model.get('m.err')[0]

if err:
    print "Requisito di safety violato."
else:
    print "ERRORE: requisito di safety non violato."

