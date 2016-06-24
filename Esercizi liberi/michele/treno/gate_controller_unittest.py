import sys
sys.path.append("../../../model_checking/dfs-michele")

from search import display_variables

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu('GateControllerTest', ['gate.mo', 'controller.mo', 'gate_controller_unittest.mo'])
model = load_fmu(fmu_path)

res = model.simulate(0, 256)

display_variables(res, ['g.speed', 'g.mode', 'g.angle', 'c.timer', 'c.mode', 'count', 'c.app', 'c.exit', 'c.lower', 'c.raise', 'c.pre_app', 'c.pre_exit'])

