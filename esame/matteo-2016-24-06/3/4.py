from shared import *
import random

fmu = compile_fmu('System', ['system_full.mo','ecu.mo','rocket.mo','monitor.mo'])
model = load_fmu(fmu)
opts = model.simulate_options()

# H = random.random()*5000+50000
# V = random.random()*2000-900
# H=50414.079987; V=888.997826
# print "H=%f, V=%f" % (H, V)
# model.set('rocket.initial_altitude', H)
# model.set('rocket.initial_velocity', V)

res = model.simulate(start_time=0, final_time=1200, options=opts)

if (model.get('monitor.crash')[0]):
    print "Crashed"
elif (model.get('rocket.altitude')[0] > 1):
    print "Still fliyng"
else:
    print "Safe touch!"

plotData(res, 'rocket.altitude', 'rocket.velocity', 'monitor.crash', 'rocket.thrust', 'rocket.mass', 'ecu.error')
