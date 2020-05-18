import numpy as np 
import matplotlib.pyplot as plt 


a = np.linspace(1,5,50)
xs=[]
x = 1
for i in range(50):
    f =  np.arcsin(x/a[i])
    xs.append(f)
print(a)
print(xs)
plt.plot(a,xs)
plt.show()