# importing matplotlib module for the plot
import matplotlib.pyplot as plot
# importing random module to generate random integers for the plot
import random
# initialising the lists
x = [0]
y = [0]
# initialising a variable to zero to track position
current = 0
for i in range(1, 100000):
   # generating a random integer between 1 and 100
   z = random.randint(1, 100)
   # checking the z range and appending corresponding values to x and y
   # appending values to the x and y
   if z == 1:
      x.append(0)
      y.append(0.16 * y[current])
   if z >= 2 and z <= 86:
      x.append(0.85 * x[current] + 0.04 * y[current])
      y.append(-0.04 * x[current] + 0.85 * y[current] +1.6)
   if z>= 87 and z<= 93:
      x.append(0.2 * x[current] - 0.26 * y[current])
      y.append(0.23 * x[current] + 0.22*(y[current])+1.6)
   if z >= 94 and z <= 100:
      x.append(-0.15 * x[current] + 0.28 * y[current])
      y.append(0.26 * x[current] + 0.24 * y[current] + 0.44)
   # incrementing the current value
   current += 1
# plotting the graph using x and y
plot.scatter(x, y, s = 0.2, edgecolor = 'blue')
plot.xlabel('x')
plot.ylabel('y')
plot.show()