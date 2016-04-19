#! /usr/bin/python

# Import compiler function
from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import sys
import logging
from mypylib.search import Search

#logging.basicConfig(filename='prova.log', level=logging.INFO)
logging.basicConfig(level=logging.INFO)

s = Search()

s.dfs()

