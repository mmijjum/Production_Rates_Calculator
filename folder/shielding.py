#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:39:33 2022

@author: mmijjum
"""
import numpy as np
import User_Interface
import pandas as pd
import Read

# # Shielding Correction
#Shielding
#lambda_sp = effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
#rho = sample density in g/cm3, user input above. 
#zmax = max depth of sample below surface in cm, user input above.

time = User_Interface.time 


lambda_sp = 160
def Sthick(lambda_sp, rho, zmax):
    return (lambda_sp/(Read.rho*Read.zmax))*(1-np.exp((-Read.rho*Read.zmax)/lambda_sp))

S_thick = []

for i in range(len(Read.zmax)):
    thickness = Sthick(lambda_sp, Read.zmax[i], Read.rho[i])
    S_thick.append(thickness)


#create dataframe of Zmax with time steps.
#zmax is non-time dependent, this is just for the sake of making the zmax shape same as other dataframes.
zmax_updated = pd.DataFrame(Read.zmax)
zmax_df = pd.concat([zmax_updated]*len(time), ignore_index=True, axis = 1)

