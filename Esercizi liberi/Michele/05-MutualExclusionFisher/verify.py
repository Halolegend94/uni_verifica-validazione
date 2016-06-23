import sys
sys.path.append('../../../model_checking/dfs-michele')

from search import dfs
from search import Model

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu("FisherMutualExclusion", ['closed_system.mo', 'cs_variable.mo', 'process.mo', 'monitor.mo', 'environment.mo'])
model = load_fmu(fmu_path)

actions = {
    'env.d.transition1'    : [False, True],
    'env.d.transition2'    : [False, True],
    'env.d.drift1'         : [-0.2, 0.0],
    'env.d.drift2'         : [0.0, 0.1],
}

state_vars = [
    'env.s.adm',
    'env.s.count',
    'env.d.transition1',
    'env.d.transition2',
    'env.d.drift1',
    'env.d.drift2',
    'm.error',
    'p1.state',
    'p1.process_time',
    'p2.state',
    'p2.process_time',
    'cs.turn',
    'admissible',
    'error',
]

var_map = {
    'env.s.adm'     : 'env.adm_start',
    'env.s.count'     : 'env.count_start',
    'env.d.transition1' : 'env.transition1_start',
    'env.d.transition2' : 'env.transition2_start',
    'env.d.drift1' : 'env.drift1_start',
    'env.d.drift2' : 'env.drift2_start',
    'm.error'       : 'm.error_start',
    'p1.state'      : 'p1.state_start',
    'p1.process_time' : 'p1.process_time_start',
    'p2.state'      : 'p2.state_start',
    'p2.process_time' : 'p2.process_time_start',
    'cs.turn': 'cs.turn_start',
    'admissible'    : 'env.adm_start',
    'error'         : 'm.error_start',
}

time_step = model.get('time_step')[0]

del model

model = Model(fmu_path, state_vars, actions, var_map, time_step)

dfs(model)

