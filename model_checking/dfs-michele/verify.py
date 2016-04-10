from search import dfs
from search import Model

from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu_path = compile_fmu("ClosedSystem", ['closed-system.mo', 'system.mo', 'monitor.mo', 'environment.mo', 'dictionary.mo', 'state.mo'])
model = load_fmu(fmu_path)

actions = {
    'env.d.noise'    : [-1, 0, 1],
    'env.d.failures' : [0],
}

state_vars = [
    'env.x.avg',
    'env.x.adm',
    'env.x.n',
    'env.x.depth',
    'env.d.noise',
    'env.d.failures',
    'monitor.y',
    'sys.x',
    'admissible',
    'error',
]

var_map = {
    'env.x.avg'      : 'env.avg0',
    'env.x.adm'      : 'env.adm0',
    'env.x.n'        : 'env.n0',
    'env.x.depth'    : 'env.depth0',
    'env.d.noise'    : 'env.noise0',
    'env.d.failures' : 'env.failures0',
    'monitor.y'      : 'monitor.y0',
    'sys.x'          : 'sys.x0',
    'env.d.noise'    : 'env.noise0',
    'env.d.failures' : 'env.failures0',
    'admissible'     : 'env.adm0',
    'error'          : 'monitor.y0',
}

time_step = model.get('env.T')[0]

del model

model = Model(fmu_path, state_vars, actions, var_map, time_step)

dfs(model)

