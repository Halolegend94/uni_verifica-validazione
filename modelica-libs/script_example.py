# directories
molib_dir = ""
pylib_dir = ""

#script vars
model_name = "Test"

files = [
        "test.mo",
        "test_unittest.mo",
]

end_time = 10.0

plot_variables = [
        'x',
        'y',
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

