#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:21:32 2023

@author: mmijjum
"""



import numpy as np
import pandas as pd
import Read
import muons
import neutron_spallation
import proton_spallation
import scaling_factor
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
erosion = 5*(10**-3) #cm/yr, per Dunai (2010)
dt = 250000
rho = 2.32
if Read.system == 1:
    slhl = 1 * (91.6318 + 14.7771) #1 = qtz non dimensional scaling factor, from Greg's make_consts
if Read.system == 2:
    slhl = 1.369 * (80.1750 + 13.0628) #1.369 = LSDn non-dimensional correction factor (excluding a data point from calibration dataset, per Marissa)
if Read.system == 3:
    slhl = 1.369 * (80.1750 + 13.0628) #1.369 = LSDn non-dimensional correction factor (excluding a data point from calibration dataset, per Marissa)
if Read.system == 4:
    slhl = 1.272 * (11.8702 + 1.6269) #1.272 = non dimensional scaling factor, from Greg's make_consts
texposures = np.arange(1000,600000,100000)
z = shielding.z_df
z0 = Read.z_from_surface
concentrations = []
pn_df = neutron_spallation.pn_df
sthick = shielding.S_thick[0]
n = len(texposures)
sthick_updated = [item for item in sthick for i in range(n)]
n0_updated= [item for item in n0 for i in range(n)]

if Read.muons == 'True': 
    
    Pmu = muons.pmuons_df

    def func(sthick,tempvals):
        return sthick*slhl*tempvals
    
    for k in range(len(texposures)):      
        for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
            for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
                if dt < texposures[k]:
                    dt = texposures[k]
                temp = (scaling_factor.Siteprod_df.iloc[i][j]* np.exp(-erosion*texposures[k]/lambdasp) * dt)
                tempvals.append(temp)

    
    tempvals_df = pd.DataFrame([(tempvals[n:n+len(Read.time)]) for n in range(0, len(tempvals), len(Read.time))])
    #muons part

    for k in range(len(texposures)):
        for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
            for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
                temp = Pmu[j][i] * (erosion * texposures[k] + (shielding.z_df[j][i])/2) * dt
                tempvalsmu.append(temp)
        
    tempvals_df_mu = pd.DataFrame([(tempvalsmu[n:n+len(Read.time)]) for n in range(0, len(tempvalsmu), len(Read.time))])
        
    iteration = []
    for i in range(len(tempvals_df)):
        x = tempvals_df.iloc[i][0]
        y = tempvals_df_mu.iloc[i][0]
        # for j in range(len(tempvals_df.iloc[0])):
        #     l = func(sthick_updated[i],x) + y
        #     if l < n0_updated[i]:
        #         x += tempvals_df.iloc[i][j+1]
        #         y += tempvals_df_mu.iloc[i][j+1]
        #     else:
        #         iteration.append(j)
        #         break
           
    # exp_age = []
    # a = []
    # b = []
    # for i in range (len(tempvals_df)):
    #     a = (np.sum(tempvals_df.iloc[i][0:iteration[i]]))
    #     b = (np.sum(tempvals_df_mu.iloc[i][0:iteration[i]]))
    #     dt2 = (n0[i] - (sthick[i] *slhl * a) - (Pmu.iloc[i][iteration[i]] * b)) / ((sthick[i]*slhl) + Pmu.iloc[i][iteration[i]]) 
    #     expage = iteration[i] * dt + dt2
    #     exp_age.append(expage)


# if Read.muons == 'True': 
    
#     for j in range(len(texposures)):
#         for i in range(len(Read.site_lat)):
#             for k in range(len(Read.time)):
#                 if texposures[j] <= dt:
#                     Cspall = (shielding.S_thick[0][i]*(pn_df[k][i] + proton_spallation.pp_df[2][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*texp_bin1[j]))
#         #         Cmuons = muons.pmuons_df[2][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*texp_bin1[j]))
#         #         Ctot = Cspall + Cmuons
#         #         concentrations.append(Cspall + Cmuons)
            
# for j in range(len(texp_bin2)):
#     for i in range(len(Read.site_lat)):
#         Cspall = (shielding.S_thick[0][0]*(neutron_spallation.pn_df[2][i] + proton_spallation.pp_df[2][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[1][i] + proton_spallation.pp_df[1][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*(texp_bin2[j] - dt)))
#         Cmuons = muons.pmuons_df[2][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*dt)) + muons.pmuons_df[1][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*(texp_bin2[j]-dt)))
#         Ctot = Cspall + Cmuons
#         concentrations.append(Cspall + Cmuons)
        
# for j in range(len(texp_bin3)):
#     for i in range(len(Read.site_lat)):
#         Cspall = (shielding.S_thick[0][0]*(neutron_spallation.pn_df[2][i] + proton_spallation.pp_df[2][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[1][i] + proton_spallation.pp_df[1][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[0][i] + proton_spallation.pp_df[0][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*(texp_bin3[j]-2*dt)))
#         Cmuons = muons.pmuons_df[2][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*dt)) + muons.pmuons_df[1][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*(dt))) +  muons.pmuons_df[0][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*(texp_bin3[j]-2*dt)))
#         Ctot = Cspall + Cmuons
#         concentrations.append(Cspall + Cmuons)
        
# c10k = concentrations[0:7] #all predicted concentrations (fpj) for 7 samples at one exposure age (len: exp ages)
# c50k = concentrations[7:14]
# c100k = concentrations[14:21]
# c150k = concentrations[21:28]
# c200k = concentrations[28:35]
# c250k = concentrations[35:42]
# c300k = concentrations[42:49]
# c350k = concentrations[49:56]
# c400k = concentrations[56:63]
# c450k = concentrations[63:70]
# c500k = concentrations[70:77]
# c510k = concentrations[77:84]
# c520k = concentrations[84:91]
# c530k = concentrations[91:98]
# c540k = concentrations[98:105]
# c550k = concentrations[105:112]
# c600k = concentrations[112:119]

# fmj = [2380000,2630000,2750000,330000,730000,340000,590000]

# chi = [560000,590000,570000,550000,540000,600000,560000]



# temp1 = []
# temp2 = []
# temp3 = []
# temp4 = []
# temp5 = []
# temp6 = []
# temp7 = []
# temp8 = []
# temp9 = []
# temp10 = []
# temp11 = []
# temp12 = []
# temp13 = []
# temp14 = []
# temp15 = []
# temp16 = []
# temp17 = []


# for i in range(len(c10k)):
#     temp1.append(((c10k[i] - fmj[i]) / chi[i])**2)
#     temp2.append(((c50k[i] - fmj[i]) / chi[i])**2)
#     temp3.append(((c100k[i] - fmj[i]) / chi[i])**2)
#     temp4.append(((c150k[i] - fmj[i]) / chi[i])**2)
#     temp5.append(((c200k[i] - fmj[i]) / chi[i])**2)
#     temp6.append(((c250k[i] - fmj[i]) / chi[i])**2)
#     temp7.append(((c300k[i] - fmj[i]) / chi[i])**2)
#     temp8.append(((c350k[i] - fmj[i]) / chi[i])**2)
#     temp9.append(((c400k[i] - fmj[i]) / chi[i])**2)
#     temp10.append(((c450k[i] - fmj[i]) / chi[i])**2)
#     temp11.append(((c500k[i] - fmj[i]) / chi[i])**2)
#     temp12.append(((c510k[i] - fmj[i]) / chi[i])**2)
#     temp13.append(((c520k[i] - fmj[i]) / chi[i])**2)
#     temp14.append(((c530k[i] - fmj[i]) / chi[i])**2)
#     temp15.append(((c540k[i] - fmj[i]) / chi[i])**2)
#     temp16.append(((c550k[i] - fmj[i]) / chi[i])**2)
#     temp17.append(((c600k[i] - fmj[i]) / chi[i])**2)


# chisq1 = (1/7) * np.sum(temp1)
# chisq2 = (1/7) * np.sum(temp2)
# chisq3 = (1/7) * np.sum(temp3)
# chisq4 = (1/7) * np.sum(temp4)
# chisq5 = (1/7) * np.sum(temp5)
# chisq6 = (1/7) * np.sum(temp6)
# chisq7 = (1/7) * np.sum(temp7)
# chisq8 = (1/7) * np.sum(temp8)
# chisq9 = (1/7) * np.sum(temp9)
# chisq10 = (1/7) * np.sum(temp10)
# chisq11 = (1/7) * np.sum(temp11)
# chisq12 = (1/7) * np.sum(temp12)
# chisq13 = (1/7) * np.sum(temp13)
# chisq14 = (1/7) * np.sum(temp14)
# chisq15 = (1/7) * np.sum(temp15)
# chisq16 = (1/7) * np.sum(temp16)
# chisq17 = (1/7) * np.sum(temp17)