import sys
import os
sys.path.append("../../../model_checking/dfs-cristian")
sys.path.append("../../../")
from PyLib.Pareto import Pareto
import numpy as numpy

model_files = [f for f in os.listdir(".") if ".mo" in f]

def kpi1(*varss):
    return varss[0][0]

def kpi2(*varss):
    return varss[0][0]

p = Pareto(model_files,
        "prova",
        ['p1', 'p2'],
        [numpy.arange(1, 20, 0.5), numpy.arange(1, 25, 0.5)], #parma values
        ['i1', 'i2'], #input var
        [[1, 5], [1, 6]], #input limits
        'y',
         2, #sim time
         5)  #timepoints


kpiFunctions = [[kpi1, [0]], [kpi2, [1]]]

j = p.findFrontier(0.8, 0.1, False,  kpiFunctions)
for d in j:
    if d[3] == True:
        print d
