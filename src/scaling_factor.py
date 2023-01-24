#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:41:07 2022

@author: mmijjum
"""

import numpy as np
import User_Interface
import pandas as pd
import Rc
import neutron_spallation
import proton_spallation
import Pmag_paleolat


#Calculate scaling factor from spallation of protons + neutrons

time = User_Interface.time 
Siteprod = []

if User_Interface.system == 1:
    #qtz
    #Nuclide Specific Scaling Factors
    # p3nref_q = 90.0788 #nat's
    # p3pref_q = 13.6184
    p3nref_q = 91.6318
    p3pref_q = 14.7771
    HeRef_qtz = p3nref_q + p3pref_q  #reference production rate
    #HeRef_qtz = p3nref_q + p3pref_q #reference production rate
    
    #Nuclide specific scaling factors as f(Rc)
    for n in range(len(Rc.Rc)):
        for i in range(len(time)):
            SiteHe_temp_qtz = (neutron_spallation.pn_df.iloc[n,i] + proton_spallation.pp_df.iloc[n,i])/HeRef_qtz #scaling factor
            Siteprod.append(SiteHe_temp_qtz)
            

if User_Interface.system == 2:
    #SiteHe for cpx:
    # p3nref_cpx = 78.8285 #these are nat's values
    # p3pref_cpx = 11.9608
    p3nref_cpx = 80.1750
    p3pref_cpx = 13.0628
    HeRef_cpx = p3nref_cpx + p3pref_cpx #reference production rate, internal

    #HeRef_cpx = (p3nref_au + p3pref_au) #reference production rate
    #Nuclide specific scaling factors as f(Rc)
    for n in range(len(Rc.Rc)):
        for i in range(len(time)):
            SiteHe_temp_cpx = (neutron_spallation.pn_df.iloc[n,i] +proton_spallation.pp_df.iloc[n,i])/HeRef_cpx #scaling factor
            Siteprod.append(SiteHe_temp_cpx)

if User_Interface.system ==3 :
    #SiteHe for olivine: 
    #Nuclide Specific Scaling Factors
    p3nref_ol = 81.3239
    p3pref_ol = 12.5509
    HeRef_cpx = p3nref_ol + p3pref_ol
    #Nuclide specific scaling factors as f(Rc)
    for n in range(len(Rc.Rc)):
        for i in range(len(time)):        
            SiteHe_temp_ol = (neutron_spallation.pn_df.iloc[n,i] + proton_spallation.pp_df.iloc[n,i])/HeRef_ol #scaling factor
            Siteprod.append(SiteHe_temp_ol)

if User_Interface.system == 4:
    #qtz
    #Nuclide Specific Scaling Factors
    p21nref_q = 90.0788
    p21pref_q = 13.6184
    NeRef_qtz = p21nref_q + p21pref_q #reference production rate
    
    #Nuclide specific scaling factors as f(Rc)
    for n in range(len(Rc.Rc)):
        for i in range(len(time)):  
            SiteNe_temp_qtz = (neutron_spallation.pn_df.iloc[n,i] + proton_spallation.pp_df.iloc[n,i])/NeRef_qtz #scaling factor
            Siteprod.append(SiteNe_temp_qtz)
# import math

# def truncate(number, decimals=0):
#     """
#     Returns a value truncated to a specific number of decimal places.
#     """
#     if not isinstance(decimals, int):
#         raise TypeError("decimal places must be an integer.")
#     elif decimals < 0:
#         raise ValueError("decimal places has to be 0 or more.")
#     elif decimals == 0:
#         return math.trunc(number)

#     factor = 10.0 ** decimals
#     return math.trunc(number * factor) / factor

# sf_updated = []
# for i in range(len(Siteprod)):
#     temp = truncate(Siteprod[i],2)
#     sf_updated.append(temp)
    
Siteprod_df = pd.DataFrame([(Siteprod[n:n+len(time)]) for n in range(0, len(Siteprod), len(time))])

     
#define SLHL. Ref is pre-calculated above, dependent on mineral/nuclide system. 
if User_Interface.system ==1:
    ref = HeRef_qtz
if User_Interface.system ==2: 
    ref = 105.437561
if User_Interface.system == 3: 
    ref = HeRef_ol
if User_Interface.system == 4:
    ref = NeRef_qtz


