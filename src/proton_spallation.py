#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:46:54 2022

@author: mmijjum

This script will calculate the production of some nuclide-mineral pair due to proton spallation. 

Based on Sato et al. (2008) Neutron Spectrum, and PARMA (analytical function approx.
                                                         )
This code was originally implemented in MATLAB by Nat Lifton in 2013. This modified version was written by Moe Mijjum.

"""

import numpy as np
import pandas as pd
import Rc
import Read
import atm_depth


time = Read.time 


s = 624.5718; #Solar modulation- uses constant value that Lifton (2008)/code uses for samples beyond 10 Ma
smin = 400; #Units of MV
smax = 1200; #Units of MV
w = 0.2

#PROTONS
p3p_cpx = []
p3p_ol = []
p3p_qtz = []
p21p_qtz = []
A = 1
Z = 1
Ep = 938.27 #Rest mass of a proton
U = (4-1.675)*(np.pi)*(A/Z)*1e-7 # Unit conversion factor
p3p = []

df = np.logspace(0,5.3010,200) #Energy spectrum [MeV]. From LSD, data from Sato & Nita (2008) 
E = pd.DataFrame(df)
E.columns = ['Energy']
E_df = pd.concat([E.T]*len(Rc.Rc), ignore_index=True)

Elis = np.zeros((1,len(E)))
Beta = np.zeros((1,len(E)))
Rlis = np.zeros((1,len(E)))
phiTOA = np.zeros((1,len(E)))
phiLIS = np.zeros((1,len(E)))
phiSec = np.zeros((1,len(E)))
phiPtot = np.zeros((1,len(E)))
p10p = np.zeros((1,len(E)))
empty = []
Etoa = []

phiPri = []
x = atm_depth.x[0].to_numpy().flatten().tolist()
E = np.logspace(0,5.3010,200) #Energy spectrum [MeV]. From LSD, data from Sato & Nita (2008) 

for i in range(len(x)):
    for j in range(len(E)): 
            Etoa_temp = E[j]+ 2.1153*x[i]
            Etoa.append(Etoa_temp)

Etoa_df = pd.DataFrame([(Etoa[n:n+200]) for n in range(0, len(Etoa), len(E))]) 

def Rtoa(Etoa):
    return 0.001*np.sqrt((A*Etoa)**2 + 2*A*Ep*Etoa)/Z
Rtoa = Rtoa(Etoa_df) #shape (samples*time,len(E))

def b(s1, s2, s3, s4):
    return s1+s2*atm_depth.x[0]+s3*atm_depth.x[0]**2+s4*atm_depth.x[0]**3

b1 = b(Read.secondary_spectrum.iloc[0]['values'],Read.secondary_spectrum.iloc[1]['values'],Read.secondary_spectrum.iloc[2]['values'],Read.secondary_spectrum.iloc[3]['values'])
b2 = b(Read.secondary_spectrum.iloc[4]['values'],Read.secondary_spectrum.iloc[5]['values'],Read.secondary_spectrum.iloc[6]['values'],Read.secondary_spectrum.iloc[7]['values'])
b3 = b(Read.secondary_spectrum.iloc[8]['values'],Read.secondary_spectrum.iloc[9]['values'],Read.secondary_spectrum.iloc[10]['values'],Read.secondary_spectrum.iloc[11]['values'])
b4 = b(Read.secondary_spectrum.iloc[12]['values'],Read.secondary_spectrum.iloc[13]['values'],Read.secondary_spectrum.iloc[14]['values'],Read.secondary_spectrum.iloc[15]['values'])

def Elisfun(Etoa):
    return Etoa + s*Z/A
Elis = Elisfun(Etoa_df)

def Betafun(Elisx):
    return np.sqrt(1-(Ep/(Ep + Elisx*A))**2) # Particle speed relative to light
Beta = Betafun(Elis)


def Rlisfun(Elisx):
    return  0.001*np.sqrt((A*Elisx)**2 + 2*A*Ep*Elisx)/Z
Rlis = Rlisfun(Elis)

def Cfun(p1, p2, p3, p4, Elisx):
    return p1 + p2/(1 + np.exp((Elisx - p3)/p4))
C = Cfun(Read.primary_spectrum.iloc[6]['values'],Read.primary_spectrum.iloc[7]['values'],Read.primary_spectrum.iloc[8]['values'],Read.primary_spectrum.iloc[9]['values'], Elis)

def phiTOAfun(C,B,p1,Rlis,p2,Rtoa):
    return (C*(B**p1)/(Rlis**p2))*(Rtoa/Rlis)**2
phiTOA = phiTOAfun(C,Beta,Read.primary_spectrum.iloc[4]['values'],Rlis,Read.primary_spectrum.iloc[5]['values'], Rtoa)


for i in range(len(Beta)):
    for j in range(len(E)):
        phiPri_temp = (U/Beta.iloc[i,j])*phiTOA.iloc[i,j]*(Read.primary_spectrum.iloc[1]['values']*np.exp(-Read.primary_spectrum.iloc[2]['values']*x[i]) + (1 - Read.primary_spectrum.iloc[1]['values'])*np.exp(-Read.primary_spectrum.iloc[3]['values']*x[i]))
        phiPri.append(phiPri_temp)
phiPri_df = pd.DataFrame([(phiPri[n:n+200]) for n in range(0, len(phiPri), len(E))]) 

def minmax(g1, g2, g3, g4, g5):
    return g1 + g2*Rc.Rc.iloc[: , 0:] + g3/(1 + np.exp((Rc.Rc.iloc[: , 0:] - g4)/g5))
g1min = minmax(Read.h_values_protons.iloc[0]['values'] , Read.h_values_protons.iloc[2]['values'] ,Read.h_values_protons.iloc[4]['values'] ,Read.h_values_protons.iloc[6]['values'] ,Read.h_values_protons.iloc[8]['values'] )
g1max = minmax(Read.h_values_protons.iloc[1]['values'] , Read.h_values_protons.iloc[3]['values'] ,Read.h_values_protons.iloc[5]['values'] ,Read.h_values_protons.iloc[7]['values'] ,Read.h_values_protons.iloc[9]['values'] )
g2min = minmax(Read.h_values_protons.iloc[10]['values'] , Read.h_values_protons.iloc[12]['values'] ,Read.h_values_protons.iloc[14]['values'] ,Read.h_values_protons.iloc[16]['values'] ,Read.h_values_protons.iloc[18]['values'] )
g2max = minmax(Read.h_values_protons.iloc[11]['values'] , Read.h_values_protons.iloc[13]['values'] ,Read.h_values_protons.iloc[15]['values'] ,Read.h_values_protons.iloc[17]['values'] ,Read.h_values_protons.iloc[19]['values'] )
g3min = minmax(Read.h_values_protons.iloc[20]['values'] , Read.h_values_protons.iloc[22]['values'] ,Read.h_values_protons.iloc[24]['values'] ,Read.h_values_protons.iloc[26]['values'] ,Read.h_values_protons.iloc[28]['values'] )
g3max = minmax(Read.h_values_protons.iloc[21]['values'] , Read.h_values_protons.iloc[23]['values'] ,Read.h_values_protons.iloc[25]['values'] ,Read.h_values_protons.iloc[27]['values'] ,Read.h_values_protons.iloc[29]['values'] )
g4min = minmax(Read.h_values_protons.iloc[30]['values'] , Read.h_values_protons.iloc[32]['values'] ,Read.h_values_protons.iloc[34]['values'] ,Read.h_values_protons.iloc[36]['values'] ,Read.h_values_protons.iloc[38]['values'] )
g4max = minmax(Read.h_values_protons.iloc[31]['values'] , Read.h_values_protons.iloc[33]['values'] ,Read.h_values_protons.iloc[35]['values'] ,Read.h_values_protons.iloc[37]['values'] ,Read.h_values_protons.iloc[39]['values'] )

g5 = minmax(Read.h_values_protons.iloc[40]['values'] , Read.h_values_protons.iloc[41]['values'] ,Read.h_values_protons.iloc[42]['values'] ,Read.h_values_protons.iloc[43]['values'] ,Read.h_values_protons.iloc[43]['values'] )
g6 = minmax(Read.h_values_protons.iloc[45]['values'] , Read.h_values_protons.iloc[46]['values'] ,Read.h_values_protons.iloc[47]['values'] ,Read.h_values_protons.iloc[48]['values'] ,Read.h_values_protons.iloc[49]['values'] )


phiP = []
for i in range(len(g1min)):
    for j in range(len(time)):
        phiPmin = g1min.iloc[i,j]*(np.exp(-g2min.iloc[i,j]*x[i]) - g3min.iloc[i,j]*np.exp(-g4min.iloc[i,j]*x[i])) 
        phiPmax = g1max.iloc[i,j]*(np.exp(-g2max.iloc[i,j]*x[i]) - g3max.iloc[i,j]*np.exp(-g4max.iloc[i,j]*x[i])) 
        
        f3 = g5.iloc[i,j] + g6.iloc[i,j]*x[i]
        f2 = (phiPmin - phiPmax)/(smin**f3 - smax**f3)
        f1 = phiPmin - f2*smin**f3
        
        phiP_temp = f1 + f2*s**f3
        phiP.append(phiP_temp)
phiP_df = pd.DataFrame([(phiP[n:n+len(time)]) for n in range(0, len(phiP), len(time))])

phiSec = []
df2p = []

for i in range(len(phiP_df)):
    for j in range(len(time)):
        for k in range(len(E)):
            phiSec_temp = (phiP_df.iloc[i,j]*b1[i]*E[k]**b2[i])/(1 + b3[i]*E[k]**b4[i])
            phiSec.append(phiSec_temp)

phiSec_df = pd.DataFrame([(phiSec[n:n+200]) for n in range(0, len(phiSec), len(E))]) #checked 1/27, sliiiightly off

def Ecfun(Rc):
    return (np.sqrt((1000*Rc.iloc[: , 0:]*Z)**2 + Ep**2) - Ep)/A
Ec = Ecfun(Rc.Rc)


Es1_list = []
Es2_list = []
for i in range(len(Ec)):
    for j in range(len(time)):
        Es = 1.3691*(Ec.iloc[i,j] - 2.0665*x[i])
        Es1 = max(108.33,Es)
        Es2 = max(2301.3,Es)
        Es1_list.append(Es1)
        Es2_list.append(Es2)  
Es1_df = pd.DataFrame([(Es1_list[n:n+len(time)]) for n in range(0, len(Es1_list), len(time))]) #checked 1/27
Es2_df = pd.DataFrame([(Es2_list[n:n+len(time)]) for n in range(0, len(Es2_list), len(time))]) #checked 1/27

Es1_updated = Es1_df.stack().tolist() #this flattens ES1 df into a list so you can incorporate it into the for loop below
Es2_updated = Es2_df.stack().tolist() #this flattens ES1 df into a list so you can incorporate it into the for loop below
E_updated = E_df.loc[E_df.index.repeat(len(time))].reset_index(drop=True)

updated_phiPri = phiPri_df.loc[phiPri_df.index.repeat(len(time))]

for i in range(len(updated_phiPri)):
    for j in range(len(E)):
        df2p_temp = (updated_phiPri.iloc[i,j])*(np.tanh(3.4643*(E[j]/Es1_updated[i] - 1)) + 1)/2 + phiSec_df.iloc[i,j]*(np.tanh(1.6752*(1 - E[j]/Es2_updated[i])) + 1)/2 
        df2p.append(df2p_temp)
phiPtot = pd.DataFrame([(df2p[n:n+200]) for n in range(0, len(df2p), len(E))]) #checked 2/1, works


p3p_qtz = []
p3p_cpx = []
p3p_ol = []
p21p_qtz = []

for i in range(len(Rc.Rc)*len(time)):

    if Read.system == 1: #qtz
        p3p_temp_qtz = (np.trapz(phiPtot.T.iloc[:,i]*Read.Onx3df[0],E_df.iloc[0,:])*Read.NatomsQtzO+ np.trapz(phiPtot.T.iloc[:,i]*Read.Sinx3df[0], E_df.iloc[0,:])*Read.NatomsQtzSi)*(1e-27*3.1536e7)
        p3p_qtz.append(p3p_temp_qtz)

    #Inserted from Dave Parmelee's code (MS thesis, NMT 2014) to account for composition
    #dependence of clinopyroxene

    if Read.system == 2: #cpx
        p3p_temp_cpx = (np.trapz(phiPtot.T.iloc[:,i]*Read.Onx3df[0], E_df.iloc[0,:])*Read.NatomsCpxAuO +
        np.trapz(phiPtot.T.iloc[:,i]*(Read.Sinx3df[0]),E_df.iloc[0,:])*Read.NatomsCpxAuSi +
        np.trapz(phiPtot.T.iloc[:,i]*(Read.Alnx3df[0]),E_df.iloc[0,:])*Read.NatomsCpxAuAl +
        np.trapz(phiPtot.T.iloc[:,i]*(Read.Mgnx3df[0]), E_df.iloc[0,:])*Read.NatomsCpxAuMg +
        np.trapz(phiPtot.T.iloc[:,i]*(Read.Fenx3df[0]), E_df.iloc[0,:])*Read.NatomsCpxAuFe +
        np.trapz(phiPtot.T.iloc[:,i]*(Read.Canx3df[0]), E_df.iloc[0,:])*Read.NatomsCpxAuCa)*(1e-27*3.1536e7)
        p3p_cpx.append(p3p_temp_cpx)

    if Read.system == 3: #olivine
        p3p_temp_ol = (np.trapz(phiPtot.T.iloc[:,i]*Read.Onx3df[0], E_df.iloc[0,:])*Read.NatomsOlFo80O +
        np.trapz(phiPtot.T.iloc[:,i]*(Read.Sinx3df[0]), E_df.iloc[0,:])*Read.NatomsOlFo80Si + 
        np.trapz(phiPtot.T.iloc[:,i]*(Read.Mgnx3df[0]), E_df.iloc[0,:])*Read.NatomsOlFo80Mg +
        np.trapz(phiPtot.T.iloc[:,i]*(Read.Fenx3df[0]), E_df.iloc[0,:])*Read.NatomsOlFo80Fe)*(1e-27*3.1536e7)
        p3p_ol.append(p3p_temp_ol)

    #21-Ne
    if Read.system == 4:
        Natoms = 1.00228e22
        p21pdf_qtz = (np.trapz(phiPtot.T.iloc[:,i]*Read.Sinx21df[0],E_df.iloc[0,:])*Natoms) *(1e-27*3.1536e7)
        p21p_qtz.append(p21pdf_qtz)

if Read.system == 1:
    pp = p3p_qtz
if Read.system == 2:
    pp = p3p_cpx 
if Read.system ==3:
    pp = p3p_ol 
if Read.system == 4:
    pp = p21p_qtz
    
#bin_names = ['0 - 50 kyr', '50 kyr - 5 Ma', '5 - 10 Ma', '10 - 15 Ma', '15 - 20 Ma', '20 - 25 Ma', '25 - 30 Ma', 
            #'30 - 35 Ma', '35 - 40 Ma', '40 - 45 Ma', '45 - 50 Ma', '50 - 55 Ma', '55 - 60 Ma', '60 - 65 Ma', '65 - 70 Ma']

pp_df = pd.DataFrame([(pp[n:n+len(time)]) for n in range(0, len(pp), len(time))])


if Read.erosion[0] == str:
    pp_df[:] = pp_df.values[:, ::-1]
