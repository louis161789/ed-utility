#Plot spin relaxation times vs k-grid density
#
#

import matplotlib.pyplot as plt
import numpy as np

#safely divide by zero
def divzero(x,y):
    if y==0: return 0
    return x/y


nk = np.loadtxt('kgridconv.cbmin.b5.dat', usecols=0)   
invsrt = np.loadtxt('kgridconv.cbmin.b5.dat', usecols=1)
srt = np.zeros(len(nk))
srttot = np.zeros(int(len(nk)/2))
invsrttot = np.zeros(int(len(nk)/2))
nkavg = np.zeros(int(len(nk)/2))

    
for j in range(0,len(nk),2):
    invsrttot[j//2] = (invsrt[j] + invsrt[j+1])
    srttot[j//2] = divzero(1,invsrttot[j//2]) * 1e6    #convert to micro seconds
    nkavg[j//2] = (nk[j] + nk[j+1])/2

for i in range(len(nk)):
    srt[i] = divzero(1,invsrt[i]) * 1e6    #convert to micro seconds


    
    
plt.plot(nkavg, srttot, '+', markersize = 8,label='Conduction Band Minimum')
plt.plot(nkavg, srttot, 'b', linewidth = 1)
plt.hlines(290.5,0,220,colors='k', linestyle='dashed', linewidth= 0.75)
#plt.plot(nk, srt, '+')
#plt.semilogy(nkavg,srttot, '+')

plt.ylim([280,300])
plt.yticks([280,290,300])
plt.tick_params(axis='both', direction = 'in', labelsize = 15)
plt.xlim(0, 220)
plt.xticks([0,50,100,150,200],['0',r'$50^{3}$',r'$100^{3}$',r'$150^{3}$',r'$200^{3}$'])
plt.xlabel(r'$\mathbf{k}$-grid density', size = 15)
plt.ylabel(r'Spin Relaxation Time ($\mu$s)', size = 15)
#plt.margins(0)
plt.tight_layout()
plt.legend(fontsize=12)

#plt.savefig('srtconv.cbmin.pdf')
