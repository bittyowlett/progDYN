
import matplotlib.pyplot as plt
import numpy as np


def x_np1(x,r):
    return r*np.sin(x)

def Iterate(func,times,x0,r):
    x = [x0]

    for i in range(times):
        x.append(func(x[-1],r))

    return x

 
R = np.linspace(0,10,1001)

data_r = []
data_y = []

for r in R:
    # Initial 1000 iteration
    x_init = Iterate(x_np1,1000,0.5,r)

    # Next 1000 iterations
    x_data = Iterate(x_np1,1000,x_init[-1],r)
   
    for x in x_data:
        data_r.append(r)
        data_y.append(x)

plt.plot(data_r,data_y,"b.",markersize=0.2)
plt.xlabel(r'$\alpha$')
plt.ylabel("x*")
plt.title('Orbit diagram for $x_{n+1} = $' r'$\alpha sin(x)$'  )
plt.show()





