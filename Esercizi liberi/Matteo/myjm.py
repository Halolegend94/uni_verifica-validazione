from pymodelica import compile_fmu
from pyfmi import load_fmu

import matplotlib.pyplot as plt

def load(moduleName, moduleFile):
    return load_fmu(compile_fmu(moduleName,moduleFile))

def plot(res, *vs):
    plt.figure(1)
    for i, v in enumerate(vs):
        plt.subplot(len(vs),1,i+1)
        plt.title(v)
        plt.plot(res['time'], res[v])
        plt.grid()
    plt.show()
