#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:18:31 2023

This script was originally written by Greg Balco as part of the CRONUS-Earth online calculators: http://hess.ess.washington.edu/math/
Based on version 1.2, written in September 2016.

It was modified by Moe Mijjum to be compatible with SPRITE calculator, in Python.

@author: mmijjum
"""
import numpy as np
import Read
import atm_depth_MCADAM
from scipy.interpolate import interp1d
import scipy.integrate as integrate
import scipy.special as special
import pandas as pd

if Read.system == 4:
    def thresh(x):
        if(x < 1):
            return 1
        return x

    #define range/momentum relation table for muons in standard rock in Groom and others 2001
    data = Read.data_muons # column 1 is momentum [MeV/c], column 2 is g/cm2
    
    #H = atm_depth_MCADAM.x
    h = atm_depth_MCADAM.x/1.019716
    rho = Read.rho
    z_temp = Read.z_from_surface
    Z = z_temp * rho #convert depth from surface from cm to g/cm2
    
    H = (1013.25 - h)*1.019716 #atm_depth_MCADAM.x is already in g/cm2, difference?
    
    #find vertical flux at SLHL
    a = 258.5*(100**2.66)
    b = 75 * (100**1.66)
    
    phi_vert_slhl = (a/((Z + 21000) * (((Z + 1000)**1.66) + b))) * np.exp(-5.5e-6 * Z)

    #Convert user-input depth below surface
    
    
    def Rv0(z):
        a = np.exp(-5.5e-6*z)
        b = z + 21000
        c = (z+1000)**1.66 + 1.567e5
        dadz = -5.5e-6 * np.exp(-5.5e-6*z)
        dbdz = 1
        dcdz = 1.66 * (z+1000)**0.66
        

        
        return -5.401e7 * (b * c * dadz - a*(c*dbdz + b*dcdz))/(b**2 * c**2)
    
    
    def LZ(z):
        P_MeVc = np.exp(interp1d(np.log(data.iloc[:,1]),np.log(data.iloc[:,0]))(np.log(z)))
        
        
        return 263 + 150 * (P_MeVc/1000)

    
    R_vert_slhl = Rv0(Z)
    
    R_Vert_site_list = []
    for i in range(len(Z)):
        #deal with zero situation
        Z_new = thresh(Z[i])
        R_Vert_site_temp = R_vert_slhl[i] * np.exp(H.div(LZ(Z_new)))
        R_Vert_site_list.append(R_Vert_site_temp)
    R_vert_site = R_Vert_site_list[0]
    #find flux of vertical muons at site
    #f = lambda x: Rv0(x)* np.exp(H.div(LZ(x)))
    
    phi_vert_site = []
    for k in range(len(Z)):
        for i in range(len(H.iloc[0])):
            Z_new= thresh(Z[k])
            tol = phi_vert_slhl[k] * 1e-4
            f = lambda x: Rv0(x)* np.exp(H.iloc[k,i]/LZ(x))
            temp = integrate.quad(f, Z_new, 2e5+1, epsabs = tol)
            phi_vert_site.append(temp[0])
        
    phi_200k = (1/((2e5+21000) * (((2e5+1000)**1.66) + b))) * np.exp(-5.5e-6 * 2e5)
    phi_vert_site = phi_vert_site + phi_200k;
    
    
    # find the total flux of muons at site
    # angular distribution exponent
    
    #If alpha = 1, then beta also is 1
    
    Beta = 1
    
    # internally defined constants
    
    aalpha = 1
    
    
    #sigma0 = sigma190 if alpha is known. Sigma 0 = cross section for fast muons at 1 GeV
    
    sigma = 4.199e-30 #units = cm2. From Balco (2019). 0.0042 mb.
    
    phi = []
    
    P_fast = []
    for i in range(len(H.iloc[0,:])):
        for j in range(len(H)):
            nofz = 3.21 - 0.297*np.log((Z[j]+H.iloc[j,i])/100 + 42) + 1.21e-5*(Z[j]+H.iloc[j,i])
            dndz = (-0.297/100)/((Z[j]+H.iloc[j,i])/100 + 42) + 1.21e-5
            phi_temp = phi_vert_site[j] * 2 * np.pi / (nofz+1)
            # # # that was in muons/cm2/s
            # # # convert to muons/cm2/yr
            phi.append(phi_temp*60*60*24*365)
    
            # #find the total stopping rate of muons at site
            R_temp = (2*np.pi/(nofz+1))*R_vert_site.iloc[j,i] - phi_vert_site[j]*(-2*np.pi*((nofz+1)**-2))*dndz
    
        
            # #that was in total muons/g/s
            # #convert to negative muons/g/yr
    
            R = R_temp*0.44*60*60*24*365
            
    
            Ebar = 7.6 + 321.7*(1 - np.exp(-8.059e-6*Z[j])) + 50.7*(1-np.exp(-5.05e-7*Z[j]));
    
    
            #fast muon production
            
            P_fast_temp = phi[i]*Beta*(Ebar**aalpha)*sigma*1.0228e22 #2e5 = consts.Natoms 
            P_fast.append(P_fast_temp)
    #negative muon capture #IGNORE FOR OW, ONLY DOING FAST MUONS
    
    
    pmuons_df = pd.DataFrame([(P_fast[n:n+len(H.iloc[0,:])]) for n in range(0, len(P_fast), len(H.iloc[0,:]))])
    
    ##SAVE ATTENUATION LENGTHS FOR FINAL FIGURE##
    atten = []
    for i in range(len(Z)):
        #deal with zero situation
        Z_new = thresh(Z[i])
        LZ_temps = LZ(Z_new)
        atten.append(LZ_temps)
      
    
    if Read.paleo[0] == 1:
        pmuons_df[:] = pmuons_df.values[:, ::-1]
        
