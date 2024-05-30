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
import mcadam
import Pmag_paleolat
import glob
import os
# import atm_depth
# import shielding
# import scaling_factor
# import neutron_spallation
# import proton_spallation
# import muons
import matplotlib.gridspec as gridspec


os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)

"""
Climate Data
"""
elevations = np.arange(0,5001,500)
# ERA40 = [1028.664348
# ,971.610977
# ,917.170475
# ,865.248965
# ,815.754994
# ,768.599501
# ,723.695775
# ,680.959421
# ,640.308321
# ,601.662595
# ,564.944569]

# standard = [1033.227237
# ,973.417892
# ,916.443484
# ,862.200037
# ,810.586253
# ,761.503465
# ,714.855602
# ,670.549150
# ,628.493115
# ,588.598980
# ,550.780674]

# VALDES = [1018.662499
# ,961.930398
# ,907.807301
# ,856.199073
# ,807.014024
# ,760.162867
# ,715.558687
# ,673.116896
# ,632.755200
# ,594.393560
# ,557.954153]

# era40 = []
# valdes = []
# for i in range(len(ERA40)):
#     era40.append(standard[i]-ERA40[i])
#     valdes.append(standard[i]-VALDES[i])

# plt.plot(elevations, era40, '#016c59', label = 'standard atmosphere - ERA40')
# #plt.plot(elevations, standard)
# plt.plot(elevations,valdes, '--', c='#67a9cf', label = 'standard atmosphere - Valdes et al. (2021)')

# plt.ylabel('Atmospheric depth difference (g/cm${^2}$)', fontsize = 11)
# plt.xlabel('Elevation (MASL)', fontsize = 11)
# plt.legend()
#plt.savefig(directory+'/plots_updated/Figure_0.svg', dpi = 300, bbox_inches='tight')

# time = np.arange(0,70.25,0.25)
# era40 = Read.era40_v_time[1:]
# std = Read.std_v_time[1:]
# valdes = Read.valdes_v_time[1:]

# plt.plot(time,era40.iloc[0][:],'#016c59', label = 'ERA40')
# plt.plot(time,valdes.iloc[0][:],'--',c='#3690c0', label = 'Valdes et al. (2021)')
# plt.plot(time,std.iloc[0][:],'-.',c='#a6bddb' ,label = 'standard atmosphere')

# plt.legend()
# plt.xlabel('Time (Ma)', fontsize = 11)
# plt.ylabel('Atmospheric depth (g/cm${^2}$)', fontsize = 11)

# plt.savefig(directory+'/plots_updated/Figure_0B.pdf', dpi = 300, bbox_inches='tight')



"""
Flux comparisons 

"""
# plt.figure(figsize=(8,6)) 
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[0]*neutron_spallation.E.iloc[:,0],c = 'black', label = 'Sea level, pole')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[2]*neutron_spallation.E.iloc[:,0], c = 'darkblue', label = 'Sea level, equator')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[8]*neutron_spallation.E.iloc[:,0], '--', c = 'darkgreen', label = '2000 masl, pole')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[10]*neutron_spallation.E.iloc[:,0],  c = 'darkgreen', label = '2000 masl, equator')


# plt.ylabel('Differential Flux' r'$ \;\times$' 'Energy ' '$ (cm^{-2} s^{-1}$)', fontsize = 13)
# plt.xlabel('Energy (MeV)', fontsize = 13)
# # plt.legend(loc='lower left')
# plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
# plt.savefig(directory+'/plots/Figure_1_modified.svg', dpi = 300, bbox_inches='tight')

"""
Figure 1
Rc vs. Scaling Factor
"""
# # create figure and axis objects with subplots()
# # in excel sheet: set every lat to 0-90, lon = 0, elevation = 0. Uncomment out the part of pmag that hard-codes the latitudes (so it doesn't vary w time)
# # only run for like 1 Ma, bc you're only gonna use the first value anyways.
# # note: make sure you hard code atm depth to 1033 g/cm2


# paleolatitudes = np.arange(0,91,2)
# fig,ax = plt.subplots()


# #make a plot with different y-axis using second axis object
# ax.plot(paleolatitudes, Read.Rc_full[1][1:],linewidth = 2.5, color="#016c59")
# ax.plot(paleolatitudes, Read.Rc_half[1][1:],linewidth = 2.5, color="#016c59", linestyle = '-.')

# ax.set_ylim(top = 15)

# ax.set_ylabel("Cutoff Rigidity (GV)",
#               color="#016c59",
#               fontsize=13)
# ax.set_xlabel("Geomagnetic Latitude", fontsize = 13)
# ax.spines['left'].set_color('#016c59')
# ax.tick_params(axis='y', colors='#016c59')

# # twin object for two different y-axis on the sample plot
# ax2=ax.twinx()
# ax2.plot(paleolatitudes, Read.sf_half[1][1:], linewidth = 2.5,
#         color="#67a9cf", linestyle = '-.', label = "$M_{half}$")
# ax2.plot(paleolatitudes, Read.sf_full[1][1:],linewidth =2.5,
#         color="#67a9cf", label = "$M_{present}$")


# # set x-axis label
# # set y-axis label
# ax2.set_xlim(left=0)
# ax2.set_xlim(right=90)
# ax2.set_ylabel("Scaling Factor",color="#67a9cf",fontsize=13)
# ax2.tick_params(axis='y', colors='#67a9cf')

# ax2.legend(loc = 'right')

# plt.savefig(Read.directory+'/plots_updated/Figure_2.pdf', dpi = 300, bbox_inches='tight')

#DO NUT RUN, SAVED CSV's##
# Rc_half = Rc.Rc.iloc[:,0]
# Rc_half.to_csv(directory+'/text_for_plots/Rc_half.csv') 

# sf_half = scaling_factor.Siteprod_df[0]
# sf_half.to_csv(directory+'/text_for_plots/sf_half.csv') 

