#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:32:26 2022

@author: mmijjum

This script converts user-supplied latitude values into paleolatitude
- only over timeframe specified by user.

"""

import Read
import numpy as np
import pmagpy.pmag as pmag
import pandas as pd
import matplotlib.pyplot as plt

time = Read.time 


#PmagPy paleolatitude calculations
vals = [] #storage for pmagpy data 

#The following for loop converts the user-supplied latitude values (Read.lat) to paleolatitude through time.

for i in range(0,len(Read.lat)):
    for j in time:
        data=[str(Read.plate),Read.lat[i], Read.lon[i],j] 
        pmag.apwp(data, print_results = False) #change to true if you want to see the output
        vals.append(pmag.apwp(data))

df = pd.DataFrame(vals) 
df.columns = ['Age', 'Paleolat', 'Dec','Inc','Pole_lat','Pole_Long'] 
Paleolat = df['Paleolat']
Inc = df['Inc']

pl_df = pd.DataFrame([(Paleolat.values.tolist()[n:n+len(time)]) for n in range(0, len(Paleolat.values.tolist()), len(time))])
inc_df  = pd.DataFrame([(Paleolat.values.tolist()[n:n+len(time)]) for n in range(0, len(Paleolat.values.tolist()), len(time))])

#RUN THIS IF YOU'RE MAKING FIG. 3
# pl_temp = np.repeat(90,len(time))
# pl_df = pd.DataFrame([(pl_temp[n:n+101]) for n in range(0, len(pl_temp), len(time))])

#RUN THIS to create non-time varying paleolatitude dataframe
# pl = np.repeat(Read.site_lat.values, len(time))
# pl_df = pd.DataFrame([(pl[n:n+len(time)]) for n in range(0, len(pl), len(time))])
