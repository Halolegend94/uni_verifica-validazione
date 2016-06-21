#! /opt/jmodelica/bin/jm_ipython.sh

#  #! /home/enrico/JModelica.org/build/Python/jm_ipython.sh


###! /usr/bin/env python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys


fmu = compile_fmu('Process', ['process.mo'])

model = load_fmu(fmu)
opts = model.simulate_options()
#opts['CVode_options']['maxh'] = 1.0e-6   # Max integrator step size
#opts['filter'] = 'plant.*' 
#opts['result_handling'] = 'memory'  #save in RAM...instead of in a file
#opts['ncp'] = 500 #Change the number of communication points
 
maxt = 20
res = model.simulate(start_time=0, final_time=maxt, options=opts)

#sys.exit();

t = res['time']

rows = 4
cols = 2
maxy =  5 # max(res['v3']);


# col 1
fig = 1
# 1 (1,1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['x'])
plt.grid()
#plt.axis([0, maxt, 0, maxy])
plt.title('x')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['ga'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('ga')
#
fig = fig + 1
# 3 (3, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['kr'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('kr')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['gb'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('gb')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['kw'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('kw')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['gc'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('gc')
#
fig = fig + 1
# 2 (2, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['m'])
plt.grid()
#plt.axis([0, maxt, -2, 2])
plt.title('m')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['kr'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('kr')
#
plt.show()