# Rc_full = Rc.Rc.iloc[:,0]
# Rc_full.to_csv(directory+'/text_for_plots/Rc_full.csv') 

# sf_full = scaling_factor.Siteprod_df[0]
# sf_full.to_csv(directory+'/text_for_plots/sf_full.csv') 

#Panel B

#READ IN FILES
# midlats = scaling_factor.Siteprod_df.iloc[0][:]
# poles = scaling_factor.Siteprod_df.iloc[1][:]
# equator =scaling_factor.Siteprod_df.iloc[2][:]

# midlats.to_csv(directory+'/text_for_plots/midlats.csv') 
# poles.to_csv(directory+'/text_for_plots/poles.csv') 
# equator.to_csv(directory+'/text_for_plots/equator.csv') 

# medians = np.linspace(0,8,281)

# midlats = Read.midlats[1][1:]
# poles = Read.poles[1][1:]
# equator = Read.equator[1][1:]

# plt.plot(medians,midlats,'#3690c0',linewidth = 2.5, label = '45N, 120W, sea level')
# plt.plot(medians,poles,'#016450',linestyle='-.', linewidth = 2.5, label = 'Poles, sea level')
# plt.plot(medians,equator,'#a6bddb',linestyle='--',linewidth = 2.5, label = 'Equator, sea level')

# plt.ylabel('Scaling factor', fontsize = 13)
# plt.xlabel('Dipole moment (10$^{22}$ Am$^2$)', fontsize = 13)
# plt.legend()

# plt.savefig(Read.directory+'/plots/Figure1B.pdf', dpi = 300, bbox_inches='tight')

"""
Figure 2
PALEOLAT FIGURE

UPDATED: 1/30
"""

# time = np.linspace(0,70,281)
##DO NOT RUN THESE FILES, THEY ARE SAVED##
# IN = Pmag_paleolat.pl_df.iloc[0]
# IN.to_csv(directory+'/text_for_plots/IN.csv') 


# SA = Pmag_paleolat.pl_df.iloc[1]
# SA.to_csv(directory+'/text_for_plots/SA.csv') 
 

# GL = Pmag_paleolat.pl_df.iloc[2]
# GL.to_csv(directory+'/text_for_plots/GL.csv') 


# AF = Pmag_paleolat.pl_df.iloc[3]
# AF.to_csv(directory+'/text_for_plots/AF.csv') 

#BEGIN UNCOMMENTING~~

# fig = plt.figure(figsize=(10.5, 8.5))
# spec = fig.add_gridspec(3,3)
# fig.text(0.06, 0.65, 'Normalized paleolatitude', va='center', rotation='vertical', size =15)
# fig.text(0.45, 0.34, 'Time (Ma)', va='center', rotation='horizontal', size =15)

# time = np.arange(0,70+0.25,0.25)
# ax0 = fig.add_subplot(spec[0, :])
# ax0.plot(time,Read.IN.iloc[:,1]/Read.IN.iloc[0,1], linewidth = 2.5, c = 'royalblue', label = 'India (20N, 73E)')
# ax0.plot(time,Read.GL.iloc[:,1]/Read.GL.iloc[0,1], linewidth = 2.5, c = 'mediumorchid')
# ax0.plot(time,(Read.SA.iloc[:,1]+90)/(Read.SA.iloc[0,1]+90), linewidth = 2.5, c = 'darkblue')
# ax0.plot(time,(Read.AF.iloc[:,1]+90)/(Read.AF.iloc[0,1]+90), linewidth = 2.5, c = 'mediumseagreen')
# ax0.text(65,0, 'A', fontsize = 22)

# plt.axhspan(0.85, 1.1, xmin=0, xmax=1, color = 'gray', alpha = 0.5)

# ax0.set_xlim(0, 70)
# plt.legend()
# #annotate_axes(ax0, 'ax0')

# ax10 = fig.add_subplot(spec[1, :])
# ax10.plot(time,Read.GL.iloc[:,1]/Read.GL.iloc[0,1], linewidth = 2.5, c = 'mediumorchid', label = 'Greenland (75N, 42W)')
# ax10.plot(time,(Read.SA.iloc[:,1]+90)/(Read.SA.iloc[0,1]+90), linewidth = 2.5, c = 'darkblue', label = 'Northern Chile (19S, 69W)')
# ax10.plot(time,(Read.AF.iloc[:,1]+90)/(Read.AF.iloc[0,1]+90), linewidth = 2.5, c = 'mediumseagreen', label = 'South Africa (31S, 22E)')
# ax10.set_xlim(0, 70)
# ax10.text(65,0.93, 'B', fontsize = 22)

# plt.legend()


# plt.savefig(directory+'/plots/Figure_4.png', dpi = 300, bbox_inches='tight')
"""
Figure 3
Workflow figure
"""


"""
Figure 4
MCADAM Model

"""


"""
FIGURE 5
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

#x = Read.sf_50kyr.iloc[:,1]

# plt.rcParams["figure.figsize"] = [5,4] #update figure size 


# # plt.plot(time1, Read.sf_250ka.iloc[:,1].repeat(5).reset_index(drop=True).iloc[4:].reset_index(drop=True)/x, c = 'gray',  label = 'SF(250 kyr) : SF(50 kyr)')
# # plt.plot(time2,  Read.sf_250ka.iloc[:,1]/Read.sf_1ma.iloc[:,1].repeat(4).reset_index(drop=True).iloc[3:].reset_index(drop=True), c = 'darkgreen', label = 'SF(250 kyr): SF(1 Myr)')
# # plt.xlabel('Time (Ma)', fontsize = 13)
# # plt.ylabel('Scaling factor ratio', fontsize = 13)
# # plt.legend(loc = 'lower right')
# # plt.xlim(0,70)
# # plt.axhline(y = 1, color = 'black', lw = 3)
# w = 0.02
# plt.ylim(0,0.8)
# data = Read.sf_250ka.iloc[:,1].repeat(5).reset_index(drop=True).iloc[4:].reset_index(drop=True)/x
# data2= Read.sf_250ka.iloc[:,1]/Read.sf_1ma.iloc[:,1].repeat(4).reset_index(drop=True).iloc[3:].reset_index(drop=True)
# x, bins, p = plt.hist(data,  bins=np.arange(min(data), max(data) + w, w), density = True,color = 'darkblue', label = 'SF(250 kyr) : SF(50 kyr)')
# y, bins, q = plt.hist(data2,bins=np.arange(min(data2), max(data2) + w, w), density = True, color = 'cornflowerblue', alpha = 0.7, label = 'SF(250 kyr): SF(1000 kyr)')

# for item in p:
#     item.set_height(item.get_height()/sum(x))
# for item in q:
#     item.set_height(item.get_height()/sum(y))
# plt.legend(bbox_to_anchor=(0, 0.2), prop={'size':9}, loc = 'lower left')
# plt.xlabel('Scaling factor ratio', fontsize = 13)
# plt.ylabel('Normalized number of occurrences', fontsize = 13)
# plt.savefig(Read.directory+'/plots/Figure_6.svg', dpi = 300, bbox_inches='tight')


"""
FIGURE 6
Atmospheric Depth / SF variations

