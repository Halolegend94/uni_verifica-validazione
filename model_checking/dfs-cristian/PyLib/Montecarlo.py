from pymodelica import compile_fmu
from pyfmi import load_fmu
import math
from RandomActionGenerator import RandomActionGenerator
import sys
class Montecarlo:

    def __init__(self, files, modelName, input_vars, limits, simTime, numPoints, unsafeVar):
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

    def verify(self, delta, epsilon, onlyExtremes, verbose, param_names = None, param_values = None, mat = None):

        #generate M input matrices or use the give ones
        matrices = None
        if mat != None:
            matrices = mat
        else:
            #compute number of trials
            M = int(math.ceil(math.log(delta) / math.log(1 - epsilon)))
            #create a random matrix generator
            gen = RandomActionGenerator(self.limits)

            matrices = []
            for i in xrange(M):
                matrices.append(gen.randomMatrix(self.simulationTime, self.timePoints, onlyExtremes))

        result = []
        if verbose:
            print "Starting {} simulations..".format(M)
        i = 0
        for distMatrix in matrices: #run M simulations
            if verbose:
                print "Simultation: {}/{}                \r".format(i + 1,len(matrices)),
            i = i+1
            sys.stdout.flush()
            #print distMatrix
            input_object = (self.input_vars, distMatrix)
            #set params, if any
            if param_names != None:
                j = 0
                for c in param_names:
                    self.model.set(c, param_values[j])

            self.model.initialize()
            res = self.model.simulate(start_time=0, final_time=self.simulationTime, input=input_object, options=self.opts)

            #check if there is an unsafe state
            y = self.model.get(self.unsafeVar)[0]
            if y == 1:
                result.append(distMatrix)
            self.model.reset()
        if verbose:
            print ""
        return result;
