#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 10:58:40 2023

@author: mmijjum
"""

import numpy as np
import pandas as pd
import Read
import scaling_factor
import neutron_spallation
import proton_spallation
import shielding
import muons

n0 = Read.nuclide_concentration
sthick = shielding.S_thick[0]
stopo = Read.s_topo
if Read.system == 1:
    slhl = 1 * (91.6318 + 14.7771) #1 = qtz non dimensional scaling factor, from Greg's make_consts
if Read.system == 2:
    slhl = 1.369 * (80.1750 + 13.0628) #1.369 = LSDn non-dimensional correction factor (excluding a data point from calibration dataset, per Marissa)
if Read.system == 3:
    slhl = 1.369 * (80.1750 + 13.0628) #1.369 = LSDn non-dimensional correction factor (excluding a data point from calibration dataset, per Marissa)
if Read.system == 4:
    slhl = 1.272 * (11.8702 + 1.6269) #1.272 = non dimensional scaling factor, from Greg's make_consts
tempvals = []
tempvalsmu = []
lambdasp = 160 #effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
lambdamu = 1500 #muon attenuation length in at/g/yr (Balco supplementary)
#lambdamu=8780 #3he, larsen
texp = Read.texp
dt = 250000

nbins = texp//dt
dt2 = texp - nbins*dt
z0 = Read.z_from_surface
#Pmu = 0.23 #larsen et al, this is for comparing 3He muon production

erosion = []
# for i in range(len(n0)):
#     er = ((neutron_spallation.pn_df.iloc[i][0] + proton_spallation.pp_df.iloc[i][0]) * lambdasp) / n0[i]
#     erosion.append(er)

    
Pmu = muons.pmuons_df

def func(sthick,stopo,conc):
    return sthick*stopo*slhl*conc

def myfunction(erosion):
        
    for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
        for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
            temp = (scaling_factor.Siteprod_df.iloc[i][j]* np.exp((-erosion[i]*i)/lambdasp)* dt) + Pmu.iloc[i][j] * np.exp(((-erosion[i]*i)-shielding.z_df.iloc[i][j]/2)/lambdamu) * dt
            tempvals.append(temp)
    
    
    tempvals_df = pd.DataFrame([(tempvals[n:n+len(Read.time)]) for n in range(0, len(tempvals), len(Read.time))])
      
    concentrations = []
    
    for i in range(len(tempvals_df)):
        x = np.sum(tempvals_df.iloc[i][0:int(nbins)])
        concentrations.append(x)
    
    residual = []
    for i in range(len(erosion)):
        temp = (scaling_factor.Siteprod_df[int(nbins)][i]* np.exp((-erosion[i]*i)/lambdasp)* dt2) + Pmu[int(nbins)][i] * np.exp(((-erosion[i]*i)-shielding.z_df[int(nbins)][i]/2)/lambdamu) * dt2
        residual.append(temp)
    
    total_concentration = []
    for i in range(len(concentrations)):
        x = residual[i] + concentrations[i]
        y = func(sthick[i],stopo[i],x)
        total_concentration.append(y)

