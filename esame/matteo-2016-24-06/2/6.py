from shared import *

fmu = compile_fmu('System', ['system.mo','plant.mo','ad.mo','da.mo','controller.mo'])
model = load_fmu(fmu)
opts = model.simulate_options()

model.set('plant.iL0', 0)
model.set('plant.vO0', 0)

res = model.simulate(start_time=0, final_time=0.05, options=opts)

if (model.get('controller.intoAlpha')[0]):
    print "Y INSIDE 5+-alpha"
else:
    print "Y OUTSIDE 5+-alpha"
print "alhpa =",model.get('controller.alpha')[0]

plotData(res, 'plant.y', 'controller.intoAlpha')
