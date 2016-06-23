#! /opt/jmodelica/bin/jm_ipython.sh

#  #! /home/enrico/JModelica.org/build/Python/jm_ipython.sh


###! /usr/bin/env python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys
import numpy as N
import random
import math


def input_function2(t) :
    return N.array([5.5 + 4.5*N.sin(2*3.14*0.1*t), 1 if (N.sin(2*3.14*0.1*t) >= 0) else 0])
#     return N.array([10, 1])

def input_function1(t) :
    return N.array([5.5 + 3.5*N.sin(2*3.14*0.05*t) + 2.0*N.sin(2*3.14*1*t) ])
#     return N.array([10, 1])

def input_function_rand(t) :
    return N.array([1.0 + 9.0*random.random()])
#     return N.array([10, 1])


fmu = compile_fmu('System', ['system.mo', 'ad.mo', 'controller.mo', 'fifo.mo', 'constants.mo', 'monitor.mo'])

maxt = 1000  # timehorizon

#n = 2*maxt # timepoints
n = maxt/100 # timepoints
r = 1 # inputs
u = N.zeros((n, r + 1))
u[0][0] = 0

epsilon = 0.1
delta = 0.1
samples = int(math.ceil(math.log(delta)/math.log(1 - epsilon)))

print "samples = %d" % (samples)

random.seed(0)

myfile = open('log', 'w');

#print('sample-number monitor');
print >> myfile, "# sample monitor";

#for j in xrange(1):  # debugging
for j in xrange(samples):

    # define input
    for k in xrange(n):
        t = float(k)*(float(maxt)/float(n-1))
        u[k][0] = t
        #u[k][1] = 1.0 + 9.0*random.random()  # random 
        u[k][1] = 0.1 + 0.9*random.randint(0, 1)
        #u[k][1] = 10 if (N.sin(2*3.14*0.001*t) >= 0) else 1  # with T=50 fails
        #print "u[%d] = (%f, %f)" % (t, u[t][0], u[t][1])

    model = load_fmu(fmu)
    opts = model.simulate_options()
    opts['CVode_options']['verbosity'] = 50 # No output
#opts['CVode_options']['maxh'] = 1.0e-1   # Max integrator step size
#opts['filter'] = 'plant.*' 
#opts['result_handling'] = 'memory'  #save in RAM...instead of in a file
#opts['ncp'] = 500 #Change the number of communication points    
#model.set('p1.v', v1);
#model.set('p2.v', v2);

    input_object = (['p'], u)
    res = model.simulate(start_time=0, final_time=maxt, input=input_object, options=opts)
    monitor = model.get('monitor.y');
    print "%d %d" % (j, monitor) ;
    if (monitor == 1) :
        print >> myfile, "begin counterexample sample %d" % (j) ;
        for k in xrange(n):       
            print >> myfile, "%f %f" % (u[k][0] , u[k][1]) ;
        print >> myfile, "end counterexample sample %d" % (j) ;

myfile.close();

#sys.exit()

t = res['time']

rows = 2
cols = 2
maxy =  5 # max(res['v3']);


# col 1
fig = 1
# 1 (1,1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['fifo.x'])
plt.grid()
#plt.axis([0, maxt, -1, 2])
plt.title('fifo.x')
#
fig = fig + 1
# 4 (1, 2)
plt.subplot(rows,cols,fig)
plt.plot(t, res['fifo.p_out'])
plt.grid()
#plt.axis([0, maxt, -1, 2])
plt.title('fifo.p_out')
#
fig = fig + 1
# 3 (3, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['fifo.u'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('fifo.u')
#
fig = fig + 1
# 3 (3, 1)
plt.subplot(rows,cols,fig)
plt.plot(t, res['monitor.y'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('monitor.y')
#
#
#
#
#
plt.show()


