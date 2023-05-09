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
import scaling_factor
# import neutron_spallation
# # import proton_spallation
# import matplotlib.gridspec as gridspec


os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)



"""
Figure 1 
Flux comparisons 

"""
# #need specific excel sheet. Ran using quartz conditions. Only need 1 time bin
# plt.figure(figsize=(8,6)) 
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[0]*neutron_spallation.E.iloc[:,0], c = 'darkblue', label = 'Terrestrial surface at poles (neutrons)')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[2]*neutron_spallation.E.iloc[:,0], c = 'darkblue', label = 'Sea level, equator')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[4]*neutron_spallation.E.iloc[:,0], '--',c = 'darkgreen', label = '1000 masl, pole')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[6]*neutron_spallation.E.iloc[:,0], c = 'darkgreen',label = '1000 masl, equator')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[8]*neutron_spallation.E.iloc[:,0], '--', c = 'darkgreen', label = '2000 masl, pole')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[10]*neutron_spallation.E.iloc[:,0],  c = 'darkgreen', label = '2000 masl, equator')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[12]*neutron_spallation.E.iloc[:,0], '--',c = 'darkgreen', label = '4000 masl, pole')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[14]*neutron_spallation.E.iloc[:,0], c = 'darkblue',label = '4000 masl, equator')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[16]*neutron_spallation.E.iloc[:,0],'--', c = 'purple',label = '6000 masl, pole')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[18]*neutron_spallation.E.iloc[:,0], c = 'purple',label = '6000 masl, equator')

# plt.ylabel('Differential Flux' r'$ \;\times$' 'Energy ' '$ (cm^{-2} s^{-1}$)', fontsize = 13)
# plt.xlabel('Energy (MeV)', fontsize = 13)
# plt.legend(loc='lower left')
# # plt.savefig(directory+'/plots/Figure_1.pdf', dpi = 300, bbox_inches='tight')


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

# ax.set_ylim(top = 19)

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

# plt.savefig(Read.directory+'/plots/Figure_2.png', dpi = 300, bbox_inches='tight')

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
MCADAM Model

"""







"""
Figure 4
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
FIGURE 5
Atmospheric Depth / SF variations

"""
# x = scaling_factor.Siteprod_df
# GL_STD_sf = x[0][0:17]
# GL_STD_sf.to_csv(directory+'/text_for_plots/Figure_5_GL_STD')
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
import matplotlib.patches as patches
# fig = plt.figure(figsize=(4,4))

# alt = np.arange(0,5001,500)


# plt.plot([0,40], [0,40], 'k-') #1:1 line
# plt.plot(Read.GL_STD.iloc[1:12][1],Read.GL_ERA40.iloc[1:12][1], 'x-',  markersize = 4, label = 'High latitude: 75N,40E ', c = 'darkmagenta')
# plt.plot(Read.EC_STD.iloc[1:12][1],Read.EC_ERA40.iloc[1:12][1], 'x-',    markersize = 4,label = 'Equator: 0N, 78E' , c = 'green')
# plt.ylabel('Scaling factor using ERA40')
# plt.xlabel('Scaling factor using standard atmosphere')


# plt.legend()
# plt.savefig(Read.directory+'/plots/Figure_5.pdf', dpi = 300, bbox_inches='tight')

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


# plt.savefig(Read.directory+'/plots/Figure_5.png', dpi = 300, bbox_inches='tight')

"""
FIGURE 6
Scaling factor TV and Constant

