#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:54:41 2022

@author: mmijjum
"""
import numpy as np
 

## USER input information HERE ##
system = 1 #see above for options
system_b = 0 #see above for options
system_c = 0 #see above for options
stdatm = 1
muons = False
timerange = [0,70]
resolution = int(250000)/10**6
time = np.linspace(timerange[0], timerange[1], int(timerange[1]/resolution)) # time bins

plate = 'SA'

