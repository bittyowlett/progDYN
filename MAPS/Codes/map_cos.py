import numpy as np
import matplotlib.pyplot as plt 

seedlist = [0, 0.2, 0.4, 0.6, 0.8];

for seed in seedlist:
    r = 1
    x0 = seed 
    x = [x0]
    it = 30
    i=1
    while i<it:
        rel = np.cos(r*x0) 
        x.append(rel)
        x0 = rel
        i += 1

    n = np.linspace(1,it,it)
    plt.plot(n,x,label='seed=%s'%seed)
    
plt.xlabel("n (number of steps)")
plt.ylabel("x(n+1)")
plt.legend()
plt.title("Time series for $x_{n+1}=cos(x_n)$")
plt.show()