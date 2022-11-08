#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:32:26 2022

@author: mmijjum
"""

import User_Interface
import Read
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

df = pd.DataFrame(vals) 
df.columns = ['Age', 'Paleolat', 'Dec','Inc','Pole_lat','Pole_Long'] 
Paleolat = df['Paleolat']
pl_df = pd.DataFrame([(Paleolat.values.tolist()[n:n+len(time)]) for n in range(0, len(Paleolat.values.tolist()), len(time))])

#x = pl_df.iloc[0]
#india, present day to 70 Ma
#plt.plot(time,x)
#plt.plot(time, pl_df.iloc[1])


# plt.figure()
# plt.subplot(211)
# plt.plot(time,x, color='blue',c = 'blue', label = '20N, 73E')
# plt.legend(loc = 'lower left', frameon=True)
# plt.subplot(212)
# plt.plot(time,pl_df.iloc[1], color='green', label = '19S, 69W')
# plt.xlabel('Time [Ma]')
# plt.legend(frameon=True)
# plt.savefig('paleolat_subplots.png', dpi = 300, bbox_inches='tight')
