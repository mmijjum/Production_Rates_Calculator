# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:44:57 2023

@author: kebri
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
MCADAM_qpi3 = pd.read_csv(directory+'/Data/MCADAM_1b.csv') 

#Read in volcanic and archeomagnetic data from GEOMAGIA50.v3 (Brown et al., 2015)
#Calculate mean and std
GEOMAGIA = pd.read_csv(directory+'/Data/archeo010.csv', header=1)
GEOMAGIA_median = np.median(GEOMAGIA['VADM[E22_AmE2]'])
GEOMAGIA_std = np.std(GEOMAGIA['VADM[E22_AmE2]'])

#Calculate uncertainty envelopes at +/- 1 sigma
MCADAM_qpi3['upper'] = MCADAM_qpi3['50%'] + (1 * MCADAM_qpi3['std'])
MCADAM_qpi3['lower'] = MCADAM_qpi3['50%'] - (1 * MCADAM_qpi3['std'])
GEOMAGIA_upper = GEOMAGIA_median + (GEOMAGIA_std * 1)
GEOMAGIA_lower = GEOMAGIA_median - (GEOMAGIA_std * 1)

#Combine data
new_row = pd.DataFrame({'age': 0, '50%': GEOMAGIA_median, 'upper': GEOMAGIA_upper, 'lower': GEOMAGIA_lower}, index=[0])
PINT_df = pd.concat([new_row, MCADAM_qpi3]).reset_index(drop = True)
PINT_df.rename(columns={'50%': 'median'}, inplace=True)

#Timesteps for different bin sizes
ts_50kyr = np.arange(0, 71.005, 0.05) # 50 kyr bins
ts_250kyr = np.arange(0, 71.005, 0.25) # 250 kyr bins
ts_1ma = np.arange(0, 71.005, 1) # 1 Myr bins


# #BELOW added by Moe for use in rest of model

array = PINT_df['median'].values[1::]

def groupedAvg(myArray, N=5):
    result = np.cumsum(myArray, 0)[N-1::N]/float(N)
    result[1:] = result[1:] - result[:-1]
    return result

z = groupedAvg(array)

updated = np.insert(z,0, PINT_df['median'].values[0])
temp_median = pd.DataFrame(updated)
temp_median.columns = ['median']
ts_250kyr_updated = pd.Series(ts_250kyr)
temp_median['age'] = ts_250kyr_updated
updated_df =  temp_median[(temp_median['age'] >= Read.timerange[0]) & (temp_median['age'] < Read.timerange[1])]
medians = updated_df['median']

