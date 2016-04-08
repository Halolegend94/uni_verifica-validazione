#! /usr/bin/env python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt


# ecu2 (only measure acceleration, discrete time estimation of velocity and position)
fmu = compile_fmu('MoonLanding', ['celestial.mo', 'rocket.mo', 'moonlanding1.mo', 'ecu2.mo'])

model = load_fmu(fmu)
opts = model.simulate_options()
#opts['ncp'] = 1000 #Change the number of communication points
#opts['CVode_options']['maxh'] = 1.0e-4   # Options specific for CVode

#model.set('apollo.initialmass', 1038.358)
print "Apollo initial Mass %f\n" % model.get('apollo.initialmass') 
#model.set('apollo.initialmass', 2000.00)

#altitude = model.get('apollo.initial_altitude')
print "Apollo initial altitude = %f\n" % model.get('apollo.initial_altitude')

#velocity = model.get('apollo.initial_velocity')
print "Apollo initial velocity = %f\n" % model.get('apollo.initial_velocity')

res = model.simulate(start_time=0, final_time=500, options=opts)


x = res['time']
y1 = res['apollo.altitude']
y2 = res['apollo.velocity']
y3 = res['apollo.acceleration']
y4 = res['apollo.thrust']


#plt.plot(x, y1, x, y2, x, y3)
#plt.legend(('altitude', 'velocity', 'acceleration'))
#plt.plot(x, z)
#plt.grid()
#plt.show()

rows = 4
cols = 2
fig = 1

# 1
plt.figure(1)
plt.subplot(rows,cols,fig)
plt.plot(x,y1)
plt.grid()
plt.title('altitude')
fig = fig + 1
# 2
plt.subplot(rows,cols,fig)
plt.plot(x,y2)
plt.grid()
plt.title('velocity')
fig = fig + 1
# 3
plt.subplot(rows,cols,fig)
plt.plot(x,y3)
plt.grid()
plt.title('acceleration')
fig = fig + 1
# 4
plt.subplot(rows,cols,fig)
plt.plot(x,y4)
plt.title('thrust')
plt.xlabel('t[s]')
plt.grid()
# 5
fig = fig + 1
plt.subplot(rows,cols,fig)
plt.plot(x,res['ctr.astep'])
plt.title('ecu measured acceleration')
plt.xlabel('t[s]')
plt.grid()
# 6
fig = fig + 1
plt.subplot(rows,cols,fig)
plt.plot(x,res['ctr.velocity'])
plt.title('ecu estimated velocity')
plt.xlabel('t[s]')
plt.grid()
# 7 
fig = fig + 1
plt.subplot(rows,cols,fig)
plt.plot(x,res['ctr.altitude'])
plt.title('ecu estimated altitude')
plt.xlabel('t[s]')
plt.grid()
# 8
fig = fig + 1
plt.subplot(rows,cols,fig)
#plt.plot()
plt.plot(x, res['ctr.vstep'], x, res['ctr.astep'])
plt.title('vstep + astep')
plt.legend(['ctr.vstep','ctr.astep'])
plt.xlabel('t[s]')
plt.grid()

plt.show()
