#! /opt/jmodelica/bin/jm_ipython.sh

#  #! /home/enrico/JModelica.org/build/Python/jm_ipython.sh


###! /usr/bin/env python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys


fmu = compile_fmu('Store', ['store.mo'])

model = load_fmu(fmu)
opts = model.simulate_options()
#opts['CVode_options']['maxh'] = 1.0e-6   # Max integrator step size
#opts['filter'] = 'plant.*' 
#opts['result_handling'] = 'memory'  #save in RAM...instead of in a file
#opts['ncp'] = 500 #Change the number of communication points
 
maxt = 10
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
plt.plot(t, res['k'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('k')
fig = fig + 1
# 2 (2, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['k1'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('k1')
fig = fig + 1
# 3 (3, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['k2'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('k2')
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['g1k1'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('g1k1')
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['g2k1'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('g2k1')
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['g1k0'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('g1k0')
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['g2k0'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('g2k0')
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['g2k0'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('g2k0')


plt.show()
