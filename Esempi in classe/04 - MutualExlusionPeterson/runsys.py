#! /usr/bin/env python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys


fmu = compile_fmu('ClosedSystem', ['closed-system.mo', 'system.mo', 'monitor.mo', 'environment.mo', 'dictionary.mo', 'state.mo'])

model = load_fmu(fmu)
opts = model.simulate_options()
opts['ncp'] = 500 #Change the number of communication points
 
maxt = 5
res = model.simulate(start_time=0, final_time=maxt, options=opts)

#sys.exit();

t = res['time']

rows = 3
cols = 2
maxy =  5 # max(res['v3']);


# col 1
fig = 1
# 1 (1,1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['sys.x'])
plt.grid()
#plt.axis([0, maxt, 0, maxy])
plt.title('sys.x')
fig = fig + 1
# 2 (2, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['sys.u'])
plt.grid()
#plt.axis([0, maxt, -2, 2])
plt.title('sys.u')
fig = fig + 1
# 3 (3, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['sys.noise'])
plt.grid()
#plt.axis([0, maxt, -1, 2])
plt.title('sys.noise')
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['monitor.x'])
plt.grid()
#plt.axis([0, maxt, -1, 2])
plt.title('monitor.x')
fig = fig + 1
# 5 (2, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['monitor.y'])
plt.grid()
plt.axis([0, maxt, -0.5, 1.5])
plt.title('monitor.y')
fig = fig + 1
# 6 (2, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['env.d.noise'])
plt.grid()
plt.axis([0, maxt, -1.5, 1.5])
plt.title('env.d.noise')


plt.show()