"""
##DO NOT RE RUN THIS PART##
# x = scaling_factor.Siteprod_df
# GL_STD_sf = x[0][0:17]
# GL_STD_sf.to_csv(directory+'/text_for_plots/Figure_7_GL_STD')


# x = scaling_factor.Siteprod_df
# EC_STD_sf = x[0][17::]
# EC_STD_sf.to_csv(directory+'/text_for_plots/Figure_7_EC_STD')

# x = scaling_factor.Siteprod_df
# GL_ERA40_sf = x[0][0:17]
# GL_ERA40_sf.to_csv(directory+'/text_for_plots/Figure_7_GL_ERA40')

# x = scaling_factor.Siteprod_df
# EC_ERA40_sf = x[0][17::]
# EC_ERA40_sf.to_csv(directory+'/text_for_plots/Figure_7_EC_ERA40')


# x = scaling_factor.Siteprod_df
# GL_climate_sf = x[0][0:17]
# GL_climate_sf.to_csv(directory+'/text_for_plots/Figure_6_GL_climate')

# x = scaling_factor.Siteprod_df
# EC_climate_sf = x[0][17::]
# EC_climate_sf.to_csv(directory+'/text_for_plots/Figure_6_EC_climate')

# x = scaling_factor.Siteprod_df
# GL_climate_sf_70 = x[20][0:17]
# GL_climate_sf_70.to_csv(directory+'/text_for_plots/Figure_6_GL_climate_70')

# x = scaling_factor.Siteprod_df
# EC_climate_sf_70 = x[20][17::]
# EC_climate_sf_70.to_csv(directory+'/text_for_plots/Figure_6_EC_climate_70')

#START RUN#
# from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,mark_inset)
# import matplotlib.patches as patches


# alt = np.arange(0,5001,500)


# fig, ax1 = plt.subplots()
# ax1.set_aspect('equal')
# ax1.plot(Read.GL_STD.iloc[1:12][1],Read.GL_climate.iloc[1:12][1], 'x-',  linewidth = 2, markersize = 6, label = 'High latitude: 75N,40E', c = '#014636')
# ax1.plot(Read.EC_STD.iloc[1:12][1],Read.EC_climate.iloc[1:12][1], 'x-',   linewidth = 2,  markersize = 6,label = 'Equator: 0N, 78E' , c = '#67a9cf')
# plt.grid()
# ax1.set_ylabel('Scaling factor using climate')
# ax1.set_xlabel('Scaling factor using standard atmosphere')
# ax1.legend(loc=0)

# ax1.set_ylim(0,40)
# ax1.set_xlim(0,40)

# rect = patches.Rectangle((0, 0), 5, 5, linewidth=1, edgecolor='k', facecolor='none')
# ax1.add_patch(rect)

# left, bottom, width, height = [0.53, 0.2, 0.20, 0.25] # modify to move the inset curve and change its size
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(Read.GL_STD.iloc[1:12][1],Read.GL_climate.iloc[1:12][1], 'x-',  linewidth = 2, markersize = 6, label = 'High latitude: 75N,40E ', c = '#014636')
# ax2.plot(Read.EC_STD.iloc[1:12][1],Read.EC_climate.iloc[1:12][1], 'x-',  linewidth = 2,   markersize = 6,label = 'Equator: 0N, 78E' , c = '#67a9cf')

# ax2.set_xlim(0,5)
# ax2.set_ylim(0,5)
# ax2.set_xticks([0, 2,4])
# ax2.set_yticks([0,2,4])
# ax2.tick_params(axis='both', which='major', labelsize=8)

# ax1.plot(Read.GL_STD.iloc[1:12][1],Read.GL_ERA40.iloc[1:12][1], 'o-',  linewidth = 2, markersize = 4, label = 'High latitude: 75N,40E ', c = '#014636')
# ax1.plot(Read.EC_STD.iloc[1:12][1],Read.EC_ERA40.iloc[1:12][1], 'o-',   linewidth = 2,  markersize = 4,label = 'Equator: 0N, 78E' , c = '#67a9cf')

# ax1.set_ylabel('Scaling factor using ERA40')
# ax1.set_xlabel('Scaling factor using standard atmosphere')
# ax1.legend(loc=0)
# ax1.set_ylim(0,40)
# ax1.set_xlim(0,40)

# rect = patches.Rectangle((0, 0), 5, 5, linewidth=1, edgecolor='k', facecolor='none')
# ax1.add_patch(rect)

# left, bottom, width, height = [0.53, 0.2, 0.20, 0.25] # modify to move the inset curve and change its size
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(Read.GL_STD.iloc[1:12][1],Read.GL_ERA40.iloc[1:12][1], 'o-',  linewidth = 2, markersize = 4, label = 'High latitude: 75N,40E ', c = '#014636')
# ax2.plot(Read.EC_STD.iloc[1:12][1],Read.EC_ERA40.iloc[1:12][1], 'o-',  linewidth = 2,   markersize = 4,label = 'Equator: 0N, 78E' , c = '#67a9cf')

# ax2.set_xlim(0,5)
# ax2.set_ylim(0,5)
# ax2.set_xticks([0, 2,4])
# ax2.set_yticks([0,2,4])
# ax2.tick_params(axis='both', which='major', labelsize=8)
# plt.grid()
ottb# plt.savefig(Read.directory+'/plots_updated/Figure_6A.svg', dpi = 300, bbox_inches='tight')


# fig = plt.figure(figsize=(4,4))

# alt = np.arange(0,5001,500)


# fig, ax1 = plt.subplots()
# ax1.set_aspect('equal')
# ax1.plot(Read.GL_STD.iloc[1:12][1],Read.GL_climate_70.iloc[1:12][1], 'x-',  linewidth = 2, markersize = 6, label = 'High latitude: 75N,40E ', c = '#014636')
# ax1.plot(Read.EC_STD.iloc[1:12][1],Read.EC_climate_70.iloc[1:12][1], 'x-',   linewidth = 2,  markersize = 6,label = 'Equator: 0N, 78E' , c = '#67a9cf')

# ax1.set_ylabel('Scaling factor using climate')
# ax1.set_xlabel('Scaling factor using standard atmosphere')
# ax1.legend(loc=0)
# ax1.set_ylim(0,40)
# ax1.set_xlim(0,40)
# plt.grid()
# rect = patches.Rectangle((0, 0), 5, 5, linewidth=1, edgecolor='k', facecolor='none')
# ax1.add_patch(rect)

# left, bottom, width, height = [0.53, 0.2, 0.20, 0.25] # modify to move the inset curve and change its size
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(Read.GL_STD.iloc[1:12][1],Read.GL_climate_70.iloc[1:12][1], 'x-',  linewidth = 2, markersize = 6, label = 'High latitude: 75N,40E ', c = '#014636')
# ax2.plot(Read.EC_STD.iloc[1:12][1],Read.EC_climate_70.iloc[1:12][1], 'x-',  linewidth = 2,   markersize = 6,label = 'Equator: 0N, 78E' , c = '#67a9cf')

# ax2.set_xlim(0,5)
# ax2.set_ylim(0,5)
# ax2.set_xticks([0, 2,4])
# ax2.set_yticks([0,2,4])
# ax2.tick_params(axis='both', which='major', labelsize=8)

# ax1.plot(Read.GL_STD.iloc[1:12][1],Read.GL_ERA40.iloc[1:12][1], 'o-',  linewidth = 2, markersize = 4, label = 'High latitude: 75N,40E ', c = '#014636')
# ax1.plot(Read.EC_STD.iloc[1:12][1],Read.EC_ERA40.iloc[1:12][1], 'o-',   linewidth = 2,  markersize = 4,label = 'Equator: 0N, 78E' , c = '#67a9cf')

# ax1.set_ylabel('Scaling factor using ERA40')
# ax1.set_xlabel('Scaling factor using standard atmosphere')
# ax1.legend(loc=0)
# ax1.set_ylim(0,40)
# ax1.set_xlim(0,40)

# rect = patches.Rectangle((0, 0), 5, 5, linewidth=1, edgecolor='k', facecolor='none')
# ax1.add_patch(rect)

# left, bottom, width, height = [0.53, 0.2, 0.20, 0.25] # modify to move the inset curve and change its size
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(Read.GL_STD.iloc[1:12][1],Read.GL_ERA40.iloc[1:12][1], 'o-',  linewidth = 2, markersize = 4, label = 'High latitude: 75N,40E ', c = '#014636')
# ax2.plot(Read.EC_STD.iloc[1:12][1],Read.EC_ERA40.iloc[1:12][1], 'o-',  linewidth = 2,   markersize = 4,label = 'Equator: 0N, 78E' , c = '#67a9cf')

# ax2.set_xlim(0,5)
# ax2.set_ylim(0,5)
# ax2.set_xticks([0, 2,4])
# ax2.set_yticks([0,2,4])
# ax2.tick_params(axis='both', which='major', labelsize=8)
# plt.grid()
# plt.savefig(Read.directory+'/plots_updated/Figure_6B.png', dpi = 300, bbox_inches='tight')


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

# neg = Read.sf_negative_sigma.iloc[1][1:]
# pos = Read.sf_positive_sigma.iloc[1][1:]
# median = Read.sf_regular_sigma.iloc[1][1:]
# const = Read.sf_constant_sigma.iloc[1][1:]

# tvfield_neg = Read.sf_tvfieldonly_negsigma.iloc[1][1:]
# tvfield_pos = Read.sf_tvfieldonly_possigma.iloc[1][1:]
# tvfield_avg = Read.sf_tvfieldonly_sigma.iloc[1][1:]
# tvlat = Read.sf_tvlatonly_sigma.iloc[1][1:]

# # # #BEGIN
# time = np.linspace(0,70,281)
# f = plt.figure(figsize=(10,4))
# ax = f.add_subplot(121)
# ax2 = f.add_subplot(122)
# ax.plot(time,median, linewidth = 2, c = '#016c59',label = 'time-varying field and latitude')
# ax.plot(time,const, '--',linewidth = 2.5,c = 'black', label = 'constant field and latitude')
# ax.fill_between(time, pos, median,  color = '#a6bddb', alpha = 0.5)
# ax.fill_between(time, median, neg, color =  '#a6bddb', alpha = 0.5)

# ax.set_xlim(0,70)
# ax.plot(time, neg, '#a6bddb')
# ax.plot(time,pos,'#a6bddb')

# ax.vlines(66.052, 0.50, 0.95, linewidth = 2.5)
# ax.set_xlabel('Time (Ma)', fontsize = 13)
# ax.set_ylabel('Scaling Factor', fontsize = 13)
# ax.legend(loc = 'lower left')

# ax2.plot(time,tvfield_avg, linewidth = 2.5,c = '#014636',label = 'time-varying field, constant latitude')
# ax2.plot(time,tvlat, '--',linewidth = 2.5,c = '#67a9cf', label = 'constant field, time-varying latitude')
# ax2.plot(time, tvfield_neg, '#a6bddb')
# ax2.plot(time,tvfield_pos,'#a6bddb')
# ax2.fill_between(time, tvfield_pos, tvfield_avg,  color = '#a6bddb', alpha = 0.5)
# ax2.fill_between(time, tvfield_avg, tvfield_neg, color =  '#a6bddb', alpha = 0.5)


# ax2.set_xlim(0,70)
# ax2.vlines(66.052, 0.50, 0.95,linewidth = 2.5)
# ax2.set_xlabel('Time (Ma)', fontsize = 13)
# ax2.legend(loc = 'lower left')
# plt.setp(ax2.get_yticklabels(), visible=False)


# plt.savefig(directory+'/plots_updated/Figure_8.pdf', dpi = 300, bbox_inches='tight')




"""
FIGURE 9
EVENSTAR DATASET
# """
# exp_ages_time_varying = [123764.70513124338,
#  999950.5881550129,
#  2809842.973923239,
#  1437709.5492099412,
#  1597412.2430487473,
#  2306374.286561611,
#  2811905.9936664747,
#  5205562.436422755,
#  804638.461019477,
#  1027097.292649448,
#  3243379.122532165,
#  5272036.169905982,
#  4814983.263867728,
#  5004348.192627103,
#  5798579.472430228,
#  3801760.946131991,
#  4043021.3848517216,
#  4190083.484928454,
#  3974482.253474694,
#  10867014.793712351,
#  7457939.823871471,
#  11504457.347719094,
#  10174352.548386587,
#  10034978.260752263,
#  2501601.075564036,
#  2442727.0967175965,
#  1917534.0170423328,
#  2085500.9806046379]


