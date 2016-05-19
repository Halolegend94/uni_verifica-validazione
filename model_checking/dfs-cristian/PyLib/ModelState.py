from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys
import os

class ModelState:

    #constructor
    #PARAMS:
    #   - statekeys: the set of variables that define the state of a model
    #   - getdict: used to get and set the parameters of the model
    #   - inputs: array of variables that represents input to the model
    #   - sysName: the name of the main class of the system
    #   - tumeStempVarName. the name of the timestep variable in the environment model
    #   - admissibleVar: the name of the variable that store the admissibility of a state
    #   - unsafeVar: the name of the variable inside the monitor that establishes id the system is unsafe
    def __init__(self, statekeys, getdict, inputs, sysName, timeStepVarName, admissibleVar, unsafeVar):
        #set the instance variables
        # statekeys is used to get and set parameters inside the model
        self.statekeys = statekeys
        self.TimeZero = 0
        self.TimeStep = 1
        self.t = 0 #current time in TimeStep stemps
        
        #this dictionary is used to get variables values using the names
        #of their correspondent parameters.
        self.getdict = getdict
        self.inputs = inputs
        #compile the model
        model_files = [f for f in os.listdir(".") if ".mo" in f]
        fmu = compile_fmu(sysName, model_files)
        self.model = load_fmu(fmu)
        self.opts = self.model.simulate_options()
        self.opts['result_handling'] = 'memory'
        self.opts['CVode_options']['verbosity'] = 50 # No output
        self.TimeStep = self.model.get(timeStepVarName)
        return


    #simulation times
    def start_time(self):
        return self.t * self.TimeStep

    def end_time(self):
        return ((self.t + 0.99999) * self.TimeStep)

    #functions to get and set parameters
    def model_get(self, key):
        return self.model.get(self.getdict[key])

    def model_set(self, key, value):
        self.model.set(key, value)
        return

    #advance the model
    def model_next(self):
        res = self.model.simulate(start_time=self.start_time(), final_time=self.end_time(), options=self.opts)
        return

    #get the state of the entire model
    def get_model_state(self):
        x = {}
        for k in self.statekeys:
            x[k] = self.model_get(k)
        return x

    #manipulate time
    def get_init_time(self):
        return self.TimeZero

    def advance_time(self, mtime):
        return mtime + 1

    def set_model_time(self, time):
        self.t = time
        return

    def set_model_state(self, x):
        for k in self.statekeys:
            self.model_set(k, x[k])
        return

    def set_model_input(self, act):
        ind = 0
        for i in inputs:
            self.model_set(i, act[ind++])
        return

    #check if the sate is admissible
    def isAmissible(self, x):
        return x[admissibleVar]

    #check if the state is unsafe
    def isUnsafe(self, x):
        return x[unsafeVar]

    def get_model_next_state(self, x = None, a = None):
        if(x == None):
            return self.get_model_state()
        else:
            self.model.reset()
            self.set_model_state(x)
            self.set_model_input(a)
            #self.set_model_time(mytime)
            # compute next state
            self.model_next()
            return self.get_model_state()
