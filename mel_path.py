#Script to plot and compare spin flip matrix elements
#along a k path

import matplotlib.pyplot as plt
import numpy as np

#import data from files. Columns are band indexes, rows are equally spaced k points

mel_x = np.loadtxt('path_new.g1.degen.dat', unpack = 'true')
mel_xp = np.loadtxt('path_new_g1.dat', unpack = 'true')
#mel_xpp = np.loadtxt('mel_u444.dat', unpack = 'true')

rydtoev = 13.60569
mel_x = mel_x*rydtoev
mel_xp = mel_xp*rydtoev

#symtest=np.flip(mel_x, 1) - mel_xp
#ratio= symtest/mel_xp

#mel_xred = np.zeros([8,125])
#mel_xpred = np.zeros([8,125])

#for j in range(0,15,2):
#    mel_xred[j//2] = mel_x[j,:] + mel_x[j+1,:]
#    mel_xpred[j//2] = mel_xp[j,:] + mel_xp[j+1,:]



#delta = mel_xred - mel_xpred #difference between two symmetry lines
#fracdelta = np.divide(delta, mel_x)

#k = np.linspace(0.05,1,20)
k = np.array(range(379)) #k point index
#k = np.array(range(125)) #k point index
#k=np.array([1,2])

for i in range(8,10):
    
    plt.semilogy(k, mel_x[i], '+', markersize='3', label=f'Band 1 to {i+1}')
    #plt.semilogy(k, mel_xp[i], 'v', markersize='3', label=f' Band 2 to {i+1}', color=f'C{i%8}')
    #plt.semilogy(k, mel_xpp[i], 'x', markersize='3', label=f'444 Band {i+1}', color=f'C{i%8}')
    #plt.semilogy(k, abs(symtest[i]), '+', markersize='3', label=f'Absolute Diff Band 9 to {i+1}')
    #plt.semilogy(k, abs(ratio[i]), '+', markersize='3', label=f'Fractional Diff Band 9 to {i+1}')
    #plt.plot(k, mel_x[i], '+', markersize='2', label=f'666 Band {i+1}')
    #plt.plot(k, mel_xp[i], 'o', markersize='2', label=f'555 Band {i+1}')
    #plt.plot(k, mel_xpp[i], 'o', markersize='2', label=f'444 Band {i+1}')
    #plt.plot(k, delta[i], linewidth =0.5, label='down/up - up/down')
    
    
    #plt.xlim(50,250)
    #plt.ylim(0,0.04)

#for i in range(7,8):    
#    
#    plt.semilogy(k, mel_x[i], '+', markersize='3', label=f'666 Band {i+1}', color=f'C{i%8}')
#    plt.semilogy(k, mel_xp[i], 'v', markersize='3', label=f'555 Band {i+1}', color=f'C{i%8}')
#    plt.semilogy(k, mel_xpp[i], 'x', markersize='3', label=f'444 Band {i+1}', color=f'C{i%8}')

#plt.xlabel('Coarse Grid', size = 18)

locs=[0, 100, 215, 256, 378]
labels=['L', r'$\Gamma$', 'X', 'K', r'$\Gamma$']
plt.xticks(locs, labels)
plt.tick_params(axis='both', direction = 'in', labelsize = 15)
plt.xlabel(r'$\mathbf{k}$', size = 18)
plt.ylabel(r"$|M_{n',n}^{\Uparrow \Downarrow}\left(\mathbf{k'},\Gamma\right)|$ (eV)", size = 18)
plt.minorticks_off()    
#plt.yticks([1e-8,1e-2])
plt.margins(0)
plt.tight_layout()    
plt.legend(loc = 'lower right', ncol=1, fontsize=8)
plt.minorticks_off()    

#plt.savefig('mel_coarse_78.pdf')
#plt.show()

#print(mel_x[15,49], mel_xp[15,49], delta[15,49])
#print(np.max(mel_x))