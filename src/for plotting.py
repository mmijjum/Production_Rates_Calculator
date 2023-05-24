#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:57:00 2022

@author: mmijjum
"""
import numpy as np

import matplotlib.pyplot as plt
import Read
import pandas as pd
import Rc
import Pmag_paleolat
import glob
import os
import shielding
import scaling_factor
import neutron_spallation
import proton_spallation
import muons
# import matplotlib.gridspec as gridspec


os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)



"""
Figure 1 
Flux comparisons 

"""
# plt.figure(figsize=(8,6)) 
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[0]*neutron_spallation.E.iloc[:,0], '--',c = 'darkblue', label = 'Sea level, pole')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[2]*neutron_spallation.E.iloc[:,0], c = 'darkblue', label = 'Sea level, equator')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[8]*neutron_spallation.E.iloc[:,0], '--', c = 'darkgreen', label = '2000 masl, pole')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[10]*neutron_spallation.E.iloc[:,0],  c = 'darkgreen', label = '2000 masl, equator')


# plt.ylabel('Differential Flux' r'$ \;\times$' 'Energy ' '$ (cm^{-2} s^{-1}$)', fontsize = 13)
# plt.xlabel('Energy (MeV)', fontsize = 13)
# plt.legend(loc='lower left')
# plt.savefig(directory+'/plots/Figure_1.svg', dpi = 300, bbox_inches='tight')


"""
Figure 2
Rc vs. Scaling Factor
"""
# # create figure and axis objects with subplots()
# # in excel sheet: set every lat to 0-90, lon = 0, elevation = 0. Uncomment out the part of pmag that hard-codes the latitudes (so it doesn't vary w time)
# # only run for like 1 Ma, bc you're only gonna use the first value anyways.
# # note: make sure you hard code atm depth to 1033 g/cm2


# paleolatitudes = np.arange(0,92,2)
# fig,ax = plt.subplots()


# # make a plot with different y-axis using second axis object
# ax.plot(paleolatitudes, Read.Rc_full[1][1:],color="darkblue")
# ax.plot(paleolatitudes, Read.Rc_half[1][1:],color="darkblue", linestyle = '-.')

# ax.set_ylim(top = 15)

# ax.set_ylabel("Cutoff Rigidity (GV)",
#               color="darkblue",
#               fontsize=13)
# ax.set_xlabel("Geomagnetic Latitude", fontsize = 13)
# ax.spines['left'].set_color('darkblue')
# ax.tick_params(axis='y', colors='darkblue')

# # twin object for two different y-axis on the sample plot
# ax2=ax.twinx()
# ax2.plot(paleolatitudes, Read.sf_full[1][1:],
#         color="darkgreen", label = "$M_{present}$")
# ax2.plot(paleolatitudes, Read.sf_half[1][1:],
#         color="darkgreen", linestyle = '-.', label = "$M_{half}$")
# ax2.set_ylim(top = 1.1)
# # set x-axis label
# # set y-axis label
# ax2.set_xlim(left=0)
# ax2.set_xlim(right=90)
# ax2.set_ylabel("Scaling Factor",color="darkgreen",fontsize=13)
# ax2.tick_params(axis='y', colors='darkgreen')

# ax2.legend(loc = 'right')

# plt.savefig(Read.directory+'/plots/Figure_2.pdf', dpi = 300, bbox_inches='tight')

# ##DO NUT RUN, SAVED CSV's##
# Rc_half = Rc.Rc.iloc[:,0]
# Rc_half.to_csv(directory+'/text_for_plots/Rc_half.csv') 

# sf_half = scaling_factor.Siteprod_df[0]
# sf_half.to_csv(directory+'/text_for_plots/sf_half.csv') 

# Rc_full = Rc.Rc.iloc[:,0]
# Rc_full.to_csv(directory+'/text_for_plots/Rc_full.csv') 

# sf_full = scaling_factor.Siteprod_df[0]
# sf_full.to_csv(directory+'/text_for_plots/sf_full.csv') 


"""
Figure 3
PALEOLAT FIGURE

