#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:18:59 2023

@author: mmijjum
"""

import mcadam
import matplotlib.pyplot as plt
import numpy as np
import os
import Read

#SET DIRECTORY
os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)

#Fig. 1
# means = mcadam.means
# time = np.linspace(0,70,281)

# y2  =np.repeat(5.45,len(time))
# plt.plot(time, mcadam.means, c = 'cornflowerblue', label = 'This Model')
# plt.plot(time, y2, '--',c = 'darkblue', label = 'long-term average (Lifton et al., 2014)')
# plt.xlabel('Time [Ma]')
# plt.ylabel('Paleointensity [Am^2 * 10^22]')
# plt.legend()
# plt.savefig(directory+'/plots/Prospectus/magnetic_field_variations.png', dpi = 300, bbox_inches='tight')


#Fig. 2

time = np.linspace(0,70,281)
# IN = Pmag_paleolat.pl_df.iloc[0]
# IN.to_csv(directory+'/plots/IN.csv') 
# sf_india = scaling_factor.Siteprod_df.iloc[0]
# sf_india.to_csv(directory+'/plots/sf_IN.csv') 
# sf_india_const = scaling_factor.Siteprod_df.iloc[0]
# sf_india_const.to_csv(directory+'/plots/sf_IN_const.csv') 

# SA = Pmag_paleolat.pl_df.iloc[1]
# SA.to_csv(directory+'/plots/SA.csv') 
# sf_sa = scaling_factor.Siteprod_df.iloc[1]
# sf_sa.to_csv(directory+'/plots/sf_SA.csv') 

# GL = Pmag_paleolat.pl_df.iloc[2]
# GL.to_csv(directory+'/plots/GL.csv') 
# sf_GL = scaling_factor.Siteprod_df.iloc[2]
# sf_GL.to_csv(directory+'/plots/sf_GL.csv') |

# AF = Pmag_paleolat.pl_df.iloc[3]
# AF.to_csv(directory+'/plots/AF.csv') 
# sf_AF = scaling_factor.Siteprod_df.iloc[3]
# sf_AF.to_csv(directory+'/plots/sf_AF.csv') 

fig, (ax1,ax2) = plt.subplots(1,2, sharex = True, figsize=(18, 6))

ax1.plot(time,Read.IN.iloc[:,1], c = 'darkblue', label = 'India, 20N, 73E')
ax1.tick_params(axis='both', which='major', labelsize=22)
ax2.plot(time, Read.SA.iloc[:,1], 'darkgreen', label = 'South America: 19S, 69W')
ax2.tick_params(axis='both', which='major', labelsize=22)

plt.savefig(directory+'/plots/prospectus/paleolat_subplots.png', dpi = 300, bbox_inches='tight')
