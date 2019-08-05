#Plot Si band structure with SOC 

import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
 
plt.margins(0)
plt.ylabel("Energy (eV)", fontsize=18)
plt.xlabel("k", weight ='bold', fontsize=18)
#set axis labels
locs=[0.0, 0.8660, 1.8660, 2.8660, 4.2802]
labels=['L', r'$\Gamma$', 'X', 'K', r'$\Gamma$']
plt.xticks(locs, labels)
plt.tick_params(axis='both', direction = 'in', labelsize = 18)
plt.hlines(0,0,4.2802, colors='k', linestyle='dashed', linewidth= 0.75)
plt.text(4.2802,0, r'$E_F$', verticalalignment = 'center', fontsize = 15)



from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
axins = zoomed_inset_axes(ax, 22, loc=4) # zoom-factor, location

for i in range(24):
    #load data (default delimiter is whitespace)
    x = pd.read_csv('sibands.dat.gnu', delimiter ='\s+', skiprows=(i*82), nrows=81, header =None)
    x[1] = x[1] - 6.2453 
    #plot bands
    ax.plot(x[0], x[1], linewidth = 0.5, c='b')


    axins.plot(x[0],x[1], linewidth = 0.5, c='b')



x1, x2, y1, y2 = 0.845, 0.885, -0.2, 0.1 # specify the limits
axins.set_xlim(x1, x2) # apply the x-limits
axins.set_ylim(y1, y2) # apply the y-limits
plt.yticks([])
plt.xticks([])

from mpl_toolkits.axes_grid1.inset_locator import mark_inset
mark_inset(ax, axins, loc1=3, loc2=1, fc="none", ec="0.5")

fig = plt.gcf()
fig.set_size_inches(10, 6)
plt.savefig("bands_vc.png")



