from shared import *

fmu = compile_fmu('System', ['plant_unit.mo','plant.mo'])
model = load_fmu(fmu)
opts = model.simulate_options()

model.set('plant.iL0', 0)
model.set('plant.vO0', 0)
model.set('u0', 0)

res = model.simulate(start_time=0, final_time=6, options=opts)

if (model.get('low_check')[0]):
    print "Y > 0"
else:
    print "Y = 0"

plotData(res, 'plant.y', 'plant.Vi', 'low_check')
