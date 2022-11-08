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
dt = 250000
tempvals = []

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
for i in range (len(tempvals_df)):
    x = tempvals_df[0][i]
    for j in range(len(tempvals_df.iloc[0])):
        l = func(sthick[i],x)
        if l < n0[i]:
            x += tempvals_df.iloc[i][j+1]
        else:
            iteration.append(j)
            break
        
exp_age = []
for i in range (len(tempvals_df)):
    for j in range(len(tempvals_df.iloc[0])):
        dt2 = (n0[i] - sthick[i] * slhl * (np.sum(tempvals_df.iloc[i][0:iteration[i]]))) / (sthick[i] * slhl * (tempvals_df.iloc[i][iteration[i]+1]/dt)) 
        expage = iteration[i] * dt + dt2
    exp_age.append(expage)

# model = [2938560.5499232844,
#  2323492.52452905,
#  2839555.1848216136,
#  5167302.67053074,
#  3269044.9421652267,
#  4986705.108083467,
#  4573653.246334221,
#  5006455.036073259,
#  5772659.306975413,
#  3597705.538425242,
#  4328385.843081659,
#  4351561.765819313,
#  4137731.7036931664,
#  11088936.51908915,
#  7808584.93281309,
#  11704687.40787323,
#  10440487.93995546,
#  10295680.504444081,
#  2594213.3924643635,
#  2605916.445905864]

# ans = []
# for i in range(len(exp_age)):
#    x =  exp_age[i] - model[i]
#    ans.append(x)