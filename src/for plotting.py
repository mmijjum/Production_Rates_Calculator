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
# import shielding
# import scaling_factor
# import neutron_spallation
# import proton_spallation
# import muons
# # import matplotlib.gridspec as gridspec


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

# sf_50kyr = scaling_factor.Siteprod_df.iloc[0]
# sf_50kyr.to_csv(directory+'/text_for_plots/sf_50kyr.csv')

# sf_1ma = scaling_factor.Siteprod_df.iloc[0]
# sf_1ma.to_csv(directory+'/text_for_plots/sf_1ma.csv') 

# sf_1ma= scaling_factor.Siteprod_df.iloc[0]
# sf_1ma.to_csv(directory+'/text_for_plots/sf_1ma.csv') 

time1 =  np.arange(0,70.05,0.05)
time2=  np.arange(0,70.05,0.25)

x = Read.sf_50kyr.iloc[:,1]

plt.rcParams["figure.figsize"] = [5,5] #update figure size 
# plt.scatter(time, Read.sf_250kyr.iloc[:,1]/sub[:], s = 20, marker = 's', c = 'cornflowerblue',  label = '250 kyr')
# plt.scatter(time, Read.sf_250kyr.iloc[:,1]/gupdated[:], s = 15 ,c = 'teal', label = '1ma')
plt.plot(time1, Read.sf_250kyr.iloc[:,1].repeat(5).reset_index(drop=True).iloc[4:].reset_index(drop=True)/x,  c = 'black',  label = '50 kyr')
plt.plot(time2,  Read.sf_250kyr.iloc[:,1]/Read.sf_1ma.iloc[:,1].repeat(4).reset_index(drop=True).iloc[3:].reset_index(drop=True) ,c = 'cornflowerblue', label = '1ma')
plt.xlabel('Time (Ma)', fontsize = 13)
plt.ylabel('Scaling Factor_250kyr/Scaling Factor_50kyr or 1 Ma', fontsize = 13)
plt.legend(loc = 'lower right')
plt.xlim(0,70)
# plt.savefig(Read.directory+'/plots/Figure_6.png', dpi = 300, bbox_inches='tight')


"""
FIGURE 7
Atmospheric Depth / SF variations

"""
##DO NOT RE RUN THIS PART##
# x = scaling_factor.Siteprod_df
# GL_STD_sf = x[0][0:17]
# GL_STD_sf.to_csv(directory+'/text_for_plots/Figure_7_GL_STD')


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


# plt.savefig(Read.directory+'/plots/Figure_7.pdf', dpi = 300, bbox_inches='tight')

"""
FIGURE 8
Scaling factor TV and Constant

"""

# time = np.linspace(0,70,281)

# #DONT RUN THIS PART
# # sf_india = scaling_factor.Siteprod_df.iloc[0]
# # sf_india.to_csv(directory+'/text_for_plots/sf_IN.csv') 
# # sf_india_const = scaling_factor.Siteprod_df.iloc[0]
# # sf_india_const.to_csv(directory+'/text_for_plots/sf_IN_const.csv') 
# # sf_india_tvfieldonly = scaling_factor.Siteprod_df.iloc[0]
# # sf_india_tvfieldonly.to_csv(directory+'/text_for_plots/sf_india_tvfieldonly.csv') 
# # sf_india_tvlatonly = scaling_factor.Siteprod_df.iloc[0]
# # sf_india_tvlatonly.to_csv(directory+'/text_for_plots/sf_india_tvlatonly.csv') 

# #BEGIN
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

# plt.savefig(directory+'/plots/Figure_8.svg', dpi = 300, bbox_inches='tight')




"""
FIGURE 9
EVENSTAR DATASET
# """
exp_ages_time_varying = [153314.203642404,
  1063820.5100204153,
  2847482.7374481456,
  1483703.0151992992,
  1619858.8405796194,
  2328887.5510545364,
  2820918.0621247436,
  5206844.358581369,
  856593.9573540317,
  1083407.741920759,
  3240016.729671602,
  5206262.755691444,
  4737208.90650021,
  5012242.12510085,
  5807532.528858626,
  3754387.202307274,
  4075595.8333139275,
  4204931.606741165,
  3993122.406600973,
  10922319.23135215,
  7507563.746867171,
  11609943.780034997,
  10262424.426664524,
  10109188.436821004,
  2535585.4747373904,
  2482431.042764656,
  1965239.6350605849,
  2134897.840916636]


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

exp_neon_tv = [964636.5218687267,
  945516.4200716061,
  308360.6068593414,
  141180.12129145692,
  353630.06850379624,
  259588.21639104147,
  299521.0388332062,
  43341.36271360939,
  2153345.18716209,
  2250321.7641752944,
  3105748.0394419623,
  6065541.487116116,
  3013995.633376721,
  2222584.6558110155]

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

