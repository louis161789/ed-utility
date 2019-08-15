#Plot spin relaxation times vs carrier energy
#
#

import matplotlib.pyplot as plt
import numpy as np

#safely divide by zero
def divzero(x,y):
    if y==0: return 0
    return x/y


condmin = 6.7827    #conduction band minimum
#energy relative to condmin
energy = np.loadtxt('srt_cbmin_wind_1.dat', usecols=0) - condmin      
invsrt = np.loadtxt('srt_cbmin_wind_1.dat', usecols=1)
srt = np.zeros(len(energy))


for i in range(len(energy)):
    srt[i] = divzero(1,invsrt[i]) * 1000    #convert to ms
    

plt.plot(energy, srt, '+', label = 'Vacancy')
#plt.semilogy(energy,srt, '+')

#plt.ylim([0,2])
#plt.yticks([0,0.2])
locs=[0, 0.05, 0.1]
labels=[r'$\varepsilon_C$', r'$\varepsilon_C$ + 50', r'$\varepsilon_C$ + 100']
plt.xticks(locs, labels)
plt.tick_params(axis='both', direction = 'in', labelsize = 15)
plt.xlim(-0.02, 0.1)
plt.vlines(0,0,np.max(srt), linewidth=1)
plt.xlabel('Carrier Energy (meV)', size = 15)
plt.ylabel('Spin Relaxation Time (ms)', size = 15)
plt.margins(0)
plt.tight_layout()
plt.legend(fontsize=12)

#plt.savefig('srtenergy.cbmin_wind.pdf')