# exp_ages_constant= [114228.05791045129,
#  915946.3467122873,
#  2738524.329526318,
#  1337892.329096456,
#  1492716.4114716016,
#  2237688.836019829,
#  2737022.7304163054,
#  5020979.568684665,
#  730821.6829189667,
#  938896.583164952,
#  3152139.0098045915,
#  5070621.350176061,
#  4631739.899436452,
#  4825366.17480535,
#  5623508.560978162,
#  3695269.4978240505,
#  3950957.8542163633,
#  4083156.2323068194,
#  3882028.5922924485,
#  11323751.27282418,
#  7584169.781085953,
#  12086889.969182406,
#  10509988.870293442,
#  10352712.57702584,
#  2442963.7472036444,
#  2385523.147630269,
#  1834586.2395702424,
#  2009533.8964364766]

# exp_neon_tv = [899178.2239571962,
#  881190.6642503834,
#  259997.35382776128,
#  114824.4914495859,
#  304978.6339121114,
#  212150.12984814626,
#  250571.26324864503,
#  34985.91799025203,
#  2098806.2918170462,
#  2192313.0001936136,
#  3083125.499253487,
#  6039894.976639283,
#  2995217.1577257384,
#  2171667.694324269]

# exp_neon_const = [812782.8357428286,
#  795981.1233760518,
#  238097.90154721637,
#  105264.3354208746,
#  278198.6007551687,
#  195317.64176282572,
#  230676.87001299247,
#  32043.77088924872,
#  2011808.5130362157,
#  2111057.733012669,
#  2983165.7621081476,
#  5898613.305004761,
#  2896141.6064051455,
#  2089912.6167371792]

