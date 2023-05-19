#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:21:32 2023

@author: mmijjum
"""



import numpy as np
import pandas as pd
import Read
import muons
import neutron_spallation
import proton_spallation
import scaling_factor
import shielding
import matplotlib.pyplot as plt
import os


erosion = Read.erosion.dropna()
texp = Read.texp
dt = 250000

nbins = texp//dt
dt2 = texp - nbins*dt
z0 = Read.z_from_surface
lambdasp = 160
lambdamu = 1300
tempvals = []

error = Read.nuclide_uncertainty
data = Read.nuclide_concentration

for j in range(len(erosion)):
    for i in range(len(z0)):
        for k in range(int(nbins+1)):
            Cspall = (shielding.S_thick[0][i]*(neutron_spallation.pn_df[k][i] + proton_spallation.pp_df[k][i])) / ((Read.rho[i] * erosion[j]) / lambdasp) * np.exp(-(Read.rho[i]*z0[i]/lambdasp)) * (1-np.exp(-(Read.rho[i]*erosion[j]/lambdasp)*dt))
            Cmuons = muons.pmuons_df[k][i] / ((Read.rho[i] * erosion[j]) / lambdamu) * np.exp(-(Read.rho[i]*z0[i]/lambdamu)) * (1-np.exp(-(Read.rho[i]*erosion[j]/lambdamu)*dt)) 
            Ctot = Cspall + Cmuons
            tempvals.append(Cspall + Cmuons)

tempvals_df = pd.DataFrame([(tempvals[n:n+int(nbins+1)]) for n in range(0, len(tempvals), int(nbins+1))])

concentrations = []

for i in range(len(tempvals_df)):
    x = np.sum(tempvals_df.iloc[i][0:int(nbins)])
    concentrations.append(x)


residual = []
for j in range(len(erosion)):
    for i in range(len(z0)):
        Cspall = (shielding.S_thick[0][i]*(neutron_spallation.pn_df[int(nbins)][i] + proton_spallation.pp_df[int(nbins)][i])) / ((Read.rho[i] * erosion[j]) / lambdasp) * np.exp(-(Read.rho[i]*z0[i]/lambdasp)) * (1-np.exp(-(Read.rho[i]*erosion[j]/lambdasp)*dt2))
        Cmuons = muons.pmuons_df[int(nbins)][i] / ((Read.rho[i] * erosion[j]) / lambdamu) * np.exp(-(Read.rho[i]*z0[i]/lambdamu)) * (1-np.exp(-(Read.rho[i]*erosion[j]/lambdamu)*dt2)) 
        Ctot = Cspall + Cmuons
        residual.append(Cspall + Cmuons)

total_concentration = []
for i in range(len(concentrations)):
    x = residual[i] + concentrations[i]
    total_concentration.append(x)

data_updated = pd.concat([data]*len(erosion), ignore_index=True)
error_updated = pd.concat([error]*len(erosion), ignore_index=True)

def chisqg(ydata,ymod,sd):  
      """  
 Returns the chi-square error statistic as the sum of squared errors between  
 Ydata(i) and Ymodel(i). If individual standard deviations (array sd) are supplied,   
 then the chi-square error statistic is computed as the sum of squared errors  
 divided by the standard deviations.     Inspired on the IDL procedure linfit.pro.  
 See http://en.wikipedia.org/wiki/Goodness_of_fit for reference.  
   
 x,y,sd assumed to be Numpy arrays. a,b scalars.  
 Returns the float chisq with the chi-square statistic.  
   
 Rodrigo Nemmen  
 http://goo.gl/8S1Oo  
 
 Modified by Moe Mijjum
      """  
      # Chi-square statistic (Bevington, eq. 6.9)  
      chisq=np.sum( ((ydata-ymod)/sd)**2 )  
        
      return chisq

chi_squared = []
for i in range(len(total_concentration)):
    chi_squared.append(chisqg(data_updated[i], total_concentration[i], error_updated[i]))

chi_df = pd.DataFrame([(chi_squared[n:n+len(z0)]) for n in range(0, len(chi_squared), len(z0))])

#[[min(chi_squared[i:i+len(z0)]) for i in range(0, len(chi_squared), len(z0))]]
for i in range(len(erosion)):
    plt.plot(chi_df.iloc[i][:],'.-', label = "Erosion Rate ={} cm/yr".format(erosion[i]))
    plt.ylabel('Chi-squared')
    plt.xlabel('sample #')
    plt.legend()
