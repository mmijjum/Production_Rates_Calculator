#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:37:36 2023

@author: mmijjum
"""

import numpy as np
import pandas as pd
import Read
import scaling_factor
import neutron_spallation
import proton_spallation
import muons
import matplotlib.pyplot as plt
import os
import shielding

os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)
n0 = Read.nuclide_concentration


tempvals = []
tempvalsmu = []
lambdasp = 160 #effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
lambdamu = 1300 #muon attenuation length in at/g/yr (Balco supplementary)
erosion = 8.35*(10**-3) #cm/yr, per Dunai (2010)
dt = 250000
rho = 2.32

dt1= 49000
dt2=250000
dt3=201000

z0 = Read.z_from_surface
concentrations = []

for i in range(len(Read.site_lat)):
    Cspall = (shielding.S_thick[0][0]*(neutron_spallation.pn_df[0][i] + proton_spallation.pp_df[0][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt1)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[1][i] + proton_spallation.pp_df[1][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt2)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[2][i] + proton_spallation.pp_df[2][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*(dt3)))
    Cmuons = muons.pmuons_df[0][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*dt1)) + muons.pmuons_df[1][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*(dt2))) +  muons.pmuons_df[2][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*(dt3)))
    Ctot = Cspall + Cmuons
    concentrations.append(Cspall + Cmuons)


fmj = [2380000,2630000,2750000,330000,730000,340000,590000]

chi = [560000,590000,570000,550000,540000,600000,560000]



temp1 = []



for i in range(len(concentrations)):
    temp1.append(((concentrations[i] - fmj[i]) / chi[i])**2)



chisq1 = (1/7) * np.sum(temp1)

chisq_825neg3 = 1.8958398277837718
chisq_83neg3 = 1.8940127987215531
chisq_84neg3 = 1.8920344950891765
chisq_85neg3 = 1.892164398864299
chisq_875neg3 = 1.9008008464615083

# #CONST FIELD#
const_83= 1.8919117616165855
const_825 = 1.8924291623521552
const_85 =  1.8950029817745557

# plt.scatter(0,chisq_5neg3)
# plt.scatter(0,chisq_65neg3)
# plt.scatter(0,chisq_10neg3)
#plt.scatter(0,chisq_8neg3, label = 'erosion = 8e-3 cm/yr')
plt.scatter(0,chisq_83neg3, label = '8.3e-3')
plt.scatter(0,chisq_84neg3, label = '8.4e-3')

plt.scatter(0,chisq_85neg3, label = '8.5e-3')
plt.scatter(0,chisq_875neg3, label = '8.75e-3')

plt.scatter(0.5,const_83, marker = 's', label = 'constant 8e-3 cm/yr' )
plt.scatter(.5,const_825 , marker = 's',label = 'constant 8.25e-3 cm/yr')
plt.scatter(.5,const_85, marker = 's',label = 'constant 8.5e-3 cm/yr')

plt.ylabel('x^2')
plt.title('Chi square values for 500kyr exposure starting at 28.201 Ma')
plt.legend()
#plt.savefig(Read.directory+'/plots/chisq.png', dpi = 300, bbox_inches='tight')


# # # """FOR TESTING ONLY"""
# plt.plot(xaxis,yaxis, 'o-')  
# plt.xlabel('exposure age')
# plt.ylabel('chi squared')
# plt.plot(xaxis,yaxis, 'o-')
# plt.plot(depth,c10k)
# #plt.plot(depth,c500k)

# """FOR 2.5KM"""
# plt.plot(xaxis,Read.chisq_neg1003.values.tolist(), 'o-',label = "10*10^-3")
# plt.plot(xaxis,Read.chisq_neg625.values.tolist(), 'o-',label = "6.25*10^-3")
# plt.plot(xaxis,Read.chisq_neg53.values.tolist(), 'o-',label = "5*10^-3")
# plt.plot(xaxis,Read.chisq_neg73.values.tolist(), 'o-',label = "7*10^-3")

# plt.xlabel('Exposure Age [Years]')
# plt.ylabel('Chi Squared')
# plt.title('2.5 km above sea level')
# plt.legend()

# # plt.savefig(Read.directory+'/plots/chisq.png', dpi = 300, bbox_inches='tight')