# updated_texp_tv = []
# updated_texp_const = []


# updated_neon_tv = []
# updated_neon_const = []


# diff_tv_pyx = []
# diff_tv_qtz = []
# perdif_ev = []

# perdifneon = []
# for i in range(len(exp_ages_constant)): #convert ages from [yr] to [Ma]
#     updated = exp_ages_time_varying[i]/10**6
#     updated_texp_tv.append(updated) #Evenstar data
#     updated_const = exp_ages_constant[i]/10**6 
#     updated_texp_const.append(updated_const) #this model
#     temp = updated - updated_const
#     diff_tv_pyx.append(temp)
#     perdif_ev.append((temp/updated_const)*100)

# for i in range(len(exp_neon_tv)): #convert ages from [yr] to [Ma]
#     updatedneontv = exp_neon_tv[i]/10**6
#     updated_neon_tv.append(updatedneontv)
#     updatedneonconst = exp_neon_const[i]/10**6
#     updated_neon_const.append(updatedneonconst)
#     temp = updatedneontv - updatedneonconst
#     diff_tv_qtz.append(temp)
#     perdifneon.append((temp/updatedneonconst)*100)
    

# exp_ages_dunai = [15900030.658459842,
#  17218840.558627594,
#  13484315.229998497,
#  24086068.288904108,
#  16059125.504195761,
#  17797279.76808732,
#  11639733.465906788,
#  8031877.958063593,
#  17707901.95244436,
#  11537975.877970759,
#  14752091.425843798,
#  18692537.288270455,
#  14171877.48969891,
#  69986.11861290704,
#  132196.00182438002,
#  89426.70711649234]

# exp_ages_dunai_const = [17331545.871189587,
#  18715347.30854896,
#  14435393.136169683,
#  27422709.90482942,
#  17509247.1486647,
#  19453054.81838913,
#  12211463.267820993,
#  8137098.856875005,
#  19336755.168219406,
#  12091655.94147015,
#  16019322.10241993,
#  20626034.672335483,
#  15290118.856428267,
#  64603.2217204989,
#  122028.30769427573,
#  82548.56108730416]

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

