from pymodelica import compile_fmu
from pyfmi import load_fmu

from matplotlib import pyplot

model_name  = "MoonLanding"
model_files = [
            "MoonLanding.mo",
            "Body.mo",
            "CelestialBody.mo",
            "Rocket.mo",
            "Autopilot1.mo",
            "Autopilot2.mo"
        ]
model_path = compile_fmu(model_name, model_files)
model = load_fmu(model_path)

model.set("startApolloMass",      1100)
model.set("startApolloAltitude", 70000)
model.set("startApolloVelocity", -2200)

res = model.simulate(options={'ncp': 10000})

if res['apollo.altitude'][-1] <= 0:
    if res['apollo.velocity'][-1] >= -10:
        message = "Landed"
    else:
        message = "Crashed"
else:
    message = "Still flying"

pyplot.figure(1)

plots = ['apollo.altitude', 'apollo.thrust', 'apollo.velocity']

for i in range(len(plots)):
    pyplot.subplot(len(plots), 1, i+1)
    pyplot.plot(res['time'], res[plots[i]])
    pyplot.title(plots[i])
    pyplot.grid(True)

pyplot.suptitle(message)
pyplot.show()

