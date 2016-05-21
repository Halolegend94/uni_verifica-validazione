import sys
sys.path.append("../../../model_checking/dfs-cristian")

from PyLib.Search import Search
from PyLib.ModelState import ModelState

#statekeys
statekeys = ['s.x', 'e.current.depth', 'e.current.adm', 's.pOpen']

getdict = {}
getdict['s.x0'] = 's.x'
getdict['e.riverLoad0'] = 'e.d.riverLoad'
getdict['ec.pOpen0'] = 'ec.pOpen'
getdict['m.y0'] = 'm.y'

inputs = ['e']

m = ModelState(statekeys, getdict, inputs, sysName, timeStepVarName, admissibleVar, unsafeVar)
