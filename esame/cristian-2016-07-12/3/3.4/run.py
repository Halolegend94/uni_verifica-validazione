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

#variables to be plotted
plot_vars = [
    'm.y'
]

#plotting settings
rows = 1
cols = 1


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
res = model.simulate(start_time=0, final_time=sim_time, options=opts)
#model.reset()

plotData(rows, cols, plot_vars, res)
