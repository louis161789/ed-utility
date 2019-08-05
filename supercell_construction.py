#Script to construct atomic positions in a large supercell.
#Output contains atomic positions 
#in the format for use in QE input files

import numpy as np

#b is the basis
#a1, a2, a3 are lattice vectors

b = np.asarray([[0, 0, 0], [0.25, 0.25, 0.25]])
a1 = np.asarray([[1, 0,0], [1, 0, 0]])
a2 = np.asarray([[0, 1, 0], [0, 1, 0]])
a3 = np.asarray([[0, 0, 1], [0, 0, 1]])

#In order to tranform crystal coordiantes into Cartesian coordinates, we
#need a transformation matrix.
T_crys_to_car = np.asarray([[-0.5, 0, 0.5], [0, 0.5, 0.5], [-0.5, 0.5, 0]])

# The supercell has n*m*l unit cells; i=0-(n-1); j=0-(m-1); k=0-(l-1) only 
# for n=m case. a is the lattice constant in the unit of angstoms. c1 is the
# smallest unit cell (Angstrom). c2 is the height of the unit cell (Angstrom).
n = 8
m = 8
l = 8
c1 = 5.43 # experimental value 
#c1 = 5.4 % converged value
a_1 = n * c1
a_2 = m * c1
a_3 = l * c1

#lattice const in Bohr (for QE input celldm(1))
celldm_1=a_1/0.529177

#print atomic positions in Cartesian coords.
#Useful for xyz file format - formatted in correct way (12 numbers, 8 after dp)

print('Lattice constant for supercell (Bohr):')
print(celldm_1, '\n')

print('Cartesian coordinates (angstrom):')
for k in range(l):
    for j in range(m):
        for i in range(n):
            atom_position_crys= np.divide((b+i*a1+j*a2+k*a3),np.asarray([[n, m, l], [n, m, l]]))
            atom_position_car= np.multiply(np.asarray([[a_1, a_2, a_3],[a_1, a_2, a_3]]), 
                                           atom_position_crys @ T_crys_to_car)
            for x in range(len(b)):
                print('Si','{:12.8f} {:12.8f} {:12.8f}'.format(*atom_position_car[x])) 
