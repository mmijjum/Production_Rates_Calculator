#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:30:21 2023

@author: mmijjum
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:26:50 2023

@author: mmijjum
"""

import numpy as np
import pandas as pd
import Read
import muons
import neutron_spallation
import proton_spallation
import shielding
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)
n0 = Read.nuclide_concentration


tempvals = []
tempvalsmu = []
lambdasp = 160 #effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
lambdamu = 1300 #muon attenuation length in at/g/yr (Balco supplementary)
erosion = 20*(10**-3) #cm/yr, per Dunai (2010)
dt = 250000
rho = 2.32

texp_bin1 = [10000,50000,100000,150000,200000,250000]
texp_bin2 = [300000,350000,400000,450000,500000]
texp_bin3 = [510000,520000,530000,540000,550000,600000]

z0 = np.arange(0,100,2)
concentrations = []


    
# for i in range(len(z0)):
#     Cspall = (shielding.S_thick[0][0]*(neutron_spallation.pn_df[0][i] + proton_spallation.pp_df[0][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[1][i] + proton_spallation.pp_df[1][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt))
#     Cmuons = muons.pmuons_df[0][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*dt)) + muons.pmuons_df[1][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*(dt))) 
#     Ctot = Cspall + Cmuons
#     concentrations.append(Cspall + Cmuons)
# np.savetxt(directory+"/text_for_plots/lib_20e3.csv", 
#             concentrations,
#             delimiter =", ", 
#             fmt ='% s')



plt.plot(z0,Read.lib3e3[0], c = 'darkblue', label=r'3$\times 10^{-3}$ cm/yr')
plt.plot(z0,Read.lib10e3[0], c = 'cornflowerblue', label = r'10$\times 10^{-3}$ cm/yr')
plt.plot(z0,Read.lib20e3[0], c = 'teal',label = r'20$\times 10^{-3}$ cm/yr')
x = [15,15,15,35,45,35,55]
y = [2380000.00,2630000.00,2750000.00,330000.00,730000.00,340000.00,590000.00]

plt.scatter(15,2380000.00, c = 'midnightblue', alpha = 0.7)
e = [560000.00,
590000.00,
570000.00,
550000.00,
540000.00,
600000.00,
560000.00]

ex = [2,2,2,2,2,2,2]
plt.errorbar(x,y, xerr = ex, yerr=e, fmt='o',color = 'k', markersize = 4)
plt.scatter(15,2630000.00, c = 'midnightblue', alpha = 0.7)
plt.scatter(15,2750000.00, c = 'midnightblue', alpha = 0.7)


plt.scatter(35,330000.00, c = 'midnightblue', alpha = 0.7)
plt.scatter(45,730000.00, c = 'midnightblue', alpha = 0.7)
plt.scatter(35,340000.00, c = 'midnightblue', alpha = 0.7)
plt.scatter(55,590000.00, c = 'midnightblue', alpha = 0.7)
plt.legend()
plt.xlim(0,100)
plt.ylim(0,5e6)
plt.xlabel('Depth below surface (cm)', fontsize = 12)
plt.ylabel('Concentration (atoms/g)', fontsize = 12)
plt.savefig(Read.directory+'/plots/Figure_10.pdf', dpi = 300, bbox_inches='tight')
