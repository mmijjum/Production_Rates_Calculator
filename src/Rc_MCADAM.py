#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:06:36 2022
len(mcadam.means)
@author: mmijjum

This script calculates cutoff rigidity.
Equation from Dunai (2001) 

"""

import Read
import numpy as np
import Pmag_paleolat_MCADAM
import mcadam
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)
time = Read.time 

mu_knot = (1.256*10**-6)*10**22 #m kg s-2 A-2, permeability of free space.
c = 299792458 #m/s, speed of light.
R = 6.378*10**6 #m, radius of Earth.
Rc_list = []

#constant field
M_constant = 5.45938 #long term average from LSDn. M/M0 in final time bin is .7048, DGRF value from Lifton (2014) for M0 is 7.746*10^22 Am^-2

M_modern =  7.747 #LSDn 2010 DGRF 
M_half = M_modern/2
LSDn_M = Read.LSDn_M

"""
This Rc calculation will run the MCADAM pmag dataset only

"""
for x in range (len(Pmag_paleolat_MCADAM.pl_df)):
    for i in range(len(mcadam.medians)):
        Rc_calc = (((mcadam.medians[i]*mu_knot*c)/(16*np.pi*R**2))*((np.cos(np.deg2rad(Pmag_paleolat_MCADAM.pl_df.iloc[x,i])))**4))/10**9 #divided by 10^9 to convert [V] to [GV]
        Rc_list.append(Rc_calc)
Rc = pd.DataFrame([(Rc_list[n:n+len(time)]) for n in range(0, len(Rc_list), len(time))])



#RUN THIS if you want to apply long term average only
# for x in range (len(Pmag_paleolat_MCADAM.pl_df)):
#     for i in range(len(mcadam.medians)):
#         Rc_calc = (((M_constant*mu_knot*c)/(16*np.pi*R**2))*((np.cos(np.deg2rad(Pmag_paleolat_MCADAM.pl_df.iloc[x,i])))**4))/10**9
#         Rc_list.append(Rc_calc)
# Rc = pd.DataFrame([(Rc_list[n:n+len(time)]) for n in range(0, len(Rc_list), len(time))])

"""
Below are specialized scripts for making specific figures in Mijjum et al. (2024)
"""
#uncertainty

# for x in range (len(Pmag_paleolat_MCADAM.pl_df)):
#     for i in range(len(mcadam.medians)):
#         Rc_calc = (((mcadam.sigma_75[i]*mu_knot*c)/(16*np.pi*R**2))*((np.cos(np.deg2rad(Pmag_paleolat_MCADAM.pl_df.iloc[x,i])))**4))/10**9 #divided by 10^9 to convert [V] to [GV]
#         Rc_list.append(Rc_calc)
# Rc = pd.DataFrame([(Rc_list[n:n+len(time)]) for n in range(0, len(Rc_list), len(time))])

#MODERN, FIG 2
# for x in range (len(Pmag_paleolat_MCADAM.pl_df)):
#     for i in range(len(mcadam.medians)):
#         Rc_calc = (((M_modern*mu_knot*c)/(16*np.pi*R**2))*((np.cos(np.deg2rad(Pmag_paleolat_MCADAM.pl_df.iloc[x,i])))**4))/10**9 #divided by 10^9 to convert [V] to [GV]
#         Rc_list.append(Rc_calc)
# Rc = pd.DataFrame([(Rc_list[n:n+len(time)]) for n in range(0, len(Rc_list), len(time))])