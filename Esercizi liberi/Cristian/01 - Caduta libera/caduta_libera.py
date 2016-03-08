from pymodelica import compile_fmu
from pyfmi import load_fmu

import matplotlib.pyplot as plt

fmu_name = compile_fmu("CadutaLibera", "caduta_libera.mo")
CadutaLibera = load_fmu(fmu_name)

res = CadutaLibera.simulate(final_time=200)
v = res['v']
p = res['p']
t = res['time']

plt.figure(1)
plt.plot(t, v)
plt.legend("velocita'")
plt.title("Velocita' in caduta libera")
plt.xlabel('tempo (s)')
plt.ylabel('Velocita (m/s)')
plt.figure(2)
plt.plot(t, p)
plt.legend('distanza')
plt.title('distanza  percorsa')
plt.xlabel('tempo')
plt.ylabel('distanza')
plt.show()

