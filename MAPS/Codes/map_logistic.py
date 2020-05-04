import numpy as np 
import matplotlib.pyplot as plt 
import time

start_time = time.time()
seed = 0.1;
r = 3.8282;

x0 = seed 
x = [x0]
N = 2000
i=1
while i<N:
 rel = r*x0*(1-x0)
 x.append(rel)
 x0 = rel
 i += 1



n = np.linspace(1,N,N)
plt.plot(n,x)
plt.xlabel("n (number of steps)")
plt.ylabel("x(n+1)")
plt.title("Window of chaos between periodicity at r=3.8282")
plt.show()

print("--- %s seconds ---" % (time.time() - start_time))