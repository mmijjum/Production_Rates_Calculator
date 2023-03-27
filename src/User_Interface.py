#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:54:41 2022

@author: mmijjum
"""
import numpy as np
 
"""
        User Interface for sample specific parameters

        Parameters
        ----------
        system  : integer 1 - 4 (nuclide-mineral pair)
            1 = 3He in quartz
            2 = 3He in clinopyroxene
            3 = 3He in olivine
            4 = 21Ne in quartz
        system_b : integer 0 - 4 (specify cpx/opx)
            0 = N/A (non-cpx)
            1 = enstatite
            2 = ferrosilite
            3 = wollastonite
            4 = augite
        system_c : 0 - 3 (specify olivine)
            0 = N/A (non-olivine)
            1 = Forsterite
            2 = Fayalite
            3 = F8
        
        stdatm : 0 or 1 (atmospheric depth dependence)
            0 = ERA40 reanalysis data (applicable for recent exposures)
            1 = standard atmospheric conversion (RECOMMENDED)
            
        muons : TRUE/FALSE (specify if Muons script is applicable)
            True : only for 21Ne in qtz (system = 4)
            False: all other systems (system = 1,2,3)
        
        timerange : [start, stop] of exposure duration (in Ma)
            start: minimum 0 (present day)
            stop: maximum 70
            NOTE: do not remove "+0.05"
        
        plate: string (specify plate)
            NA : North America
            SA : South America
            AF : Africa
            IN : India
            EU : Eurasia
            AU : Australia
            ANT: Antarctica
            GL : Greenland

        """

system = 2
system_b = 4
system_c = 0
stdatm = 1
muons = False
timerange = [0,0.25+0.05]
plate = 'SA'


## USER DO NOT EDIT BELOW ##
resolution = int(250000)/10**6

time = np.arange(timerange[0], timerange[1], resolution) # time bin#for 250ka resolution, with first bin being 50 ka