# # y_error = [20024,
# # 30877,
# # 52155,
# # 28716,
# # 54135,
# # 70775,
# # 40501,
# # 110558,
# # 33130,
# # 35213,
# # 69442,
# # 89892,
# # 86588,
# # 90548,
# # 77420,
# # 62253,
# # 94631,
# # 115389,
# # 101593,
# # 102604,
# # 194636,
# # 272514,
# # 210046,
# # 171295,
# # 58222,
# # 42513,
# # 35826,
# # 42440]
# # x_error = [17355,
# # 31168,
# # 50093,
# # 29221,
# # 59277,
# # 69591,
# # 38828,
# # 109016,
# # 31363,
# # 35544,
# # 66907,
# # 87171,
# # 79062,
# # 85765,
# # 96656,
# # 62143,
# # 86525,
# # 104787,
# # 93817,
# # 121054,
# # 182896,
# # 321577,
# # 242034,
# # 194538,
# # 56117,
# # 41789,
# # 36703,
# # 45282]

# # yneonev = [82499.49,
# # 55742.90,
# # 43201.36,
# # 37929.29,
# # 57143.42,
# # 31317.56,
# # 30962.38,
# # 5328.48,
# # 111686.88,
# # 161531.33,
# # 184113.38,
# # 187758.39,
# # 115246.43,
# # 168229.17]

# # xneonev = [77428.56,
# # 52316.60,
# # 37422.95,
# # 32433.23,
# # 49897.27,
# # 27000.08,
# # 27000.08,
# # 4548.96,
# # 118373.47,
# # 172179.60,
# # 174975.26,
# # 236835.20,
# # 109492.01,
# # 178914.05]

# # xneondu = [82859.2777,
# # 135587.909,
# # 112989.9241,
# # 165718.5554,
# # 124288.9165,
# # 130853.3818,
# # 92367.09305,
# # 61578.06203,
# # 119307.4952,
# # 76971.58652,
# # 107760.2211,
# # 138548.8557,
# # 115457.3798,
# # 25046.71178,
# # 35781.01682,
# # 14312.40673]

# # yneondu = [79052.48545,
# # 109848.2555,
# # 93437.68495,
# # 147986.4804,
# # 122527.0669,
# # 103009.4903,
# # 78891.49512,
# # 59214.35941,
# # 94174.20442,
# # 65742.06001,
# # 94600.16256,
# # 108413.5881,
# # 88604.29968,
# # 28889.1525,
# # 41270.21786,
# # 16508.08714]

# # xx = []
# # yy = []
# # xne =[]
# # yne = []

# # xdu = []
# # ydu = []

# for i in range(len(x_error)):
#     xx.append(x_error[i]/10**6)
#     yy.append(y_error[i]/10**6)
# for i in range(len(xneonev)):
#     xne.append(xneonev[i]/10**6)
#     yne.append(yneonev[i]/10**6)
# for i in range(len(xneondu)):
#     xdu.append(xneondu[i]/10**6)
# #     ydu.append(yneondu[i]/10**6)
# fig = plt.figure(figsize=(14,9))


# gs = gridspec.GridSpec(2,2)

# ax1=fig.add_subplot(gs[:,0])
# ax2=fig.add_subplot(gs[0,1])
# ax3=fig.add_subplot(gs[1,1])

# # ax2.set_ylim(-3.5,0.5)
# # ax2.set_xlim(2,30)
# # ax2.hlines(0,2,30)
# #fig = plt.figure(figsize=(14,12))


# gs = gridspec.GridSpec(2,2)



# ax2.set_ylim(-3.5,0.5)
# ax2.set_xlim(2,30)
# ax2.hlines(0,2,30)

# ax2.plot(updated_texp_const[0:4] ,diff_tv_pyx[0:4], 'o', c = 'limegreen', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 2')
# ax2.plot(updated_texp_const[4:17],diff_tv_pyx[4:17], 'o', c = 'royalblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 3')
# ax2.plot(updated_texp_const[17:26],diff_tv_pyx[17:26], 'o', c = 'deepskyblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 5')

# ax2.plot(updated_neon_const[0:9], diff_tv_qtz[0:9], 's', c ='teal', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 1')
# ax2.plot(updated_neon_const[9:11], diff_tv_qtz[9:11], 's', c='limegreen', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 2')
# ax2.plot(updated_neon_const[11:14], diff_tv_qtz[11:14], 's', c='royalblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 3')
# ax2.plot(updated_neon_const[13], diff_tv_qtz[13], 's', c='deepskyblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 5')

# ax2.plot(updated_dunai_const[0:5], diff_tv_dunai[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# ax2.plot(updated_dunai_const[5:9], diff_tv_dunai[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# ax2.plot(updated_dunai_const[9:13],  diff_tv_dunai[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# ax2.plot(updated_dunai_const[13:15], diff_tv_dunai[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# ax2.plot(updated_dunai_const[15:16], diff_tv_dunai[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# ax2.set_ylabel('Exposure age difference (Ma)', fontsize = 14)
# ax2.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)

# ax3.set_xlim(2,30)
# ax3.set_ylim(-14,7.5)
# ax3.plot(updated_texp_const[0:4] ,perdif_ev[0:4], 'o', c = 'limegreen', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 2')
# ax3.plot(updated_texp_const[4:17],perdif_ev[4:17], 'o', c = 'royalblue', alpha = 0.7,markersize = 8, label = '$^{3}He$ - Surface 3')
# ax3.plot(updated_texp_const[17:26],perdif_ev[17:26], 'o', c = 'deepskyblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 5')

# ax3.plot(updated_neon_const[0:9], perdifneon[0:9], 's', c ='teal', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 1')
# ax3.plot(updated_neon_const[9:11], perdifneon[9:11], 's', c='limegreen', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 2')
# ax3.plot(updated_neon_const[11:14], perdifneon[11:14], 's', c='royalblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 3')
# ax3.plot(updated_neon_const[13], perdifneon[13], 's', c='deepskyblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 5')

