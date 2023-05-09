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
GEOMAGIA_mean = np.mean(GEOMAGIA['VADM[E22_AmE2]'])
GEOMAGIA_std = np.std(GEOMAGIA['VADM[E22_AmE2]'])

#Calculate uncertainty envelopes at +/- 1 sigma
MCADAM_qpi3['upper'] = MCADAM_qpi3['mean'] + (1 * MCADAM_qpi3['std'])
MCADAM_qpi3['lower'] = MCADAM_qpi3['mean'] - (1 * MCADAM_qpi3['std'])
GEOMAGIA_upper = GEOMAGIA_mean + (GEOMAGIA_std * 1)
GEOMAGIA_lower = GEOMAGIA_mean - (GEOMAGIA_std * 1)

#Combine data
new_row = pd.DataFrame({'age': 0, 'mean': GEOMAGIA_mean, 'upper': GEOMAGIA_upper, 'lower': GEOMAGIA_lower}, index=[0])
PINT_df = pd.concat([new_row, MCADAM_qpi3]).reset_index(drop = True)

#Create interpolation functions
mean_f = interp1d(PINT_df['age'], PINT_df['mean'])
upper_f = interp1d(PINT_df['age'], PINT_df['upper'])
lower_f = interp1d(PINT_df['age'], PINT_df['lower'])

#Create model at full-resolution
timestep = np.arange(0, 71.005, 0.050) # 50 kyr bins
d = {'age': timestep, 'mean': mean_f(timestep), 'upper': upper_f(timestep), 'lower': lower_f(timestep)}
PINT_model = pd.DataFrame(data=d)
PINT_model.head()

#Timesteps for different bin sizes
ts_250kyr = np.arange(0, 71.005, 0.25) # 250 kyr bins
ts_500kyr = np.arange(0, 71.005, 0.50) # 500 kyr bins
ts_1ma = np.arange(0, 71.005, 1) # 1 Myr bins

#Setting up datasets for each timestep
d250kyr = {'age': ts_250kyr, 'mean': mean_f(ts_250kyr), 'upper': upper_f(ts_250kyr), 'lower': lower_f(ts_250kyr)}
d500kyr = {'age': ts_500kyr, 'mean': mean_f(ts_500kyr), 'upper': upper_f(ts_500kyr), 'lower': lower_f(ts_500kyr)}
d1ma = {'age': ts_1ma, 'mean': mean_f(ts_1ma), 'upper': upper_f(ts_1ma), 'lower': lower_f(ts_1ma)}

#Creating dataframes for each timestep
PINT_model_250kyr = pd.DataFrame(data=d250kyr)
PINT_model_500kyr = pd.DataFrame(data=d500kyr)
PINT_model_1ma = pd.DataFrame(data=d1ma)

#BELOW added by Moe for use in rest of model

array = PINT_model['mean'].values[1::]

def groupedAvg(myArray, N=5):
    result = np.cumsum(myArray, 0)[N-1::N]/float(N)
    result[1:] = result[1:] - result[:-1]
    return result

z = groupedAvg(array)

updated = np.insert(z,0, PINT_model['mean'].values[0])
temp_means = pd.DataFrame(updated)
temp_means.columns = ['mean']
ts_250kyr_updated = pd.Series(ts_250kyr)
temp_means['age'] = ts_250kyr_updated
updated_df =  temp_means[(temp_means['age'] >= Read.timerange[0]) & (temp_means['age'] < Read.timerange[1])]
means = updated_df['mean']

#PREVIOUS code
# updated_df =  PINT_model_250kyr[(PINT_model_250kyr['age'] >= Read.timerange[0]) & (PINT_model_250kyr ['age'] < Read.timerange[1])]
# means = updated_df['mean']

#Add GEOMAGIA vals to mean list
# time = np.arange(0,70+0.05,0.25)
# plt.xlim(0, 70)

# plt.plot(time,means, 'cornflowerblue', label = 'MCADAM')
# plt.hlines(5.4,0,70, linestyle = '--', color = 'darkblue', label = 'LSD long term average')

# plt.xlabel('Time (Ma)', size = 13)
# plt.ylabel(r'Paleointensity (Am$^2$ $\times$ 10 $^{22}$)', size = 13)
# plt.legend()

# plt.savefig(directory+'/plots/paleointensity_prelims.png', dpi = 300, bbox_inches='tight')

