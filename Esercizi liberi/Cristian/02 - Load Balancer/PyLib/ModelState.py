from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys
import os

class ModelState:

    #constructor
    def __init__(self):
        #set the instance variables
        # statekeys is used to get and set parameters inside the model
        self.TimeStep = 1
        self.TimeZero = 0
        self.t = 0 #current time in TimeStep stemps

        self.statekeys = ['e.avg0', 'e.adm0', 'e.n0', 'e.depth0', 'm.y0', 's.x0'];

        #this dictionary is used to get variables values using the names
        #of their correspondent parameters.
        self.getdict = {}
        self.getdict['e.avg0'] = 'e.current.avg'
        self.getdict['e.adm0'] = 'e.current.adm'
        self.getdict['e.n0'] = 'e.current.n'
        self.getdict['e.depth0'] = 'e.current.depth'
        self.getdict['m.y0'] = 'm.y'
        self.getdict['s.x0'] = 's.x'
        self.getdict['e.d.noise0'] = 'e.d.noise'
        self.getdict['e.d.failures0'] = 'e.d.failures'

        #Now we set all the possible disturbs
        self.actList = [[-1, 0.0, 1], [-1, 0.0, 1]];

        #compile the model
        model_files = [f for f in os.listdir(".") if ".mo" in f]
        fmu = compile_fmu("ClosedSystem", model_files)
        self.model = load_fmu(fmu)
        self.opts = self.model.simulate_options()
        self.opts['result_handling'] = 'memory'
        self.opts['CVode_options']['verbosity'] = 50 # No output
        self.TimeStep = self.model.get('e.T')
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

    def get_init_time(self):
        return self.TimeZero

    def advance_time(self, mtime):
        return mtime + 1

    def set_model_time(self, time):
        self.t = time
        return

    def init_actions(self):
        a = {}
        #set index values, -1 is a special value used as mark
        a['i1'] = -1
        a['i2'] = -1
        a['v1'] = -1
        a['v2'] = -1
        return a

    def next_action(self, a):
        if(a['i2'] < len(self.actList[1]) - 1):
            a['i2'] = a['i2'] + 1
            a['v2'] = self.actList[1][a['i2']]
            return 1
        elif(a['i1'] < len(self.actList[0]) - 1):
            a['i2'] = 0;
            a['v2'] = self.actList[1][0]
            a['i1'] = a['i1'] + 1
            a['v1'] = self.actList[0][a['i1']]
            return 1
        else:
            return 0

    def set_model_state(self, x):
        for k in self.statekeys:
            self.model_set(k, x[k])
        return

    def set_model_input(self, a):
        self.model_set('e.noise0', a['v1'])
        self.model_set('e.failures0', a['v2'])
        return

    #check if the sate is admissible
    def adm(self, x):
        return x['e.adm0']

    #check if the state is unsafe
    def isUnsafe(self, x):
        return x['m.y0']

    def get_model_next_state(self, x = None, a = None):
        if(x == None):
            self.model_next()
            return self.get_model_state()
        else:
            self.model.reset()
            self.set_model_state(x)
            self.set_model_input(a)
            #self.set_model_time(mytime)
            # compute next state
            self.model_next()
            return self.get_model_state()