UPDATED: 1/30
"""

# time = np.linspace(0,70,281)
##DO NOT RUN THESE FILES, THEY ARE SAVED##
# # IN = Pmag_paleolat.pl_df.iloc[0]
# # IN.to_csv(directory+'/text_for_plots/IN.csv') 


# # SA = Pmag_paleolat.pl_df.iloc[1]
# # SA.to_csv(directory+'/text_for_plots/SA.csv') 
 

# # GL = Pmag_paleolat.pl_df.iloc[2]
# # GL.to_csv(directory+'/text_for_plots/GL.csv') 


# # AF = Pmag_paleolat.pl_df.iloc[3]
# # AF.to_csv(directory+'/text_for_plots/AF.csv') 

#BEGIN UNCOMMENTING~~

# fig = plt.figure(figsize=(10.5, 8.5))
# spec = fig.add_gridspec(3,3)
# fig.text(0.06, 0.65, 'Normalized paleolatitude', va='center', rotation='vertical', size =15)
# fig.text(0.45, 0.34, 'Time (Ma)', va='center', rotation='horizontal', size =15)

# time = np.arange(0,70+0.25,0.25)
# ax0 = fig.add_subplot(spec[0, :])
# ax0.plot(time,Read.IN.iloc[:,1]/Read.IN.iloc[0,1], 'royalblue', label = 'India (20N, 73E)')
# ax0.plot(time,Read.GL.iloc[:,1]/Read.GL.iloc[0,1], 'darkblue')
# ax0.plot(time,(Read.SA.iloc[:,1]+90)/(Read.SA.iloc[0,1]+90), 'mediumseagreen')
# ax0.plot(time,(Read.AF.iloc[:,1]+90)/(Read.AF.iloc[0,1]+90), 'darkgreen')
# ax0.text(65,0, 'A', fontsize = 22)

# plt.axhspan(0.85, 1.1, xmin=0, xmax=1, color = 'gray', alpha = 0.5)

# ax0.set_xlim(0, 70)
# plt.legend()
# #annotate_axes(ax0, 'ax0')

# ax10 = fig.add_subplot(spec[1, :])
# ax10.plot(time,Read.GL.iloc[:,1]/Read.GL.iloc[0,1], 'darkblue', label = 'Greenland (75N, 42W)')
# ax10.plot(time,(Read.SA.iloc[:,1]+90)/(Read.SA.iloc[0,1]+90), 'mediumseagreen', label = 'Northern Chile (19S, 69W)')
# ax10.plot(time,(Read.AF.iloc[:,1]+90)/(Read.AF.iloc[0,1]+90), 'darkgreen', label = 'South Africa (31S, 22E)')
# ax10.set_xlim(0, 70)
# ax10.text(65,0.93, 'B', fontsize = 22)

# plt.legend()


# plt.savefig(directory+'/plots/Figure_4.svg', dpi = 300, bbox_inches='tight')
"""
Figure 4
Workflow figure
"""


"""
Figure 5
MCADAM Model

"""


"""
FIGURE 6
Comparing bin size

"""

#DO NOT RUN BELOW#

# sf_50kyr = scaling_factor.Siteprod_df.iloc[0]
# sf_50kyr.to_csv(directory+'/text_for_plots/sf_50kyr.csv')

# sf_1ma = scaling_factor.Siteprod_df.iloc[0]
# sf_1ma.to_csv(directory+'/text_for_plots/sf_1ma.csv') 

# sf_250ka= scaling_factor.Siteprod_df.iloc[0]
# sf_250ka.to_csv(directory+'/text_for_plots/sf_250ka.csv') 

#START RUN#
# time1 =  np.arange(0,70.05,0.05)
# time2=  np.arange(0,70.05,0.25)

# x = Read.sf_50kyr.iloc[:,1]

# plt.rcParams["figure.figsize"] = [5,5] #update figure size 
# # plt.scatter(time, Read.sf_250kyr.iloc[:,1]/sub[:], s = 20, marker = 's', c = 'cornflowerblue',  label = '250 kyr')
# # plt.scatter(time, Read.sf_250kyr.iloc[:,1]/gupdated[:], s = 15 ,c = 'teal', label = '1ma')
# plt.plot(time1, Read.sf_250ka.iloc[:,1].repeat(5).reset_index(drop=True).iloc[4:].reset_index(drop=True)/x, c = 'cornflowerblue',  label = 'SF(250kyr) : SF(50kyr)')
# plt.plot(time2,  Read.sf_250ka.iloc[:,1]/Read.sf_1ma.iloc[:,1].repeat(4).reset_index(drop=True).iloc[3:].reset_index(drop=True), c = 'black', label = 'SF(250kyr): SF(1 Ma)')
# plt.xlabel('Time (Ma)', fontsize = 13)
# plt.ylabel('Scaling factor ratio', fontsize = 13)
# plt.legend(loc = 'lower right')
# plt.xlim(0,70)
# plt.savefig(Read.directory+'/plots/Figure_6.svg', dpi = 300, bbox_inches='tight')


"""
FIGURE 7
Atmospheric Depth / SF variations

