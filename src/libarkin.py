#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:26:50 2023

@author: mmijjum
"""

import numpy as np
import pandas as pd
import Read
import scaling_factor
import neutron_spallation
import proton_spallation
import Muons_v2
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
erosion = 5.6*(10**-3) #cm/yr, per Dunai (2010)
dt = 250000
rho = 2.32

texp_bin1 = [10000,40000,50000,100000,150000,200000,250000]
texp_bin2 = [260000,270000,280000,290000,300000,310000,330000,350000,400000,450000,500000]
texp_bin3 = [510000,520000,530000,540000,550000,600000,600200,620000,630000,640000,650000,750000]

z0 = Read.z_from_surface
concentrations = []
pmuons_df = Muons_v2.pmuons_df
for j in range(len(texp_bin1)):
    for i in range(len(Read.site_lat)):
        Cspall = (shielding.S_thick[0][0]*(neutron_spallation.pn_df[0][i] + proton_spallation.pp_df[0][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*texp_bin1[j]))
        Cmuons = pmuons_df[0][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*texp_bin1[j]))
        Ctot = Cspall + Cmuons
        concentrations.append(Cspall + Cmuons)
        
for j in range(len(texp_bin2)):
    for i in range(len(Read.site_lat)):
        Cspall = (shielding.S_thick[0][0]*(neutron_spallation.pn_df[0][i] + proton_spallation.pp_df[0][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[1][i] + proton_spallation.pp_df[1][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*(texp_bin2[j] - dt)))
        Cmuons = pmuons_df[0][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*dt)) + pmuons_df[1][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*(texp_bin2[j]-dt)))
        Ctot = Cspall + Cmuons
        concentrations.append(Cspall + Cmuons)
        
for j in range(len(texp_bin3)):
    for i in range(len(Read.site_lat)):
        Cspall = (shielding.S_thick[0][0]*(neutron_spallation.pn_df[0][i] + proton_spallation.pp_df[0][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[1][i] + proton_spallation.pp_df[1][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[2][i] + proton_spallation.pp_df[2][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*(texp_bin3[j]-2*dt)))
        Cmuons = pmuons_df[0][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*dt)) + pmuons_df[1][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*(dt))) +  pmuons_df[2][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*(texp_bin3[j]-2*dt)))
        Ctot = Cspall + Cmuons
        concentrations.append(Cspall + Cmuons)
        
c10k = concentrations[0:7] #all predicted concentrations (fpj) for 7 samples at one exposure age (len: exp ages)
c50k = concentrations[7:14]
c100k = concentrations[14:21]
c150k = concentrations[21:28]
c200k = concentrations[28:35]
c250k = concentrations[35:42]
c300k = concentrations[42:49]
c350k = concentrations[49:56]
c400k = concentrations[56:63]
c450k = concentrations[63:70]
c500k = concentrations[70:77]
c510k = concentrations[77:84]
c520k = concentrations[84:91]
c530k = concentrations[91:98]
c540k = concentrations[98:105]
c550k = concentrations[105:112]
c600k = concentrations[112:119]

fmj = [2380000,2630000,2750000,330000,730000,340000,590000]

chi = [560000,590000,570000,550000,540000,600000,560000]



temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []
temp7 = []
temp8 = []
temp9 = []
temp10 = []
temp11 = []
temp12 = []
temp13 = []
temp14 = []
temp15 = []
temp16 = []
temp17 = []


for i in range(len(c10k)):
    temp1.append(((c10k[i] - fmj[i]) / chi[i])**2)
    temp2.append(((c50k[i] - fmj[i]) / chi[i])**2)
    temp3.append(((c100k[i] - fmj[i]) / chi[i])**2)
    temp4.append(((c150k[i] - fmj[i]) / chi[i])**2)
    temp5.append(((c200k[i] - fmj[i]) / chi[i])**2)
    temp6.append(((c250k[i] - fmj[i]) / chi[i])**2)
    temp7.append(((c300k[i] - fmj[i]) / chi[i])**2)
    temp8.append(((c350k[i] - fmj[i]) / chi[i])**2)
    temp9.append(((c400k[i] - fmj[i]) / chi[i])**2)
    temp10.append(((c450k[i] - fmj[i]) / chi[i])**2)
    temp11.append(((c500k[i] - fmj[i]) / chi[i])**2)
    temp12.append(((c510k[i] - fmj[i]) / chi[i])**2)
    temp13.append(((c520k[i] - fmj[i]) / chi[i])**2)
    temp14.append(((c530k[i] - fmj[i]) / chi[i])**2)
    temp15.append(((c540k[i] - fmj[i]) / chi[i])**2)
    temp16.append(((c550k[i] - fmj[i]) / chi[i])**2)
    temp17.append(((c600k[i] - fmj[i]) / chi[i])**2)


chisq1 = (1/7) * np.sum(temp1)
chisq2 = (1/7) * np.sum(temp2)
chisq3 = (1/7) * np.sum(temp3)
chisq4 = (1/7) * np.sum(temp4)
chisq5 = (1/7) * np.sum(temp5)
chisq6 = (1/7) * np.sum(temp6)
chisq7 = (1/7) * np.sum(temp7)
chisq8 = (1/7) * np.sum(temp8)
chisq9 = (1/7) * np.sum(temp9)
chisq10 = (1/7) * np.sum(temp10)
chisq11 = (1/7) * np.sum(temp11)
chisq12 = (1/7) * np.sum(temp12)
chisq13 = (1/7) * np.sum(temp13)
chisq14 = (1/7) * np.sum(temp14)
chisq15 = (1/7) * np.sum(temp15)
chisq16 = (1/7) * np.sum(temp16)
chisq17 = (1/7) * np.sum(temp17)

#Read.chisq_neg203.idxmin()

xaxis = [10000,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000,510000,520000,530000,540000,550000,600000]
depth = [15,15,15,35,45,35,55]

# # """FOR TESTING ONLY"""
# yaxis = [chisq1,chisq2,chisq3,chisq4,chisq5,chisq6, chisq7,chisq8,chisq9,chisq10,chisq11,chisq12,chisq13,chisq14,chisq15,chisq16,chisq17]
# plt.plot(xaxis,yaxis, 'o-')  
# plt.xlabel('exposure age')
# plt.ylabel('chi squared')
# plt.plot(xaxis,yaxis, 'o-')
# plt.plot(depth,c10k)
#plt.plot(depth,c500k)

"""FOR 2.5KM"""
plt.plot(xaxis,Read.chisq_neg1003.values.tolist(), 'o-',label = "10*10^-3")
plt.plot(xaxis,Read.chisq_neg625.values.tolist(), 'o-',label = "6.25*10^-3")
plt.plot(xaxis,Read.chisq_neg53.values.tolist(), 'o-',label = "5*10^-3")
plt.plot(xaxis,Read.chisq_neg73.values.tolist(), 'o-',label = "7*10^-3")

plt.xlabel('Exposure Age [Years]')
plt.ylabel('Chi Squared')
plt.title('2.5 km above sea level')
plt.legend()

# plt.savefig(Read.directory+'/plots/chisq.png', dpi = 300, bbox_inches='tight')

""" FOR CONSTANT FIELD"""
# # plt.plot(xaxis,Read.SLchisq_neg53.values.tolist(), 'o-',label = "5*10^-3")
# # plt.plot(xaxis,Read.SLchisq_neg33.values.tolist(), 'o-',label = "3*10^-3")

# # plt.plot(xaxis,Read.SLchisq_neg3.values.tolist(), 'o-',label = "10^-3")
# #plt.plot(xaxis,Read.SLchisq_neg093.values.tolist(), 'o-',label = "0.9*10^-3")
# plt.plot(xaxis,Read.SLchisq_neg083.values.tolist(), 'o-',label = "0.8*10^-3")
# plt.plot(xaxis,Read.SLchisq_neg073.values.tolist(), 'o-',label = "0.7*10^-3")
# plt.plot(xaxis,Read.SLchisq_neg063.values.tolist(), 'o-',label = "0.6*10^-3")

# plt.plot(xaxis,Read.SLchisq_neg053.values.tolist(), 'o-',label = "0.5*10^-3")
# #plt.plot(xaxis,Read.SLchisq_neg033.values.tolist(), 'o-',label = "0.3*10^-3")

# plt.xlabel('Exposure Age [Years]')
# plt.ylabel('Chi Squared')
# plt.title('Sea Level')
# plt.legend()

#yaxis_neg33 = yaxis
#yaxis_neg203 = yaxis
#yaxis_neg153 = yaxis
#yaxis_neg103 = yaxis
#yaxis_neg6253 = yaxis
# yaxis_neg53 = yaxis
#yaxis_neg73 = yaxis


#CONSTANT
# SLyaxis_neg53 = yaxis
# #SLyaxis_neg6253 = yaxis
# #SLyaxis_neg73 = yaxis



# # # # # ##NOTE TO MOE: for first three plot lines, the min is the last exp age (600k). For 53 the min is 300k


# np.savetxt(directory+"/text_for_plots/SLchisq_neg53.csv", 
#             SLyaxis_neg53,
#             delimiter =", ", 
#             fmt ='% s')



