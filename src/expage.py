#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:14:38 2023

@author: mmijjum
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:22:28 2022

@author: mmijjum


"""

#Exposure Age


import numpy as np
import pandas as pd
import Read
import scaling_factor
import shielding
import muons

n0 = Read.nuclide_concentration
sthick = shielding.S_thick[0]
stopo = Read.s_topo
erosion = Read.erosion
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
dt = 250000
#Pmu = 0.23 #larsen et al, this is for comparing 3He muon production
dt_start = (Read.time1 + 0.25) - Read.timerange[0]

firstbin  = []

for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
    temp_start = (scaling_factor.Siteprod_df.iloc[i][0]* np.exp((-erosion[i]*i)/lambdasp)* (dt_start*10**6))
    firstbin.append(temp_start)

bin1 = pd.Series(firstbin)


if Read.muons == 'False': 
    #For 3He
    def func(sthick,stopo,tempvals):
        return sthick*stopo*slhl*tempvals
    
            
    for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
        for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
            temp = (scaling_factor.Siteprod_df.iloc[i][j]* np.exp((-erosion[i]*i)/lambdasp)* dt)
            tempvals.append(temp)
          #   n = sthick * slhl * temp
          #   if n == n0:
    
    tempvals_df = pd.DataFrame([(tempvals[n:n+len(Read.time)]) for n in range(0, len(tempvals), len(Read.time))])
    tempvals_df[0] = bin1

    #muons part

    iteration = []
    for i in range(len(tempvals_df)):
        x = tempvals_df.iloc[i][0]
        for j in range(len(tempvals_df.iloc[0])):
            l = func(sthick[i],stopo[i], x)
            if l < n0[i]:
                x += tempvals_df.iloc[i][j+1]
            else:
                iteration.append(j)
                break
                
            
    exp_age = []
    for i in range (len(tempvals_df)):
        a = (np.sum(tempvals_df.iloc[i][0:iteration[i]]))
        dt2 = ((n0[i]/(sthick[i] *stopo[i]* slhl)) - a) / (scaling_factor.Siteprod_df.iloc[i][iteration[i]]* np.exp((-erosion[i]*i)/lambdasp))
        expage = ((iteration[i]-1) * dt) + (dt_start*10**6) + dt2
        exp_age.append(expage)

    
        # Pmu = 0.23
        # lambdamu=8780
    
        # def func(sthick,tempvals):
        #     return sthick*slhl*tempvals
        
                
        # for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
        #     for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
        #         temp = (scaling_factor.Siteprod_df.iloc[i][j]* dt)
        #         tempvals.append(temp)
        #       #   n = sthick * slhl * temp
        #       #   if n == n0:
        
        # tempvals_df = pd.DataFrame([(tempvals[n:n+len(Read.time)]) for n in range(0, len(tempvals), len(Read.time))])
        # #muons part
        # def funcmu(Pmu,tempvalsmu):
        #     return Pmu * tempvalsmu
           
        # for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
        #     for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
        #         temp = np.exp((-shielding.z_df.iloc[i][j]/2)/lambdamu) * dt
        #         tempvalsmu.append(temp)
        
        # tempvals_df_mu = pd.DataFrame([(tempvalsmu[n:n+len(Read.time)]) for n in range(0, len(tempvalsmu), len(Read.time))])
        
        # iteration = []
        # for i in range (len(tempvals_df)):
        #     x = tempvals_df.iloc[i][0]
        #     y = tempvals_df_mu.iloc[i][0]
        #     z = Pmu
        #     for j in range(len(tempvals_df.iloc[0])):
        #         l = func(sthick[i],x) + funcmu(z,y)
        #         if l < n0[i]:
        #             x += tempvals_df.iloc[i][j+1]
        #             y += tempvals_df_mu.iloc[i][j+1]
        #             z += Pmu
        #         else:
        #             iteration.append(j)
        #             break
                
        # exp_age = []
        # a = []
        # b = []
        # for i in range (len(tempvals_df)):
        #     a = (np.sum(tempvals_df.iloc[i][0:iteration[i]]))
        #     b = (np.sum(tempvals_df_mu.iloc[i][0:iteration[i]]))
        #     dt2 = (n0[i] - (sthick[i] *slhl * a) - (Pmu * b)) / ((sthick[i]*slhl) + Pmu) 
        #     expage = iteration[i] * dt + dt2
        #     exp_age.append(expage)


if Read.muons == 'True': 
    
    Pmu = muons.pmuons_df
    firstmubin = []
    for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
        temp = Pmu.iloc[i][0] * np.exp(((-erosion[i]*i)-shielding.z_df.iloc[i][0]/2)/lambdamu) * (dt_start*10**6)
        firstmubin.append(temp)

    bin1muons = pd.Series(firstmubin)
    
    def func(sthick,stopo,tempvals):
        return sthick*stopo*slhl*tempvals
    
            
    for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
        for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
            temp = (scaling_factor.Siteprod_df.iloc[i][j]* np.exp((-erosion[i]*i)/lambdasp)* dt)
            tempvals.append(temp)
          #   n = sthick * slhl * temp
          #   if n == n0:
    
    tempvals_df = pd.DataFrame([(tempvals[n:n+len(Read.time)]) for n in range(0, len(tempvals), len(Read.time))])
    tempvals_df[0] = bin1    #muons part
  
    for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
        for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
            temp = Pmu.iloc[i][j] * np.exp(((-erosion[i]*i)-shielding.z_df.iloc[i][j]/2)/lambdamu) * dt
            tempvalsmu.append(temp)
    
    tempvals_df_mu = pd.DataFrame([(tempvalsmu[n:n+len(Read.time)]) for n in range(0, len(tempvalsmu), len(Read.time))])
    tempvals_df_mu[0] = bin1muons    #muons part

    iteration = []
    for i in range (len(tempvals_df)):
        x = tempvals_df.iloc[i][0]
        y = tempvals_df_mu.iloc[i][0]
        for j in range(len(tempvals_df.iloc[0])):
            l = func(sthick[i],stopo[i],x) + y
            if l < n0[i]:
                x += tempvals_df.iloc[i][j+1]
                y += tempvals_df_mu.iloc[i][j+1]
            else:
                iteration.append(j)
                break
            
    exp_age = []
    a = []
    b = []
    scaling_factor.Siteprod_df.iloc[i][j]
    for i in range (len(tempvals_df)):
        a = (np.sum(tempvals_df.iloc[i][0:iteration[i]]))
        b = (np.sum(tempvals_df_mu.iloc[i][0:iteration[i]]))
        dt2 = (n0[i] - (sthick[i]*stopo[i]*slhl*a) - b)/ (sthick[i]*stopo[i]*slhl* (scaling_factor.Siteprod_df.iloc[i][iteration[i]]* np.exp((-erosion[i]*i)/lambdasp)) + Pmu.iloc[i][iteration[i]]* np.exp(((-erosion[i]*i)-shielding.z_df.iloc[i][iteration[i]]/2)/lambdamu))
        expage = ((iteration[i]-1) * dt) + (dt_start*10**6) + dt2
        exp_age.append(expage)

