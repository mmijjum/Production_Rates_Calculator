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
import User_Interface
import scaling_factor
import shielding

n0 = Read.nuclide_concentration
sthick = shielding.S_thick[0]
slhl =  scaling_factor.ref
tempvals = []
tempvalsmu = []
lambdasp = 160 #effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
lambdamu = 8780
erosion = np.repeat(0,20)
dt = 250000
Pmu = 0.23 #larsen et al

import math

# def truncate(number, decimals=0):
#     """
#     Returns a value truncated to a specific number of decimal places.
#     """
#     if not isinstance(decimals, int):
#         raise TypeError("decimal places must be an integer.")
#     elif decimals < 0:
#         raise ValueError("decimal places has to be 0 or more.")
#     elif decimals == 0:
#         return math.trunc(number)

#     factor = 10.0 ** decimals
#     return math.trunc(number * factor) / factor

# sthick_updated = []
# for i in range(len(sthick)):
#     temp = truncate(sthick[i],2)
#     sthick_updated.append(temp)
    
#if User_Interface.system == 4: 
#spallation part

# def func(sthick,tempvals):
#     return sthick*slhl*tempvals

    
# for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
#     for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
#         temp = (scaling_factor.Siteprod_df.iloc[i][j]* dt)
#         tempvals.append(temp)
#       #   n = sthick * slhl * temp
#       #   if n == n0:

# tempvals_df = pd.DataFrame([(tempvals[n:n+len(User_Interface.time)]) for n in range(0, len(tempvals), len(User_Interface.time))])
# #muons part
# def funcmu(tempvalsmu):
#     return Pmu * tempvalsmu
   
# for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
#     for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
#         temp = np.exp((shielding.z_df.iloc[i][j]/2)/lambdamu) * dt
#         tempvalsmu.append(temp)

# tempvals_df_mu = pd.DataFrame([(tempvalsmu[n:n+len(User_Interface.time)]) for n in range(0, len(tempvalsmu), len(User_Interface.time))])

# iteration = []
# for i in range (len(tempvals_df)):
#     x = tempvals_df.iloc[i][0]
#     y = tempvals_df_mu.iloc[i][0]
#     for j in range(len(tempvals_df.iloc[0])):
#         l = func(sthick[i],x) + funcmu(y)
#         if l < n0[i]:
#             x += tempvals_df.iloc[i][j+1]
#             y += tempvals_df_mu.iloc[i][j+1]
#         else:
#             iteration.append(j)
#             break
        
# exp_age = []
# for i in range (len(tempvals_df)):
#     a = (np.sum(tempvals_df.iloc[i][0:iteration[i]]))
#     b = (np.sum(tempvals_df_mu.iloc[i][0:iteration[i]]))
#     dt2 = ((n0[i] - (sthick[i] * slhl * a) - (Pmu * b))/ (stexphick[i] * slhl) * Pmu)/ scaling_factor.Siteprod_df.iloc[i][iteration[i]+1]
#     expage = iteration[i] * dt + dt2
#     exp_age.append(expage)

def func(sthick,tempvals):
    return sthick*slhl*tempvals

    
for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
    for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
        temp = (scaling_factor.Siteprod_df.iloc[i][j]* dt)
        tempvals.append(temp)
      #   n = sthick * slhl * temp
      #   if n == n0:

tempvals_df = pd.DataFrame([(tempvals[n:n+len(User_Interface.time)]) for n in range(0, len(tempvals), len(User_Interface.time))])

iteration = []
for i in range(len(tempvals_df)):
    x = tempvals_df.iloc[i][0]
    for j in range(len(tempvals_df.iloc[0])):
        l = func(sthick[i],x)
        if l < n0[i]:
            x += tempvals_df.iloc[i][j+1]
        else:
            iteration.append(j)
            break
            
        
exp_age = []
for i in range (len(tempvals_df)):
    a = (np.sum(tempvals_df.iloc[i][0:iteration[i]]))
    dt2 = ((n0[i]/(sthick[i] * slhl)) - a) / (scaling_factor.Siteprod_df.iloc[i][iteration[i]])
    expage = iteration[i] * dt + dt2
    exp_age.append(expage)
