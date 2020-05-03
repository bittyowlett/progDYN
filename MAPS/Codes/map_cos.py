import numpy as np
import matplotlib.pyplot as plt 

seed = 0.2;
r = 1
x0 = seed 
x = [x0]
it = 1000
i=1
while i<it:
 rel = np.cos(r*x0) 
 x.append(rel)
 x0 = rel
 i += 1

n = np.linspace(1,it,it)
plt.plot(n,x)
plt.xlabel("n (number of steps)")
plt.ylabel("x(n+1)")
plt.show()