"""

time = np.linspace(0,70,281)

##DONT RUN THIS PART
# sf_india = scaling_factor.Siteprod_df.iloc[0]
# sf_india.to_csv(directory+'/text_for_plots/sf_IN.csv') 
# sf_india_const = scaling_factor.Siteprod_df.iloc[0]
# sf_india_const.to_csv(directory+'/text_for_plots/sf_IN_const.csv') 
# sf_india_tvfieldonly = scaling_factor.Siteprod_df.iloc[0]
# sf_india_tvfieldonly.to_csv(directory+'/text_for_plots/sf_india_tvfieldonly.csv') 
# sf_india_tvlatonly = scaling_factor.Siteprod_df.iloc[0]
# sf_india_tvlatonly.to_csv(directory+'/text_for_plots/sf_india_tvlatonly.csv') 

##BEGIN
# f = plt.figure(figsize=(10,4))
# ax = f.add_subplot(121)
# ax2 = f.add_subplot(122)
# ax.plot(time,Read.sf_IN.iloc[:,1], c = 'cornflowerblue',label = 'time-varying field and latitude')
# ax.plot(time,Read.sf_IN_const.iloc[:,1], '--',c = 'gray', label = 'constant field and latitude')
# ax.set_xlim(0,70)
# ax.set_ylim(0.55,0.95)
# ax.vlines(66.052, 0.55, 0.95)
# ax.set_xlabel('Time (Ma)', fontsize = 13)
# ax.set_ylabel('Scaling Factor', fontsize = 13)
# ax.legend(loc = 'lower left')

# ax2.plot(time,Read.sf_IN_tvfieldonly.iloc[:,1], c = 'darkblue',label = 'time-varying field, constant latitude')
# ax2.plot(time,Read.sf_IN_tvlatonly.iloc[:,1], '--',c = 'darkgray', label = 'constant field, time-varying latitude')
# ax2.set_xlim(0,70)
# ax2.set_ylim(0.55,0.95)
# ax2.vlines(66.052, 0.55, 0.95)
# ax2.set_xlabel('Time (Ma)', fontsize = 13)
# ax2.legend(loc = 'lower left')

# plt.setp(ax2.get_yticklabels(), visible=False)

# plt.savefig(directory+'/plots/Figure_6.png', dpi = 300, bbox_inches='tight')




"""
FIGURE 7
Atmospheric Depth / SF variations

