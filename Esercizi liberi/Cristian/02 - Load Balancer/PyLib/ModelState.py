from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt

class ModelState:

    #constructor
    def __init__(self):
        #set the instance variables
        # statekeys is used to get and set parameters inside the model
        self.statekeys = ['e.avg0', 'e.adm0', 'e.n0', 'e.depth0', 'm.y0', 's.x0'];

        self.getdict = {}
        self.getdict['e.avg0'] = x
