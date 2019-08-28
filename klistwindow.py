#script to choose selected k points from a k grid
#output new k grid for nscf calc


import numpy as np

kgrid = np.loadtxt('kgrid200.hole.cart.dat',skiprows=2, usecols=[0,1,2])  #initial k grid
winind = np.loadtxt('window_indices.hole.200.cart.dat', dtype=int)       #indices of k points to select

newkgrid = []

#add only select elements to new grid
for j in range(len(winind)):
    newkgrid.append(kgrid[winind[j]-1,:])   #fortran arrays index from 1 

newkgrid=np.asarray(newkgrid)


#print new k points
#print('K_POINTS tpida')
print('K_POINTS crystal')
print(len(newkgrid))
for i in range(len(newkgrid)):
    print('{0:9.6f} {1:9.6f} {2:9.6f} {3:9.6f}'.format(*newkgrid[i,:], 1.0/len(newkgrid)))
