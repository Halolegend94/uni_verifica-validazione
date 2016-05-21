from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys
import os

class ModelState:

    #constructor
    #PARAMS:
    #   - statekeys: the set of variables that define the state of a model
    #   - params: array of variables that represents input to the model
    #   - getdict: used to get variables of the model throungh associated parameters
    #   - sysName: the name of the main class of the system
    #   - tumeStempVarName. the name of the timestep variable in the environment model
    #   - admissibleVar: the name of the variable that store the admissibility of a state
    #   - unsafeVar: the name of the variable inside the monitor that establishes id the system is unsafe
    def __init__(self, statekeys, params, getdict, sysName, timeStepVarName, admissibleVar, unsafeVar):
        #set the instance variables
        self.statekeys = statekeys
        self.getdict = getdict
        self.params = params

        self.TimeZero = 0
        self.TimeStep = 1
        self.t = 0 #current time in TimeStep stemps

        #compile the model
        model_files = [f for f in os.listdir(".") if ".mo" in f]
        fmu = compile_fmu(sysName, model_files)
        self.model = load_fmu(fmu)

        self.opts = self.model.simulate_options()
        self.opts['result_handling'] = 'memory'
        self.opts['CVode_options']['verbosity'] = 50 # No output

        self.TimeStep = self.model.get(timeStepVarName) #Update timestep
        return


    #simulation times
    def __start_time(self):
        return self.t * self.TimeStep

    def __end_time(self):
        return ((self.t + 0.99999) * self.TimeStep)

    #functions to get and set parameters
    def model_get(self, key):
        return self.model.get(self.getdict[key])

    #get the state of the entire model
    def get_model_state(self):
        x = {}
        for k in self.statekeys:
            x[k] = self.model.get(self.getdict[k])
        return x

    #manipulate time
    def get_init_time(self):
        return self.TimeZero

    def advance_time(self, mtime):
        return mtime + 1

    def set_model_time(self, time):
        self.t = time
        return

    #manipulate model state and params
    def set_model_state(self, x):
        for k in self.statekeys:
            self.model.set(k, x[k])
        return

    def set_model_params(self, act):
        ind = 0
        for i in self.params:
            self.model.set(i, act[ind])
            ind += 1
        return


    def get_model_next_state(self, x = None, a = None, mytime = None):
        if(x == None):
            return self.get_model_state()
        else:
            self.model.reset()
            self.set_model_state(x)
            self.set_model_params(a)
            self.set_model_time(mytime)
            # compute next state
            self.model.simulate(start_time=self.__start_time(), final_time=self.__end_time(), options=self.opts)
            return self.get_model_state()


    #check if the sate is admissible
    def isAdmissible(self, x):
        return x[admissibleVar]

    #check if the state is unsafe
    def isUnsafe(self, x):
        return x[unsafeVar]
