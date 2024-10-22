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
import Rc
import neutron_spallation
import proton_spallation
import glob
import os
# import neutrons_LSDn
# import protons_LSDn

os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)

#Calculate scaling factor from spallation of protons + neutrons
#NOTE: all 'refs' were calculated using this model, for a hypothetical sample at SLHL.

time = Read.time 
# time_LSDn = Read.LSDn_tv

Siteprod = []
Siteprod_LSDn = []

if Read.system == 1:
    p3nref_q = 91.452156
    p3pref_q = 14.750325
    HeRef_qtz = p3nref_q + p3pref_q  #reference production rate
    
    #Nuclide specific scaling factors as f(Rc)
    for n in range(len(Rc.Rc)):
        for i in range(len(time)):
            SiteHe_temp_qtz = (neutron_spallation.pn_df.iloc[n,i] + proton_spallation.pp_df.iloc[n,i])/HeRef_qtz #scaling factor
            Siteprod.append(SiteHe_temp_qtz)
    # for n in range(len(Rc.Rc_LSDn)):
    #     for i in range(len(time_LSDn)):
    #         SiteHe_temp_qtz_LSDn = (neutrons_LSDn.pn_df.iloc[n,i] + protons_LSDn.pp_df.iloc[n,i])/HeRef_qtz #scaling factor
    #         Siteprod_LSDn.append(SiteHe_temp_qtz_LSDn)
            

if Read.system == 2:
    p3nref_cpx = 80.017751 
    p3pref_cpx =  13.039046 
    HeRef_cpx = p3nref_cpx + p3pref_cpx #reference production rate, internal

    #Nuclide specific scaling factors as f(Rc)
    for n in range(len(Rc.Rc)):
        for i in range(len(time)):
            SiteHe_temp_cpx = (neutron_spallation.pn_df.iloc[n,i] +proton_spallation.pp_df.iloc[n,i])/HeRef_cpx #scaling factor
            Siteprod.append(SiteHe_temp_cpx)
    # for n in range(len(Rc.Rc_LSDn)):
    #     for i in range(len(time_LSDn)):
    #         SiteHe_temp_cpx_LSDn = (neutrons_LSDn.pn_df.iloc[n,i] + protons_LSDn.pp_df.iloc[n,i])/HeRef_cpx #scaling factor
    #         Siteprod_LSDn.append(SiteHe_temp_cpx_LSDn)
            

if Read.system ==3 :
    #SiteHe for olivine: 
    #Nuclide Specific Scaling Factors
    p3nref_ol = 78.28355
    p3pref_ol = 13.197369 
    HeRef_ol = p3nref_ol + p3pref_ol
    #Nuclide specific scaling factors as f(Rc)
    for n in range(len(Rc.Rc)):
        for i in range(len(time)):        
            SiteHe_temp_ol = (neutron_spallation.pn_df.iloc[n,i] + proton_spallation.pp_df.iloc[n,i])/HeRef_ol #scaling factor
            Siteprod.append(SiteHe_temp_ol)
    # for n in range(len(Rc.Rc_LSDn)):
    #     for i in range(len(time_LSDn)):
    #         SiteHe_temp_ol_LSDn = (neutrons_LSDn.pn_df.iloc[n,i] + protons_LSDn.pp_df.iloc[n,i])/HeRef_ol #scaling factor
    #         Siteprod_LSDn.append(SiteHe_temp_ol_LSDn)
            

if Read.system == 4:
    p21nref_q = 11.847124
    p21pref_q = 1.624044
    NeRef_qtz = p21nref_q + p21pref_q #reference production rate
    
    for n in range(len(Rc.Rc)):
        for i in range(len(time)):  
            SiteNe_temp_qtz = (neutron_spallation.pn_df.iloc[n,i] + proton_spallation.pp_df.iloc[n,i])/NeRef_qtz #scaling factor
            Siteprod.append(SiteNe_temp_qtz)
    # for n in range(len(Rc.Rc_LSDn)):
    #     for i in range(len(time_LSDn)):
    #         SiteNe_temp_qtz_LSDn = (neutrons_LSDn.pn_df.iloc[n,i] + protons_LSDn.pp_df.iloc[n,i])/NeRef_qtz #scaling factor
    #         Siteprod_LSDn.append(SiteNe_temp_qtz_LSDn)
            

    
Siteprod_df= pd.DataFrame([(Siteprod[n:n+len(time)]) for n in range(0, len(Siteprod), len(time))])
#Siteprod_df_LSDn = pd.DataFrame([(Siteprod_LSDn[n:n+len(time_LSDn)]) for n in range(0, len(Siteprod_LSDn), len(time_LSDn))])

# n = 8 # number of bins in Siteprod_df to replace (0-2Ma)
# Siteprod_df_shortened = Siteprod_df_temp.drop(columns=Siteprod_df_temp.columns[:n])
# Siteprod_df = pd.concat([Siteprod_df_LSDn, Siteprod_df_shortened], axis=1, ignore_index = True)

Siteprod_df[0].to_csv(directory+'/text_for_plots_updated/sf_climate_EQ.csv') 