exp_ages_dunai = [964636.5218687267,
  945516.4200716061,
  308360.6068593414,
  141180.12129145692,
  353630.06850379624,
  259588.21639104147,
  299521.0388332062,
  43341.36271360939,
  2153345.18716209,
  2250321.7641752944,
  3105748.0394419623,
  6065541.487116116,
  3013995.633376721,
  2222584.6558110155]
exp_ages_dunai_const = [809860.9281488108,
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
# # # # exp_ages_muons_tv = [265411.22053419525,
# # # #  982919.8929994438,
# # # #  2532603.9804173275,
# # # #  1430560.7831150235,
# # # #  1351247.2152844712,
# # # #  1854444.7045112464,
# # # #  2534867.7285628067,
# # # #  4233540.39638492,
# # # #  1060190.8802123163,
# # # #  1080490.0372512478,
# # # #  2996807.1740701823,
# # # #  4104499.1670110016,
# # # #  4630602.751959682,
# # # #  4371676.975538476,
# # # #  4752786.197871009,
# # # #  2801979.6923513245,
# # # #  3348352.497011173,
# # # #  3613128.693939878,
# # # #  3178873.597239819,
# # # #  9216300.193334645,
# # # #  6559055.491510672,
# # # #  9884634.340030625,
# # # #  8497581.02133486,
# # # #  8574486.078128759,
# # # #  2375024.7017890974,
# # # #  2159250.57668627,
# # # #  1619310.1095379305,
# # # #  1921898.406673565]

# # # # exp_ages_muons_const = [265411.22053419525,
# # # #  771696.2992130874,
# # # #  2364046.9253956983,
# # # #  1288396.5269947306,
# # # #  1901956.603620552,
# # # #  2011372.7603821848,
# # # #  2787759.838818932,
# # # #  4342267.915258035,
# # # #  831247.9372817662,
# # # #  819568.1619946248,
# # # #  2792956.736881527,
# # # #  4208692.379432997,
# # # #  4531181.999072417,
# # # #  4402361.75302382,
# # # #  4882763.30644277,
# # # #  3902945.4527308145,
# # # #  3383552.0548880612,
# # # #  3609680.411813231,
# # # #  3575907.6624627025,
# # # #  10031769.90397615,
# # # #  6791671.54704856,
# # # #  10539331.19720867,
# # # #  9130919.117084693,
# # # #  9209053.512951447,
# # # #  2086283.9840488157,
# # # #  2057308.5445523043,
# # # #  1583453.4291142398,
# # # #  1886041.726249874]

updated_texp_tv = []
updated_texp_const = []

# updated_texp_tv_40 = []
# updated_texp_const_40 = []
# updated_muons_tv = []
# updated_muons_const = []
# updated_muons_tv_40 = []
# updated_muons_const_40 = []
updated_dunai_const = []
updated_dunai = []
updated_neon_tv = []
updated_neon_const = []
diff_tv_dunai = []

diff_tv_pyx = []
diff_tv_qtz = []
perdif = []

perdifneon = []
for i in range(len(exp_ages_constant)): #convert ages from [yr] to [Ma]
    updated = exp_ages_time_varying[i]/10**6
    updated_texp_tv.append(updated) #Evenstar data
    updated_const = exp_ages_constant[i]/10**6 
    updated_texp_const.append(updated_const) #this model
    temp = updated - updated_const
    diff_tv_pyx.append(temp)
    perdif.append(temp/updated)

for i in range(len(exp_neon_tv)): #convert ages from [yr] to [Ma]
    updatedneontv = exp_neon_tv[i]/10**6
    updated_neon_tv.append(updatedneontv)
    updatedneonconst = exp_neon_const[i]/10**6
    updated_neon_const.append(updatedneonconst)
    temp = updatedneontv - updatedneonconst
    diff_tv_qtz.append(temp)
    perdifneon.append(temp/updatedneontv)
    
for i in range(len(exp_ages_dunai)):
    updated_dunaix = exp_ages_dunai[i]/10**6
    updated_dunai_constx = exp_ages_dunai_const[i]/10**6
    updated_dunai.append(updated_dunaix)
    updated_dunai_const.append(updated_dunai_constx)
    temp = updated_dunaix - updated_dunai_constx
    diff_tv_dunai.append(temp)
# # # #     # updatedmuons = exp_ages_muons_tv[i]/10**6
# # # #     # updated_muons_tv.append(updatedmuons)
# # # #     # updatedmuonsconst = exp_ages_muons_const[i]/10**6
# # # #     # updated_muons_const.append(updatedmuonsconst)

# plt.rcParams["figure.figsize"] = [5,5] #update figure size
# plt.xlim(2,12)
# plt.axhline(y = 0, c = 'black')
# plt.plot(updated_texp_const[0:4] ,diff_tv_pyx[0:4], 'o', c = 'limegreen', alpha = 0.7, label = '$^{3}He$ - Surface 2')
# plt.plot(updated_texp_const[4:17],diff_tv_pyx[4:17], 'o', c = 'royalblue', alpha = 0.7, label = '$^{3}He$ - Surface 3')
# plt.plot(updated_texp_const[17:26],diff_tv_pyx[17:26], 'o', c = 'deepskyblue', alpha = 0.7, label = '$^{3}He$ - Surface 5')

# plt.plot(updated_neon_const[0:9], diff_tv_qtz[0:9], 's', c ='teal', alpha = 0.7,label = '$^{21}Ne$ - Surface 1')
# plt.plot(updated_neon_const[9:11], diff_tv_qtz[9:11], 's', c='darkblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 2')
# plt.plot(updated_neon_const[11:14], diff_tv_qtz[11:14], 's', c='royalblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 3')
# plt.plot(updated_neon_const[13], diff_tv_qtz[13], 's', c='deepskyblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 5')

# plt.xlabel('Exposure age using LSDn long term average (Ma)')
# plt.ylabel('Exposure age difference (our model - long term average) (Ma) ')


# plt.plot(updated_texp_const[0:4] ,perdif[0:4], 'o', c = 'limegreen', alpha = 0.7, label = '$^{3}He$ - Surface 2')
# # plt.plot(updated_texp_const[4:17],diff_tv_pyx[4:17], 'o', c = 'royalblue', alpha = 0.7, label = '$^{3}He$ - Surface 3')
# # plt.plot(updated_texp_const[17:26],diff_tv_pyx[17:26], 'o', c = 'deepskyblue', alpha = 0.7, label = '$^{3}He$ - Surface 5')

# plt.plot(updated_neon_const[0:9], perdifneon[0:9], 's', c ='teal', alpha = 0.7,label = '$^{21}Ne$ - Surface 1')
# plt.plot(updated_neon_const[9:11], diff_tv_qtz[9:11], 's', c='darkblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 2')
# plt.plot(updated_neon_const[11:14], diff_tv_qtz[11:14], 's', c='royalblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 3')
# plt.plot(updated_neon_const[13], diff_tv_qtz[13], 's', c='deepskyblue', alpha = 0.7,label = '$^{21}Ne$ - Surface 5')

# # # # # plt.plot(updated_muons_const[0:4],updated_muons_tv[0:4], 'x', markersize = 3, c = 'darkblue')
# # # # # plt.plot(updated_muons_const[4:17],updated_muons_tv[4:17], 'x', markersize = 3, c = 'darkblue')
# # # # # plt.plot(updated_muons_const[17:26],updated_muons_tv[17:26], 'x', markersize = 3, c = 'darkblue')

# # plt.savefig(Read.directory+'/plots/Figure_9.pdf', dpi = 300, bbox_inches='tight')




# plt.xlim(0,20)
# plt.axhline(y = 0, c = 'black')
# plt.plot(updated_dunai_const[0:5], diff_tv_dunai[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# plt.plot(updated_dunai_const[5:9], diff_tv_dunai[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# plt.plot(updated_dunai_const[9:13],  diff_tv_dunai[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# plt.plot(updated_dunai_const[13:15], diff_tv_dunai[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# plt.plot(updated_dunai_const[15:16], diff_tv_dunai[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
# plt.ylabel('Exposure age difference (our model - long term average) (Ma) ')
# plt.xlabel('Exposure age using LSDn long term average (Ma)')
# plt.savefig(Read.directory+'/plots/dunai.pdf', dpi = 300, bbox_inches='tight')



"""
FIG 10
LIBARKIN DATASET

"""
# tempvals = []
# tempvalsmu = []
# lambdasp = 160 #effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
# lambdamu = 1300 #muon attenuation length in at/g/yr (Balco supplementary)
# erosion = 3*(10**-3) #cm/yr, per Dunai (2010)
# dt = 250000
# rho = 2.32

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
# np.savetxt(directory+"/text_for_plots/lib_3e3.csv", 
#             concentrations,
#             delimiter =", ", 
#             fmt ='% s')



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
# plt.xlim(0,100)
# plt.ylim(0,5e6)
# plt.xlabel('Depth below surface (cm)', fontsize = 12)
# plt.ylabel('Concentration (atoms/g)', fontsize = 12)
# plt.savefig(Read.directory+'/plots/Figure_10.png', dpi = 300, bbox_inches='tight')





