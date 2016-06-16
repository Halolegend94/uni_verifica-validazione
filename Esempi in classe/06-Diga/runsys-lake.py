#! /opt/jmodelica/bin/jm_ipython.sh

#  #! /home/enrico/JModelica.org/build/Python/jm_ipython.sh


###! /usr/bin/env python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys
import numpy as N


def input_function(t) :
    return N.array([5.5 + 4.5*N.sin(2*3.14*0.1*t), 1 if (N.sin(2*3.14*0.1*t) >= 0) else 0])
#     return N.array([10, 1])


fmu = compile_fmu('Lake', ['lake.mo'])

model = load_fmu(fmu)
opts = model.simulate_options()
#opts['CVode_options']['maxh'] = 1.0e-1   # Max integrator step size
#opts['filter'] = 'plant.*' 
#opts['result_handling'] = 'memory'  #save in RAM...instead of in a file
#opts['ncp'] = 500 #Change the number of communication points     
#model.set('p1.v', v1);
#model.set('p2.v', v2);

maxt = 100
input_object = (['p', 'u'], input_function)
res = model.simulate(start_time=0, final_time=maxt, input=input_object, options=opts)

t = res['time']

rows = 3
cols = 1
maxy =  5 # max(res['v3']);


# col 1
fig = 1
# 1 (1,1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['x'])
plt.grid()
#plt.axis([0, maxt, -1, 2])
plt.title('x')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['p'])
plt.grid()
#plt.axis([0, maxt, -1, 2])
plt.title('p')
#
fig = fig + 1
# 3 (3, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['u'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('u')
#
#
#
#
#
plt.show()


