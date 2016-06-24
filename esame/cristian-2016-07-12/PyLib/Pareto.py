import math
import sys
import numpy
import os
from pymodelica import compile_fmu
from pyfmi import load_fmu
from ActionGenerator import ActionGenerator
from RandomActionGenerator import RandomActionGenerator
from PyLib.Montecarlo import Montecarlo

class Pareto:

    def __init__(self, model_files, modelName, parameters, values, inputs, limits, monitor_var, sim_time, timepoints):
        self.mca = Montecarlo(model_files, modelName, inputs, limits, sim_time, timepoints, monitor_var)
        self.monitor = monitor_var
        self.params = parameters
        self.timepoints = timepoints
        self.values = values
        self.limits = limits
        self.inputs = inputs
        self.simTime = sim_time
        return
    '''
    kpiFunctions: array that has the following format
        [
        function, [param indexes]
        ...
        ]
    '''
    def findFrontier(self, delta, epsilon, kpiFunctions):
        act = ActionGenerator(self.values)
        #compute number of trials
        M = int(math.ceil(math.log(delta) / math.log(1 - epsilon)))
        #create a random matrix generator
        gen = RandomActionGenerator(self.limits)
        matrices = []
        for i in xrange(M):
            matrices.append(gen.randomMatrix(self.simTime, self.timepoints, onlyExtremes))

        '''
        output format: list of vectors of the type
            [# errors found, parameters' values, is on the frontier] if on the frontier ->  #errors = 0
        '''

        mca_outputs = [] #used to store run results
        current = act.next()
        print "starting {} * {} = {} simulations..".format(act.cardinality, M, M*act.cardinality)
        i = 0
        while(current != None): #for each combination of parameters..
            result = self.mca.verifyInputs(delta, epsilon, False, self.params, current, matrices)
            print "set {} of {} done.               \r".format(i+1, act.cardinality),
            mca_outputs.append([len(result), current])
            current = act.next()
            i+=1
        print ""

        #compute params kpi values
        print "computing kpi values.."
        mappedKPIs = []
        for val in mca_outputs:
            params = val[1] #get parameters' values
            mappedKPIsRow = []
            for kpiFunc in kpiFunctions:
                func = kpiFunc[0]
                selectedParams = []
                for ind in kpiFunc[1]:
                    selectedParams.append(params[ind])
                compVal = func(selectedParams)
                mappedKPIsRow.append(compVal)
            mappedKPIs.append(val + [mappedKPIsRow])

        #now we can compute the frontier
        print "computing the frontier.."
        output = []
        numrows = len(mappedKPIs)
        numcols = len(mappedKPIs[0][2])
        for i in xrange(numrows):
            undomined = False
            if mappedKPIs[i][0] == 0: #parameters valid
                undomined = True
                for k in xrange(numrows):
                    if mappedKPIs[k][0] > 0 or k == i: #params not valid
                        continue
                    t = False
                    for j in xrange(numcols):
                        if mappedKPIs[i][2][j] > mappedKPIs[k][2][j]:
                            t = True #i non dominato da k
                            break
                    undomined = undomined and t
                    if undomined == False: #i dominato da k
                        break #non serve continuare il confronto
            output.append(mappedKPIs[i] + [undomined])
        return output
