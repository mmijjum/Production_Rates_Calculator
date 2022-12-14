#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:32:26 2022

@author: mmijjum

This script converts user-supplied latitude values into paleolatitude
- only over timeframe specified by user in User_Interface.

"""

import User_Interface
import Read
import numpy as np
import pmagpy.pmag as pmag
import pandas as pd
import matplotlib.pyplot as plt

time = User_Interface.time 


#PmagPy paleolatitude calculations
vals = [] #storage for pmagpy data 

#The following for loop converts the user-supplied latitude values (Read.lat) to paleolatitude through time.
#Plate is specified in User_Interface.py

for i in range(0,len(Read.lat)):
    for j in time:
        data=[str(User_Interface.plate),Read.lat[i], Read.lon[i],j] 
        pmag.apwp(data, print_results = False) #change to true if you want to see the output
        vals.append(pmag.apwp(data))

#save outputs in usable dataframes for later.
# pl = np.repeat(Read.site_lat.values, len(time))
# pl_df = pd.DataFrame([(pl[n:n+len(time)]) for n in range(0, len(pl), len(time))])



df = pd.DataFrame(vals) 
df.columns = ['Age', 'Paleolat', 'Dec','Inc','Pole_lat','Pole_Long'] 
Paleolat = df['Paleolat']

pl_df = pd.DataFrame([(Paleolat.values.tolist()[n:n+len(time)]) for n in range(0, len(Paleolat.values.tolist()), len(time))])

#RUN THIS IF YOU'RE MAKING FIG. 3
# pl_temp = np.repeat(90,len(time))
# pl_df = pd.DataFrame([(pl_temp[n:n+101]) for n in range(0, len(pl_temp), len(time))])
