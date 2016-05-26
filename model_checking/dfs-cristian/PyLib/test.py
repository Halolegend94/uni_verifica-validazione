from RandomActionGenerator import RandomActionGenerator
import matplotlib.pyplot as plt
c = RandomActionGenerator([[54, 60], [5, 250], [0, 12], [34, 50]])

for i in c.randomMatrix(10, 10):
    print i
