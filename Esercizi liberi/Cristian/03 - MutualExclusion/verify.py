import sys
import os
sys.path.append("../../../model_checking/dfs-cristian")
sys.path.append("../../../")
from PyLib.Search import Search
#from PyLib.Montecarlo import Montecarlo
from Utilities.PlotData import plotData
from PyLib.ModelState import ModelState

#### Inizio Script

#tutti i file .mo nella cartella
model_files = [f for f in os.listdir(".") if ".mo" in f]

statekeys = ['process1.myState0', 'process2.myState0', 'e.current.admissible', 'm.y']
params = ['process1.myState0', 'process2.myState0']
getdict = {'process1.myState0' : 'process1.myState',
            'process2.myState0' : 'process2.myState',
            'e.current.admissible' : 'e.current.admissible',
            'm.y' : 'm.y'
            }

#PARAMS:
#   - statekeys: the set of variables that define the state of a model
#   - params: array of variables that represents input to the model
#   - getdict: used to get variables of the model throungh associated parameters
#   - sysName: the name of the main class of the system
#   - tumeStempVarName. the name of the timestep variable in the environment model
#   - admissibleVar: the name of the variable that store the admissibility of a state
#   - unsafeVar: the name of the variable inside the monitor that establishes id the system is unsafe
modelState = ModelState(statekeys, params, getdict, "ClosedSystem", 2, 'e.current.admissible', 'm.y')

actions = [[1, 2, 3], [1, 2, 3]]

s = Search()
s.dfs(modelState, actions, 3)
