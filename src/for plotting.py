#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:57:00 2022

@author: mmijjum
"""
import numpy as np

import matplotlib.pyplot as plt
import Read
import pandas
import Rc
import Pmag_paleolat
import glob
import os
import scaling_factor
#import neutron_spallation
# import proton_spallation
# import matplotlib.gridspec as gridspec


os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)



"""
Figure 1 
Flux comparisons 

"""
#need specific excel sheet. Ran using quartz conditions. Only need 1 time bin. 
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[0]*neutron_spallation.E.iloc[:,0], '--', c = 'darkblue', label = 'Sea level, pole')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[2]*neutron_spallation.E.iloc[:,0], c = 'darkblue', label = 'Sea level, equator')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[4]*neutron_spallation.E.iloc[:,0], '--',c = 'darkgreen', label = '1000 masl, pole')
# #plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[6]*neutron_spallation.E.iloc[:,0], c = 'darkgreen',label = '1000 masl, equator')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[8]*neutron_spallation.E.iloc[:,0], '--', c = 'darkgreen', label = '2000 masl, pole')
# plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[10]*neutron_spallation.E.iloc[:,0],  c = 'darkgreen', label = '2000 masl, equator')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[12]*neutron_spallation.E.iloc[:,0], '--',c = 'darkgreen', label = '4000 masl, pole')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[14]*neutron_spallation.E.iloc[:,0], c = 'darkblue',label = '4000 masl, equator')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[16]*neutron_spallation.E.iloc[:,0],'--', c = 'purple',label = '6000 masl, pole')
# # plt.plot(neutron_spallation.E.iloc[:,0], neutron_spallation.PhiGMev[18]*neutron_spallation.E.iloc[:,0], c = 'purple',label = '6000 masl, equator')


# plt.ylabel('Differential Flux  of Neutrons * Energy [cm^-2 s^-1]')
# plt.xlabel('Energy [MeV]')
# plt.legend()
# plt.savefig(directory+'/plots/Figure_1.pdf', dpi = 300, bbox_inches='tight')


"""
Figure 2
Rc vs. Scaling Factor
"""
# create figure and axis objects with subplots()
# in excel sheet: set every lat to 0-90, lon = 0, elevation = 0. Uncomment out the part of pmag that hard-codes the latitudes (so it doesn't vary w time)
# only run for like 1 Ma, bc you're only gonna use the first value anyways.
# note: make sure you hard code atm depth to 1033 g/cm2
# paleolatitudes = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
# fig,ax = plt.subplots()
# # make a plot
# ax.plot(paleolatitudes, scaling_factor.Siteprod_df[0],
#         color="darkgreen")
# ax.set_ylim(top = 1.1)
# # set x-axis label
# ax.set_xlabel("Geomagnetic Latitude", fontsize = 13)
# # set y-axis label
# ax.set_ylabel("Scaling Factor",
#               color="darkgreen",
#               fontsize=13)


# # twin object for two different y-axis on the sample plot
# ax2=ax.twinx()
# # make a plot with different y-axis using second axis object
# ax2.plot(paleolatitudes, Rc.Rc.iloc[:,0],color="darkblue")
# ax2.set_ylim(top = 19)

# ax2.set_ylabel("Cutoff Rigidty [GV]",color="darkblue",fontsize=13)
# plt.savefig(Read.directory+'/plots/Figure_2.svg', dpi = 300, bbox_inches='tight')


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

# ax0 = fig.add_subplot(spec[0, :])
# ax0.plot(time,Read.IN.iloc[:,1]/Read.IN.iloc[0,1], 'royalblue')
# ax0.plot(time,Read.GL.iloc[:,1]/Read.GL.iloc[0,1], 'darkblue')
# ax0.plot(time,(Read.SA.iloc[:,1]+90)/(Read.SA.iloc[0,1]+90), 'mediumseagreen')
# ax0.plot(time,(Read.AF.iloc[:,1]+90)/(Read.AF.iloc[0,1]+90), 'darkgreen')
# #annotate_axes(ax0, 'ax0')

# ax10 = fig.add_subplot(spec[1, 0])
# ax10.plot(time,Read.GL.iloc[:,1]/Read.GL.iloc[0,1], 'darkblue')

# #ax10.title.set_text('Greenland: 75N, 42W')
# # annotate_axes(ax10, 'ax10')

# ax11 = fig.add_subplot(spec[1,1], sharey = ax10)
# #ax11.sharey(ax10)
# ax11.plot(time,(Read.SA.iloc[:,1]+90)/(Read.SA.iloc[0,1]+90), 'mediumseagreen')
# #ax11.title.set_text('South America: 19S, 69W')

# # annotate_axes(ax11, 'ax11')

# ax20 = fig.add_subplot(spec[1,2], sharey = ax10)
# ax20.plot(time,(Read.AF.iloc[:,1]+90)/(Read.AF.iloc[0,1]+90), 'darkgreen')
# #ax20.title.set_text('Africa: 0N, 20W')

# plt.savefig(directory+'/plots/Figure_4.pdf', dpi = 300, bbox_inches='tight')


"""
FIGURE 5
Atmospheric Depth / SF variations

