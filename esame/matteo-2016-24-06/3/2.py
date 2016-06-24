from shared import *

fmu = compile_fmu('System', ['system.mo','rocket.mo','monitor.mo'])
model = load_fmu(fmu)
opts = model.simulate_options()

model.set('t0', 0)

res = model.simulate(start_time=0, final_time=60, options=opts)

if (model.get('monitor.crash')[0]):
    print "Crashed"
else:
    print "Safe touch!"

plotData(res, 'rocket.altitude', 'rocket.velocity', 'monitor.crash')
