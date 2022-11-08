#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:06:36 2022

@author: mmijjum
"""
import numpy as np
import User_Interface
import Pmag_paleolat
import mcadam
import pandas as pd

time = User_Interface.time 

mu_knot = (1.256*10**-6)*10**22 #m kg s-2 A-2
c = 299792458 #m/s
R = 6.378*10**6 #m
Rc_list = []

for x in range (len(Pmag_paleolat.pl_df)):
    for i in range(len(mcadam.means)):
        Rc_calc = (((mcadam.means[i]*mu_knot*c)/(16*np.pi*R**2))*((np.cos(np.deg2rad(Pmag_paleolat.pl_df.iloc[x,i])))**4))/10**9

        Rc_list.append(Rc_calc)
Rc = pd.DataFrame([(Rc_list[n:n+len(time)]) for n in range(0, len(Rc_list), len(time))])

Rc