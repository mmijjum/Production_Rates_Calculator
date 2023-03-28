#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:39:33 2022

@author: mmijjum

This script calculates the shielding scaling factor due to sample THICKNESS (NOT depth below surface)

From Balco (2008), modified by Moe Mijjum for Python. 
"""
import numpy as np
import User_Interface
import pandas as pd
import Read



time = User_Interface.time 


lambda_sp = 160 #g/cm2, from Balco (2008) 
def Sthick(lambda_sp, rho, zmax):
    return (lambda_sp/(Read.rho*Read.zmax))*(1-np.exp((-Read.rho*Read.zmax)/lambda_sp))

S_thick = []

for i in range(len(Read.zmax)):
    thickness = Sthick(lambda_sp, Read.zmax[i], Read.rho[i])
    S_thick.append(thickness)

#create dataframe of Zmax with time steps.
#zmax is non-time dependent, this is just for the sake of making the zmax shape same as other dataframes.
zmax = (Read.zmax) #user-specified in excel sheet: cm
rho = (Read.rho) #user-specified in excel sheet: g/cm3

z_df = pd.concat([zmax.mul(rho)]*len(time), ignore_index=True, axis = 1)