# ax3.plot(updated_dunai_const[0:5], perdif[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# ax3.plot(updated_dunai_const[5:9], perdif[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# ax3.plot(updated_dunai_const[9:13],  perdif[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# ax3.plot(updated_dunai_const[13:15], perdif[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# ax3.plot(updated_dunai_const[15:16], perdif[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# ax3.set_ylabel('Exposure age percent difference (%)', fontsize = 14)
# ax3.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)
# ax3.hlines(0,2,30)



# ax1.set_xlim(2,30)
# ax1.plot([2,30], [2,30], 'k-')
# ax1.plot(updated_neon_const[0:9], updated_neon_tv[0:9],  's', c = 'teal', markersize = 7)
# ax1.plot(updated_neon_const[9:11], updated_neon_tv[9:11],  's', c='limegreen', markersize = 7)
# ax1.plot(updated_neon_const[11:14], updated_neon_tv[11:14], 's', c='royalblue', markersize = 7)
# ax1.plot(updated_neon_const[13], updated_neon_tv[13],  's', c='deepskyblue', markersize = 7)

# ax1.plot(updated_texp_const[0:4],updated_texp_tv[0:4], 'o', c='limegreen', markersize = 7)
# ax1.plot(updated_texp_const[4:17],updated_texp_tv[4:17], 'o', c = 'royalblue', markersize = 7)
# ax1.plot(updated_texp_const[17:26],updated_texp_tv[17:26], 'o', c = 'deepskyblue', markersize = 7)

# ax1.plot(updated_dunai_const[0:5],updated_dunai[0:5], 's', c='midnightblue', markersize = 7)
# ax1.plot(updated_dunai_const[5:9],updated_dunai[5:9], 's', c='purple',markersize =7)
# ax1.plot(updated_dunai_const[9:13],updated_dunai[9:13], 's', c='mediumpurple', markersize = 7)
# ax1.plot(updated_dunai_const[13:15],updated_dunai[13:15], 's', c='skyblue', markersize =7)
# ax1.plot(updated_dunai_const[15:16],updated_dunai[15:16], 's', c='hotpink', markersize = 7)
# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 14)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)
# ax2.legend()

# plt.savefig(Read.directory+'/plots_updated/evenstar.pdf', dpi = 300, bbox_inches='tight')

# ax1.set_xlim(2,30)
# ax1.plot([2,30], [2,30], 'k-')
# # ax1.errorbar(updated_neon_const[0:9], updated_neon_tv[0:9], yerr = yne[0:9], xerr = xne[0:9], fmt = 's', c = 'teal', capsize = 2, markersize = 7)
# # ax1.errorbar(updated_neon_const[9:11], updated_neon_tv[9:11], yerr = yne[9:11], xerr = xne[9:11], fmt = 's', c='limegreen', capsize = 2, markersize = 7)
# # ax1.errorbar(updated_neon_const[11:14], updated_neon_tv[11:14], yerr = yne[11:14], xerr = xne[11:14], fmt = 's', c='royalblue', capsize = 2, markersize = 7)
# # ax1.errorbar(updated_neon_const[13], updated_neon_tv[13], yerr = yne[13], xerr = xne[13], fmt = 's', c='deepskyblue', capsize = 2, markersize = 7)

# # ax1.errorbar(updated_texp_const[0:4],updated_texp_tv[0:4],yerr = yy[0:4], xerr=  xx[0:4], fmt = 'o', c='limegreen', capsize = 2, markersize = 7)
# # ax1.errorbar(updated_texp_const[4:17],updated_texp_tv[4:17],yerr = yy[4:17], xerr=  xx[4:17], fmt = 'o', c = 'royalblue', capsize = 2, markersize = 7)
# # ax1.errorbar(updated_texp_const[17:26],updated_texp_tv[17:26],yerr = yy[17:26], xerr=  xx[17:26], fmt = 'o', c = 'deepskyblue', capsize = 2, markersize = 7)

# # ax1.errorbar(updated_dunai_const[0:5],updated_dunai[0:5],yerr = ydu[0:5], xerr=  xdu[0:5], fmt = 's', c='midnightblue', capsize = 2, markersize = 7)
# # ax1.errorbar(updated_dunai_const[5:9],updated_dunai[5:9],yerr = ydu[5:9], xerr=  xdu[5:9], fmt = 's', c='purple', capsize = 2, markersize =7)
# # ax1.errorbar(updated_dunai_const[9:13],updated_dunai[9:13],yerr = ydu[9:13], xerr=  xdu[9:13], fmt = 's', c='mediumpurple', capsize = 2, markersize = 7)
# # ax1.errorbar(updated_dunai_const[13:15],updated_dunai[13:15],yerr = ydu[13:15], xerr=  xdu[13:15], fmt = 's', c='skyblue', capsize = 2, markersize =7)
# # ax1.errorbar(updated_dunai_const[15:16],updated_dunai[15:16],yerr = ydu[15:16], xerr=  xdu[15:16], fmt = 's', c='hotpink', capsize = 2, markersize = 7)
# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 13)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 13)
# ax2.legend()
# #plt.savefig(Read.directory+'/plots/Figure_9.svg', dpi = 300, bbox_inches='tight')

"""
FIG 10
LIBARKIN DATASET

# """
# tempvals = []
# tempvalsmu = []
# lambdasp = 160 #effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
# #lambdamu = 1300 #muon attenuation length in at/g/yr (Balco supplementary)
# rho = 2.32
# erosion = (3*(10**-3)) #in cm/yr
# dt2 = 250000
# dt1 = 49000
# dt3 = 201000

# texp_bin1 = [10000,50000,100000,150000,200000,250000]
# texp_bin2 = [300000,350000,400000,450000,500000]
# texp_bin3 = [510000,520000,530000,540000,550000,600000]

