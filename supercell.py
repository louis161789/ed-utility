import numpy as np

# Bohr unit
lat = 10.2612
bohr2ang = 0.529177249
# convert from Bohr to angstrom
lat = lat * bohr2ang

# lattice vectors in lat unit
lat_vec = np.array([[-0.500000,0.000000,0.500000],
                    [0.000000,0.500000,0.500000],
		    [-0.500000,0.500000,0.000000]])
# convert to angstrom
lat_vec = lat_vec*lat

# basis: crystal unit
basis = np.array([[0.000000,0.000000,0.000000],
                  [0.250000,0.250000,0.250000]])

# supercell size
nx = 4; ny = 4; nz = 4

natom = len(basis)

site = np.zeros([natom,3],dtype = np.float64)

for ia in range(natom):
    site[ia] = basis[ia][0]*lat_vec[0] + basis[ia][1]*lat_vec[1] + basis[ia][2]*lat_vec[2]

print lat/bohr2ang*nx
print natom*nx*ny*nz

for iz in range(nz):
    for iy in range(ny):
        for ix in range(nx):
	    move = ix*lat_vec[0] + iy*lat_vec[1] + iz*lat_vec[2]
            for ia in range(natom):
	        pos = site[ia] + move
                print "Si  {:14.8f}   {:14.8f}   {:14.8f}".format(pos[0],pos[1],pos[2])

