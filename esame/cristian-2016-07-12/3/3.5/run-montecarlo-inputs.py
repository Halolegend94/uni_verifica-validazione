#!/home/cristian/Sviluppo/JModelica2/jmodelica/bin/jm_ipython.sh
# Script utlizzato per laciare i modelli
# Autore: Cristian Di Pietrantonio

# import necessari
from pymodelica import compile_fmu
from pyfmi import load_fmu
import numpy as N
import os
import random
import math
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

m = Montecarlo(model_files,
                model_name,
                ['vr', 'vw'],
                [],
                [],
                100, #simulation time
                0,    #num points
                'm.y'   #unsafeVar
                );

# genera la matrice degli input
mat = []
nProve = int(math.ceil(math.log(delta) / math.log(1 - margin)))
timepoints = N.linspace(0., 100, 100) #create time points

for i in xrange(nProve):
    "create matrix rows"
    matrix = N.zeros((100, 3))
    j = 0
    while j < 100:
        matrix[j][0] = timepoints[j]
        matrix[j + 1][0] = timepoints[j + 1]
        matrix[j][1] =  4*random.random() + 1
        matrix[j + 1][1] =  6 - matrix[j][1]
        matrix[j][2] =  4*random.random() + 1
        matrix[j + 1][2] =  6 - matrix[j][2]
        j = j + 2
    mat.append(matrix)

results = m.verifyInputs(delta, margin, True, None, None, mat);
if len(results) > 0:
    print "Error found."
else:
    print "No error found with confidence {} and margin ".format(confidence, margin)
