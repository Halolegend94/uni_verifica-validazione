# Script utlizzato per laciare i modelli
# Autore: Cristian Di Pietrantonio

# import necessari
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys
import os
import numpy as N

def input_function(t) :
    return N.array([10*N.sin(2*3.14*5*t), 10*N.cos(2*3.14*5*t)])


#funzione per plottare i dati
def plottaDati(rows, cols, arraydict, vals):
    # col 1
    fig = 1
    t = res['time']
    for i in range(0, len(arraydict)):

        plt.subplot(rows,cols, fig)
        plt.plot(t, vals[arraydict[i]])
        plt.grid()
        plt.title(arraydict[i])
        fig = fig + 1
    plt.show()


model_name="ClosedSystem"

#sono caricati tutti i file ".mo" nella cartella
model_files = [f for f in os.listdir(".") if ".mo" in f]

#input_object = (['noise', 'failures'], input_function)

model_comp = compile_fmu(model_name, model_files)
model = load_fmu(model_comp)
maxt = 10
res = model.simulate(start_time=0, final_time=maxt, options={'ncp':1000})

plottaDati(3, 2, ['s.x', 's.d.noise', 's.d.failures', 'm.y'], res)
