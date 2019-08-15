#Script to create uniformly distributed k points around a particular point
#for k points around band extrema
#for crystal units in QE



import numpy as np

density = 20                #1D equivalent density to calculate for (NxNxN)

k0 = 0.84                          #central k point (kx dir)
width =  0.16                          #length of sampling cube in recip. space
N =  int(density*width)                   #no. of sample points in 1D (NxNxN)

step = width/N                        #spacing between k points


k_init=np.zeros(3)-width/2 + step/2       


#translation vectors for crystal coordinates
kx=np.asarray([k0/2,k0/2,0])
kmx=-kx
ky=np.asarray([0,k0/2,k0/2])
kmy=-ky
kz=np.asarray([k0/2,0,k0/2])
kmz=-kz


#print out k points in format for nscf calculations
print('K_POINTS crystal')
print(N*N*N*6)
for x in range(N):
    for y in range(N):
        for z in range(N):
            print('{:9.6f} {:9.6f} {:9.6f} {:9.6f}'.format(kx[0]+k_init[0]+step*x, kx[1]+k_init[1]+step*y, kx[2]+k_init[2]+step*z, 1.0/(N*N*N*6)))
            print('{:9.6f} {:9.6f} {:9.6f} {:9.6f}'.format(kmx[0]+k_init[0]+step*x, kmx[1]+k_init[1]+step*y, kmx[2]+k_init[2]+step*z, 1.0/(N*N*N*6)))
            print('{:9.6f} {:9.6f} {:9.6f} {:9.6f}'.format(ky[0]+k_init[0]+step*x, ky[1]+k_init[1]+step*y, ky[2]+k_init[2]+step*z, 1.0/(N*N*N*6)))
            print('{:9.6f} {:9.6f} {:9.6f} {:9.6f}'.format(kmy[0]+k_init[0]+step*x, kmy[1]+k_init[1]+step*y, kmy[2]+k_init[2]+step*z, 1.0/(N*N*N*6)))
            print('{:9.6f} {:9.6f} {:9.6f} {:9.6f}'.format(kz[0]+k_init[0]+step*x, kz[1]+k_init[1]+step*y, kz[2]+k_init[2]+step*z, 1.0/(N*N*N*6)))
            print('{:9.6f} {:9.6f} {:9.6f} {:9.6f}'.format(kmz[0]+k_init[0]+step*x, kmz[1]+k_init[1]+step*y, kmz[2]+k_init[2]+step*z, 1.0/(N*N*N*6)))
            



