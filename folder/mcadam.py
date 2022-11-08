#!/usr/bin/env python
# coding: utf-8


#Imports and dependencies
import User_Interface
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#get_ipython().run_line_magic('matplotlib', 'inline')


#Set directory
#os.chdir('/drive/notebooks/ProdRateCalc')

#Convert MCADAM xlsx to csv and manually remove rows past 70Ma or pandas has an aneurysm 
#Read in MCADAM model (QPI>=3)
MCADAM_qpi3 = pd.read_csv('MCADAM_1b.csv')

#Adding new columns for upper and lower bounds using +/- 2 STD
MCADAM_qpi3['upper'] = MCADAM_qpi3['mean'] + (2 * MCADAM_qpi3['std'])
MCADAM_qpi3['lower'] = MCADAM_qpi3['mean'] - (2 * MCADAM_qpi3['std'])

#Preview dataframe
MCADAM_qpi3.head()


#Plot of relevant subset of MCADAM (QPI>=3) at full resolution (~55kyr bins)
f = plt.figure()
plt.plot(MCADAM_qpi3['age'], MCADAM_qpi3['mean'], color='orange')
plt.plot(MCADAM_qpi3['age'], MCADAM_qpi3['lower'], color='gray', alpha=0.4)
plt.plot(MCADAM_qpi3['age'], MCADAM_qpi3['upper'], color='gray', alpha=0.4)
plt.fill_between(MCADAM_qpi3['age'], MCADAM_qpi3['upper'], MCADAM_qpi3['lower'], color='steelblue', alpha=0.2)
plt.ylabel('MCADAM Mean Dipole (1e22 Am2)')
plt.xlabel('Age Step Realization (Ma)')
plt.ylim(0,12)
f.savefig('MCADAM_1b-full_res.png')

#Create interpolation function
mean_f = interp1d(MCADAM_qpi3['age'], MCADAM_qpi3['mean'])
#print(mean_f(54)) # Test at some random time to make sure it works

#Do the same for the upper and lower bounds
upper_f = interp1d(MCADAM_qpi3['age'], MCADAM_qpi3['upper'])
lower_f = interp1d(MCADAM_qpi3['age'], MCADAM_qpi3['lower'])

#Use interpolation function to create new dataframe with specified timestep
#To change timestep, follow: timestep = np.arange(0.055, 71.005, x) where x is your desired bin size

timestep = np.arange(0.055, 71.005, 0.25) # 250 kyr bins
d = {'age': timestep, 'mean': mean_f(timestep), 'upper': upper_f(timestep), 'lower': lower_f(timestep)}
MCADAM_qpi3_int = pd.DataFrame(data=d)

#Preview new dataframe
MCADAM_qpi3_int.head()


# Create list of means
#means = MCADAM_qpi3_int['mean']
#means =  MCADAM_qpi3_int[(MCADAM_qpi3_int['age']) >= User_Interface.timerange[0] & (MCADAM_qpi3_int['age'] <= User_Interface.timerange[1])]
#means.head()

#Plot of MCADAM model (QPI>=3) interpolated to 250kyr timesteps
plt.plot(MCADAM_qpi3_int['age'], MCADAM_qpi3_int['mean'], color='orange')
plt.plot(MCADAM_qpi3_int['age'], MCADAM_qpi3_int['lower'], color='gray', alpha=0.4)
plt.plot(MCADAM_qpi3_int['age'], MCADAM_qpi3_int['upper'], color='gray', alpha=0.4)
plt.fill_between(MCADAM_qpi3_int['age'], MCADAM_qpi3_int['upper'], MCADAM_qpi3_int['lower'], color='steelblue', alpha=0.2)
plt.ylabel('MCADAM Mean Dipole (1e22 Am2)')
plt.xlabel('Age Step Realization (Ma)')
plt.ylim(0,12)
plt.savefig('MCADAM_1b-250kyr_step.png')


#Use Excel to remove columns past ArcheoVolcanic or pandas has an aneurysm 
#Read in all GEOMAGIA data (query: Intensities, VADM)
GEOMAGIA = pd.read_csv('archeo010.csv', header=1)

#Calculate mean and stdev for all GEOMAGIA data
GEOMAGIA_mean = np.mean(GEOMAGIA['VADM[E22_AmE2]'])
GEOMAGIA_std = np.std(GEOMAGIA['VADM[E22_AmE2]'])

#Check results
#print('The mean field (0-55kyr) is', np.format_float_positional(GEOMAGIA_mean, precision=2), 'Am2 and the std is', np.format_float_positional(GEOMAGIA_std, precision=2), 'Am2.')


#### FOUR PANEL PLOT BELOW ####
## Make datasets for subplots we want to compare against full res

#Create interpolation function
mean_f = interp1d(MCADAM_qpi3['age'], MCADAM_qpi3['mean'])
#print(mean_f(0.055)) # Test at x years to make sure it works

#Do the same for the upper and lower bounds
upper_f = interp1d(MCADAM_qpi3['age'], MCADAM_qpi3['upper'])
lower_f = interp1d(MCADAM_qpi3['age'], MCADAM_qpi3['lower'])

#Use interpolation function to create new dataframe with specified timestep
#To change timestep: ts_x = np.arange(0.055, 71.005, x) where x is your desired bin size
ts_1ma = np.arange(0.055, 71.005, 1) # 1 Myr bins
ts_500kyr = np.arange(0.055, 71.005, 0.50) # 500 kyr bins
ts_250kyr = np.arange(0.055, 71.005, 0.25) # 250 kyr bins

