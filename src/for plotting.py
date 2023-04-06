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
# import scaling_factor
import neutron_spallation
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

# paleolatitudes = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
# fig,ax = plt.subplots()


# # make a plot with different y-axis using second axis object
# ax.plot(paleolatitudes, Read.Rc_full[1][1:],color="darkblue")
# ax.plot(paleolatitudes, Read.Rc_half[1][1:],color="darkblue", linestyle = '-.')

# ax.set_ylim(top = 19)

# ax.set_ylabel("Cutoff Rigidity (GV)",
#               color="darkblue",
#               fontsize=13)
# ax.set_xlabel("Geomagnetic Latitude", fontsize = 13)

# # twin object for two different y-axis on the sample plot
# ax2=ax.twinx()
# ax2.plot(paleolatitudes, Read.sf_full[1][1:],
#         color="darkgreen", label = 'present day field')
# ax2.plot(paleolatitudes, Read.sf_half[1][1:],
#         color="darkgreen", linestyle = '-.', label = 'present day field/2')
# ax2.set_ylim(top = 1.1)
# # set x-axis label
# # set y-axis label
# ax2.set_xlim(left=0)
# ax2.set_xlim(right=90)
# ax2.set_ylabel("Scaling Factor",color="darkgreen",fontsize=13)

# ax2.legend(loc = 'right')

# plt.savefig(Read.directory+'/plots/Figure_2.pdf', dpi = 300, bbox_inches='tight')

# ##DO NUT RUN, SAVED CSV's##
# # Rc_half = Rc.Rc.iloc[:,0]
# # Rc_half.to_csv(directory+'/text_for_plots/Rc_half.csv') 

# # sf_half = scaling_factor.Siteprod_df[0]
# # sf_half.to_csv(directory+'/text_for_plots/sf_half.csv') 

# # Rc_full = Rc.Rc.iloc[:,0]
# # Rc_full.to_csv(directory+'/text_for_plots/Rc_full.csv') 

# # sf_full = scaling_factor.Siteprod_df[0]
# # sf_full.to_csv(directory+'/text_for_plots/sf_full.csv') 

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


# alt = np.arange(0,8001,500)


# # plt.plot([0,3], [0,3], 'k-') #1:1 line
# plt.plot(Read.GL_STD[1],Read.GL_ERA40[1], 'x-',  markersize = 4, label = 'High latitude', c = 'darkmagenta')
# plt.plot(Read.EC_STD[1],Read.EC_ERA40[1], 'x-',    markersize = 4,label = 'Equator' , c = 'green')
# plt.ylabel('Scaling factor using ERA40')
# plt.xlabel('Scaling factor using standard atmosphere')


# plt.legend()
# plt.savefig(Read.directory+'/plots/Figure_5.pdf', dpi = 300, bbox_inches='tight')


"""
FIGURE 6
Scaling factor TV and Constant

"""

# time = np.linspace(0,70,281)

##DONT RUN THIS PART
# # sf_india = scaling_factor.Siteprod_df.iloc[0]
# # sf_india.to_csv(directory+'/text_for_plots/sf_IN.csv') 
# # sf_india_const = scaling_factor.Siteprod_df.iloc[0]
# # sf_india_const.to_csv(directory+'/text_for_plots/sf_IN_const.csv') 

##BEGIN
# plt.plot(time,Read.sf_IN.iloc[:,1], c = 'darkgreen',label = 'time-varying field + latitude')
# plt.plot(time,Read.sf_IN_const.iloc[:,1], '--',c = 'darkblue', label = 'constant field + latitude')
# plt.legend()
# plt.xlabel('Time [Ma]')
# plt.ylabel('Scaling Factor')
# plt.savefig(directory+'/plots/Figure_6.pdf', dpi = 300, bbox_inches='tight')


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
# exp_ages_time_varying = [2768814.7852780037,
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
#   2411367.4649931323]

# exp_ages_constant = [2990674.9547791057,
#   2431916.217552013,
#   2974591.3992882436,
#   5456791.598782122,
#   3418179.2227333765,
#   5483880.018366278,
#   5009229.467293485,
#   5245524.757105527,
#   6113163.708160606,
#   3999211.357593979,
#   4310674.068886829,
#   4442160.370589831,
#   4223348.946027382,
#   12319371.654837996,
#   8275636.121384772,
#   13188879.74707849,
#   11468208.919486826,
#   11291749.683707338,
#   2664551.4317678516,
#   2585317.380928394]