"""
##WORKFLOW, made in illustrator##


"""
Figure 8
Time varying field vs. Constant 
For present - 25 Ma and 40-65Ma
Including Muons
UPDATED 1/30
"""
exp_ages_time_varying = [155593.52786932606,
 1068864.5019616704,
 2865937.8722111513,
 1490859.532007292,
 1628887.9718646037,
 2343864.935508115,
 2840328.7869525645,
 5259549.472205835,
 861343.346514223,
 1088559.3685330306,
 3262584.719259309,
 5263686.871632526,
 4785395.377776698,
 5060101.985331145,
 5858703.780555014,
 3783933.7410848946,
 4106142.141980563,
 4238009.598268062,
 4022884.7556443047,
 11003117.794626001,
 7586094.784725537,
 11692324.887176575,
 10342822.89944322,
 10188947.914359374,
 2552627.341035063,
 2496687.2776202634,
 1976516.641467161,
 2148052.0873481794]

exp_ages_constant = [123788.57275789027,
 992608.0601948479,
 2968655.6947280755,
 1450321.8535919287,
 1602643.1662383978,
 2409491.1477360856,
 2947162.2389736497,
 5406473.6923960075,
 785195.75932338,
 1008751.7006882153,
 3386662.2202707627,
 5418024.084532633,
 4949073.613545629,
 5201138.962016999,
 6061436.255854619,
 3946894.108034649,
 4278386.705606539,
 4406785.074010707,
 4189716.1617380097,
 12221265.915827842,
 8211982.257018811,
 13087434.595280413,
 11379998.683515336,
 11201758.987958398,
 2643316.0303535247,
 2571250.308911892,
 1988876.5496879644,
 2178537.4577767653]

exp_neon_tv = [1306845.1255969384,
 1258287.3647597993,
 381864.3303699156,
 254954.54699896005,
 478986.1134439893,
 270179.9425125776,
 333922.4262346815,
 84982.44629013207,
 2384971.0658685495,
 2286001.142546658,
 3420734.842287784,
 6525435.017848848,
 3148199.800081636,
 2507743.1464642044]

exp_neon_const =  [1108315.8620698294,
 1059757.7974818319,
 268792.7044840601,
 254946.47715577335,
 365915.17197197385,
 352103.5900102401,
 251600.63040524072,
 84978.77752181498,
 2402271.341291927,
 2358069.467202251,
 3735179.200323837,
 6704330.923486828,
 3554715.2836084124,
 2286134.7752009244]

exp_ages_dunai = [12079356.192299709,
 13243766.367313802,
 10226092.626417426,
 19169399.21252651,
 12359658.090757791,
 13637574.563267816,
 8365572.549046695,
 5682988.316644355,
 13458657.26751266,
 8595986.509027485,
 11081818.386184158,
 14615303.475366574,
 10606710.375174612,
 107348.07816393787,
 202768.59208743824,
 137166.98876503174]

exp_ages_dunai_const = [12138950.788789494,
 12970666.541489856,
 9934981.671404669,
 19274627.48051447,
 12081487.205194987,
 13704418.904514944,
 8403927.916413188,
 5704804.809174601,
 13525501.390303448,
 8308602.68569148,
 11135397.325000148,
 14362946.778750991,
 10657111.587570492,
 107348.06214576238,
 202768.56183088454,
 137166.96829736306]
# # exp_ages_muons_tv = [265411.22053419525,
# #  982919.8929994438,
# #  2532603.9804173275,
# #  1430560.7831150235,
# #  1351247.2152844712,
# #  1854444.7045112464,
# #  2534867.7285628067,
# #  4233540.39638492,
# #  1060190.8802123163,
# #  1080490.0372512478,
# #  2996807.1740701823,
# #  4104499.1670110016,
# #  4630602.751959682,
# #  4371676.975538476,
# #  4752786.197871009,
# #  2801979.6923513245,
# #  3348352.497011173,
# #  3613128.693939878,
# #  3178873.597239819,
# #  9216300.193334645,
# #  6559055.491510672,
# #  9884634.340030625,
# #  8497581.02133486,
# #  8574486.078128759,
# #  2375024.7017890974,
# #  2159250.57668627,
# #  1619310.1095379305,
# #  1921898.406673565]

# # exp_ages_muons_const = [265411.22053419525,
# #  771696.2992130874,
# #  2364046.9253956983,
# #  1288396.5269947306,
# #  1901956.603620552,
# #  2011372.7603821848,
# #  2787759.838818932,
# #  4342267.915258035,
# #  831247.9372817662,
# #  819568.1619946248,
# #  2792956.736881527,
# #  4208692.379432997,
# #  4531181.999072417,
# #  4402361.75302382,
# #  4882763.30644277,
# #  3902945.4527308145,
# #  3383552.0548880612,
# #  3609680.411813231,
# #  3575907.6624627025,
# #  10031769.90397615,
# #  6791671.54704856,
# #  10539331.19720867,
# #  9130919.117084693,
# #  9209053.512951447,
# #  2086283.9840488157,
# #  2057308.5445523043,
# #  1583453.4291142398,
# #  1886041.726249874]

updated_texp_tv = []
updated_texp_const = []
updated_texp_tv_40 = []
updated_texp_const_40 = []
updated_muons_tv = []
updated_muons_const = []
updated_muons_tv_40 = []
updated_muons_const_40 = []
updated_dunai_const = []
updated_dunai = []
updated_neon_tv = []
updated_neon_const = []
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
# for i in range(len(exp_ages_dunai)):
#     updated_dunaix = exp_ages_dunai[i]/10**6
#     updated_dunai_constx = exp_ages_dunai_const[i]/10**6
#     updated_dunai.append(updated_dunaix)
#     updated_dunai_const.append(updated_dunai_constx)

#     # updatedmuons = exp_ages_muons_tv[i]/10**6
#     # updated_muons_tv.append(updatedmuons)
#     # updatedmuonsconst = exp_ages_muons_const[i]/10**6
#     # updated_muons_const.append(updatedmuonsconst)

plt.plot([0,15], [0,15], 'k-') #1:1 line
plt.rcParams["figure.figsize"] = [5,5] #update figure size
plt.plot(updated_texp_const[0:4],updated_texp_tv[0:4], 'o', c = 'darkblue', alpha = 0.7, label = '$^{3}He$ - Surface 2')
plt.plot(updated_texp_const[4:17],updated_texp_tv[4:17], 'o', c = 'royalblue', alpha = 0.7, label = '$^{3}He$ - Surface 3')
plt.plot(updated_texp_const[17:26],updated_texp_tv[17:26], 'o', c = 'deepskyblue', alpha = 0.7, label = '$^{3}He$ - Surface 5')

plt.plot(updated_neon_const[0:9], updated_neon_tv[0:9], 's', c ='teal', alpha = 0.7,label = '$^{21}Ne$ - Surface 1')
plt.plot(updated_neon_const[9:11], updated_neon_tv[9:11], 's', c='darkblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 2')
plt.plot(updated_neon_const[11:14], updated_neon_tv[11:14], 's', c='royalblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 3')
plt.plot(updated_neon_const[13], updated_neon_tv[13], 's', c='deepskyblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 5')

plt.legend()

#plt.plot(updated_texp_const[26:28],updated_texp_tv[26:28], 'o', c = 'lightsteelblue', alpha = 0.7, label = '0-25 Ma')

# # plt.plot(updated_muons_const[0:4],updated_muons_tv[0:4], 'x', markersize = 3, c = 'darkblue')
# # plt.plot(updated_muons_const[4:17],updated_muons_tv[4:17], 'x', markersize = 3, c = 'darkblue')
# # plt.plot(updated_muons_const[17:26],updated_muons_tv[17:26], 'x', markersize = 3, c = 'darkblue')




plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
plt.xlabel('Exposure Age [Ma] constant field', fontsize = 10)
plt.ylabel('Exposure Age [Ma] time-varying field', fontsize = 10)
plt.savefig(Read.directory+'/plots/Figure_8.pdf', dpi = 300, bbox_inches='tight')


# plt.plot(updated_dunai[0:5],updated_dunai_const[0:5],  's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# plt.plot(updated_dunai[5:9],updated_dunai_const[5:9],  's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# plt.plot(updated_dunai[9:13],updated_dunai_const[9:13],  's', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# plt.plot(updated_dunai[13:15],updated_dunai_const[13:15],  's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# plt.plot(updated_dunai[15:16],updated_dunai_const[15:16],  's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
# plt.xlabel('Exposure Age [Ma] constant field', fontsize = 10)
# plt.ylabel('Exposure Age [Ma] time-varying field', fontsize = 10)
# plt.savefig(Read.directory+'/plots/Figure_11.svg', dpi = 300, bbox_inches='tight')



"""
FIGURE 9
Comparing bin size