#Setting up datasets for each timestep
d1ma = {'age': ts_1ma, 'mean': mean_f(ts_1ma), 'upper': upper_f(ts_1ma), 'lower': lower_f(ts_1ma)}
d500kyr = {'age': ts_500kyr, 'mean': mean_f(ts_500kyr), 'upper': upper_f(ts_500kyr), 'lower': lower_f(ts_500kyr)}
d250kyr = {'age': ts_250kyr, 'mean': mean_f(ts_250kyr), 'upper': upper_f(ts_250kyr), 'lower': lower_f(ts_250kyr)}


#Creating dataframes for each timestep
MCADAM_qpi3_int_1ma = pd.DataFrame(data=d1ma)
MCADAM_qpi3_int_500kyr = pd.DataFrame(data=d500kyr)
MCADAM_qpi3_int_250kyr = pd.DataFrame(data=d250kyr)

#Preview new dataframe
#MCADAM_qpi3_int_55kyr.head()

## Make plot with subplots for each timestep we are testing
fig, axs = plt.subplots(2, 2, figsize=(14, 8))

# 55kyr bins (full resolution) subplot
axs[0, 0].plot(MCADAM_qpi3['age'], MCADAM_qpi3['mean'], color='maroon', linewidth=0.75)
axs[0, 0].plot(MCADAM_qpi3['age'], MCADAM_qpi3['lower'], color='gray', linewidth=0.5, alpha=0.6)
axs[0, 0].plot(MCADAM_qpi3['age'], MCADAM_qpi3['upper'], color='gray', linewidth=0.5, alpha=0.6)
axs[0, 0].fill_between(MCADAM_qpi3['age'], MCADAM_qpi3['upper'], MCADAM_qpi3['lower'], color='cadetblue', alpha=0.2)
axs[0, 0].set_ylabel('MCADAM Mean Dipole (1e22 Am2)')
axs[0, 0].set_ylim(0, 12)
axs[0, 0].text(20, 11.25, '55kyr bins (full resolution)')

# 250kyr bins subplot
axs[0, 1].plot(MCADAM_qpi3_int_250kyr['age'], MCADAM_qpi3_int_250kyr['mean'], color='maroon', linewidth=0.75)
axs[0, 1].plot(MCADAM_qpi3_int_250kyr['age'], MCADAM_qpi3_int_250kyr['lower'], color='gray', linewidth=0.5, alpha=0.6)
axs[0, 1].plot(MCADAM_qpi3_int_250kyr['age'], MCADAM_qpi3_int_250kyr['upper'], color='gray', linewidth=0.5, alpha=0.6)
axs[0, 1].fill_between(MCADAM_qpi3_int_250kyr['age'], MCADAM_qpi3_int_250kyr['upper'], MCADAM_qpi3_int_250kyr['lower'], color='cadetblue', alpha=0.2)
axs[0, 1].set_ylim(0, 12)
#axs[0, 1].set_title('250kyr bins')
axs[0, 1].text(30, 11.25, '250kyr bins')

# 500kyr bins subplot
axs[1, 0].plot(MCADAM_qpi3_int_500kyr['age'], MCADAM_qpi3_int_500kyr['mean'], color='maroon', linewidth=0.75)
axs[1, 0].plot(MCADAM_qpi3_int_500kyr['age'], MCADAM_qpi3_int_500kyr['lower'], color='gray', linewidth=0.5, alpha=0.6)
axs[1, 0].plot(MCADAM_qpi3_int_500kyr['age'], MCADAM_qpi3_int_500kyr['upper'], color='gray', linewidth=0.5, alpha=0.6)
axs[1, 0].fill_between(MCADAM_qpi3_int_500kyr['age'], MCADAM_qpi3_int_500kyr['upper'], MCADAM_qpi3_int_500kyr['lower'], color='cadetblue', alpha=0.2)
axs[1, 0].set_ylabel('MCADAM Mean Dipole (1e22 Am2)')
axs[1, 0].set_xlabel('Age Step Realization (Ma)')
axs[1, 0].set_ylim(0, 12)
axs[1, 0].text(30, 11.25, '500kyr bins')

# 1Ma bins subplot
axs[1, 1].plot(MCADAM_qpi3_int_1ma['age'], MCADAM_qpi3_int_1ma['mean'], color='maroon', linewidth=0.75)
axs[1, 1].plot(MCADAM_qpi3_int_1ma['age'], MCADAM_qpi3_int_1ma['lower'], color='gray', linewidth=0.5, alpha=0.6)
axs[1, 1].plot(MCADAM_qpi3_int_1ma['age'], MCADAM_qpi3_int_1ma['upper'], color='gray', linewidth=0.5, alpha=0.6)
axs[1, 1].fill_between(MCADAM_qpi3_int_1ma['age'], MCADAM_qpi3_int_1ma['upper'], MCADAM_qpi3_int_1ma['lower'], color='cadetblue', alpha=0.2)
axs[1, 1].set_xlabel('Age Step Realization (Ma)')
axs[1, 1].set_ylim(0, 12)
axs[1, 1].text(30, 11.25, '1Ma bins')

fig.savefig('MCADAM_Binning_Comparison.png')

means_df =  MCADAM_qpi3_int[(MCADAM_qpi3_int['age'] <= User_Interface.timerange[1])]
means = means_df['mean']

