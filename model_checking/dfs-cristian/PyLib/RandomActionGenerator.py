import random
import math
import numpy as N

class RandomActionGenerator:
    "This class is used to generate random inputs."
    "If x1, x2, ..., xn are the inputs, limits is a list of couples (min, max)"
    def __init__(self, limits):
        self.length = len(limits);
        self.limits = limits;
        return

    def randomSequence(self):
        out = [None] * self.length
        for i in range(self.length):
            minV = self.limits[i][0]
            maxV = self.limits[i][1]
            t = (maxV - minV)
            out[i] = minV + t * (random.randint(0, 1000) / 1000.0)
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
