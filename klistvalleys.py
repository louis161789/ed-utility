#script to choose selected k points from a k grid
#output new k grid for nscf calc


import numpy as np

kgrid = np.loadtxt('newkgrid200.tight.dat',skiprows=2, usecols=[0,1,2])  #initial k grid



newkgrid = []

#add only select elements to new grid
for j in range(len(kgrid)):
    if ((kgrid[j,1] < -0.3) and (kgrid[j,2] < -0.3)):
        newkgrid.append(kgrid[j,:])   #fortran arrays index from 1 

newkgrid=np.asarray(newkgrid)


#print new k points
#print('K_POINTS tpida')
print('K_POINTS crystal')
print(len(newkgrid))
for i in range(len(newkgrid)):
    print('{0:9.6f} {1:9.6f} {2:9.6f} {3:9.6f}'.format(*newkgrid[i,:], 1.0/len(newkgrid)))
