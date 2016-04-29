from pymodelica import compile_fmu
from pyfmi import load_fmu

from matplotlib import pyplot

import numpy

fmu_path = compile_fmu("FisherMutualExclusion", ['closed_system.mo', 'cs_variable.mo', 'process.mo', 'monitor.mo', 'environment.mo'])
model = load_fmu(fmu_path)

time        = [ 0.0,   0.1,   0.1,   0.8,   0.8,   1.3,   1.4]
transition1 = [True,  True,  True,  True, False, False, False]
transition2 = [True,  True, False, False, False,  True,  True]
drift1      = [ 0.0,   0.0,   0.0,   0.0,   0.0,   0.0,   0.0]
drift2      = [ 0.0,   0.0,   0.0,   0.0,   0.0,   0.0,   0.0]

inputs = numpy.transpose(numpy.vstack((time, transition1, transition2, drift1, drift2)))

input_tuple = (['env.d.transition1', 'env.d.transition2', 'env.d.drift1', 'env.d.drift2'], inputs)

res = model.simulate(0, 1.5, input = input_tuple)

pyplot.figure(1)

pyplot.subplot(3, 2, 1)
pyplot.plot(res['time'], res['cs.turn'])
pyplot.grid()
pyplot.title("turn")

pyplot.subplot(3, 2, 2)
pyplot.plot(res['time'], res['error'])
pyplot.grid()
pyplot.title("error")

pyplot.subplot(3, 2, 3)
pyplot.plot(res['time'], res['p1.state'])
pyplot.grid()
pyplot.title("state 1")

pyplot.subplot(3, 2, 4)
pyplot.plot(res['time'], res['p2.state'])
pyplot.grid()
pyplot.title("state 2")

pyplot.subplot(3, 2, 5)
pyplot.plot(res['time'], res['env.d.transition1'])
pyplot.grid()
pyplot.title("transition 1")

pyplot.subplot(3, 2, 6)
pyplot.plot(res['time'], res['env.d.transition2'])
pyplot.grid()
pyplot.title("transition 2")

pyplot.show()

