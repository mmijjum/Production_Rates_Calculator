#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:41:07 2022

@author: mmijjum

This script calculates spallogenic scaling factors as a function of time. 
OUTPUT: Siteprod_df (dataframe of scaling factors through time for each sample.)

"""
import numpy as np
import Read
import pandas as pd
import Rc_MCADAM
import neutron_spallation_MCADAM
import proton_spallation_MCADAM
import glob
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)

#Calculate scaling factor from spallation of protons + neutrons
#NOTE: all 'refs' were calculated using this model, for a hypothetical sample at SLHL.

time = Read.time 

Siteprod = []
Siteprod_LSDn = []

if Read.system == 1:
    p3nref_q = 91.452156
    p3pref_q = 14.750325
    HeRef_qtz = p3nref_q + p3pref_q  #reference production rate
    
    #Nuclide specific scaling factors as f(Rc)
    for n in range(len(Rc_MCADAM.Rc)):
        for i in range(len(time)):
            SiteHe_temp_qtz = (neutron_spallation_MCADAM.pn_df.iloc[n,i] + proton_spallation_MCADAM.pp_df.iloc[n,i])/HeRef_qtz #scaling factor
            Siteprod.append(SiteHe_temp_qtz)
 
if Read.system == 2:
    p3nref_cpx = 80.017751 
    p3pref_cpx =  13.039046 
    HeRef_cpx = p3nref_cpx + p3pref_cpx #reference production rate, internal

    #Nuclide specific scaling factors as f(Rc)
    for n in range(len(Rc_MCADAM.Rc)):
        for i in range(len(time)):
            SiteHe_temp_cpx = (neutron_spallation_MCADAM.pn_df.iloc[n,i] +proton_spallation_MCADAM.pp_df.iloc[n,i])/HeRef_cpx #scaling factor
            Siteprod.append(SiteHe_temp_cpx)

if Read.system ==3 :
    #SiteHe for olivine: 
    #Nuclide Specific Scaling Factors
    p3nref_ol = 78.28355
    p3pref_ol = 13.197369 
    HeRef_ol = p3nref_ol + p3pref_ol
    #Nuclide specific scaling factors as f(Rc)
    for n in range(len(Rc_MCADAM.Rc)):
        for i in range(len(time)):        
            SiteHe_temp_ol = (neutron_spallation_MCADAM.pn_df.iloc[n,i] + proton_spallation_MCADAM.pp_df.iloc[n,i])/HeRef_ol #scaling factor
            Siteprod.append(SiteHe_temp_ol)
    

if Read.system == 4:
    p21nref_q = 11.847124
    p21pref_q = 1.624044
    NeRef_qtz = p21nref_q + p21pref_q #reference production rate
    
    for n in range(len(Rc_MCADAM.Rc)):
        for i in range(len(time)):  
            SiteNe_temp_qtz = (neutron_spallation_MCADAM.pn_df.iloc[n,i] + proton_spallation_MCADAM.pp_df.iloc[n,i])/NeRef_qtz #scaling factor
            Siteprod.append(SiteNe_temp_qtz)
 

    
Siteprod_df= pd.DataFrame([(Siteprod[n:n+len(time)]) for n in range(0, len(Siteprod), len(time))])