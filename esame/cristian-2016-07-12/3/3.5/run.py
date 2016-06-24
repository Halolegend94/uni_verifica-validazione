#!/home/cristian/Sviluppo/JModelica2/jmodelica/bin/jm_ipython.sh
# Script utlizzato per laciare i modelli
# Autore: Cristian Di Pietrantonio

# import necessari
from pymodelica import compile_fmu
from pyfmi import load_fmu
import numpy as N
import os
import sys
import random
import math
sys.path.append("../../PyLib")
from PlotData import plotData
from RandomActionGenerator import RandomActionGenerator

#sono caricati tutti i file ".mo" nella cartella superiore (file in comune)
model_files = ["../" + f for f in os.listdir("..") if ".mo" in f]
#sono caricati tutti i file ".mo" nella cartella attuale
model_files += [ f for f in os.listdir(".") if ".mo" in f]
model_name="System"
#==============================================
#================ SETTINGS ====================
#==============================================

#simulation time
sim_time = 100

timepoints = N.linspace(0., 100, 100) #create time points

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

inputs = (['vr', 'vw'], matrix)

#variables to be plotted
plot_vars = [
    'm.y', 'f.x', 'c.u'
]

#plotting settings
rows = 2
cols = 2


#==============================================
#================INPUT=========================
#==============================================
# def inputFunction(t):
#     return N.array([4 * 4 * t])
#
#
# inputs = (['input1'], [inputFunction])


# =============================================

## start simulation
model_comp = compile_fmu(model_name, model_files)
model = load_fmu(model_comp)
opts = model.simulate_options()

#opts['ncp'] = 1000 #Change the number of communication points
#opts['CVode_options']['maxh'] = 1.0e-7
#opts['initialize'] = False
#opts['CVode_options']['verbosity'] = 100 # No output

#model.initialize()
res = model.simulate(start_time=0, final_time=sim_time, input=inputs, options=opts)
#model.reset()

plotData(rows, cols, plot_vars, res)
