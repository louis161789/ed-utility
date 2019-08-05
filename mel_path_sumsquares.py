#Script to plot sum of squares of spin flip matrix elements
#along a k path

import matplotlib.pyplot as plt
import numpy as np


#import data from files. Columns are band indexes, rows are equally spaced k points
#unpack transposes this into arrays
mel_ns = np.loadtxt('ed_nonspinor.dat')
sqmel_ns= np.square(mel_ns)
sum_sqmel_ns=np.sum(sqmel_ns,1)
sqrt_sum_sqmel_ns=np.sqrt(sum_sqmel_ns)

mel_x = np.loadtxt('ed_u666.dat',usecols = (0,1,2,3,4,5,6,7),unpack = 'true')
mel_xp= np.loadtxt('ed_u666_ibnd2.dat', usecols= (0,1,2,3,4,5,6,7), unpack = 'true')
sqmel_x= np.square(mel_x)
#sqmel_xp = 0
sqmel_xp= np.square(mel_xp)
sqmel= sqmel_x + sqmel_xp
sum_sqmel=np.sum(sqmel,0)
sqrt_sum_sqmel=np.sqrt(sum_sqmel)

k = np.array(range(372)) #k point index

plt.plot(k, sqrt_sum_sqmel, markersize='2', label='spinor')
plt.plot(k, sqrt_sum_sqmel_ns, markersize='2', label='non-spinor')
#plt.semilogy(k, sqrt_sum_sqmel, markersize='2', label='spinor')
#plt.semilogy(k,sqrt_sum_sqmel_ns, markersize='2', label='non-spinor')


locs=[0, 86, 186, 265, 371]
labels=['L', r'$\Gamma$', 'X', 'K', r'$\Gamma$']
plt.xticks(locs, labels)
plt.tick_params(axis='both', direction = 'in', labelsize = 12)
plt.xlabel('k', size='12')
plt.ylabel(r"$\sqrt{\sum_{nn'}{|M_{n'k'nk}}}|^2}$ (Ryd)")
plt.margins(0)
plt.tight_layout()

plt.legend(loc = 'best', fontsize=8)
    
#plt.savefig('ed_spinvnonspin_vb1.pdf')