"""

# # #This is testing using the Evenstar Dataset. 
# #FOR 0-25MA
# age250 = [2768814.7852780037,
#   2248207.300541437,
#   2741539.525003936,
#   5107076.41764413,
#   3159569.0728202676,
#   5108018.95259798,
#   4640289.046260925,
#   4913645.370893386,
#   5706446.686550266,
#   3660411.029096094,
#   3983111.2540024156,
#   4112798.331950483,
#   3904084.2200530013,
#   10737925.276977753,
#   7381647.68935432,
#   11412837.334886586,
#   10087786.024035417,
#   9936179.90547212,
#   2461604.0058712866,
#   2411367.4649931323] #using 250 ka bins

# age50 = [2747423.5349986902,
#   2223095.3845128245,
#   2719036.0556255244,
#   5084596.120275133,
#   3132327.868657709,
#   5083965.331721996,
#   4616978.370183475,
#   4890930.40714782,
#   5669668.789635737,
#   3630101.256214381,
#   3961026.124548674,
#   4089151.324590964,
#   3876927.2947889157,
#   10700797.902502893,
#   7348665.262892835,
#   11374069.81445638,
#   10052157.969277393,
#   9901388.154132914,
#   2439258.358300369,
#   2386586.9584862404]  #using 250 ka bins.

# age_1ma = [2924810.234995724,
#   2451586.337555025,
#   2907706.3449905072,
#   5274094.288564094,
#   3310957.9870377565,
#   5287296.109743877,
#   4825192.659220409,
#   5081329.3131247405,
#   5923292.07426654,
#   3834964.8671806045,
#   4142233.937749951,
#   4281597.309933332,
#   4066253.5834281878,
#   10877356.72304969,
#   7581504.491545926,
#   11557717.78630856,
#   10214133.833518948,
#   10062821.5672929,
#   2647676.63087064,
#   2593155.2261833437]

# updated_texp_diff_250_50= []
# updated_texp_diff_250_1ma = []
# updated_age_250 = []
# updated_age_50 = []
# updated_age_1ma = []

# time = np.linspace(0,70,281)
# for i in range(len(age50)): #convert ages from [yr] to [Ma]
#     updated = age50[i]/10**6
#     updated_age_50.append(updated)
#     updated_250 = age250[i]/10**6 
#     updated_age_250.append(updated_250)
#     diff1 = updated_250/updated
#     updated_1ma = age_1ma[i]/10**6
#     updated_age_1ma.append(updated_1ma)
#     diff2 = updated_250/updated_1ma
#     updated_texp_diff_250_50.append(diff1)
#     updated_texp_diff_250_1ma.append(diff2)
    
# plt.scatter(updated_age_250, updated_texp_diff_250_50, c = 'blue', label = '50 kyr')
# plt.scatter(updated_age_250,  updated_texp_diff_250_1ma, c = 'darkmagenta', label = '1 Myr')
# plt.xlabel('$T_{exposure(250kyr)}$ (Ma)')
# plt.ylabel("$T_{exposure(250kyr)}$ / $T_{exposure(50kyr)}$ $_{or}$ $_{(1Myr)}$ ")
# plt.legend()
# plt.savefig(Read.directory+'/plots/Figure_9.pdf', dpi = 300, bbox_inches='tight')



# sf_50kyr = scaling_factor.Siteprod_df.iloc[0]
# sf_50kyr.to_csv(directory+'/text_for_plots/sf_50kyr.csv')

# sf_250kyr = scaling_factor.Siteprod_df.iloc[0]
# sf_250kyr.to_csv(directory+'/text_for_plots/sf_250kyr.csv') 

# sf_1ma= scaling_factor.Siteprod_df.iloc[0]
# sf_1ma.to_csv(directory+'/text_for_plots/sf_1ma.csv') 

# time =  np.arange(0,20.05,0.25)
# time50 = np.arange(0,20.05,0.05)
# time1 = np.arange(0,20.05,1)
# x = Read.sf_50kyr.iloc[:,1]
# sub = x[::5]
# plt.rcParams["figure.figsize"] = [5,5] #update figure size 
# plt.xlim(0,20)
# plt.scatter(time, Read.sf_250kyr.iloc[:,1]/sub, s = 20, marker = 's', c = 'black',  label = '250 kyr')
# #plt.scatter(time50, Read.sf_50kyr.iloc[:,1], s = 15, c = 'cornflowerblue', alpha = 0.5, label = '50 kyr')
# #plt.scatter(time1, Read.sf_1ma.iloc[:,1], s = 15 ,c = 'seagreen', label = '1ma')
# plt.xlabel('Time (Ma)', fontsize = 13)
# plt.ylabel('Scaling Factor', fontsize = 13)
# plt.legend(loc = 'lower right')
#plt.savefig(Read.directory+'/plots/Figure_12_alt.png', dpi = 300, bbox_inches='tight')
"""
FIG X
LIBARKIN DATASET