# z0 = np.arange(0,102,2)
# concentrations = []
# lambdamu = [270.4025448920097,
#   274.9372570467424,
#   278.13155424768183,
#   280.7343789517444,
#   282.84834647839074,
#   284.660106845728,
#   286.31349756855957,
#   287.9757281535187,
#   289.516459198588,
#   291.103221766351,
#   292.6029218013917,
#   294.0283931916488,
#   295.3895999442067,
#   296.7488552020244,
#   298.1690670244588,
#   299.5449208856159,
#   300.88063015490684,
#   302.1797722975252,
#   303.44541631024646,
#   304.6802190032463,
#   305.88649897457054,
#   307.2175391394648,
#   308.544341747117,
#   309.8493357308708,
#   311.1338055065029,
#   312.398909799448,
#   313.6456984545915,
#   314.8751264406627,
#   316.08806560360387,
#   317.28531459791793,
#   318.4676073313087,
#   319.63562018713145,
#   320.7899782351222,
#   321.95226462147866,
#   323.2171719602245,
#   324.47137641152597,
#   325.7152705918301,
#   326.9492222457257,
#   328.1735764491849,
#   329.3886575649421,
#   330.5947709835189,
#   331.79220467815344,
#   332.9812305975691,
#   334.16210591694244,
#   335.33507416446423,
#   336.50036623840316,
#   337.72712627344026,
#   339.043875095838,
#   340.3553725591056,
#   341.6617483776725,
#   342.9631264842444]

    
# for i in range(len(z0)):
#     Cspall = (shielding.S_thick[0][0]*(neutron_spallation.pn_df[0][i] + proton_spallation.pp_df[0][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt1)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[1][i] + proton_spallation.pp_df[1][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt2))+ (shielding.S_thick[0][0]*(neutron_spallation.pn_df[2][i] + proton_spallation.pp_df[2][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt3))
#     Cmuons = muons.pmuons_df[0][i] / ((rho * erosion) / lambdamu[i]) * np.exp(-(rho*z0[i]/lambdamu[i])) * (1-np.exp(-(rho*erosion/lambdamu[i])*dt1)) + muons.pmuons_df[1][i] / ((rho * erosion) / lambdamu[i]) * np.exp(-(rho*z0[i]/lambdamu[i])) * (1-np.exp(-(rho*erosion/lambdamu[i])*(dt2))) + muons.pmuons_df[2][i] / ((rho * erosion) / lambdamu[i]) * np.exp(-(rho*z0[i]/lambdamu[i])) * (1-np.exp(-(rho*erosion/lambdamu[i])*(dt3))) 
#     Ctot = Cspall + Cmuons
#     concentrations.append(Cspall + Cmuons)
# np.savetxt(directory+"/text_for_plots_updated/lib_3e3.csv", 
#             concentrations,
#             delimiter =", ", 
#             fmt ='% s')



# plt.plot(z0,Read.lib3e3[0], c = 'darkblue', label=r'3$\times 10^{-3}$ cm/yr')
# plt.plot(z0,Read.lib10e3[0], c = 'cornflowerblue', label = r'10$\times 10^{-3}$ cm/yr')
# plt.plot(z0,Read.lib20e3[0], c = 'teal',label = r'20$\times 10^{-3}$ cm/yr')

# x = [15,15,15,35,45,35,55]
# y = [2380000.00,2630000.00,2750000.00,330000.00,730000.00,340000.00,590000.00]

# e = [560000.00,
# 590000.00,
# 570000.00,
# 550000.00,
# 540000.00,
# 600000.00,
# 560000.00]

# ex = [2,2,2,2,2,2,2]
# plt.errorbar(x,y, xerr = ex, yerr=e, fmt='o',c = 'black', markersize = 5)

# plt.legend()
# plt.xlim(0,100)
# plt.ylim(0,5e6)
# plt.xlabel('Depth below paleosurface (cm)', fontsize = 12)
# plt.ylabel(r'Concentration ($\times 10^{6}$atoms/g)', fontsize = 12)
# plt.savefig(Read.directory+'/plots_updated/Figure_10.png', dpi = 300, bbox_inches='tight')


"""
1:1 LINE COMPARISON
"""
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

# for i in range(len(exp_ages_constant)): #convert ages from [yr] to [Ma]
#     updated = exp_ages_time_varying[i]/10**6
#     updated_texp_tv.append(updated) #Evenstar data
#     updated_const = exp_ages_constant[i]/10**6 
#     updated_texp_const.append(updated_const) #this model

# for i in range(len(exp_neon_tv)): #convert ages from [yr] to [Ma]
#     updatedneontv = exp_neon_tv[i]/10**6
#     updated_neon_tv.append(updatedneontv)
#     updatedneonconst = exp_neon_const[i]/10**6
#     updated_neon_const.append(updatedneonconst)

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



# plt.xlabel('LSDn average exposure ages')
# plt.ylabel('SPRITE exposure ages')


# plt.savefig(Read.directory+'/plots/1to1.png', dpi = 300, bbox_inches='tight')




#CLIMATE SIMULATION COMPARISON
# alts = np.arange(0,5001,500)
# time = np.arange(0,25.01,0.25)

# atm_2 = Read.atm_2[1::]
# atm_1 = Read.atm_1[1::]
# atm_0 = Read.atm_0[1::]
# plt.plot(alts,atm_2.iloc[0:11][0], '--', label = 'Climate data')
# plt.plot(alts,atm_1.iloc[0:11][0],'-.', label = 'Standard Atmosphere')
# plt.plot(alts,atm_0.iloc[0:11][0], label = 'ERA40')
# plt.ylabel('Atmospheric Depth [g/cm2]')
# plt.xlabel('Sample elevation [MASL]')
# plt.legend()

# # plt.plot(time,atm_2.iloc[0], '--', label = 'Climate data')
# # plt.plot(time,atm_1.iloc[0],'-.', label = 'Standard atmosphere')
# # plt.plot(time,atm_0.iloc[0], label = 'ERA40')
# # plt.xlabel('Time (Ma)')
# # plt.ylabel('Atmospheric Depth (g/cm2)')
# # plt.legend()
# plt.savefig(Read.directory+'/plots/atm_depth_comparison_elevations.png', dpi = 300, bbox_inches='tight')

