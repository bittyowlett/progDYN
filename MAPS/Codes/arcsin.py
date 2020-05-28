import numpy as np 
import matplotlib.pyplot as plt 


a = np.linspace(-5,5,50)
xs=[]
xsdot=[]
x = 2
for i in range(50):
    f =  np.arcsin(x/a[i])
    fdot = np.cos(f)
    xs.append(f)
    xsdot.append(fdot)
print(a)
print(xs)
plt.plot(a,xs,'b')
plt.plot(a,xsdot,'r')
plt.show()