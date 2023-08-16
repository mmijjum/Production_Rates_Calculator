# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:44:57 2023

@author: kebri

Updated by Moe Mijjum on May 15th, 2023
"""
#Imports and dependencies
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import os
import Read
import matplotlib.pyplot as plt

#Set path
directory = os.path.dirname(__file__)

#Read in excerpt of MCADAM1.b model (QPI>=3) (Bono et al., 2021)

MCADAM_250ka_full = pd.read_excel(directory+'/Data/mcadam_v1b_cosmo250kyr.xlsx', index_col=0) 
MCADAM_250 = MCADAM_250ka_full.iloc[0:281]

temp_median =pd.concat([MCADAM_250['age'],MCADAM_250['50%']],axis=1)
updated_df =  temp_median[(temp_median['age'] >= Read.time[0]) & (temp_median['age'] <= Read.time[-1])]
medians = updated_df['50%'].reset_index(drop=True)

#50kyr resolution model
#need to update time range in 'read' to use this

# MCADAM_50ka_full = pd.read_excel(directory+'/Data/mcadam_v1b_cosmo50kyr.xlsx', index_col=0) 
# MCADAM_50 = MCADAM_50ka_full[0:1401]
# temp_median =pd.concat([MCADAM_50['age'],MCADAM_50['50%']],axis=1)
# updated_df =  temp_median[(temp_median['age'] >= Read.time[0]) & (temp_median['age'] <= Read.time[-1])]
# medians = updated_df['50%']

#1000kyr resolution model
#need to update time range in 'read' to use this
# MCADAM_1000ka_full = pd.read_excel(directory+'/Data/mcadam_v1b_cosmo1000kyr.xlsx', index_col=0) 
# MCADAM_1000 = MCADAM_1000ka_full.iloc[0:71]
# temp_median =pd.concat([MCADAM_1000['age'],MCADAM_1000['50%']],axis=1)
# updated_df =  temp_median[(temp_median['age'] >= Read.time[0]) & (temp_median['age'] <= Read.time[-1])]
# medians = updated_df['50%']
