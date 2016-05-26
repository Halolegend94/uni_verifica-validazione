import random
import math
class RandomActionGenerator:

    def __init__(self, length, limits):
        self.length = length;
        self.limits = limits;
        return

    def next(self):
        out = [None] * self.length
        for i in range(self.length):
            minV = self.limits[i][0]
            maxV = self.limits[i][1]
            t = (maxV - minV) / 2
            out[i] = self.limits[i][0] + t - t*math.sin(3.14*5*random.randint(0, 1000))
        return out