"""
##DO NOT RE RUN THIS PART##
# x = scaling_factor.Siteprod_df
# GL_STD_sf = x[0][0:17]
# GL_STD_sf.to_csv(directory+'/text_for_plots/Figure_7_GL_STD')

# x = scaling_factor.Siteprod_df
# GL_ERA40_sf = x[0][0:17]
# GL_ERA40_sf.to_csv(directory+'/text_for_plots/Figure_7_GL_ERA40')

# x = scaling_factor.Siteprod_df
# EC_ERA40_sf = x[0][17::]
# EC_ERA40_sf.to_csv(directory+'/text_for_plots/Figure_7_EC_ERA40')

# x = scaling_factor.Siteprod_df
# EC_STD_sf = x[0][17::]
# EC_STD_sf.to_csv(directory+'/text_for_plots/Figure_7_EC_STD')


#START RUN#
# from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,
#                                                   mark_inset)
# import matplotlib.patches as patches
# fig = plt.figure(figsize=(4,4))

# alt = np.arange(0,5001,500)


# fig, ax1 = plt.subplots()
# ax1.set_aspect('equal')
# ax1.plot(Read.GL_STD.iloc[1:12][1],Read.GL_ERA40.iloc[1:12][1], 'x-',  markersize = 4, label = 'High latitude: 75N,40E ', c = 'darkmagenta')
# ax1.plot(Read.EC_STD.iloc[1:12][1],Read.EC_ERA40.iloc[1:12][1], 'x-',    markersize = 4,label = 'Equator: 0N, 78E' , c = 'green')
# ax1.set_ylabel('Scaling factor using ERA40')
# ax1.set_xlabel('Scaling factor using standard atmosphere')
# ax1.legend(loc=0)
# ax1.set_ylim(0,40)
# ax1.set_xlim(0,40)

# rect = patches.Rectangle((0, 0), 5, 5, linewidth=1, edgecolor='k', facecolor='none')
# ax1.add_patch(rect)

# left, bottom, width, height = [0.53, 0.2, 0.20, 0.25] # modify to move the inset curve and change its size
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(Read.GL_STD.iloc[1:12][1],Read.GL_ERA40.iloc[1:12][1], 'x-',  markersize = 4, label = 'High latitude: 75N,40E ', c = 'darkmagenta')
# ax2.plot(Read.EC_STD.iloc[1:12][1],Read.EC_ERA40.iloc[1:12][1], 'x-',    markersize = 4,label = 'Equator: 0N, 78E' , c = 'green')
# ax2.set_xlim(0,5)
# ax2.set_ylim(0,5)
# ax2.set_xticks([0, 2,4])
# ax2.set_yticks([0,2,4])
# ax2.tick_params(axis='both', which='major', labelsize=8)

# plt.savefig(Read.directory+'/plots/Figure_7.svg', dpi = 300, bbox_inches='tight')

"""
FIGURE 8
Scaling factor TV and Constant

"""


# # #DONT RUN THIS PART
# sf_india = scaling_factor.Siteprod_df.iloc[0]
# sf_india.to_csv(directory+'/text_for_plots/sf_IN.csv') 
# sf_india_const = scaling_factor.Siteprod_df.iloc[0]
# sf_india_const.to_csv(directory+'/text_for_plots/sf_IN_const.csv') 
# sf_india_tvfieldonly = scaling_factor.Siteprod_df.iloc[0]
# sf_india_tvfieldonly.to_csv(directory+'/text_for_plots/sf_india_tvfieldonly.csv') 
# sf_india_tvlatonly = scaling_factor.Siteprod_df.iloc[0]
# sf_india_tvlatonly.to_csv(directory+'/text_for_plots/sf_india_tvlatonly.csv') 

# # #BEGIN
time = np.linspace(0,70,281)
# f = plt.figure(figsize=(10,4))
# ax = f.add_subplot(121)
# ax2 = f.add_subplot(122)
# ax.plot(time,Read.sf_IN.iloc[:,1], c = 'cornflowerblue',label = 'time-varying field and latitude')
# ax.plot(time,Read.sf_IN_const.iloc[:,1], '--',c = 'gray', label = 'constant field and latitude')
# ax.set_xlim(0,70)
# #ax.set_ylim(0.50,0.90)
# ax.vlines(66.052, 0.50, 0.90)
# ax.set_xlabel('Time (Ma)', fontsize = 13)
# ax.set_ylabel('Scaling Factor', fontsize = 13)
# ax.legend(loc = 'lower left')

# ax2.plot(time,Read.sf_IN_tvfieldonly.iloc[:,1], c = 'darkblue',label = 'time-varying field, constant latitude')
# ax2.plot(time,Read.sf_IN_tvlatonly.iloc[:,1], '--',c = 'darkblue', label = 'constant field, time-varying latitude')
# ax2.set_xlim(0,70)
# #ax2.set_ylim(0.50,0.90)
# ax2.vlines(66.052, 0.50, 0.90)
# ax2.set_xlabel('Time (Ma)', fontsize = 13)
# ax2.legend(loc = 'lower left')
# plt.setp(ax2.get_yticklabels(), visible=False)

# plt.plot(time,Read.sf_IN.iloc[:,1], c = 'cornflowerblue',label = 'time-varying field and latitude')
# plt.plot(time,Read.sf_IN_const.iloc[:,1], '--',c = 'gray', label = 'constant field and latitude')
# plt.plot(time,Read.sf_IN_tvfieldonly.iloc[:,1], c = 'darkblue',label = 'time-varying field, constant latitude')
# plt.plot(time,Read.sf_IN_tvlatonly.iloc[:,1], '--',c = 'darkblue', label = 'constant field, time-varying latitude')
# plt.legend()
# plt.savefig(directory+'/plots/scaling_factors.png', dpi = 300, bbox_inches='tight')




"""
FIGURE 9
EVENSTAR DATASET
# """
# exp_ages_time_varying = [131996.26202489913,
#   1023626.3006114559,
#   2818578.1182617154,
#   1442111.5909461104,
#   1572187.6926164788,
#   2278513.403392353,
#   2789561.569762896,
#   5190519.589554306,
#   824517.3451888387,
#   1039899.2318907074,
#   3213175.7139825514,
#   5186659.724390685,
#   4721445.394785178,
#   5000015.329512211,
#   5759439.620363143,
#   3711836.322560931,
#   4060198.6266656416,
#   4191863.641518183,
#   3972943.0084628374,
#   10899929.349473981,
#   7500679.307668893,
#   11590489.115385713,
#   10242831.200003851,
#   10087732.900187513,
#   2503058.2716951943,
#   2450012.1182982484,
#   1919685.6734813016,
#   2088176.22741603]


