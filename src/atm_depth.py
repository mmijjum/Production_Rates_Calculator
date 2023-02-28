#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:25:17 2022

@author: mmijjum

This script converts the user-supplied elevation to an atmospheric depth.

It will perfrom the ERA40 reanalysis if user specified '0' for standard atmosphere in User_Interface
It will perform a standard atmospheric conversion if user specifies '1' for standard atmosphere in User_Interface.

This was originally written by Greg Balco, then modified by Brent Goehring and Nat Lifton. This version was modified by Moe Mijjum for python. 

"""

import numpy as np
import pandas as pd
import scipy as sci
import Read
import Pmag_paleolat
import User_Interface
import math

def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor
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
empty = []
for i in range(len(Pmag_paleolat.pl_df.to_numpy().flatten().tolist())):
    dtdz = lr[0] + lr[1]*Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i] + lr[2]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**2 + lr[3]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**3 + lr[4]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**4 + lr[5]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**5 + lr[6]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**6;
    dtdz = -dtdz
    differential.append(dtdz)
    
if User_Interface.stdatm == 0: #ERA40
    for i in range(len(slp)):
        sp = slp[i] * np.exp( (gmr/differential[i]) * (np.log(temp[i]) - np.log(temp[i] - (alt_list[i]*differential[i])) ) )
        sp = float(sp)
        empty.append(sp)
    sample_pressure = pd.DataFrame([(empty[n:n+len(time)]) for n in range(0, len(empty), len(time))])

if User_Interface.stdatm == 1:
    for i in range(len(alt_list)):
        differential = 0.0065
        sp = 1013.25 * np.exp((gmr/differential)*(np.log(288.15) - np.log(288.15 - (alt_list[i]*differential))))
        empty.append(sp)
    sample_pressure = pd.DataFrame([(empty[n:n+len(time)]) for n in range(0, len(empty), len(time))])


x_updated = []
for i in range(len(empty)):
    temp = truncate(empty[i],0)
    x_updated.append(float(temp))
xdf = pd.DataFrame([(x_updated[n:n+len(time)]) for n in range(0, len(x_updated), len(time))])

#convert pressure to atmospheric depth
def atmdepth(x):
    return x*(1.019716)
x = atmdepth(xdf)

# xn = np.repeat(1013.25*1.019716, len(xdf)*2)
# x = pd.DataFrame([(xn[n:n+len(time)]) for n in range(0, len(xn), len(time))])
