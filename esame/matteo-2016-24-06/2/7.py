from shared import *
import math
import random

fmu = compile_fmu('System', ['system.mo','plant.mo','ad.mo','da.mo','controller.mo'])
model = load_fmu(fmu)
opts = model.simulate_options()
opts['CVode_options']['verbosity'] = 50

M = int(math.ceil(math.log(0.2) / math.log(1 - 0.2)))
print "Trials:", M

for i in xrange(M):
    model.reset();
    L = random.random()*2
    V = random.random()*8
    print "Trial %d: L=%f, V=%f" % (i+1, L, V)
    model.set('plant.iL0', L)
    model.set('plant.vO0', V)
    model.set('controller.alpha', 0.35)

    res = model.simulate(start_time=0, final_time=0.02, options=opts)

    if (model.get('controller.intoAlpha')[0]):
        continue

    print "Y OUTSIDE 5+-alpha"
    print "alhpa =",model.get('controller.alpha')[0]
    break
print "Done"
