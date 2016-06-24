#! /usr/bin/env python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import numpy as N


# ecu2 (only measure acceleration, discrete time estimation of velocity and position)
fmu = compile_fmu('System', ['system.mo','Train.mo','ecu.mo','gate.mo'])

model = load_fmu(fmu)
opts = model.simulate_options()
#~ opts['ncp'] = 1000 #Change the number of communication points
#opts['CVode_options']['maxh'] = 1.0e-4   # Options specific for CVode

model.set('train.x0', -2000)

v = N.zeros((4, 2))
v[0][0] = 0; v[0][1] = 0;
v[1][0] = 30; v[1][1] = 20;
v[2][0] = 60; v[2][1] = 10;
v[3][0] = 90; v[3][1] = 30;

input_object = (['v'], v)
res = model.simulate(start_time=0, final_time=150, options=opts, input=input_object)

#funzione per plottare i dati
import matplotlib.pyplot as plt
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

plotData(res, 'train.x', 'train.v', 'gate.g', 'gate.gv', 'ecu.open', None, 'ecu.close')
