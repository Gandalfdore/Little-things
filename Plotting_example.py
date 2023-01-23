# -*- coding: utf-8 -*-
"""
PLOTTER TOOLS

@author: MOON_PENGUIN
"""
import numpy as np
import matplotlib.pyplot as plt


plt.style.use('coolplot.mplstyle')

x = np.linspace(0,1,100)
y = np.linspace(0,1,100)

# ------------------Using simple plt-----------------------

# plt.plot (x,y)

# ------------------Using axis-----------------------

fig1, (ax1) = plt.subplots(1, 1, figsize = (5, 3.5), dpi = 200)   ## define a plot

ax1.plot(x,y,'-', color='#ffe24e',linewidth=1.5, label='Some legend info')                     ## input data (x, y, errorbars, legend label, etc.)
# ax1.errorbar(x, y, yerr=y/100, xerr=x/100, fmt="o",linewidth=1.5, label='Some legend info')


ax1.set_xlabel('$A$ $Label$ $(units)$', fontsize=12)      ## Axis labels
ax1.set_ylabel('$A$ $Label$ $(units)$', fontsize=12)

# ax1.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)         ## Makingthe tickers look nice
# ax1.tick_params(direction='in', which='major', length=6)
# ax1.tick_params(direction='in', which='minor', length=3)


# ax1.set_xlim([0,1])       ## Setting the limits of the axis to show and the scales
# ax1.set_ylim([0,1])
# ax1.set_yscale('log')


# plt.tight_layout()   ## use if you have multiple plots in one figure

plt.legend()    
plt.show()             ## plot

# fig1.savefig('Something.png')   


