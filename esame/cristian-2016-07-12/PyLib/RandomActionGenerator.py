import random
import math
import numpy as N

class RandomActionGenerator:
    '''
    Description: this class is used to generate random sequences. Domains can be descrete and continuous.
    limits is an array of the form
        [
            [isDiscrete, [values]], ...
        ]
    '''
    def __init__(self, limits):
        self.length = len(limits);
        self.limits = limits;
        return

    '''
    Description: generate a random sequence
    '''
    def randomSequence(self):
        out = [None] * self.length
        for i in xrange(self.length):
            if(self.limits[i][0] == 0): #the range is continuous
                minV = self.limits[i][1][0]
                maxV = self.limits[i][1][1]
                t = (maxV - minV)
                out[i] = minV + t * (random.uniform(0, 1))
            else:
                out[i] = self.limits[i][1][random.randint(0, len(self.limits[i][1]) - 1)]
        return out


    def randomMatrix(self, numSeconds, timepointsNumber):
        "create time column"
        timepoints = N.linspace(0., numSeconds, timepointsNumber) #create time points
        "create matrix rows"
        matrix = N.zeros((timepointsNumber, self.length + 1))
        for i in xrange(timepointsNumber):
            row = self.randomSequence()
            matrix[i][0] = timepoints[i]
            for j in xrange(self.length):
                matrix[i][1 + j] = row[j]
        return matrix
