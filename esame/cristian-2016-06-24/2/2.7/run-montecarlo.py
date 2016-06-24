#!/home/cristian/Sviluppo/JModelica2/jmodelica/bin/jm_ipython.sh
# Script utlizzato per laciare i modelli
# Autore: Cristian Di Pietrantonio

# import necessari
from pymodelica import compile_fmu
from pyfmi import load_fmu
import numpy as N
import os
import sys
sys.path.append("../../PyLib")
from PlotData import plotData
from Montecarlo import Montecarlo

#sono caricati tutti i file ".mo" nella cartella superiore (file in comune)
model_files = ["../" + f for f in os.listdir("..") if ".mo" in f]
#sono caricati tutti i file ".mo" nella cartella attuale
model_files += [ f for f in os.listdir(".") if ".mo" in f]
model_name="System"
#==============================================
#================ SETTINGS ====================
#==============================================
delta = 0.2;
confidence = 1 - delta;
margin = 0.2;

limits = [
    [0, [0, 2]],
    [0, [0, 8]]
]

m = Montecarlo(model_files,
                model_name,
                [],
                ['p1', 'p2'],
                limits,
                0.02, #simulation time
                0, #num points
                'v' #unsafeVar
                );

results = m.verifyParams(delta, margin, True)
if len(results) > 0:
    print "Error found."
    for trace in results:
        print trace
else:
    print "No error found with confidence "
