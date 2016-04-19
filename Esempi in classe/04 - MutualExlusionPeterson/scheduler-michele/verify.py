import sys
sys.path.append('../../../model_checking/dfs-michele')

from search import dfs
from search import Model

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu("SchedulerSystem", ['closed_system.mo', 'system.mo', 'monitor.mo', 'environment.mo'])
model = load_fmu(fmu_path)

actions = {
    'env.d.turn'    : [1, 2, 3],
}

state_vars = [
    'env.s.turn',
    'env.s.count',
    'env.s.adm',
    'env.d.turn',
    'm.error',
    'p1.state',
    'p2.state',
    't.turn',
    'admissible',
    'error',
]

var_map = {
    'env.s.turn'    : 'env.turn_start',
    'env.s.count'   : 'env.count_start',
    'env.s.adm'     : 'env.adm_start',
    'env.d.turn'    : 'env.disturbance_start',
    'm.error'       : 'm.error_start',
    'p1.state'      : 'p1.state_start',
    'p2.state'      : 'p2.state_start',
    't.turn'        : 't.turn_start',
    'admissible'    : 'env.adm_start',
    'error'         : 'm.error_start',
}

time_step = model.get('env.T')[0]

del model

model = Model(fmu_path, state_vars, actions, var_map, time_step)

dfs(model)

