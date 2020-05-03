import numpy as np 
import matplotlib.pyplot as plt 
import time

start_time = time.time()             # start time of execution of code
seed = 0.1;                          # seed value or starting value

rnum = 5                           # number of values 'r' takes. 
rlist = np.linspace(0.1,4,rnum)        # array storing all values of 'r'

plt.figure()                         # generating a figure element beforehand
x0 = seed                            # assigning the first element as the seed
x = [x0]
N = 5                               # N: Total number of steps for which the map is generated 
xlist = []                           # creating an empty list to store all x(n+1) maps for all r's

              # here begins TWO while loops. one with i computes a x map with N steps 
              # another one with j evluates x's for all set of r's              

n = np.linspace(1,N,N)               # n represents the list containing the number of steps taken

for j in range(len(rlist)):
	for i in n:
		rel = rlist[j]*x0*(1-x0)
		x.append(rel) 
		x0 = rel
	xlist.append(x)

xlistarr = np.asarray(xlist)
print(n)

for i in range(0,N):
	#print(rlist)
	#print(xlistarr[:,i])
	plt.plot(rlist,xlistarr[:,i])
	
plt.show()

print("--- %s seconds ---" % (time.time() - start_time))
