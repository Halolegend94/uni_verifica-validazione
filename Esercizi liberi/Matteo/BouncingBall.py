import myjm

mod = myjm.load("BouncingBall","BouncingBall.mo")
res = mod.simulate(final_time=20, options = {'ncp':1000})
myjm.plot(res, 'height')