# exp_ages_constant=[114400.49565798171,
#   917329.0518705035,
#   2751355.8402647623,
#   1344161.0993252213,
#   1473394.0657873328,
#   2224522.064947964,
#   2720917.8318576734,
#   4991435.653787645,
#   724923.5683262685,
#   931319.1949078307,
#   3126699.593423725,
#   4973918.624462918,
#   4543407.160283238,
#   4812717.1869177325,
#   5608767.36018699,
#   3614767.3369865143,
#   3961286.539982639,
#   4078001.1497473023,
#   3877127.438196669,
#   11309454.76557007,
#   7606839.109954978,
#   12123018.074383643,
#   10541403.567087896,
#   10368523.26303627,
#   2446694.6469513695,
#   2396470.5016860655,
#   1849428.0879702813,
#   2025791.0757406428]

# exp_neon_tv = [925394.9003644264,
#   907557.1721116758,
#   276612.40319194266,
#   122540.79545892825,
#   322327.13753088925,
#   227052.2907854808,
#   267801.40712947334,
#   37299.39263586361,
#   2096294.213187858,
#   2189679.5142527027,
#   3061778.4589791135,
#   5985087.135238934,
#   2968169.8326294757,
#   2163056.8551527187]

# exp_neon_const = [809860.9281488108,
#   793119.6169726079,
#   237012.03447028896,
#   104784.26787107512,
#   276929.85080212716,
#   195750.59034431167,
#   231188.1972169888,
#   31842.72636385542,
#   2017729.6458384574,
#   2117270.9750331547,
#   2958672.607989357,
#   5850182.994291976,
#   2868402.6018716474,
#   2089254.4066904038]



# updated_texp_tv = []
# updated_texp_const = []


# updated_neon_tv = []
# updated_neon_const = []


# diff_tv_pyx = []
# diff_tv_qtz = []
# perdif = []

# perdifneon = []
# for i in range(len(exp_ages_constant)): #convert ages from [yr] to [Ma]
#     updated = exp_ages_time_varying[i]/10**6
#     updated_texp_tv.append(updated) #Evenstar data
#     updated_const = exp_ages_constant[i]/10**6 
#     updated_texp_const.append(updated_const) #this model
#     temp = updated - updated_const
#     diff_tv_pyx.append(temp)
#     perdif.append((temp/updated_const)*100)

# for i in range(len(exp_neon_tv)): #convert ages from [yr] to [Ma]
#     updatedneontv = exp_neon_tv[i]/10**6
#     updated_neon_tv.append(updatedneontv)
#     updatedneonconst = exp_neon_const[i]/10**6
#     updated_neon_const.append(updatedneonconst)
#     temp = updatedneontv - updatedneonconst
#     diff_tv_qtz.append(temp)
#     perdifneon.append((temp/updatedneonconst)*100)
    