# exp_ages_muons_tv = [2753701.4107777853,
#   2056795.4435907109,
#   2555151.201061768,
#   5023786.798965172,
#   3036213.925069018,
#   5024321.868726578,
#   4531786.161718714,
#   4786715.492061025,
#   5546595.182462663,
#   3536620.176497739,
#   3802736.2381327846,
#   4025090.5900709876,
#   3784680.5793326064,
#   10552959.960047904,
#   7278845.120270775,
#   11285533.425735576,
#   10018403.433793591,
#   9791145.702431163,
#   2298236.0942358165,
#   2286441.4922106797]

# exp_ages_muons_const = [2804694.601454547,
#   2291451.7704243823,
#   2801180.6267542527,
#   5296654.495290533,
#   3288119.3619893105,
#   5303227.6317730425,
#   5001584.898952547,
#   5055488.738484894,
#   6024849.306097686,
#   3806980.741328083,
#   4262879.589419506,
#   4293269.676632794,
#   4050497.5906659523,
#   12263282.93816918,
#   8254035.283485948,
#   13040516.707969276,
#   11297650.29089213,
#   11257175.75048956,
#   2537307.567803689,
#   2518794.2504755203]


# updated_texp_tv = []
# updated_texp_const = []
# updated_texp_tv_40 = []
# updated_texp_const_40 = []
# updated_muons_tv = []
# updated_muons_const = []
# updated_muons_tv_40 = []
# updated_muons_const_40 = []
# for i in range(len(exp_ages_constant)): #convert ages from [yr] to [Ma]
#     updated = exp_ages_time_varying[i]/10**6
#     updated_texp_tv.append(updated) #Evenstar data
#     updated_const = exp_ages_constant[i]/10**6 
#     updated_texp_const.append(updated_const) #this model
    

#     updatedmuons = exp_ages_muons_tv[i]/10**6
#     updated_muons_tv.append(updatedmuons)
#     updatedmuonsconst = exp_ages_muons_const[i]/10**6
#     updated_muons_const.append(updatedmuonsconst)

# plt.plot([0,16], [0,16], 'k-') #1:1 line
# plt.rcParams["figure.figsize"] = [5,5] #update figure size
# plt.plot(updated_texp_const,updated_texp_tv, 'o', c = 'darkblue', alpha = 0.7, label = '0-25 Ma')
# plt.plot(updated_muons_const,updated_muons_tv, 'x', markersize = 3, c = 'cornflowerblue', label = '0-25 Ma w muons')
# plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
# plt.xlabel('Exposure Age [Ma] constant field', fontsize = 10)
# plt.ylabel('Exposure Age [Ma] time-varying field', fontsize = 10)
# plt.savefig(Read.directory+'/plots/Figure_8.svg', dpi = 300, bbox_inches='tight')




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
    
# plt.scatter(updated_age_50, updated_texp_diff_250_50, c = 'blue', label = '50 ka')
# plt.scatter(updated_age_1ma,  updated_texp_diff_250_1ma, c = 'darkmagenta', label = '1 Ma')
# plt.xlabel('Exposure Age [Ma]')
# plt.ylabel('Exposure Age (250 ka) / Exposure Age (50ka or 1 Ma)')
# plt.legend()

# plt.savefig(Read.directory+'/plots/Figure_9.png', dpi = 300, bbox_inches='tight')

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
plt.figure(figsize=(8,6)) 
plt.yscale('log')
plt.xscale('log')
plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[0]*neutron_spallation.E.iloc[:,0], c = 'darkblue', label = 'Terrestrial surface at poles (neutrons)')
#plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[2]*neutron_spallation.E.iloc[:,0], c = 'darkblue', label = 'Sea level, equator')
#plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[4]*neutron_spallation.E.iloc[:,0], '--',c = 'darkgreen', label = '1000 masl, pole')
#plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[6]*neutron_spallation.E.iloc[:,0], c = 'darkgreen',label = '1000 masl, equator')
#plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[8]*neutron_spallation.E.iloc[:,0], '--', c = 'darkgreen', label = '2000 masl, pole')
#plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[10]*neutron_spallation.E.iloc[:,0],  c = 'darkgreen', label = '2000 masl, equator')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[12]*neutron_spallation.E.iloc[:,0], '--',c = 'darkgreen', label = '4000 masl, pole')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[14]*neutron_spallation.E.iloc[:,0], c = 'darkblue',label = '4000 masl, equator')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[16]*neutron_spallation.E.iloc[:,0],'--', c = 'purple',label = '6000 masl, pole')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[18]*neutron_spallation.E.iloc[:,0], c = 'purple',label = '6000 masl, equator')

leya = pd.read_csv(directory+'/text_for_plots/leyadata.csv')
plt.yscale('log')
plt.xscale('log')
plt.plot(leya['x'],leya[' y']*leya['x'], label = 'Meteoroid surface (protons)', c = 'cornflowerblue')
