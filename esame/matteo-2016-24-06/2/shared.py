from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import numpy as N

def plotData(vals, *arraydict):
    rows = (len(arraydict)+1)/2
    cols = 2
    fig = 0
    plt.figure(1)
    t = vals['time']
    xend = max(t)
    for i in range(0, len(arraydict)):
        fig = fig + 1
        if (arraydict[i] == None): continue
        plt.subplot(rows,cols, fig)
        currentRange = vals[arraydict[i]]
        plt.plot(t, currentRange)
        plt.axis([0,xend,min(currentRange) - 1, max(currentRange) + 1])
        plt.title(arraydict[i])
        plt.grid()
    plt.show()
    return
