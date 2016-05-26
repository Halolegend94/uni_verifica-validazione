import sys
sys.path.append("../../../model_checking/dfs-cristian")

from PyLib.Search import Search
from PyLib.ModelState import ModelState

#statekeys
statekeys = ['ec.quantX0', 'e.adm0', 'm.y0']

getdict = {}
getdict['s.x0'] = 's.x'
getdict['e.riverLoad0'] = 'e.d.riverLoad'
getdict['ec.pOpen0'] = 'ec.pOpen'
getdict['ec.quantX0'] = 'ec.quantX'
getdict['e.adm0'] = 'e.current.adm'
getdict['m.y0'] = 'm.y'

params = ['e.riverLoad0']
m = ModelState(statekeys, params, getdict, 'ClosedSystem', 'ec.T', 'e.adm0', 'm.y0')

actions = range(1, 10, 1)
d = Search()
d.dfs(m, actions, 3)
