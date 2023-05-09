#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:20:39 2022

@author: mmijjum

This script will calculate the production of some nuclide-"mineral pair due to neutron spallation. 

Based on Sato et al. (2008) Neutron Spectrum, and PARMA (analytical function approx.)
This code was originally implemented in MATLAB by Nat Lifton in 2013. This modified version was written by Moe Mijjum.

"""


import numpy as np
import pandas as pd
import Read
import atm_depth
import Rc

time = Read.time 


df = np.logspace(0,5.3010,200) #Energy spectrum [MeV]. From LSD, data from Sato & Nita (2008) 
E = pd.DataFrame(df)
E.columns = ['Energy']
E = E.T

s = 624.5718; #Solar modulation- uses constant value that Lifton (2008)/code uses for samples beyond 1,100 years.
Et = 2.5e-8; #Thermal neutron energy in MeV

smin = 400; #Units of MV
smax = 1200; #Units of MV
w = 0.2 #water content. 

# Ground-Level Spectrum
g3 = 10**(Read.ground_level_spectrum.iloc[0]['values'] + (Read.ground_level_spectrum.iloc[1]['values'])/(w + Read.ground_level_spectrum.iloc[2]['values']))
g5 = Read.ground_level_spectrum.iloc[3]['values'] + (Read.ground_level_spectrum.iloc[4]['values']*w) + Read.ground_level_spectrum.iloc[5]['values']*(w**2);

def fG(E):
    return (10**(Read.ground_level_spectrum.iloc[6]['values'] + Read.ground_level_spectrum.iloc[7]['values']*np.log10(E/g3)*(1-np.tanh(Read.ground_level_spectrum.iloc[8]['values']*np.log10(E/g5)))))
fG_df = fG(E) #GROUND LEVEL

# Thermal Neutron Spectrum
g6 = (Read.thermal_neutron_spectrum.iloc[0]['values'] + Read.thermal_neutron_spectrum.iloc[1]['values']*np.exp(-Read.thermal_neutron_spectrum.iloc[2]['values']*w))/(1 + Read.thermal_neutron_spectrum.iloc[3]['values']*np.exp(-Read.thermal_neutron_spectrum.iloc[4]['values']*w))
#PhiT = g6*((E/Et)**2)*np.exp(-E/Et)
PhiT = 0 #Can calculate, literally always gives 0. Thermal neutron. 


# Total Ground-Level Flux

def minmax(b1, b2, b3, b4, b5):
    return b1 + (b2*Rc.Rc.iloc[: , 0:]) + b3/(1 + np.exp((Rc.Rc.iloc[: , 0:] - b4)/b5))
a1min = minmax(Read.b_values.iloc[0]['values'], Read.b_values.iloc[2]['values'],Read.b_values.iloc[4]['values'],Read.b_values.iloc[6]['values'],Read.b_values.iloc[8]['values'])
a1max = minmax(Read.b_values.iloc[1]['values'],Read.b_values.iloc[3]['values'],Read.b_values.iloc[5]['values'],Read.b_values.iloc[7]['values'],Read.b_values.iloc[9]['values'])

a2min = minmax(Read.b_values.iloc[10]['values'],Read.b_values.iloc[12]['values'],Read.b_values.iloc[14]['values'],Read.b_values.iloc[16]['values'],Read.b_values.iloc[18]['values'])
a2max = minmax(Read.b_values.iloc[11]['values'],Read.b_values.iloc[13]['values'],Read.b_values.iloc[15]['values'],Read.b_values.iloc[17]['values'],Read.b_values.iloc[19]['values'])

a3min = minmax(Read.b_values.iloc[20]['values'],Read.b_values.iloc[22]['values'],Read.b_values.iloc[24]['values'],Read.b_values.iloc[26]['values'],Read.b_values.iloc[28]['values'])
a3max = minmax(Read.b_values.iloc[21]['values'], Read.b_values.iloc[23]['values'],Read.b_values.iloc[25]['values'],Read.b_values.iloc[27]['values'],Read.b_values.iloc[29]['values'])

a4min = minmax(Read.b_values.iloc[30]['values'],Read.b_values.iloc[32]['values'], Read.b_values.iloc[34]['values'],Read.b_values.iloc[36]['values'],Read.b_values.iloc[38]['values'])
a4max = minmax(Read.b_values.iloc[31]['values'],Read.b_values.iloc[33]['values'], Read.b_values.iloc[35]['values'], Read.b_values.iloc[37]['values'], Read.b_values.iloc[39]['values'])


a5 = minmax(Read.basic_spectrum.iloc[0]['values'],Read.basic_spectrum.iloc[1]['values'], Read.basic_spectrum.iloc[2]['values'],Read.basic_spectrum.iloc[3]['values'],Read.basic_spectrum.iloc[4]['values'])
a9 = minmax(Read.basic_spectrum.iloc[5]['values'],Read.basic_spectrum.iloc[6]['values'],Read.basic_spectrum.iloc[7]['values'],Read.basic_spectrum.iloc[8]['values'],Read.basic_spectrum.iloc[9]['values'])
a10 = minmax(Read.basic_spectrum.iloc[10]['values'],Read.basic_spectrum.iloc[11]['values'],Read.basic_spectrum.iloc[12]['values'],Read.basic_spectrum.iloc[13]['values'],Read.basic_spectrum.iloc[14]['values'])
a11 = minmax(Read.basic_spectrum.iloc[15]['values'],Read.basic_spectrum.iloc[16]['values'],Read.basic_spectrum.iloc[17]['values'],Read.basic_spectrum.iloc[18]['values'],Read.basic_spectrum.iloc[19]['values'])

b5 = minmax(Read.b_values.iloc[40]['values'],Read.b_values.iloc[41]['values'],Read.b_values.iloc[42]['values'],Read.b_values.iloc[43]['values'],Read.b_values.iloc[44]['values'])
b6 = minmax(Read.b_values.iloc[45]['values'],Read.b_values.iloc[46]['values'],Read.b_values.iloc[47]['values'],Read.b_values.iloc[48]['values'],Read.b_values.iloc[49]['values'])

c4 = []
c12 = []
PhiLmin_values = []
PhiLmax_values = []
f3_values = []
f2_values = []
f1_values = []
PhiL_values = []

x = atm_depth.x[0].to_numpy().flatten().tolist()

for n in range(len(atm_depth.sample_pressure)):
    for i in range(len(time)):
        c4_vals = a5.iloc[n,i] + Read.a_values.iloc[0]['values']*x[n]/(1 + Read.a_values.iloc[1]['values']*np.exp(Read.a_values.iloc[2]['values']*x[n])) #lethargy^-1
        c4.append(c4_vals)
       
        c12_vals = a9.iloc[n,i]*(np.exp(-a10.iloc[n,i]*x[n]) + a11.iloc[n,i]*np.exp(-Read.a_values.iloc[3]['values']*x[n])) # MeV
        c12.append(c12_vals)
        
        PhiLmin = a1min.iloc[n,i]*(np.exp(-a2min.iloc[n,i]*x[n]) - a3min.iloc[n,i]*np.exp(-a4min.iloc[n,i]*x[n])) #Length of Rc
        PhiLmin_values.append(PhiLmin)
    
        PhiLmax = a1max.iloc[n,i]*(np.exp(-a2max.iloc[n,i]*x[n]) - a3max.iloc[n,i]*np.exp(-a4max.iloc[n,i]*x[n])) 
        PhiLmax_values.append(PhiLmax)
        
        f3 = b5.iloc[n,i] + (b6.iloc[n,i]*x[n])
        f3_values.append(f3)


c4_df = pd.DataFrame([(c4[n:n+len(time)]) for n in range(0, len(c4), len(time))])
c12_df = pd.DataFrame([(c12[n:n+len(time)]) for n in range(0, len(c12), len(time))])

PhiLmin_df = pd.DataFrame([(PhiLmin_values[n:n+len(time)]) for n in range(0, len(PhiLmin_values), len(time))])
PhiLmax_df = pd.DataFrame([(PhiLmax_values[n:n+len(time)]) for n in range(0, len(PhiLmax_values), len(time))])

f3_df = pd.DataFrame([(f3_values[n:n+len(time)]) for n in range(0, len(f3_values), len(time))]) 

for n in range(len(atm_depth.sample_pressure)):
    for i in range(len(time)):
         f2 = (PhiLmin_df.iloc[n,i] - PhiLmax_df.iloc[n,i])/((smin**f3_df.iloc[n,i]) - (smax**f3_df.iloc[n,i]))
         f2_values.append(f2)
    
         f1 = PhiLmin_df.iloc[n,i]  - f2*smin**f3_df.iloc[n,i]
         f1_values.append(f1)
     
         PhiL = f1 + (f2*s**f3_df.iloc[n,i])
         PhiL_values.append(PhiL)
    

f2_df = pd.DataFrame([(f2_values[n:n+len(time)]) for n in range(0, len(f2_values), len(time))])
f1_df = pd.DataFrame([(f1_values[n:n+len(time)]) for n in range(0, len(f1_values), len(time))])
PhiL_df = pd.DataFrame([(PhiL_values[n:n+len(time)]) for n in range(0, len(PhiL_values), len(time))])


E = np.logspace(0,5.3010,200) #Energy spectrum [MeV]. From LSD, data from Sato & Nita (2008) 

PhiB_list = []
PhiB_df_temp = pd.DataFrame()
PhiB_df = pd.DataFrame()

for i in range(len(c4_df.to_numpy().flatten().tolist())):
    PhiB = (0.23555*(E/2.3779)**0.72597)*np.exp(-E/2.3799) + c4_df.to_numpy().flatten().tolist()[i]*np.exp((-(np.log10(E) - np.log10(123.91))**2)/(2*(np.log10(2.2318))**2)) + 0.0010791*np.log10(E/3.6435e-12)*(1 + np.tanh(1.6595*np.log10(E/8.4782e-8)))*(1 - np.tanh(1.5054*np.log10(E/c12_df.to_numpy().flatten().tolist()[i])))
    PhiB_list.append(PhiB)
out = np.concatenate(PhiB_list).ravel()
PhiB_df = pd.DataFrame([(out[n:n+200]) for n in range(0, len(out), len(E))])

fG_df = pd.DataFrame(np.repeat(fG_df.values, len(Rc.Rc)*len(time), axis=0))


PhiG_values = []
df2 = []
PhiG_temp = (PhiB_df*fG_df+ PhiT)
p3n_qtz = []
p3n_cpx = []
p3n_ol = []
p21n_qtz = []

df = np.logspace(0,5.3010,200) #Energy spectrum [MeV]. From LSD, data from Sato & Nita (2008) 
E = pd.DataFrame(df)
E.columns = ['Energy']
E_df = pd.concat([E.T]*len(Rc.Rc), ignore_index=True)
#E_df = E*len(Rc)
#E_df


for n in range(len(c4_df)):
    for i in range(len(time)):
        for k in range(len(E)):
            PhiG = (PhiL_df.iloc[n,i])*PhiG_temp.iloc[0,k]
            PhiG_values.append(PhiG)
            df2_temp = PhiG/E_df.iloc[0,k]
            df2.append(df2_temp)
PhiGMev_temp = pd.DataFrame([(df2[n:n+200]) for n in range(0, len(df2), len(E))])  
PhiGMev = PhiGMev_temp.T

for i in range(len(Rc.Rc)*len(time)):

    if Read.system == 1: #qtz
        p3n_temp_qtz = (np.trapz(PhiGMev.iloc[:,i]*Read.Onx3df[0],E_df.iloc[0,:])*Read.NatomsQtzO+ np.trapz(PhiGMev.iloc[:,i]*Read.Sinx3df[0], E_df.iloc[0,:])*Read.NatomsQtzSi)*(1e-27*3.1536e7)
        p3n_qtz.append(p3n_temp_qtz)

    #Inserted from Dave Parmelee's code (MS thesis, NMT 2014) to account for composition
    #dependence of clinopyroxene

    if Read.system == 2: #cpx
        p3n_temp_cpx = (np.trapz(PhiGMev.iloc[:,i]*Read.Onx3df[0], E_df.iloc[0,:])*Read.NatomsCpxAuO +
        np.trapz(PhiGMev.iloc[:,i]*(Read.Sinx3df[0]),E_df.iloc[0,:])*Read.NatomsCpxAuSi +
        np.trapz(PhiGMev.iloc[:,i]*(Read.Alnx3df[0]),E_df.iloc[0,:])*Read.NatomsCpxAuAl +
        np.trapz(PhiGMev.iloc[:,i]*(Read.Mgnx3df[0]), E_df.iloc[0,:])*Read.NatomsCpxAuMg +
        np.trapz(PhiGMev.iloc[:,i]*(Read.Fenx3df[0]), E_df.iloc[0,:])*Read.NatomsCpxAuFe +
        np.trapz(PhiGMev.iloc[:,i]*(Read.Canx3df[0]), E_df.iloc[0,:])*Read.NatomsCpxAuCa)*(1e-27*3.1536e7)
        p3n_cpx.append(p3n_temp_cpx)

    if Read.system == 3: #olivine
        p3n_temp_ol = (np.trapz(PhiGMev.iloc[:,i]*Read.Onx3df[0], E_df.iloc[0,:])*Read.NatomsOlFo80O +
        np.trapz(PhiGMev.iloc[:,i]*(Read.Sinx3df[0]), E_df.iloc[0,:])*Read.NatomsOlFo80Si + 
        np.trapz(PhiGMev.iloc[:,i]*(Read.Mgnx3df[0]), E_df.iloc[0,:])*Read.NatomsOlFo80Mg +
        np.trapz(PhiGMev.iloc[:,i]*(Read.Fenx3df[0]), E_df.iloc[0,:])*Read.NatomsOlFo80Fe)*(1e-27*3.1536e7)
        p3n_ol.append(p3n_temp_ol)

    #21-Ne
    if Read.system == 4:
        Natoms = 1.00228e22
        p21ndf_qtz = (np.trapz(PhiGMev.iloc[:,i]*Read.Sinx21df[0],E_df.iloc[0,:])) *(Natoms*1e-27*3.1536e7)
        p21n_qtz.append(p21ndf_qtz)


if Read.system == 1:
    pn = p3n_qtz
if Read.system == 2:
    pn = p3n_cpx
if Read.system == 3:
    pn = p3n_ol
if Read.system == 4:
    pn = p21n_qtz
lst = pn 
pn_df = pd.DataFrame([(lst[n:n+len(time)]) for n in range(0, len(lst), len(time))])

if Read.erosion[0] == str:
    pn_df[:] = pn_df.values[:, ::-1]
