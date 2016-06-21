import sys
import os
sys.path.append("../../../model_checking/dfs-cristian")
sys.path.append("../../../")
from PyLib.Montecarlo import Montecarlo
from Utilities.PlotData import plotData
model_files = [f for f in os.listdir(".") if ".mo" in f]

m = Montecarlo(model_files, "ClosedSystem", ['riverLoad'], [[1, 10]], 1000, 10, 'm.y')
res = m.verify(0.1, 0.01, True)
print "errors: {}".format(len(res))
if len(res) > 0:
    plotData(2, 2, ['s.riverLoad', 'm.y', 's.x', 'ec.pOpen'], res[0])
