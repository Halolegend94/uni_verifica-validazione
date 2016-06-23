from pymodelica import compile_fmu
from pyfmi import load_fmu
import math
from RandomActionGenerator import RandomActionGenerator
import sys

class Pareto

    def __init__(self, model_files, parameters, values, inputs, limits, monitor_var, sim_time, timepoints, delta, epsilon):
        fmu = compile_fmu(modelName, model_files)
        self.model = load_fmu(fmu)
        self.opts = self.model.simulate_options()
        self.opts = self.model.simulate_options()
        self.opts['result_handling'] = 'memory'
        self.opts['CVode_options']['verbosity'] = 100 # No output
        self.opts['initialize'] = False # No output
        self.monitor = monitor_var
        self.params = params
        self.timepoints = timepoints
        self.values = values
        self.limits = limits
        self.inputs = inputs
        self.delta = delta
        self.epsilon = epsilon
        self.simTime = sim_time
        return

    def findPoints(self):
        gen = RandomActionGenerator(self.limits)
        self.act = ActionGenerator(values)
        current = act.next()
        while(current != None):
            #set parameters to the model
            i = 0
            for p in observed_vars:
                self.model.set(p, current[i])
                i = i + 1

            #simulations
            #compute number of trials
            M = int(math.ceil(math.log(self.delta) / math.log(1 - self.epsilon)))
            #create a random matrix generator
            gen = RandomActionGenerator(self.limits)
            result = []
            print "Starting {} simulations..".format(M)
            for i in xrange(M): #run M simulations
                print "Simultation: {}/{}                \r".format(i + 1, M),
                sys.stdout.flush()
                #set up input object
                distMatrix = gen.randomMatrix(self.simulationTime, self.timePoints, onlyExtremes)
                #print distMatrix
                input_object = (self.input_vars, distMatrix)
                self.model.initialize()
                res = self.model.simulate(start_time=0, final_time=self.simulationTime, input=input_object, options=self.opts)

                #check if there is an unsafe state
                y = self.model.get(self.unsafeVar)[0]
                if y == 1:
                    result.append(res) #run number and input sequence at failure time
                self.model.reset()
            print ""
            distMatrix = gen.randomMatrix(self.simTime, self.timepoints, False)
            #print distMatrix
            input_object = (self.inputs, distMatrix)
            self.model.initialize()
            res = self.model.simulate(start_time=0, final_time=self.simTime, input=input_object, options=self.opts)

            #check if there is an unsafe state
            y = self.model.get(self.monitor_var)[0]
            if y == 1:
                result.append(res) #run number and input sequence at failure time
            self.model.reset()
