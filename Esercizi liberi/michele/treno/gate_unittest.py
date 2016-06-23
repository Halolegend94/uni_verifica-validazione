import sys
sys.path.append("../../../model_checking/dfs-michele")

from search import display_variables

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu('GateTest', ['gate.mo', 'gate_unittest.mo'])
model = load_fmu(fmu_path)

res = model.simulate(0, 64)

display_variables(res, ['g.speed', 'g.angle', 'g.mode', 'g.lower', 'g.raise'])

