import myjm

mod = myjm.load("MoonLanding","moonLanding.mo")
#~ mod.set('apollo.mass', 1100)
res = mod.simulate(final_time=500)
myjm.plot(res, 'apollo.altitude','apollo.velocity')
