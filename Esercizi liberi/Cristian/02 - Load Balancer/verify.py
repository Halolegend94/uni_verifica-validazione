import sys
import os
sys.path.append("../../../model_checking/dfs-cristian")
sys.path.append("../../../")
from PyLib.Montecarlo import Montecarlo
from Utilities.PlotData import plotData
model_files = [f for f in os.listdir(".") if ".mo" in f]

m = Montecarlo(model_files, "ClosedSystem", ['noise', 'failures'], [[-1, 1], [-1, 1]], 1000, 10, 'm.y')
res = m.verify(0.1, 0.01, False)
print "errors: {}".format(len(res))
if len(res) > 0:
    plotData(2, 2, ['s.x', 'm.y'], res[0])
