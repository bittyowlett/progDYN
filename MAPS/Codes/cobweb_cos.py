import numpy as np 
import matplotlib.pyplot as plt 

xplot = np.linspace(-2,2,40)
plt.plot(xplot,np.sin(xplot),'b',label='y=sin(x)')
plt.plot(xplot,xplot,'--b',label='y=x')
plt.legend()

seed = 0.2
x = [x0]

i=1
while i<1000:
 rel = np.sin(x0) 
 x.append(rel)
 x0 = rel
 A1 = np.array([])
 i += 1









plt.show()