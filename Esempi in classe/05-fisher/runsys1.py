#! /opt/jmodelica/bin/jm_ipython.sh

#  #! /home/enrico/JModelica.org/build/Python/jm_ipython.sh


###! /usr/bin/env python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys
import numpy as N

n = 1 # timepoints
r = 4 # inputs
u = N.zeros((n, r + 1))
u[0][0] = 0

fmu = compile_fmu('System', ['system.mo', 'process.mo', 'store.mo', 'monitor.mo'])

model = load_fmu(fmu)
opts = model.simulate_options()
opts['CVode_options']['maxh'] = 1.0e-1   # Max integrator step size
#opts['filter'] = 'plant.*' 
#opts['result_handling'] = 'memory'  #save in RAM...instead of in a file
#opts['ncp'] = 500 #Change the number of communication points     
c1 = 8;
c2 = 11;
# pass a=8, b=3
# fail a = 9, b = 3
a = 9;  #7, 8, 9, 10
b = 3;  # 2, 3, 4, 5
v1 = -0.2;
v2 = 0.1
u[0][1] = a
u[0][2] = b
u[0][3] = c1
u[0][4] = c2
model.set('p1.v', v1);
model.set('p2.v', v2);
maxt = 100
input_object = (['A','B', 'C1', 'C2'], u)
res = model.simulate(start_time=0, final_time=maxt, input=input_object, options=opts)

t = res['time']

rows = 5
cols = 2
maxy =  5 # max(res['v3']);


# col 1
fig = 1
# 1 (1,1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['p1.x'])
plt.grid()
#plt.axis([0, maxt, 0, maxy])
plt.title('p1.x')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['p2.x'])
plt.grid()
#plt.axis([0, maxt, -1, 2])
plt.title('p2.x')
#
fig = fig + 1
# 3 (3, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['p1.m'])
plt.grid()
plt.axis([0, maxt, 0, 5])
plt.title('p1.m')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['p2.m'])
plt.grid()
plt.axis([0, maxt, 0, 5])
plt.title('p2.m')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['p1.kr'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('p1.kr')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['p2.kr'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('p2.kr')
#
fig = fig + 1
# 2 (2, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['p1.kw'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('p1.kw')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['p2.kw'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('p2.kw')
#
fig = fig + 1
# 2 (2, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['P.y'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('P.y')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['M.k'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('M.k')
#
plt.show()


