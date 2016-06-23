#! /opt/jmodelica/bin/jm_ipython.sh

#  #! /home/enrico/JModelica.org/build/Python/jm_ipython.sh


###! /usr/bin/env python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys


fmu = compile_fmu('System', ['system.mo', 'process.mo', 'store.mo', 'monitor.mo'])

# sys ok when a < (8/11)*b

myfile = open('log', 'w');

print('a b v1 c1 v2 c2 monitor');

for c1 in xrange(2):
    for c2 in xrange(2):
         model = load_fmu(fmu)
         opts = model.simulate_options()
         #opts['CVode_options']['maxh'] = 1.0e-6   # Max integrator step size
         #opts['filter'] = 'plant.*' 
         #opts['result_handling'] = 'memory'  #save in RAM...instead of in a file
         #opts['ncp'] = 500 #Change the number of communication points     
         vc1 = 3 + 2*c1;
         vc2 = 3 + 2*c2;
         a = 7; b = 11;
         v1 = -0.2;
         v2 = 0.1
         #model.set('p1.c', vc1);
         #model.set('p2.c', vc2);
         #model.set('p1.a', a);
         #model.set('p1.b', b);
         #model.set('p1.v', v1);
         #model.set('p2.a', a);
         #model.set('p2.b', b);
         #model.set('p2.v', v2);
         maxt = 30
         res = model.simulate(start_time=0, final_time=maxt, options=opts)
         monitor = model.get('P.y');

         print >> myfile, "%f %f %f %f %f %f %d" % (a, b, v1, vc1, v2, vc2, monitor) ;

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


