import numpy as np 
import matplotlib.pyplot as plt 

def drawArrow(A, B):
    plt.arrow(A[0], A[1], B[0] - A[0], B[1] - A[1], head_width=0.03, length_includes_head=True)


xplot = np.linspace(-2,2,40)
plt.plot(xplot,np.cos(xplot),'b',label='y=cos(x)')
plt.plot(xplot,xplot,'--b',label='y=x')
plt.legend()

x0 = -1.5
x = [x0]

rel = np.cos(x0) 

A1=np.array([x0,0])
A2=np.array([x0,rel])
drawArrow(A1,A2)

A1=np.array([x0,rel])
A2=np.array([rel,rel])
drawArrow(A1,A2)

for i in range(1,20):
 rel2 = np.cos(rel)
 A3=np.array([rel,rel])
 A4=np.array([rel,rel2])
 drawArrow(A3,A4)
 A1=np.array([rel,rel2])
 A2=np.array([rel2,rel2])
 drawArrow(A1,A2)
 rel = rel2
 
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cobweb Diagram')
plt.show()