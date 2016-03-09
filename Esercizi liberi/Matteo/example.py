# Import the function for compilation of models and the load_fmu method
from pymodelica import compile_fmu
from pyfmi import load_fmu

# Import the plotting library
import matplotlib.pyplot as plt

# Compile model
fmu_name = compile_fmu("example","example.mo")

# Load model
vdp = load_fmu(fmu_name)

# simulate(MoonLanding, stopTime=230)
res = vdp.simulate(final_time=10)

plt.figure(1)

plt.plot(res['time'], res['x'], res['time'], res['y'])

plt.show()