"""

# gl_std = [0.9989,1.0931,1.5614,2.3987]#5.3535]#,21.2553]
# gl_era40 = [0.9912,1.0938,1.5609,2.3980]#,5.3936]#,21.414]
# ec_std = [0.63111,0.68668,0.9593,1.4335]#,2.0954]#6.8824
# ec_era40 = [0.7162,0.7853,1.1308,1.7397]#],2.6392]#,9.1394]

# alt = [0,100,500,1000]


# plt.plot([0,3], [0,3], 'k-') #1:1 line
# plt.scatter(gl_std,gl_era40, c = alt, marker = 'o', cmap = 'plasma', vmin = 0, vmax = 2000, label = 'High latitude')
# plt.scatter(ec_std,ec_era40, c = alt, marker = 'x', cmap = 'plasma', vmin = 0, vmax = 2000, label = 'Equator')
# plt.ylabel('Scaling factor using standard atmosphere')
# plt.xlabel('Scaling factor using ERA40')

# cbar = plt.colorbar()
# cbar.set_label('Elevation', rotation = 270)

# plt.legend()
# plt.savefig(Read.directory+'/plots/Figure_5.svg', dpi = 300, bbox_inches='tight')


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
FIGURE 7
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
# # #FOR 40-65MA
# age250z = [2168943.0556243784,
#   1731005.0344781834,
#   2119077.805024399,
#   3881849.440059906,
#   2436197.9424115433,
#   3797236.6068173186,
#   3472222.080307602,
#   3754936.710317188,
#   4364932.21885633,
#   2746606.998669661,
#   3146264.2761222157,
#   3207892.7656139405,
#   3050462.8485466754,
#   8642809.117168196,
#   5907953.62561004,
#   9234609.800892549,
#   8070773.711728752,
#   7936892.007334684,
#   1920612.3647647523,
#   1901074.1548788303]


# age50z = [2170334.6280697524,
#   1732438.8213361914,
#   2120551.0420199977,
#   3881619.3118807958,
#   2437683.3133775983,
#   3797069.258840903,
#   3472679.6701391074,
#   3754779.866021021,
#   4363964.150665254,
#   2747978.614388317,
#   3147007.6957184975,
#   3208647.5851966664,
#   3051253.702529829,
#   8637940.055721866,
#   5904248.025958664,
#   9230537.334929865,
#   8065461.163987972,
#   7931561.535650669,
#   1921946.207495562,
#   1902414.7082181757]

# updated_texp_50 = []
# updated_texp_250 = []
# updated_texp_1ma = []
# updated_texp_past_50 = []
# updated_texp_past_250 = []
# error = []
# time = np.linspace(0,70,281)
# for i in range(len(age50)): #convert ages from [yr] to [Ma]
#     updated = age50[i]/10**6
#     updated_texp_50.append(updated) #Evenstar data
#     updated_250 = age250[i]/10**6 
#     updated_texp_250.append(updated_250) #this model
#     updated_1ma = age_1ma[i]/10**6
#     updated_texp_1ma.append(updated_1ma)
#     err = updated_250*0.05
#     error.append(err)
#     #updated_40 = age50z[i]/10**6
#     #updated_texp_past_50.append(updated_40) #Evenstar data
#     #updated_250z = age250z[i]/10**6 
#     #updated_texp_past_250.append(updated_250z) #this model

# plt.rcParams["figure.figsize"] = [4,3] #update figure size

# plt.plot(updated_texp_50[0:12],updated_texp_250[0:12], 'o', c = 'midnightblue', markersize=4, label = "50 ka bins")
# plt.plot(updated_texp_1ma[0:12], updated_texp_250[0:12], '^', c = 'darkmagenta', markersize = 4, label = "1 Ma bins")
# plt.errorbar(updated_texp_250[0:12], updated_texp_250[0:12],marker = 'x', c='cornflowerblue', markersize = 4, xerr=error[0:12], fmt="o", label = '250ka bins')
# plt.legend()
# plt.xlabel('Exposure Age [x] bin size')
# plt.ylabel('Exposure Age [250ka] bin size')
# plt.savefig(Read.directory+'/plots/binsize_comparison_scatter.png', dpi = 300, bbox_inches='tight')



"""
FIG A

"""




# sf_std = scaling_factor.Siteprod_df
# sf_std.to_csv(directory+'/plots/sf_std.csv') 
# sf_era = scaling_factor.Siteprod_df
# sf_era.to_csv(directory+'/plots/sf_era.csv') 

# time = np.linspace(0,70,281)
# sf_std = Read.sf_std
# sf_era = Read.sf_era

# difference = sf_std-sf_era

# plt.plot(time, difference.iloc[0][1:])
#plt.plot(time, difference.iloc[5][1:])
#plt.plot(time, difference.iloc[2][1:])

