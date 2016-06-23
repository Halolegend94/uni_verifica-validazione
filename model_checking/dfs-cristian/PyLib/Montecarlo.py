from pymodelica import compile_fmu
from pyfmi import load_fmu
import math
from RandomActionGenerator import RandomActionGenerator
import sys
class Montecarlo:

    def __init__(self, files, modelName, input_vars, limits, simTime, numPoints, unsafeVar, param_names = None, param_values = None):
        if len(input_vars) != len(limits):
            print "input_vars and limits lengths differ"
            return
        fmu = compile_fmu(modelName, files)
        self.model = load_fmu(fmu)
        self.opts = self.model.simulate_options()
        self.opts = self.model.simulate_options()
        self.opts['result_handling'] = 'memory'
        self.opts['CVode_options']['verbosity'] = 100 # No output
        self.opts['initialize'] = False # No output
        self.unsafeVar = unsafeVar
        self.length = len(limits)
        self.limits = limits
        self.simulationTime = simTime
        self.timePoints = numPoints
        self.input_vars = input_vars
        return

    def verify(self, delta, epsilon, onlyExtremes):
        #set some variables

        #compute number of trials
        M = int(math.ceil(math.log(delta) / math.log(1 - epsilon)))
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
        return result;