# f = plt.figure(figsize=(10,4))
# ax = f.add_subplot(121)
# ax2 = f.add_subplot(122)
# ax.axhline(y = 0, c = 'black')
# ax.set_xlim(2,13)
# ax.set_ylim(-0.6, 0.3)
# ax.plot(updated_texp_const[0:4] ,diff_tv_pyx[0:4], 'o', c = 'limegreen', alpha = 0.7, label = '$^{3}He$ - Surface 2')
# ax.plot(updated_texp_const[4:17],diff_tv_pyx[4:17], 'o', c = 'royalblue', alpha = 0.7, label = '$^{3}He$ - Surface 3')
# ax.plot(updated_texp_const[17:26],diff_tv_pyx[17:26], 'o', c = 'deepskyblue', alpha = 0.7, label = '$^{3}He$ - Surface 5')

# ax.plot(updated_neon_const[0:9], diff_tv_qtz[0:9], 's', c ='teal', alpha = 0.7,label = '$^{21}Ne$ - Surface 1')
# ax.plot(updated_neon_const[9:11], diff_tv_qtz[9:11], 's', c='limegreen', alpha = 0.7,label = '$^{21}Ne$ - Surface 2')
# ax.plot(updated_neon_const[11:14], diff_tv_qtz[11:14], 's', c='royalblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 3')
# ax.plot(updated_neon_const[13], diff_tv_qtz[13], 's', c='deepskyblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 5')

# ax.set_xlabel('Exposure age using LSDn long term average (Ma)')
# ax.set_ylabel('Exposure age difference (our model - long term average) (Ma) ')

# ax2.set_xlim(2,13)
# ax2.set_ylim(-6,6)
# ax2.plot(updated_texp_const[0:4] ,perdif[0:4], 'o', c = 'limegreen', alpha = 0.7, label = '$^{3}He$ - Surface 2')
# ax2.plot(updated_texp_const[4:17],perdif[4:17], 'o', c = 'royalblue', alpha = 0.7, label = '$^{3}He$ - Surface 3')
# ax2.plot(updated_texp_const[17:26],perdif[17:26], 'o', c = 'deepskyblue', alpha = 0.7, label = '$^{3}He$ - Surface 5')

# ax2.plot(updated_neon_const[0:9], perdifneon[0:9], 's', c ='teal', alpha = 0.7,label = '$^{21}Ne$ - Surface 1')
# ax2.plot(updated_neon_const[9:11], perdifneon[9:11], 's', c='limegreen', alpha = 0.7,label = '$^{21}Ne$ - Surface 2')
# ax2.plot(updated_neon_const[11:14], perdifneon[11:14], 's', c='royalblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 3')
# ax2.plot(updated_neon_const[13], perdifneon[13], 's', c='deepskyblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 5')
# ax2.set_xlabel('Exposure age using LSDn long term average (Ma)')
# ax2.set_ylabel('Exposure age percent difference')

# plt.savefig(Read.directory+'/plots/Figure_9.svg', dpi = 300, bbox_inches='tight')




"""
FIG 10
LIBARKIN DATASET

# """
# tempvals = []
# tempvalsmu = []
# lambdasp = 160 #effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
# lambdamu = 1300 #muon attenuation length in at/g/yr (Balco supplementary)
# rho = 2.32
# erosion = (5*(10**-2)) * rho #in g/cm2/yr
# dt = 250000

# texp_bin1 = [10000,50000,100000,150000,200000,250000]
# texp_bin2 = [300000,350000,400000,450000,500000]
# texp_bin3 = [510000,520000,530000,540000,550000,600000]

# z0 = np.arange(0,100,2)
# concentrations = []


    
# for i in range(len(z0)):
#     Cspall = (shielding.S_thick[0][0]*(neutron_spallation.pn_df[0][i] + proton_spallation.pp_df[0][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[1][i] + proton_spallation.pp_df[1][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt))
#     Cmuons = muons.pmuons_df[0][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*dt)) + muons.pmuons_df[1][i] / ((rho * erosion) / lambdamu) * np.exp(-(rho*z0[i]/lambdamu)) * (1-np.exp(-(rho*erosion/lambdamu)*(dt))) 
#     Ctot = Cspall + Cmuons
#     concentrations.append(Cspall + Cmuons)
# np.savetxt(directory+"/text_for_plots/lib_5e2.csv", 
#             concentrations,
#             delimiter =", ", 
#             fmt ='% s')


# plt.plot(z0,Read.lib1e3[0], c = 'lightgreen',label = r'1$\times 10^{-3}$ cm/yr')

