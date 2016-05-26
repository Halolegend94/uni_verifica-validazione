from RandomActionGenerator import RandomActionGenerator
import matplotlib.pyplot as plt
c = RandomActionGenerator(1, [[0, 20]])
out = []
for i in range(10000):
    out += c.next()

plt.hist(out, 20)
plt.show()
