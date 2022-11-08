#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:25:17 2022

@author: mmijjum
"""

import numpy as np
import pandas as pd
import scipy as sci
import Read
import Pmag_paleolat
import User_Interface

time = User_Interface.time 



lon_repeated = np.repeat(Read.lon,len(time))
lon_df = pd.DataFrame([(lon_repeated.tolist()[n:n+len(time)]) for n in range(0, len(lon_repeated.tolist()), len(time))])
alt_list = np.repeat(Read.alt, len(time))

lat_numpy = Read.ERA40lat.to_numpy()
lon_numpy = Read.ERA40lon.to_numpy()
meanT_numpy = Read.meanT.to_numpy()
meanP_numpy = Read.meanP.to_numpy()


gmr = -0.03417; # Assorted constants
dtdz = 0.0065; # Lapse rate from standard atmosphere

lon_list = []
for i in range(len(Read.site_lon)):
    if Read.lon[i] < 0: #negative longitude correction
        site_lon_updated = Read.lon[i] + 360
        lon_list.append(site_lon_updated)
    else:
        lon_list.append(Read.site_lon)

temp = []
slp = []
differential = []
sample_pressure = []

for i in range(len(Pmag_paleolat.pl_df.to_numpy().flatten().tolist())):
    t = sci.interpolate.interp2d(lon_numpy,lat_numpy,meanT_numpy)
    site_T = t(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i], lon_df.to_numpy().flatten().tolist()[i])
    site_T_degK = site_T + 273.15
    temp.append(site_T)
    p = sci.interpolate.interp2d(lon_numpy,lat_numpy,meanP_numpy)
    site_slp = p(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i], lon_df.to_numpy().flatten().tolist()[i])
    slp.append(site_slp)
    
#Lifton Lapse Rate Fit to COSPAR CIRA-86 <10 km altitude
lr = [-6.1517E-03, -3.1831E-06, -1.5014E-07, 1.8097E-09, 1.1791E-10, -6.5359E-14, -9.5209E-15]

differential = []
sp_list = []
for i in range(len(Pmag_paleolat.pl_df.to_numpy().flatten().tolist())):
    dtdz = lr[0] + lr[1]*Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i] + lr[2]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**2 + lr[3]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**3 + lr[4]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**4 + lr[5]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**5 + lr[6]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**6;
    dtdz = -dtdz
    differential.append(dtdz)
    
if User_Interface.stdatm == 0: #ERA40
    for i in range(len(slp)):
        sp = slp[i] * np.exp( (gmr/differential[i]) * (np.log(temp[i]) - np.log(temp[i] - (alt_list[i]*differential[i])) ) )
        sp = float(sp)
        sp_list.append(sp)
    sample_pressure = pd.DataFrame([(sp_list[n:n+len(time)]) for n in range(0, len(sp_list), len(time))])

empty = []
if User_Interface.stdatm == 1:
    for i in range(len(differential)):
        sp = 1013.25 * np.exp((gmr/differential[i])*(np.log(288.15) - np.log(288.15 - (alt_list[i]*differential[i]))))
        empty.append(sp)
    sample_pressure = pd.DataFrame([(empty[n:n+len(time)]) for n in range(0, len(empty), len(time))])

#convert pressure to atmospheric depth
def atmdepth(x):
    return x*1.019716

x = atmdepth(sample_pressure)

# # Back to calculating neutron spallation production