# plt.plot(z0,Read.lib3e3[0], c = 'darkblue', label=r'3$\times 10^{-3}$ cm/yr')
# plt.plot(z0,Read.lib10e3[0], c = 'cornflowerblue', label = r'10$\times 10^{-3}$ cm/yr')
# plt.plot(z0,Read.lib20e3[0], c = 'teal',label = r'20$\times 10^{-3}$ cm/yr')

# x = [15,15,15,35,45,35,55]
# y = [2380000.00,2630000.00,2750000.00,330000.00,730000.00,340000.00,590000.00]

# plt.scatter(15,2380000.00, c = 'midnightblue', alpha = 0.7)
# e = [560000.00,
# 590000.00,
# 570000.00,
# 550000.00,
# 540000.00,
# 600000.00,
# 560000.00]

# ex = [2,2,2,2,2,2,2]
# plt.errorbar(x,y, xerr = ex, yerr=e, fmt='o',color = 'k', markersize = 4)
# plt.scatter(15,2630000.00, c = 'midnightblue', alpha = 0.7)
# plt.scatter(15,2750000.00, c = 'midnightblue', alpha = 0.7)


# plt.scatter(35,330000.00, c = 'midnightblue', alpha = 0.7)
# plt.scatter(45,730000.00, c = 'midnightblue', alpha = 0.7)
# plt.scatter(35,340000.00, c = 'midnightblue', alpha = 0.7)
# plt.scatter(55,590000.00, c = 'midnightblue', alpha = 0.7)
# plt.legend()
# #plt.xlim(0,100)
# #plt.ylim(0,5e6)
# plt.xlabel('Depth below surface (cm)', fontsize = 12)
# plt.ylabel('Concentration (atoms/g)', fontsize = 12)
# plt.savefig(Read.directory+'/plots/Figure_10.svg', dpi = 300, bbox_inches='tight')


"""
DUNAI PLOT

"""

exp_ages_dunai = [16006213.45641542,
  17313912.794089656,
  13524311.021048881,
  24366318.599839468,
  16180721.70315385,
  17848066.302044936,
  11638343.60957325,
  8010583.4129260555,
  17757188.996136837,
  11585579.923780099,
  14811943.598023633,
  18837370.115619432,
  14211077.094639456,
  74286.39215131507,
  140318.74073026184,
  94921.50108223595]
exp_ages_dunai_const = [17264860.4078435,
  18643337.482291736,
  14379851.011593908,
  27317197.32506301,
  17441877.955655158,
  19312419.704735752,
  12123180.962518461,
  8078272.012801984,
  19196960.838426054,
  12061447.60824129,
  15979301.362290312,
  20574505.077746626,
  15251919.869642701,
  64405.830279700436,
  121655.45719498975,
  82296.33869072834]

# updated_dunai_const = []
# updated_dunai = []
# diff_tv_dunai = []
# perdif = []
# for i in range(len(exp_ages_dunai)):
#     updated_dunaix = exp_ages_dunai[i]/10**6
#     updated_dunai_constx = exp_ages_dunai_const[i]/10**6
#     updated_dunai.append(updated_dunaix)
#     updated_dunai_const.append(updated_dunai_constx)
#     temp = updated_dunaix - updated_dunai_constx
#     diff_tv_dunai.append(temp)
#     perdif.append((temp/updated_dunai_constx)*100)
    
# f = plt.figure(figsize=(10,4))
# ax = f.add_subplot(121)
# ax2 = f.add_subplot(122)
# ax.set_xlim(2,35)
# ax.axhline(y = 0, c = 'black')
# ax.plot(updated_dunai_const[0:5], diff_tv_dunai[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# ax.plot(updated_dunai_const[5:9], diff_tv_dunai[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# ax.plot(updated_dunai_const[9:13],  diff_tv_dunai[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# ax.plot(updated_dunai_const[13:15], diff_tv_dunai[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# ax.plot(updated_dunai_const[15:16], diff_tv_dunai[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# ax.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
# ax.set_ylabel('Exposure age difference (our model - long term average) (Ma) ')
# ax.set_xlabel('Exposure age using LSDn long term average (Ma)')
# ax2.set_xlim(2,35)

# ax2.plot(updated_dunai_const[0:5], perdif[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# ax2.plot(updated_dunai_const[5:9], perdif[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# ax2.plot(updated_dunai_const[9:13],  perdif[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# ax2.plot(updated_dunai_const[13:15], perdif[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# ax2.plot(updated_dunai_const[15:16], perdif[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# ax2.set_ylabel('Exposure age percent difference ')
# ax2.set_xlabel('Exposure age using LSDn long term average (Ma)')
# plt.savefig(Read.directory+'/plots/dunai.pdf', dpi = 300, bbox_inches='tight')


