#Script to plot and compare spin flip matrix elements
#along a k path

import matplotlib.pyplot as plt
import numpy as np

#import data from files. Columns are band indexes, rows are equally spaced k points

mel_x = np.loadtxt('mel_u666.dat', unpack = 'true')

#mel_x = np.loadtxt('ed_u666_ibnd2.dat', unpack = 'true')
mel_xp = np.loadtxt('mel_u666_ibnd2.dat', unpack = 'true')

#delta = mel_x - mel_xp #difference between two symmetry lines
#fracdelta = np.divide(delta, mel_x)

#k = np.linspace(0.05,1,20)
k = np.array(range(372)) #k point index

locs=[0, 86, 186, 265, 371]
labels=['L', r'$\Gamma$', 'X', 'K', r'$\Gamma$']
plt.xticks(locs, labels)
plt.tick_params(axis='both', direction = 'in', labelsize = 12)
plt.xlabel('k', size='12')
plt.ylabel(r"$|M_{n'k'nk}^{\Uparrow \Downarrow}|$ (Ryd)")
plt.margins(0)

for i in range(8,16):
    
    #plt.semilogy(k, mel_x[i], '+', markersize='4', label=f'Band {i+1}')
    plt.semilogy(k, mel_xp[i], 'o', markersize='2', label=f'Band {i+1}')
    #plt.plot(k, mel_x[i], '+', markersize='2', label=f'Band {i+1}')
    #plt.plot(k, mel_xp[i], 'v', markersize='2', label=f'Band {i+1}')
    #plt.plot(k, fracdelta[i], linewidth =0.5, label='x-mx')
    
    #plt.ylim(0,0.04)
    
    
    
plt.legend(loc = 'best', ncol=2, fontsize=8)
    
plt.savefig('sup_u56_gtox.pdf')

#print(mel_x[15,49], mel_xp[15,49], delta[15,49])
#print(np.max(mel_x))