import sys
import os
sys.path.append("../../model_checking/dfs-cristian")

from PyLib.Montecarlo import Montecarlo

model_files = [f for f in os.listdir(".") if ".mo" in f]

m = Montecarlo(model_files, "System", ['p'], [[1, 10]], 1000, 10, 'monitor.y')
res = m.verify(0.1, 0.01, True)
print "errors: {}".format(len(res))
