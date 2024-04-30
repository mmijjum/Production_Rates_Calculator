#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:25:17 2022

@author: mmijjum

This script converts the user-supplied elevation to an atmospheric depth.

This was originally written by Greg Balco, then modified by Brent Goehring and Nat Lifton. This version was modified by Moe Mijjum for python. 

"""

import numpy as np
import pandas as pd
import scipy as sci
import Read
import Pmag_paleolat
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
time = Read.time 
delta = Read.delta
conversion_factor = 0.01*250000
binsize= 250000

delta = delta*conversion_factor
lon_repeated = np.repeat(Read.lon,len(time))
lon_df = pd.DataFrame([(lon_repeated.tolist()[n:n+len(time)]) for n in range(0, len(lon_repeated.tolist()), len(time))])
alt_list_temp = np.repeat(Read.alt, len(time))
delta_list = np.repeat(delta, len(time)).reset_index(drop=True)

alt_list = alt_list_temp+delta_list.reset_index(drop=True)
# for j in range(len(delta)):
#     for i in range(len(alt_list)-1): ##UPDATE ALT LIST TO REFLECT UPLIFT/SUBSIDENCE
#         alt_list[i+1]=alt_list[i]+delta[j]
     
 
if Read.stdatm == 0: #ERA40, using dataset from LSDn

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
    
    temp1 = []
    slp = []
    differential = []
    sample_pressure = []
    
    for i in range(len(Pmag_paleolat.pl_df.to_numpy().flatten().tolist())):
        t = sci.interpolate.interp2d(lon_numpy,lat_numpy,meanT_numpy)
        site_T = t(lon_df.to_numpy().flatten().tolist()[i],Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])
        temp1.append(site_T)
        p = sci.interpolate.interp2d(lon_numpy,lat_numpy,meanP_numpy)
        site_slp = p(lon_df.to_numpy().flatten().tolist()[i],Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])
        slp.append(site_slp)
        
    #Lifton Lapse Rate Fit to COSPAR CIRA-86 <10 km altitude
    lr = [-6.1517E-03, -3.1831E-06, -1.5014E-07, 1.8097E-09, 1.1791E-10, -6.5359E-14, -9.5209E-15]
    
    differential = []
    empty = []
    for i in range(len(Pmag_paleolat.pl_df.to_numpy().flatten().tolist())):
        dtdz = lr[0] + lr[1]*Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i] + lr[2]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**2 + lr[3]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**3 + lr[4]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**4 + lr[5]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**5 + lr[6]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**6;
        dtdz = -dtdz
        differential.append(dtdz)
        
    for i in range(len(slp)):
        sp = slp[i] * np.exp( (gmr/differential[i]) * (np.log(temp1[i]) - np.log(temp1[i] - (alt_list[i]*differential[i])) ) )
        sp = float(sp)
        empty.append(sp)
    sample_pressure = pd.DataFrame([(empty[n:n+len(time)]) for n in range(0, len(empty), len(time))])

if Read.stdatm == 1: #Standard atmosphere
    gmr = -0.03417; # Assorted constants
    dtdz = 0.0065; # Lapse rate from standard atmosphere
        #Lifton Lapse Rate Fit to COSPAR CIRA-86 <10 km altitude
    lr = [-6.1517E-03, -3.1831E-06, -1.5014E-07, 1.8097E-09, 1.1791E-10, -6.5359E-14, -9.5209E-15]
    empty = []
        
    for i in range(len(alt_list)):
        differential = 0.0065
        sp = 1013.25 * np.exp((gmr/differential)*(np.log(288.15) - np.log(288.15 - (alt_list[i]*differential))))
        empty.append(sp)
    sample_pressure = pd.DataFrame([(empty[n:n+len(time)]) for n in range(0, len(empty), len(time))])

if Read.stdatm == 2: #climate simulation
    lat_numpy = Read.climate_lat.to_numpy() #read in lat/lon grids from climate simulation (slightly different from ERA40)
    lon_numpy = Read.climate_lon.to_numpy()
   
    a = Read.climate_mslp_a #mean sea level pressures for each time slice, each letter denotes new time slice
    b = Read.climate_mslp_b
    c = Read.climate_mslp_c
    d = Read.climate_mslp_d
    e = Read.climate_mslp_e
    f = Read.climate_mslp_f
    g = Read.climate_mslp_g
    h = Read.climate_mslp_h
    i = Read.climate_mslp_i
    j = Read.climate_mslp_j
    k = Read.climate_mslp_k
    l = Read.climate_mslp_l
    m = Read.climate_mslp_m
    n = Read.climate_mslp_n
    o = Read.climate_mslp_o
    
    mslp_merged = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o) #merge all MSLP time slices into a single grid
    
    at = Read.climate_mat_a #repeat above, but for mean annual temp
    bt = Read.climate_mat_b
    ct = Read.climate_mat_c
    dt = Read.climate_mat_d
    et = Read.climate_mat_e
    ft = Read.climate_mat_f
    gt = Read.climate_mat_g
    ht = Read.climate_mat_h
    it = Read.climate_mat_i
    jt = Read.climate_mat_j
    kt = Read.climate_mat_k
    lt = Read.climate_mat_l
    mt = Read.climate_mat_m
    nt = Read.climate_mat_n
    ot = Read.climate_mat_o

    mat_merged = (at,bt,ct,dt,et,ft,gt,ht,it,jt,kt,lt,mt,nt,ot)


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
    
    time = Read.time
    domain = [0,2,7.25,12.75,17.25,22.75,28.50,33.50,37.75,42,48.50,54,58.25,63.50,67.50,72] #using midpoints, the range of each time slice (in Ma)
    mini_durations = [0,8,21,22,18,22,23,20,17,17,26,22,17,21,16,18] #how many MCADAM bins in climate bin (e.g., between 0-2 Ma, there are 8 MCADAM bins (sized 250 ka))
    stop = (np.argmax(domain > time[-1])) - 1 #determine where in the domain to start, given user input of start time
    start_temp = min(domain, key = lambda x: abs(x-time[0]))
    start = domain.index(start_temp)#np.argmax(domain <= time[0])  #determine where in the domain to end, given user input of end time
    if stop == start: #determine how many consecutive bins will be used. If stop == start, only one bin is used.
        duration = range(start)
    
    else:
        duration = range(start,stop+1)
    
    for j in range(len(Read.site_lon)): #interpolate to identify temp/MSLP for each time bin, and resize to match 
        x = mini_durations[0]
        for k in duration:
            t = sci.interpolate.interp2d(lon_numpy,lat_numpy,mat_merged[k])
            p = sci.interpolate.interp2d(lon_numpy,lat_numpy,mslp_merged[k])
            y = x + mini_durations[k+1]
            site_T = t(lon_df.loc[j][x:y],Pmag_paleolat.pl_df.loc[j][x:y])
            site_T_degK = site_T + 273.15
            temp.append(site_T_degK)
            site_slp = p(lon_df.loc[j][x:y],Pmag_paleolat.pl_df.loc[j][x:y])
            slp.append(site_slp)
            x = y
           

            
            
    temperatures = []
    pressures = []
    for i in range(len(temp)):
        for k in range(len(temp[i])):
            x = temp[i][k][0]
            y = slp[i][k][0]
            temperatures.append(x)
            pressures.append(y)
        
            
    #Lifton Lapse Rate Fit to COSPAR CIRA-86 <10 km altitude
    lr = [-6.1517E-03, -3.1831E-06, -1.5014E-07, 1.8097E-09, 1.1791E-10, -6.5359E-14, -9.5209E-15]
    
    differential = []
    empty = []
    for i in range(len(Pmag_paleolat.pl_df.to_numpy().flatten().tolist())):
        dtdz = lr[0] + lr[1]*Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i] + lr[2]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**2 + lr[3]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**3 + lr[4]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**4 + lr[5]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**5 + lr[6]*(Pmag_paleolat.pl_df.to_numpy().flatten().tolist()[i])**6;
        dtdz = -dtdz
        differential.append(dtdz)
    pressures_new = []
    last = []
    
    
    for i in range(len(pressures)):
        sp = pressures[i] * np.exp( (gmr/differential[i]) * (np.log(temperatures[i]) - np.log(temperatures[i] - (alt_list[i]*differential[i])) ) )
        #sp = float(sp)
        empty.append(sp)

    sample_pressure = pd.DataFrame([(empty[n:n+len(time)]) for n in range(0, len(empty), len(time))])
    sample_pressure = sample_pressure.fillna(0)

#convert pressure to atmospheric depth
def atmdepth(x):
    return x*(1.019716)
x = atmdepth(sample_pressure)

##below hard codes sea level atm depth
# xn = np.repeat(1013.25*1.019716, len(x) * len(time))
# x = pd.DataFrame([(xn[n:n+len(time)]) for n in range(0, len(xn), len(time))])

# x.to_csv(Read.directory+'/text_for_plots/valdes_v_time.csv', index=False)  

