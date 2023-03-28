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
import muons

n0 = Read.nuclide_concentration
sthick = shielding.S_thick[0]

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
erosion = np.repeat(0,20)
dt = 250000
#Pmu = 0.23 #larsen et al, this is for comparing 3He muon production

if User_Interface.muons == False: 
    #For 3He
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

if User_Interface.muons == True: 
    
    Pmu = muons.pmuons_df

    def func(sthick,tempvals):
        return sthick*slhl*tempvals
    
            
    for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
        for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
            temp = (scaling_factor.Siteprod_df.iloc[i][j]* dt)
            tempvals.append(temp)
          #   n = sthick * slhl * temp
          #   if n == n0:
    
    tempvals_df = pd.DataFrame([(tempvals[n:n+len(User_Interface.time)]) for n in range(0, len(tempvals), len(User_Interface.time))])
    #muons part
    def funcmu(Pmu,tempvalsmu):
        return Pmu * tempvalsmu
       
    for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
        for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length
            temp = np.exp((-shielding.z_df.iloc[i][j]/2)/lambdamu) * dt
            tempvalsmu.append(temp)
    
    tempvals_df_mu = pd.DataFrame([(tempvalsmu[n:n+len(User_Interface.time)]) for n in range(0, len(tempvalsmu), len(User_Interface.time))])
    
    iteration = []
    for i in range (len(tempvals_df)):
        x = tempvals_df.iloc[i][0]
        y = tempvals_df_mu.iloc[i][0]
        z = Pmu.iloc[i][0]
        for j in range(len(tempvals_df.iloc[0])):
            l = func(sthick[i],x) + funcmu(z,y)
            if l < n0[i]:
                x += tempvals_df.iloc[i][j+1]
                y += tempvals_df_mu.iloc[i][j+1]
                z += Pmu.iloc[i][j+1]
            else:
                iteration.append(j)
                break
            
    exp_age = []
    a = []
    b = []
    for i in range (len(tempvals_df)):
        a = (np.sum(tempvals_df.iloc[i][0:iteration[i]]))
        b = (np.sum(tempvals_df_mu.iloc[i][0:iteration[i]]))
        dt2 = (n0[i] - (sthick[i] *slhl * a) - (Pmu.iloc[i][iteration[i]] * b)) / ((sthick[i]*slhl) + Pmu.iloc[i][iteration[i]]) 
        expage = iteration[i] * dt + dt2
        exp_age.append(expage)

