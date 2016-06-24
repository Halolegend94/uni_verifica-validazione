import sys
sys.path.append("../../../model_checking/dfs-michele")

from search import display_variables

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu('TrenoTest', ['treno.mo', 'treno_unittest.mo'])
model = load_fmu(fmu_path)

res = model.simulate(0, 256)

display_variables(res, ['t.pos', 't.speed', 't.app', 't.exit'])

