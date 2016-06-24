from shared import *
import math
import random

fmu = compile_fmu('System', ['system_full.mo','ecu.mo','rocket.mo','monitor.mo'])
model = load_fmu(fmu)
opts = model.simulate_options()

opts['CVode_options']['verbosity'] = 50

M = int(math.ceil(math.log(0.2) / math.log(1 - 0.2)))
print "Trials:", M

for i in xrange(M):
    model.reset();
    H = random.random()*5000+50000
    V = random.random()*2000-900
    print "Trial %d: H=%f; V=%f" % (i+1, H, V)
    model.set('rocket.initial_altitude', H)
    model.set('rocket.initial_velocity', V)

    res = model.simulate(start_time=0, final_time=1000, options=opts)

    if (model.get('monitor.crash')[0]):
        print "Crashed"
        break
    elif (model.get('rocket.altitude')[0] > 1):
        print "Still fliyng"
        break
    else:
        print "Safe touch!"
print "Done"
