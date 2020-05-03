import numpy as np
import matplotlib.pyplot as plt 

seed = 1;

x0 = seed 
x = [x0]

i=1
while i<1000:
 rel = np.sin(x0) 
 x.append(rel)
 x0 = rel
 i += 1

n = np.linspace(1,1000,1000)
plt.plot(n,x)
plt.xlabel("n (number of steps)")
plt.ylabel("x(n+1)")
plt.show()
