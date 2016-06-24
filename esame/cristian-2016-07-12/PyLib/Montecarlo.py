from pymodelica import compile_fmu
from pyfmi import load_fmu
import math
from RandomActionGenerator import RandomActionGenerator
import sys
'''
Description: this class performs Montecarlo model checking on inputs or parameters (not both).
Parameters:
    -   files: model files (.mo)
    -   modelName: the name of the root model to be run
    -   input_vars: array containing the names of the inputs to be provided randomly
    -   parameter_vars: array containing the names of the parameters whose values to be provided randomly
    -   limits: array of arrays, each having 2 elements to determine a continuous interval, or n elements,
        associated with a flag to indicate a continuous or discrete domain.
    -   discrete: used to indicate if the values must be choosen in a continuous space or a discrete one
    -   simTime: simulation time
    -   numPoints: number of points in input functions
    -   unsafeVar: monitor var
'''
class Montecarlo:

    def __init__(self, files, modelName, input_vars, parameter_vars, limits, simTime, numPoints, unsafeVar):
        if len(input_vars) == len(parameter_vars) and len(input_vars) == 0:
            print "Error: you need to specify some input vars or parameter vars"
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
        self.parameter_vars = parameter_vars
        self.input_vars = input_vars
        return

    '''
    Description: apply montecarlo unsing the following parameters:
        -   delta: probability of finding an error
        -   epsilon: error margin
        -   verbose: if yes, print some information during execution
        -   param_names and values: used to set parameters (used in Pareto)
        -   mat: precomputed random matrix (used in Pareto)
    '''
    def verifyInputs(self, delta, epsilon, verbose, param_names = None, param_values = None, mat = None):

        randValues = []
        #generate M input matrices or use the give ones
        matrices = None
        M = int(math.ceil(math.log(delta) / math.log(1 - epsilon)))

        if mat != None:
            matrices = mat
        else:
            #compute number of trials
            #create a random matrix generator
            gen = RandomActionGenerator(self.limits)

            matrices = []
            for i in xrange(M):
                matrices.append(gen.randomMatrix(self.simulationTime, self.timePoints))

        result = []
        if verbose:
            print "Starting {} simulations..".format(M)
        i = 0
        for distMatrix in matrices: #run M simulations
            if verbose:
                print "Simultation: {}/{}".format(i + 1,len(matrices))
            i = i+1
            sys.stdout.flush()
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

    def verifyParams(self, delta, epsilon, verbose):
        if(len(self.parameter_vars) != len(self.limits)):
            print "input_vars and limits lengths differ"
            return

        randValues = []
        gen = RandomActionGenerator(self.limits)
        #compute number of trials
        M = int(math.ceil(math.log(delta) / math.log(1 - epsilon)))
        for i in xrange(M):
            randValues.append(gen.randomSequence())

        result = []
        if verbose:
            print "Starting {} simulations..".format(M)
        i = 0

        for seq in randValues: #run M simulations
            if verbose:
                print "Simultation: {}/{} using {}                \r".format(i + 1,len(randValues), seq),
            i += 1
            sys.stdout.flush()

            #set params
            j = 0
            for c in self.parameter_vars:
                self.model.set(c, seq[j])
                j += 1

            self.model.initialize()
            res = self.model.simulate(start_time=0, final_time=self.simulationTime, options=self.opts)

            #check if there is an unsafe state
            y = self.model.get(self.unsafeVar)[0]
            if y == 1:
                result.append(seq)
            self.model.reset()
        if verbose:
            print ""
        return result;
