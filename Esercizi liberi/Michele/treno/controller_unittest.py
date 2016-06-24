import sys
sys.path.append("../../../model_checking/dfs-michele")

from search import display_variables

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu('ControllerTest', ['controller.mo', 'controller_unittest.mo'])
model = load_fmu(fmu_path)

res = model.simulate(0, 64)

display_variables(res, ['c.timer', 'c.mode', 'count', 'c.app', 'c.exit', 'c.lower', 'c.raise', 'c.pre_app', 'c.pre_exit'])

