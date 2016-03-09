import myjm

mod = myjm.load("SamplingClock","samplingClock.mo")
res = mod.simulate(final_time=10)
myjm.plot(res, 'i','r')
