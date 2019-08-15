#plot k points in 3D


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#import data (in crystal coords)
grid = np.loadtxt('kgrid20.dat', unpack='true',skiprows=2, usecols=[0,1,2])

# reciprocal lattice vectors in cartesian coordinations in 2pi/a unit where a: lattice constant
rec_vec = np.array([[-1.000000,-1.000000,1.000000],
                    [1.000000,1.000000,1.000000],
		    [-1.000000,1.000000,-1.000000]])

#transform to cartesian 
grid_cartx= -grid[0,:]+grid[1,:]-grid[2,:]
grid_carty= -grid[0,:]+grid[1,:]+grid[2,:]
grid_cartz= grid[0,:]+grid[1,:]-grid[2,:]
grid_cart=np.asarray([grid_cartx,grid_carty,grid_cartz])


#plot 3d figure
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(grid_cartx, grid_carty, grid_cartz)

plt.show()