"""
1:1 LINE COMPARISON
"""
exp_ages_time_varying = [131996.26202489913,
  1023626.3006114559,
  2818578.1182617154,
  1442111.5909461104,
  1572187.6926164788,
  2278513.403392353,
  2789561.569762896,
  5190519.589554306,
  824517.3451888387,
  1039899.2318907074,
  3213175.7139825514,
  5186659.724390685,
  4721445.394785178,
  5000015.329512211,
  5759439.620363143,
  3711836.322560931,
  4060198.6266656416,
  4191863.641518183,
  3972943.0084628374,
  10899929.349473981,
  7500679.307668893,
  11590489.115385713,
  10242831.200003851,
  10087732.900187513,
  2503058.2716951943,
  2450012.1182982484,
  1919685.6734813016,
  2088176.22741603]


exp_ages_constant=[114400.49565798171,
  917329.0518705035,
  2751355.8402647623,
  1344161.0993252213,
  1473394.0657873328,
  2224522.064947964,
  2720917.8318576734,
  4991435.653787645,
  724923.5683262685,
  931319.1949078307,
  3126699.593423725,
  4973918.624462918,
  4543407.160283238,
  4812717.1869177325,
  5608767.36018699,
  3614767.3369865143,
  3961286.539982639,
  4078001.1497473023,
  3877127.438196669,
  11309454.76557007,
  7606839.109954978,
  12123018.074383643,
  10541403.567087896,
  10368523.26303627,
  2446694.6469513695,
  2396470.5016860655,
  1849428.0879702813,
  2025791.0757406428]

exp_neon_tv = [925394.9003644264,
  907557.1721116758,
  276612.40319194266,
  122540.79545892825,
  322327.13753088925,
  227052.2907854808,
  267801.40712947334,
  37299.39263586361,
  2096294.213187858,
  2189679.5142527027,
  3061778.4589791135,
  5985087.135238934,
  2968169.8326294757,
  2163056.8551527187]

exp_neon_const = [809860.9281488108,
  793119.6169726079,
  237012.03447028896,
  104784.26787107512,
  276929.85080212716,
  195750.59034431167,
  231188.1972169888,
  31842.72636385542,
  2017729.6458384574,
  2117270.9750331547,
  2958672.607989357,
  5850182.994291976,
  2868402.6018716474,
  2089254.4066904038]



updated_texp_tv = []
updated_texp_const = []


updated_neon_tv = []
updated_neon_const = []


# errorymin = []
# errorymax = []
# errorxmin = []
# errorxmax = []
# y_errormax = [152020.4627655185,
#  1054503.2630474814,
#  2870732.7370127565,
#  1470827.9027167493,
#  1626322.9534395412,
#  2349288.025553613,
#  2830062.5631475113,
#  5301077.612776397,
#  857647.2443782075,
#  1075112.6129585204,
#  3282617.9269670527,
#  5276551.772295314,
#  4808033.169293373,
#  5090562.921789536,
#  5836859.494027289,
#  3774089.720813825,
#  4154830.0129861925,
#  4307252.632771598,
#  4074536.011696811,
#  11002533.62601701,
#  7695315.181864539,
#  11863003.437277954,
#  10452877.541896092,
#  10259027.961273413,
#  2561280.0707390523,
#  2492525.563721868,
#  1955511.1894657055,
#  2130615.9105258347]

# y_errormin= [111972.06128427974,
#  992276.4537145743,
#  2766423.4995106747,
#  1413395.279175472,
#  1518052.4317934164,
#  2211307.6272200486,
#  2749064.541006048,
#  5075360.9416002445,
#  791387.44599947,
#  1004685.8508228943,
#  3143274.7197972797,
#  5094190.257960359,
#  4634654.318178211,
#  4906942.632022505,
#  5676835.37272638,
#  3651529.5030010887,
#  3967052.0284684473,
#  4077023.52328313,
#  3874576.2792436266,
#  10797322.68331371,
#  7316123.034619844,
#  11318051.011821032,
#  10029340.19224097,
#  9916277.020403787,
#  2445949.755347677,
#  2407498.6728746286,
#  1883860.1574968977,
#  2045736.5443062254]

# x_errormax = [131755.36961228852,
#  948496.9887680341,
#  2801448.800488062,
#  1373381.992788813,
#  1532671.1908511,
#  2294113.047914247,
#  2759745.4189204066,
#  5100451.571309934,
#  756286.145447924,
#  966863.4489790403,
#  3193606.42461659,
#  5061089.824187657,
#  4622469.411196373,
#  4898482.318881757,
#  5705423.302559145,
#  3676910.5712053464,
#  4047812.0359773813,
#  4182788.377806672,
#  3970944.1622353825,
#  11430508.603039376,
#  7789735.359985818,
#  12444594.94137319,
#  10783437.57676468,
#  10563061.675332097,
#  2502811.496652089,
#  2438259.282534067,
#  1886130.6556954647,
#  2071073.4644924926]

