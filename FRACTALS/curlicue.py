import matplotlib.pyplot as plt
import math

s = math.e
seg_length = 1.
Nmax = 15000
eps = [0.]
phi = [0.]
X = [0.]
Y = [0.]

for step in range(Nmax):
	epsn = eps[-1]
	phin = phi[-1]
	epsnp1 = (epsn+2.*math.pi*s) % (2.*math.pi)
	phinp1 = epsn + (phin%(2.*math.pi))
	eps.append(epsnp1)
	phi.append(phinp1)
	X.append(X[-1]+seg_length*math.cos(phinp1))
	Y.append(Y[-1]+seg_length*math.sin(phinp1))


plt.plot(X,Y,'g')
plt.gca().set_aspect('equal', adjustable='box')
plt.title("s="+str(s))
plt.show()
