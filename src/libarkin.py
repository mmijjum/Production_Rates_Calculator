#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:26:50 2023

@author: mmijjum
"""

import numpy as np
import pandas as pd
import Read
import User_Interface
import scaling_factor
import neutron_spallation
import proton_spallation
import muons
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)
n0 = Read.nuclide_concentration

if User_Interface.system == 1:
    slhl = 131.32
if User_Interface.system == 2:
    slhl = 131.32#scaling to pyx via balco's make_consts code.
if User_Interface.system == 3:
    slhl = 131.32
if User_Interface.system == 4:
    slhl = 15.5 #Sf scaled, bc LSDn not used for 21ne, only10be in Fenton 2019? #update later

tempvals = []
tempvalsmu = []
lambdasp = 160 #effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
lambdamu = 1500 #muon attenuation length in at/g/yr (Balco supplementary)
#lambdamu=878- #3he, larsen
erosion =(10**-2) #cm/yr, per Dunai (2010)
dt = 250000
rho = 2.32
#Pmu = 0.23 #larsen et al, this is for comparing 3He muon production
texp_bin1 = [10000,50000,100000,150000,200000,250000]
texp_bin2 = [300000,350000,400000,450000,500000]
texp_bin3 = [550000,600000]

z0 = [15,15,15,20,30,20,40]
concentrations = []


for j in range(len(texp_bin1)):
    for i in range(len(Read.site_lat)):
        Cspall = ((neutron_spallation.pn_df.iloc[i][0] + proton_spallation.pp_df.iloc[i][0]) / ((rho*erosion)/lambdasp)) * np.exp(-2.32*(z0[i] - erosion*texp_bin1[j])/lambdasp) * (1 - np.exp(-((rho*erosion)/lambdasp)*texp_bin1[j]))
        Cmuons = ((muons.pmuons_df.iloc[i][0]) / ((rho*erosion)/lambdamu)) * np.exp(-2.32*(z0[i] - erosion*texp_bin1[j])/lambdamu) * (1 - np.exp(-((rho*erosion)/lambdamu)*texp_bin1[j]))
        Ctot = Cspall + Cmuons
        concentrations.append(Ctot)
        
for j in range(len(texp_bin2)):
    for i in range(len(Read.site_lat)):
        Cspall = ((neutron_spallation.pn_df.iloc[i][0] + proton_spallation.pp_df.iloc[i][0]) / ((rho*erosion)/lambdasp)) * np.exp(-2.32*(z0[i] - erosion*dt)/lambdasp) * (1 - np.exp(-((rho*erosion)/lambdasp)*dt)) + ((neutron_spallation.pn_df.iloc[i][1] + proton_spallation.pp_df.iloc[i][1]) / ((rho*erosion)/lambdasp)) * np.exp(-2.32*(z0[i] - erosion* (texp_bin2[j] - dt))/lambdasp) * (1 - np.exp(-((rho*erosion)/lambdasp)*(texp_bin2[j]-dt)))
        Cmuons = ((muons.pmuons_df.iloc[i][0]) / ((rho*erosion)/lambdamu)) * np.exp(-2.32*(z0[i] - erosion*dt)/lambdamu) * (1 - np.exp(-((rho*erosion)/lambdamu)*dt)) + ((muons.pmuons_df.iloc[i][1]) / ((rho*erosion)/lambdamu)) * np.exp(-2.32*(z0[i] - erosion*(texp_bin2[j]-dt))/lambdamu) * (1 - np.exp(-((rho*erosion)/lambdamu)*(texp_bin1[j]-dt)))
        Ctot = Cspall + Cmuons
        concentrations.append(Ctot)
        
for j in range(len(texp_bin3)):
    for i in range(len(Read.site_lat)):
        Cspall = ((neutron_spallation.pn_df.iloc[i][0] + proton_spallation.pp_df.iloc[i][0]) / ((rho*erosion)/lambdasp)) * np.exp(-2.32*(z0[i] - erosion*dt)/lambdasp) * (1 - np.exp(-((rho*erosion)/lambdasp)*dt)) + ((neutron_spallation.pn_df.iloc[i][1] + proton_spallation.pp_df.iloc[i][1]) / ((rho*erosion)/lambdasp)) * np.exp(-2.32*(z0[i] - erosion* (dt))/lambdasp) * (1 - np.exp(-((rho*erosion)/lambdasp)*(dt))) + ((neutron_spallation.pn_df.iloc[i][2] + proton_spallation.pp_df.iloc[i][2]) / ((rho*erosion)/lambdasp)) * np.exp(-2.32*(z0[i] - erosion* (texp_bin3[j] - 2*dt))/lambdasp) * (1 - np.exp(-((rho*erosion)/lambdasp)*(texp_bin3[j]-2*dt)))
        Cmuons = ((muons.pmuons_df.iloc[i][0]) / ((rho*erosion)/lambdamu)) * np.exp(-2.32*(z0[i] - erosion*dt)/lambdamu) * (1 - np.exp(-((rho*erosion)/lambdamu)*dt)) + ((muons.pmuons_df.iloc[i][1]) / ((rho*erosion)/lambdamu)) * np.exp(-2.32*(z0[i] - erosion*(texp_bin2[j]-dt))/lambdamu) * (1 - np.exp(-((rho*erosion)/lambdamu)*(texp_bin1[j]-dt)))
        Ctot = Cspall + Cmuons
        concentrations.append(Ctot)

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
c550k = concentrations[77:84]
c600k = concentrations[84:91]

fmj = [2.38*10**6,2.63*10**6,2.75*10**6,33000,73000,34000,59000]

chi = [56000,59000,57000,55000,54000,60000,56000]



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
    temp12.append(((c550k[i] - fmj[i]) / chi[i])**2)
    temp13.append(((c600k[i] - fmj[i]) / chi[i])**2)


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

xaxis = [10000,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000,550000,600000]
yaxis = [chisq1,chisq2,chisq3,chisq4,chisq5,chisq6,chisq7,chisq8,chisq9,chisq10,chisq11,chisq12,chisq13]
plt.plot(xaxis,yaxis, 'o-')
plt.xlabel('exposure age')
plt.ylabel('chi squared')
plt.plot(xaxis,yaxis, 'o-')

# plt.plot(xaxis,Read.chisq_neg53.values.tolist(), 'o-',label = "5*10^-3")
# plt.plot(xaxis,Read.chisq_neg3.values.tolist(), 'o-',label = "10^-3")
# plt.plot(xaxis,Read.chisq_neg54.values.tolist(), 'o-',label = "5*10^-4")
# plt.plot(xaxis,Read.chisq_neg4.values.tolist(), 'o-',label = "10^-4")
# plt.plot(xaxis,Read.chisq_neg55.values.tolist(), 'o-',label = "5*10^-5")
# plt.plot(xaxis,Read.chisq_neg5.values.tolist(), 'o-',label = "10^-5")
# plt.plot(xaxis,Read.chisq_neg56.values.tolist(), 'o-',label = "5*10^-6")
# plt.plot(xaxis,Read.chisq_neg6.values.tolist(), 'o-',label = "10^-6")





yaxis_neg2 = yaxis
# yaxis_neg53 = yaxis
# yaxis_neg3 = yaxis
# yaxis_neg54 = yaxis
# yaxis_neg4 = yaxis
# yaxis_neg55 = yaxis
# yaxis_neg5 = yaxis
# yaxis_neg56 = yaxis
# yaxis_neg6 = yaxis


np.savetxt(directory+"/plots/chisq_neg2.csv", 
            yaxis_neg2,
            delimiter =", ", 
            fmt ='% s')