# x_errormin = [97045.62170367487,
#  886161.1149729728,
#  2701262.880041462,
#  1314940.2058616295,
#  1414116.9407235656,
#  2154931.081981681,
#  2682090.2447949406,
#  4882419.736265357,
#  693560.9912046129,
#  895774.940836621,
#  3059792.7622308596,
#  4886747.42473818,
#  4464344.909370104,
#  4726952.054953708,
#  5512111.417814836,
#  3552624.102767683,
#  3874761.0439878968,
#  3973213.921687932,
#  3783310.7141579557,
#  11188400.928100761,
#  7423942.85992414,
#  11801441.207394095,
#  10299369.557411112,
#  10173984.850740442,
#  2390577.7972506504,
#  2354681.720838065,
#  1812725.5202450978,
#  1980508.6869887935]

for i in range(len(exp_ages_constant)): #convert ages from [yr] to [Ma]
    updated = exp_ages_time_varying[i]/10**6
    updated_texp_tv.append(updated) #Evenstar data
    updated_const = exp_ages_constant[i]/10**6 
    updated_texp_const.append(updated_const) #this model

for i in range(len(exp_neon_tv)): #convert ages from [yr] to [Ma]
    updatedneontv = exp_neon_tv[i]/10**6
    updated_neon_tv.append(updatedneontv)
    updatedneonconst = exp_neon_const[i]/10**6
    updated_neon_const.append(updatedneonconst)

# for i in range(len(y_errormin)):
#     updated = y_errormin[i]/10**6
#     errorymin.append(updated)
#     updated1 = y_errormax[i]/10**6
#     errorymax.append(updated1)
    
#     updated2 = x_errormin[i]/10**6
#     errorxmin.append(updated2)
#     updated3 = x_errormax[i]/10**6
#     errorxmax.append(updated3)
    


# #f = plt.figure(figsize=(10,4))
# #ax = f.add_subplot(121)
# #ax2 = f.add_subplot(122)
# # ax.axhline(y = 0, c = 'black')

# # ax.set_xlim(2,13)
# # ax.set_ylim(-0.6, 0.3)
# # plt.plot([0,12], [0,12], 'k-')

# # ax.plot(updated_texp_const[0:4] ,updated_texp_tv[0:4], 'o', c = 'limegreen', alpha = 0.7, label = '$^{3}He$ - Surface 2')
# # ax.plot(updated_texp_const[4:17],updated_texp_tv[4:17], 'o', c = 'royalblue', alpha = 0.7, label = '$^{3}He$ - Surface 3')
# # ax.plot(updated_texp_const[17:26],updated_texp_tv[17:26], 'o', c = 'deepskyblue', alpha = 0.7, label = '$^{3}He$ - Surface 5')

# # ax.plot(updated_neon_const[0:9], updated_neon_tv[0:9], 's', c ='teal', alpha = 0.7,label = '$^{21}Ne$ - Surface 1')
# # ax.plot(updated_neon_const[9:11], updated_neon_tv[9:11], 's', c='limegreen', alpha = 0.7,label = '$^{21}Ne$ - Surface 2')
# # ax.plot(updated_neon_const[11:14], updated_neon_tv[11:14], 's', c='royalblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 3')
# # ax.plot(updated_neon_const[13], updated_neon_tv[13], 's', c='deepskyblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 5')

# #creating error

y_error = [20024,
30877,
52155,
28716,
54135,
70775,
40501,
110558,
33130,
35213,
69442,
89892,
86588,
90548,
77420,
62253,
94631,
115389,
101593,
102604,
194636,
272514,
210046,
171295,
58222,
42513,
35826,
42440]
x_error = [17355,
31168,
50093,
29221,
59277,
69591,
38828,
109016,
31363,
35544,
66907,
87171,
79062,
85765,
96656,
62143,
86525,
104787,
93817,
121054,
182896,
321577,
242034,
194538,
56117,
41789,
36703,
45282]

xx = []
yy = []
for i in range(len(x_error)):
    xx.append(x_error[i]/10**6)
    yy.append(y_error[i]/10**6)

# plotting graph
plt.plot([0,13], [0,13], 'k-')

plt.errorbar(updated_texp_const ,updated_texp_tv,yerr = yy, xerr=  xx, fmt = 'o', capsize = 2, markersize = 5)
plt.xlabel('LSDn average exposure ages')
plt.ylabel('SPRITE exposure ages')


# plt.savefig(Read.directory+'/plots/1to1.png', dpi = 300, bbox_inches='tight')


