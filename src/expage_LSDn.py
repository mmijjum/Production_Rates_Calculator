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
ex
@author: mmijjum


"""

#Exposure Age

#SET DIRECTORY
import glob
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)
import Read
import numpy as np
import pandas as pd
import scaling_factor
import shielding
import Muons_v2
import atm_depth 

n0 = Read.nuclide_concentration
sthick = shielding.S_thick[0]
stopo = Read.s_topo
erosion = Read.erosion
if Read.system == 1:
    slhl = 1 * (91.452156 + 14.750325) #1 = qtz non dimensional scaling factor, from Greg's make_consts
if Read.system == 2:
    slhl = 1.369 * (80.175076 + 13.062843) #1.369 = LSDn non-dimensional correction factor (excluding a data point from calibration dataset, per Marissa)
if Read.system == 3:
    slhl = 1.369 * (78.28355 + 13.197369 ) #1.369 = LSDn non-dimensional correction factor (excluding a data point from calibration dataset, per Marissa)
if Read.system == 4:
    slhl = 1.272 * (11.847124 + 1.624044) #1.272 = non dimensional scaling factor, from Greg's make_consts

# if Read.system == 1:
#     slhl = 1 * (91.452156 + 14.750325) #1 = qtz non dimensional scaling factor, from Greg's make_consts
# if Read.system == 2:
#     slhl = 108.962
# if Read.system == 3:
#     slhl = 108.962
# if Read.system == 4:
#     slhl = 17.9154 #nat slhl
#     #slhl = 15.6852 #sprite slhl

tempvals = []
tempvalsmu = []
lambdasp = 160 #effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
a = 0.01036
b = -9.697e-6
htemp = atm_depth.x
#htemp[:] = htemp.values[:, ::-1] #reverse to get in correct time sequence
h = (htemp) / 1.019716 # convert back from atmospheric depth to pressure
lambdamu = 1 / (a + b*h) #muon attenuation length, equation 8 in Balco (@017)
#lambdamu = 4000
#lambdamu=8780 #3he, larsen
dt_sprite_temp = np.repeat(250000,272) #70 ma - 2 ma
dt1 = np.repeat(10,5+1)
dt2 = np.repeat(100,30+1)
dt3 = np.repeat(200,359+1)
dt4 = np.repeat(1000,724+1)
dt5 = np.repeat(2000,599+1)

dt_LSDn_temp = np.concatenate([dt1,dt2,dt3,dt4,dt5])
dt_LSDn = pd.Series(dt_LSDn_temp)
dt_sprite = pd.Series(dt_sprite_temp)
dt_temp = pd.concat([dt_LSDn, dt_sprite], ignore_index = True)
n_0 = len(dt_temp) - len(scaling_factor.Siteprod_df.iloc[0]) #how long do we need the time vector to be
dt = dt_temp.iloc[:-n_0]

#Pmu = 0.23 #larsen et al, this is for comparing 3He muon production

# dt_start = 10


# firstbin  = []

# for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
#     temp_start = (scaling_factor.Siteprod_df.iloc[i][0]* np.exp( (-erosion[i]*i)/lambdasp)* (dt_start*10**6))
#     firstbin.append(temp_start)

# bin1 = pd.Series(firstbin)


if Read.muons == 'False': 
    #For 3He
    def func(sthick,stopo,tempvals):
        return sthick*stopo*slhl*tempvals
    
            
    for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
        for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
            temp = (scaling_factor.Siteprod_df.iloc[i][j]* np.exp((-erosion[i]*i)/lambdasp)* dt[j])
            tempvals.append(temp)
          #   n = sthick * slhl * temp
          #   if n == n0:
    
    tempvals_df = pd.DataFrame([(tempvals[n:n+len(dt)]) for n in range(0, len(tempvals), len(dt))])
    #tempvals_df[0] = bin1

#     # #muons part

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
        if iteration[i] == 0:
            expage = dt2
        else:
            expage = (np.sum(dt[0:iteration[i]])) + dt2
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


# if Read.muons == 'True': 
    
#     Pmu = Muons_v2.pmuons_df
#     firstmubin = []
#     for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
#         for j in range(len(scaling_factor.Siteprod_df.iloc[0])):
#             temp = Pmu.iloc[i][0] * np.exp(((-erosion[i]*i)-shielding.z_df.iloc[i][0]/2)/lambdamu.iloc[i][0]) * (dt_start*10**6)
#             firstmubin.append(temp)
            

#     bin1muons = pd.Series(firstmubin)
    
#     def func(sthick,stopo,tempvals):
#         return sthick*stopo*slhl*tempvals
    
            
#     for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
#         for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
#             temp = (scaling_factor.Siteprod_df.iloc[i][j]* np.exp((-erosion[i]*i)/lambdasp)* dt)
#             tempvals.append(temp)
#           #   n = sthick * slhl * temp
#           #   if n == n0:
    
#     tempvals_df = pd.DataFrame([(tempvals[n:n+len(Read.time)]) for n in range(0, len(tempvals), len(Read.time))])
#     tempvals_df[0] = bin1    #muons part
  
#     for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
#         for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
#             temp = Pmu.iloc[i][j] * np.exp(((-erosion[i]*i)-shielding.z_df.iloc[i][j]/2)/lambdamu.iloc[i][j]) * dt
#             tempvalsmu.append(temp)
    
#     tempvals_df_mu = pd.DataFrame([(tempvalsmu[n:n+len(Read.time)]) for n in range(0, len(tempvalsmu), len(Read.time))])
#     tempvals_df_mu[0] = bin1muons    #muons part

#     iteration = []
#     for i in range (len(tempvals_df)):
#         x = tempvals_df.iloc[i][0]
#         y = tempvals_df_mu.iloc[i][0]
        
#         for j in range(len(tempvals_df.iloc[0])):
#             l = func(sthick[i],stopo[i],x) + y

#             if l < n0[i]:
#                 x += tempvals_df.iloc[i][j+1]
#                 y += tempvals_df_mu.iloc[i][j+1]
    
#             else:
#                 iteration.append(j)
            
#                 break
            
#     exp_age = []
#     a = []
#     b = []
#     scaling_factor.Siteprod_df.iloc[i][j]
#     for i in range (len(tempvals_df)):
#         a = (np.sum(tempvals_df.iloc[i][0:iteration[i]]))
#         b = (np.sum(tempvals_df_mu.iloc[i][0:iteration[i]]))
#         dt2 = (n0[i] - (sthick[i]*stopo[i]*slhl*a) - b)/ (sthick[i]*stopo[i]*slhl* (scaling_factor.Siteprod_df.iloc[i][iteration[i]]* np.exp((-erosion[i]*i)/lambdasp)) + Pmu.iloc[i][iteration[i]]* np.exp(((-erosion[i]*i)-shielding.z_df.iloc[i][iteration[i]]/2)/lambdamu.iloc[i][iteration[i]]))
#         expage = ((iteration[i]-1) * dt) + (dt_start*10**6) + dt2
#         exp_age.append(expage)

