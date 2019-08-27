#plot k points in 3D


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# reciprocal lattice vectors in cartesian coordinations in 2pi/a unit where a: lattice constant
#rec_vec = np.array([[-1.000000,-1.000000,1.000000],
#                    [1.000000,1.000000,1.000000],
#		    [-1.000000,1.000000,-1.000000]])

################################
def crystocart(grid):    #transform from crystal to cartesian

    #transform to cartesian 
    grid_cartx= -grid[0,:]+grid[1,:]-grid[2,:]
    grid_carty= -grid[0,:]+grid[1,:]+grid[2,:]
    grid_cartz= grid[0,:]+grid[1,:]-grid[2,:]
    grid_cart=np.asarray([grid_cartx,grid_carty,grid_cartz])
    return grid_cart

#################################

#import data (in crystal coords)
grid = np.loadtxt('kgrid200.zvalley.dat', unpack='true',skiprows=2, usecols=[0,1,2])
#grid = np.loadtxt('kgrid50.dat', unpack='true',skiprows=2, usecols=[0,1,2])

grid = crystocart(grid)     #uncomment if input k list is in crystal coords





#plot 3d figure
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(grid[0], grid[1], grid[2])

plt.show()