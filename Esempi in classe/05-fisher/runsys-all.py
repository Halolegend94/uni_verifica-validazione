#! /opt/jmodelica/bin/jm_ipython.sh

#  #! /home/enrico/JModelica.org/build/Python/jm_ipython.sh


###! /usr/bin/env python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys
import numpy as N

def kpi1(a, b) :
    return (-2*a -2*b)

def kpi2(c1, c2) :
    return (5*c1 + 5*c2)

fmu = compile_fmu('System', ['system.mo', 'process.mo', 'store.mo', 'monitor.mo'])

# sys ok when a < (8/11)*b



myfile = open('log', 'w');

#print('a b v1 c1 v2 c2 monitor');
print >> myfile, "# a b v1 c1 v2 c2 monitor kpi1 kpi2";



n = 1 # timepoints
r = 4 # inputs
u = N.zeros((n, r + 1))
u[0][0] = 0

for j1 in xrange(4):
    for j2 in xrange(4):
        for j3 in xrange(4):
            for j4 in xrange(4):
                model = load_fmu(fmu)
                opts = model.simulate_options()
                #opts['CVode_options']['maxh'] = 1.0e-6   # Max integrator step size
                #opts['filter'] = 'plant.*' 
                #opts['result_handling'] = 'memory'  #save in RAM...instead of in a file
                #opts['ncp'] = 500 #Change the number of communication points  
                #opts['CVode_options']['verbosity'] = 50 # No output
                #opts['initialize'] = False 
                #model.time = 0
                c1 = 6 + j3;
                c2 = 10 + j4;
                a = 7 + j1;  #7, 8, 9, 10
                b = 2 + j2;  # 2, 3, 4, 5
                #a = 8; b = 3;
                v1 = -0.2;
                v2 = 0.1
                u[0][1] = a
                u[0][2] = b
                u[0][3] = c1
                u[0][4] = c2
                model.set('p1.v', v1);
                model.set('p2.v', v2);
                #model.initialize()
                maxt = 100
                input_object = (['A','B', 'C1', 'C2'], u)
                res = model.simulate(start_time=0, final_time=maxt, input=input_object, options=opts)
                monitor = model.get('P.y');
                print >> myfile, "%f %f %f %f %f %f %d %f %f" % (a, b, v1, c1, v2, c2, monitor, kpi1(a, b), kpi2(c1, c2)) ;

myfile.close();

sys.exit();

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
plt.plot(t, res['P.z'])
plt.grid()
plt.axis([0, maxt, -1, 2])
plt.title('P.z')
#
plt.show()


