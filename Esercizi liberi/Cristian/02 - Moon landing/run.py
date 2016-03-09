from pymodelica import compile_fmu
from pyfmi import load_fmu
from matplotlib import pyplot

model_name="MoonLanding"

model_files = ["MoonLanding.mo", "Body.mo", "CelestialBody.mo", "Rocket.mo","CalculateThrust.mo", "Autopilot.mo"]
model_path = compile_fmu(model_name, model_files)
model = load_fmu(model_path)

res = model.simulate(options={'ncp':10000})

pyplot.figure(1)
plots = ['apollo.altitude', 'apollo.thrust', 'apollo.velocity', 'apollo.acceleration']

for i in range(len(plots)):
	pyplot.subplot(len(plots), 1, i + 1)
	pyplot.plot(res['time'], res[plots[i]])
	pyplot.title(plots[i])
	pyplot.grid(True)


pyplot.show()