"""

# xaxis = [10000,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000,510000,520000,530000,540000,550000,600000]

# # """FOR 2.5KM"""
# plt.plot(xaxis,Read.chisq_neg203.values.tolist(), 'o-', c = 'midnightblue')
# plt.plot(xaxis,Read.chisq_neg153.values.tolist(), 'o-', c = 'royalblue')
# plt.plot(xaxis,Read.chisq_neg103.values.tolist(), 'o-', c = 'cornflowerblue')
# plt.plot(xaxis,Read.chisq_neg625.values.tolist(), 'o-', c = 'lightskyblue')

# plt.plot(xaxis,Read.chisq_neg53.values.tolist(), 'o-', c = 'lightsteelblue')

# #plt.plot(xaxis,Read.chisq_neg33.values.tolist(), 'o-',label = "3*10^-3")

# #plt.plot(xaxis,Read.chisq_neg3.values.tolist(), 'o-',label = "10^-3")

# plt.xlabel('Exposure Age [Years]')
# plt.ylabel('Chi Squared')
# plt.title('2.5 km above sea level')

# plt.savefig(Read.directory+'/plots/Libarkin_2km_unlabeled.png', dpi = 300, bbox_inches='tight')


# """ FOR SEA LEVEL"""
# # # plt.plot(xaxis,Read.SLchisq_neg53.values.tolist()
# , 'o-',label = "5*10^-3")
# # # plt.plot(xaxis,Read.SLchisq_neg33.values.tolist(), 'o-',label = "3*10^-3")

# # # plt.plot(xaxis,Read.SLchisq_neg3.values.tolist(), 'o-',label = "10^-3")
# # #plt.plot(xaxis,Read.SLchisq_neg093.values.tolist(), 'o-',label = "0.9*10^-3")
# # plt.plot(xaxis,Read.SLchisq_neg083.values.tolist(), 'o-',label = "0.8*10^-3")
# # plt.plot(xaxis,Read.SLchisq_neg073.values.tolist(), 'o-',label = "0.7*10^-3")
# # plt.plot(xaxis,Read.SLchisq_neg063.values.tolist(), 'o-',label = "0.6*10^-3")
# # plt.plot(xaxis,Read.SLchisq_neg0653.values.tolist(), 'o-',label = "0.65*10^-3")
# # plt.plot(xaxis,Read.SLchisq_neg53.values.tolist(), 'o-',label = "0.5*10^-3")
# # #plt.plot(xaxis,Read.SLchisq_neg033.values.tolist(), 'o-',label = "0.3*10^-3")

# # plt.xlabel('Exposure Age [Years]')
# # plt.ylabel('Chi Squared')
# # plt.title('Sea Level')
# # plt.legend()
# # plt.savefig(Read.directory+'/plots/Libarkin_sealvel.png', dpi = 300, bbox_inches='tight')


# time = np.arange(0,70+0.05, 0.25)
# plt.plot(time, Pmag_paleolat.pl_df.iloc[0][:] , 'teal', label = 'India')


# plt.xlabel('Time [Ma]', size = 13)
# plt.ylabel('Latitude', size = 13)
# plt.savefig(Read.directory+'/plots/india_production_prelims.png', dpi = 300, bbox_inches='tight')


#need specific excel sheet. Ran using quartz conditions. Only need 1 time bin
# plt.figure(figsize=(8,6)) 
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[0]*neutron_spallation.E.iloc[:,0], c = 'darkblue', label = 'Terrestrial surface at poles (neutrons)')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[2]*neutron_spallation.E.iloc[:,0], c = 'darkblue', label = 'Sea level, equator')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[4]*neutron_spallation.E.iloc[:,0], '--',c = 'darkgreen', label = '1000 masl, pole')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[6]*neutron_spallation.E.iloc[:,0], c = 'darkgreen',label = '1000 masl, equator')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[8]*neutron_spallation.E.iloc[:,0], '--', c = 'darkgreen', label = '2000 masl, pole')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[10]*neutron_spallation.E.iloc[:,0],  c = 'darkgreen', label = '2000 masl, equator')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[12]*neutron_spallation.E.iloc[:,0], '--',c = 'darkgreen', label = '4000 masl, pole')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[14]*neutron_spallation.E.iloc[:,0], c = 'darkblue',label = '4000 masl, equator')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[16]*neutron_spallation.E.iloc[:,0],'--', c = 'purple',label = '6000 masl, pole')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[18]*neutron_spallation.E.iloc[:,0], c = 'purple',label = '6000 masl, equator')


# P0 = 100
# rho = 3
# z = np.arange(0,200)
# lambdasp = 160
# concs = []
# concs2 = []
# t1 = 1000
# t2 = 10000
# for i in range(len(z)):
#     C = P0 * np.e**(-rho*(z[i]/lambdasp))*t1
#     C2 = P0 * np.e**(-rho*(z[i]/lambdasp))*t2
#     concs.append(C)
#     concs2.append(C2)
# plt.plot(concs,z, c = 'darkblue')  
# plt.plot(concs2,z, c = 'cornflowerblue')  
# ax = plt.gca()
# ax.axes.xaxis.set_ticklabels([])
# ax.axes.yaxis.set_ticklabels([])
# ax.set_xticks([])
# ax.set_yticks([])
# plt.savefig('/Users/mmijjum/Documents/prelims scripts/depth.png', dpi = 300, bbox_inches='tight')

# P0 = 100
# rho = 3
# z = np.arange(0,200)
# lambdasp = 160
# concs = []
# concs2 = []
# erosion = 5
# t1 = 1000
# t2 = 10000
# for i in range(len(z)):
#     C = P0/rho*erosion/lambdasp * np.e**(-rho*((z[i] - erosion*t1)/lambdasp))
#     C2 = P0/rho*erosion/lambdasp * np.e**(-rho*((z[i] - erosion*t2)/lambdasp))
#     concs.append(C)
#     concs2.append(C2)
# plt.plot(concs,z, c = 'darkblue')  
# plt.plot(concs2,z, c = 'cornflowerblue')  
# ax = plt.gca()
# ax.axes.xaxis.set_ticklabels([])
# ax.axes.yaxis.set_ticklabels([])
# #plt.savefig('/Users/mmijjum/Documents/prelims scripts/depth_erosion_5.png', dpi = 300, bbox_inches='tight')
