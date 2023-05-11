#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:34:44 2023

@author: mmijjum
"""

import numpy as np
import pandas as pd
import Read
import scaling_factor
import shielding
import muons

n0 = Read.nuclide_concentration
sthick = shielding.S_thick[0]

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
erosion = np.repeat(0,20)
dt = 250000
#Pmu = 0.23 #larsen et al, this is for comparing 3He muon production




import scipy.integrate as si 
import scipy.optimize as so
from scipy.optimize import fsolve
from sympy import solve

for i in range(len(scaling_factor.Siteprod_df)): #how many samples 
    for j in range(len(scaling_factor.Siteprod_df.iloc[0])): #time length    
    
    
        def integrand(t):
            return scaling_factor.Siteprod_df.iloc[i][j]* t
        
    def func(x):
        return slhl*sthick[i] * si.quad(integrand, 0, x)[0] - n0[i]  # func is integral minus 7
    
    sol = so.fsolve(func, 0)                    # equated func to 0
    print(sol)


                
        
        
        
        
        
        
        
        