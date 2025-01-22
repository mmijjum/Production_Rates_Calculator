
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
#import scaling_factor
# import neutron_spallation
# import proton_spallation
# import muons
import matplotlib.gridspec as gridspec


os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)

"""
EVERYTHING BELOW ARE TEXT FILES FOR PLOTS MADE IN MANUSCRIPT. 

"""

#FIGURE 2 TEXT FILES
IN = pd.read_csv(directory+'/text_for_plots/IN.csv')
SA = pd.read_csv(directory+'/text_for_plots/SA.csv')
GL = pd.read_csv(directory+'/text_for_plots/GL.csv')
AF = pd.read_csv(directory+'/text_for_plots/AF.csv')

sf_IN = pd.read_csv(directory+'/text_for_plots/sf_IN.csv')
sf_SA = pd.read_csv(directory+'/text_for_plots/sf_SA.csv')
sf_GL = pd.read_csv(directory+'/text_for_plots/sf_GL.csv')
sf_AF = pd.read_csv(directory+'/text_for_plots/sf_AF.csv')

sf_IN_const = pd.read_csv(directory+'/text_for_plots/sf_IN_const.csv')

sf_IN_tvlatonly = pd.read_csv(directory+'/text_for_plots/sf_india_tvlatonly.csv')

sf_IN_tvfieldonly = pd.read_csv(directory+'/text_for_plots/sf_india_tvfieldonly.csv')

#FIGURE X TEXT FILES

pn_cpx = pd.read_csv(directory+'/text_for_plots/pn_cpx.csv')
pp_cpx = pd.read_csv(directory+'/text_for_plots/pp_cpx.csv')
pn_qtz = pd.read_csv(directory+'/text_for_plots/pn_qtz.csv')
pp_qtz = pd.read_csv(directory+'/text_for_plots/pp_qtz.csv')

mean = pd.read_csv(directory+'/text_for_plots/sf_mean.csv')
upper = pd.read_csv(directory+'/text_for_plots/sf_upper.csv')
lower = pd.read_csv(directory+'/text_for_plots/sf_lower.csv')


chisq_neg33 = pd.read_csv(directory+'/text_for_plots/chisq_neg33.csv', header = None)
chisq_neg73 = pd.read_csv(directory+'/text_for_plots/chisq_neg73.csv', header = None)

chisq_neg1003 = pd.read_csv(directory+'/text_for_plots/chisq_neg1003.csv', header = None)
chisq_neg203 = pd.read_csv(directory+'/text_for_plots/chisq_neg203.csv', header = None)
chisq_neg153 = pd.read_csv(directory+'/text_for_plots/chisq_neg153.csv', header = None)
chisq_neg103 = pd.read_csv(directory+'/text_for_plots/chisq_neg103.csv', header = None)
chisq_neg53 = pd.read_csv(directory+'/text_for_plots/chisq_neg53.csv', header = None)
chisq_neg625 = pd.read_csv(directory+'/text_for_plots/chisq_neg6253.csv', header = None)

SLchisq_neg093 = pd.read_csv(directory+'/text_for_plots/SLchisq_neg093.csv', header = None)
SLchisq_neg083 = pd.read_csv(directory+'/text_for_plots/SLchisq_neg083.csv', header = None)
SLchisq_neg073 = pd.read_csv(directory+'/text_for_plots/SLchisq_neg073.csv', header = None)
SLchisq_neg063 = pd.read_csv(directory+'/text_for_plots/SLchisq_neg063.csv', header = None)
SLchisq_neg0653 = pd.read_csv(directory+'/text_for_plots/SLchisq_neg0653.csv', header = None)
SLchisq_neg53 = pd.read_csv(directory+'/text_for_plots/SLchisq_neg53.csv', header = None)


sf_std = pd.read_csv(directory+'/text_for_plots/sf_std.csv')
sf_era= pd.read_csv(directory+'/text_for_plots/sf_era.csv')

sf_50kyr = pd.read_csv(directory+'/text_for_plots/sf_50kyr.csv')
sf_250ka = pd.read_csv(directory+'/text_for_plots/sf_250ka.csv')
sf_1ma = pd.read_csv(directory+'/text_for_plots/sf_1ma.csv')

#Figure 5

NA_ERA40 =  pd.read_csv(directory+'/text_for_plots/Figure_8_NA_ERA40', header = None)
NA_STD = pd.read_csv(directory+'/text_for_plots/Figure_8_NA_STD', header = None)
NA_climate = pd.read_csv(directory+'/text_for_plots/Figure_8_NA_climate', header = None)
NA_climate_70 = pd.read_csv(directory+'/text_for_plots/Figure_8_NA_climate_70', header = None)

EC_ERA40 =  pd.read_csv(directory+'/text_for_plots/Figure_8_EC_ERA40', header = None)
EC_STD = pd.read_csv(directory+'/text_for_plots/Figure_8_EC_STD', header = None)
EC_climate = pd.read_csv(directory+'/text_for_plots/Figure_8_EC_climate', header = None)
EC_climate_70 = pd.read_csv(directory+'/text_for_plots/Figure_8_EC_climate_70', header = None)

Rc_full = pd.read_csv(directory+'/text_for_plots/Rc_full.csv', header = None)
Rc_half = pd.read_csv(directory+'/text_for_plots/Rc_half.csv', header = None)

sf_full = pd.read_csv(directory+'/text_for_plots/sf_full.csv', header = None)
sf_half = pd.read_csv(directory+'/text_for_plots/sf_half.csv', header = None)

x_tv = pd.read_csv(directory+'/text_for_plots/x_tv.csv', header = None)
x_c = pd.read_csv(directory+'/text_for_plots/x_c.csv', header = None)

#Libarkin artificial curves
lib5e3 = pd.read_csv(directory+'/text_for_plots/lib_5e3.csv', header = None)
lib1e3 = pd.read_csv(directory+'/text_for_plots/lib_1e3.csv', header = None)
lib5e4 = pd.read_csv(directory+'/text_for_plots/lib_5e4.csv', header = None)
lib3e3 = pd.read_csv(directory+'/text_for_plots_updated/lib_3e3.csv', header = None)
lib10e3 = pd.read_csv(directory+'/text_for_plots_updated/lib_10e3.csv', header = None)
lib20e3 = pd.read_csv(directory+'/text_for_plots_updated/lib_20e3.csv', header = None)

lib3e3_0 = pd.read_csv(directory+'/text_for_plots_updated/lib_3e3_0.csv', header = None)
lib3e4_0 = pd.read_csv(directory+'/text_for_plots_updated/lib_3e4_0.csv', header = None)
lib1e4_0 = pd.read_csv(directory+'/text_for_plots_updated/lib_1e4_0.csv', header = None)

Rc_const = pd.read_csv(directory+'/text_for_plots/Rc_const.csv', header = None)
Rc_tv_latonly = pd.read_csv(directory+'/text_for_plots/Rc_tv_latonly.csv', header = None)
Rc_tv_fieldonly = pd.read_csv(directory+'/text_for_plots/Rc_tv_fieldonly.csv', header = None)
Rc_tv_both = pd.read_csv(directory+'/text_for_plots/Rc_tv_both.csv', header = None)

midlats = pd.read_csv(directory+'/text_for_plots/midlats.csv', header = None)
poles = pd.read_csv(directory+'/text_for_plots/poles.csv', header = None)
equator = pd.read_csv(directory+'/text_for_plots/equator.csv', header = None)

era40_v_time = pd.read_csv(directory+'/text_for_plots/era40_v_time.csv', header = None)
std_v_time = pd.read_csv(directory+'/text_for_plots/std_v_time.csv', header = None)
valdes_v_time = pd.read_csv(directory+'/text_for_plots/valdes_v_time.csv', header = None)

era40_v_time_65N = pd.read_csv(directory+'/text_for_plots/era40_v_time_65N.csv', header = None)
std_v_time_65N = pd.read_csv(directory+'/text_for_plots/std_v_time_65N.csv', header = None)
valdes_v_time_65N = pd.read_csv(directory+'/text_for_plots/valdes_v_time_65N.csv', header = None)

era40_v_time_0N = pd.read_csv(directory+'/text_for_plots/era40_v_time.csv', header = None)
std_v_time_0N = pd.read_csv(directory+'/text_for_plots/std_v_time.csv', header = None)
valdes_v_time_0N = pd.read_csv(directory+'/text_for_plots/valdes_v_time.csv', header = None)

sf_sigma75 = pd.read_csv(directory+'/text_for_plots_updated/sf_sigma75.csv', header = None)
sf_sigma25= pd.read_csv(directory+'/text_for_plots_updated/sf_sigma25.csv', header = None)
sf_regular_sigma = pd.read_csv(directory+'/text_for_plots_updated/sf_regular_sigma.csv', header = None)
sf_constant_sigma= pd.read_csv(directory+'/text_for_plots_updated/sf_constant_sigma.csv', header = None)

sf_tvfieldonly_25sigma = pd.read_csv(directory+'/text_for_plots_updated/sf_tvfield_only_25sigma.csv', header = None)
sf_tvfieldonly_75sigma = pd.read_csv(directory+'/text_for_plots_updated/sf_tvfield_only_75sigma.csv', header = None)
sf_tvfieldonly_sigma = pd.read_csv(directory+'/text_for_plots_updated/sf_tvfield_only_sigma.csv', header = None)
sf_tvlatonly_sigma= pd.read_csv(directory+'/text_for_plots_updated/sf_tvlatonly_sigma.csv', header = None)


uplift_constant = pd.read_csv(directory+'/text_for_plots_updated/uplift_dunai_constant.csv', header=None)
uplift_tv= pd.read_csv(directory+'/text_for_plots_updated/tv_dunai.csv',header=None)

static_constant = pd.read_csv(directory+'/text_for_plots_updated/static_constant.csv', header=None)
static_tv = pd.read_csv(directory+'/text_for_plots_updated/static_tv.csv', header=None)

uplift_constant = pd.read_csv(directory+'/text_for_plots_updated/uplift_dunai_constant.csv', header=None)
uplift_tv= pd.read_csv(directory+'/text_for_plots_updated/tv_dunai.csv',header=None)

static_constant = pd.read_csv(directory+'/text_for_plots_updated/static_constant.csv', header=None)
static_tv = pd.read_csv(directory+'/text_for_plots_updated/static_tv.csv', header=None)
####

uplift_tv_sf = pd.read_csv(directory+'/text_for_plots_updated/dunai_uplift_sf.csv',header=None)

static_tv_sf = pd.read_csv(directory+'/text_for_plots_updated/dunai_static_sf.csv', header=None)
###
uplift_const_sf = pd.read_csv(directory+'/text_for_plots_updated/dunai_uplift_sf_const.csv',header=None)

static_const_sf = pd.read_csv(directory+'/text_for_plots_updated/dunai_static_sf_const.csv', header=None)



###
# tv = pd.read_csv(directory+'/text_for_plots_updated/sf_static_v_uplift.csv',header=None)

# const = pd.read_csv(directory+'/text_for_plots_updated/sf_static_v_uplift_const.csv', header=None)

##

# tempvals_uplift = pd.read_csv(directory+'/text_for_plots_updated/tempvals_uplift.csv',header=None)
# tempvals_static = pd.read_csv(directory+'/text_for_plots_updated/tempvals_static.csv',header=None)
# tempvals_uplift_const= pd.read_csv(directory+'/text_for_plots_updated/tempvals_uplift_const.csv',header=None)
# tempvals_static_const = pd.read_csv(directory+'/text_for_plots_updated/tempvals_static_const.csv',header=None)
# ###

# ant_ERA40 = pd.read_csv(directory+'/text_for_plots/antarctica_ERA40.csv', header=None)
# ant_STD = pd.read_csv(directory+'/text_for_plots/antarctica_STD.csv', header=None)
# ant_VALDES = pd.read_csv(directory+'/text_for_plots/antarctica_valdes.csv', header=None)


# time = np.arange(0,70.1,0.25)
# plt.plot(time,ant_ERA40.iloc[1][1:], '--', c='black', label = 'ERA40')
# plt.plot(time,ant_STD.iloc[1][1:],  c='black',label = 'Standard')
# plt.plot(time,ant_VALDES.iloc[1][1:],'-.', c='black', label = 'Valdes et al. (2021)')
# plt.xlabel('Time (Ma)', fontsize = 14)
# plt.ylabel('Pressure (hPa)', fontsize = 14)
# plt.legend()
#plt.savefig(directory+'/plots_updated/Antarctica_pressure.png', dpi = 300, bbox_inches='tight')



"""
Figure 6
Climate Data
"""
# elevations = np.arange(0,5001,500)
# ERA40 = [1036.622906,
# 978.049912,
# 922.219431 ,
# 869.030156,
# 818.383504 ,
# 770.183563 ,
# 724.337055,
# 680.753283,
# 639.344096,
# 600.023836,
# 562.709303]

# standard = [1033.227237,
# 973.417892,
# 916.443484,
# 862.200037,
# 810.586253,
# 761.503465,
# 714.855602,
# 670.549150,
# 628.493115,
# 588.598980,
# 550.780674]

# VALDES = [1028.118847,
# 970.446696,
# 915.455137,
# 863.045885,
# 813.123272,
# 765.594208,
# 720.368134,
# 677.356984,
# 636.475138,
# 597.639386,
# 560.768879]
# era40 = []
# valdes = []
# # for i in range(len(ERA40)):
# #     era40.append(standard[i]-ERA40[i])
# #     valdes.append(standard[i]-VALDES[i])

# # plt.plot(elevations, era40, 'black', label = 'standard atmosphere - ERA40')
# # #plt.plot(elevations, standard)
# # plt.plot(elevations,valdes, '--', c='black', label = 'standard atmosphere - Valdes et al. (2021)')

# # plt.ylabel('Atmospheric depth difference (g/cm${^2}$)', fontsize = 11)
# # plt.xlabel('Elevation (MASL)', fontsize = 11)
# # plt.legend()
# # plt.savefig(directory+'/plots_updated/Figure_0.svg', dpi = 300, bbox_inches='tight')

# time = np.arange(0,70.25,0.25)
# era40 = era40_v_time[1:]
# std = std_v_time[1:]
# valdes =valdes_v_time[1:]

# plt.plot(time,era40.iloc[0][1:],'black', label = 'ERA40')
# plt.plot(time,valdes.iloc[0][1:],'--',c='black', label = 'Valdes et al. (2021)')
# plt.plot(time,std.iloc[0][1:],'-.',c='black' ,label = 'standard atmosphere')

# plt.legend()
# plt.xlabel('Time (Ma)', fontsize = 11)
# plt.ylabel('Atmospheric depth (g/cm${^2}$)', fontsize = 11)

# plt.savefig(directory+'/plots_updated/Figure_0B.svg', dpi = 300, bbox_inches='tight')

##POLAR LATITUDE
elevations = np.arange(0,5001,500)
ERA40 = [1027.865274,
966.526320,
908.320921,
853.116414,
800.784568,
751.201482,
704.247471,
659.806967,
617.768415,
578.024167,
540.470389]

standard = [1033.227237,
973.417892,
916.443484,
862.200037,
810.586253,
761.503465,
714.855602,
670.549150,
628.493115,
588.598980,
550.780674]

VALDES = [1018.421318,
958.209433,
901.044745,
846.799465,
795.350034,
746.577022,
700.365027,
656.602575,
615.182025,
575.999470,
538.954646]
era40 = []
valdes = []

for i in range(len(ERA40)):
    era40.append(standard[i]-ERA40[i])
    valdes.append(standard[i]-VALDES[i])

# plt.plot(elevations, era40, 'darkgreen', label = 'standard atmosphere - ERA40')
# #plt.plot(elevations, standard)
# plt.plot(elevations,valdes, '--', c='darkgreen', label = 'standard atmosphere - Valdes et al. (2021)')

# plt.ylabel('Atmospheric depth difference (g/cm${^2}$)', fontsize = 11)
# plt.xlabel('Elevation (MASL)', fontsize = 11)
# plt.legend()
# plt.savefig(directory+'/plots_updated/Figure_0_65N.svg', dpi = 300, bbox_inches='tight')




# time = np.arange(0,70.25,0.25)
# era40 = era40_v_time_65N[1:]
# std = std_v_time_65N[1:]
# valdes =valdes_v_time_65N[1:]

# plt.plot(time,era40.iloc[0][1:],'darkgreen', label = 'ERA40')
# plt.plot(time,valdes.iloc[0][1:],'--',c='darkgreen', label = 'Valdes et al. (2021)')
# plt.plot(time,std.iloc[0][1:],'-.',c='darkgreen' ,label = 'standard atmosphere')

# plt.legend()
# plt.xlabel('Time (Ma)', fontsize = 11)
# plt.ylabel('Atmospheric depth (g/cm${^2}$)', fontsize = 11)

# plt.savefig(directory+'/plots_updated/Figure_0B_65N.svg', dpi = 300, bbox_inches='tight')



##EQUATORIAL LATITUDE
# elevations = np.arange(0,5001,500)
# ERA40 = [1032.239182,
# 974.359983,
# 919.169175,
# 866.568295,
# 816.461496,
# 768.755509,
# 723.359599,
# 680.185521,
# 639.147478,
# 600.162083,
# 563.148313]

# standard = [1033.227237,
# 973.417892,
# 916.443484,
# 862.200037,
# 810.586253,
# 761.503465,
# 714.855602,
# 670.549150,
# 628.493115,
# 588.598980,
# 550.780674]

# VALDES = [1023.241311,
# 966.325165,
# 912.031334,
# 860.264558,
# 810.932088,
# 763.943650,
# 719.211397,
# 676.649877,
# 636.175989,
# 597.708941,
# 561.170215]
# era40 = []
# valdes = []

# for i in range(len(ERA40)):
#     era40.append(standard[i]-ERA40[i])
#     valdes.append(standard[i]-VALDES[i])

# # plt.plot(elevations, era40, 'cornflowerblue', label = 'standard atmosphere - ERA40')
# # #plt.plot(elevations, standard)
# # plt.plot(elevations,valdes, '--', c='cornflowerblue', label = 'standard atmosphere - Valdes et al. (2021)')

# # plt.ylabel('Atmospheric depth difference (g/cm${^2}$)', fontsize = 11)
# # plt.xlabel('Elevation (MASL)', fontsize = 11)
# # plt.legend()
# # plt.savefig(directory+'/plots_updated/Figure_0_0N.svg', dpi = 300, bbox_inches='tight')




# time = np.arange(0,70.25,0.25)
# era40 = era40_v_time_0N[1:]
# std = std_v_time_0N[1:]
# valdes =valdes_v_time_0N[1:]

# plt.plot(time,era40.iloc[0][1:],'cornflowerblue', label = 'ERA40')
# plt.plot(time,valdes.iloc[0][1:],'--',c='cornflowerblue', label = 'Valdes et al. (2021)')
# plt.plot(time,std.iloc[0][1:],'-.',c='cornflowerblue' ,label = 'standard atmosphere')

# plt.legend()
# plt.xlabel('Time (Ma)', fontsize = 11)
# plt.ylabel('Atmospheric depth (g/cm${^2}$)', fontsize = 11)

# plt.savefig(directory+'/plots_updated/Figure_0B_0N.svg', dpi = 300, bbox_inches='tight')

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
Figure 5
Comparing bin size

To run in excel:
    1) In inputs - sample India site (23N), sea level, pyroxene
    2) Need to save the scaling factor dataframe for the different temporal resolutions. You can change temporal resolution in MCADAM script.
"""

##These lines will re-make the saved SF dataframes. DO NOT RUN IF YOU'RE NOT CHANGING IT#

## sf_50kyr = scaling_factor.Siteprod_df.iloc[0]
## sf_50kyr.to_csv(directory+'/text_for_plots/sf_50kyr.csv')

## sf_1ma = scaling_factor.Siteprod_df.iloc[0]
## sf_1ma.to_csv(directory+'/text_for_plots/sf_1ma.csv') 

## sf_250ka= scaling_factor.Siteprod_df.iloc[0]
## sf_250ka.to_csv(directory+'/text_for_plots/sf_250ka.csv') 

#Start uncommenting:
time1 =  np.arange(2,70.05,0.05)
time2=  np.arange(2,70.05,0.25)

x_temp = sf_50kyr.iloc[:,1]
x = x_temp[41::] # remove first 2 Ma post LSDn update
plt.rcParams["figure.figsize"] = [5,4] #update figure size 


plt.plot(time1,sf_250ka.iloc[:,1].repeat(5).reset_index(drop=True).iloc[4:].reset_index(drop=True)/x, c = 'gray',  label = 'SF(250 kyr) : SF(50 kyr)')
plt.plot(time2, sf_250ka.iloc[:,1]/Read.sf_1ma.iloc[:,1].repeat(4).reset_index(drop=True).iloc[3:].reset_index(drop=True), c = 'darkgreen', label = 'SF(250 kyr): SF(1 Myr)')
plt.xlabel('Time (Ma)', fontsize = 13)
plt.ylabel('Scaling factor ratio', fontsize = 13)
plt.legend(loc = 'lower right')
plt.xlim(0,70)
plt.axhline(y = 1, color = 'black', lw = 3)
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
# GL_STD_sf.to_csv(directory+'/text_for_plots/Figure_8_NA_STD')


# x = scaling_factor.Siteprod_df
# EC_STD_sf = x[0][17::]
# EC_STD_sf.to_csv(directory+'/text_for_plots/Figure_8_EC_STD')

# x = scaling_factor.Siteprod_df
# NA_ERA40_sf = x[0][0:17]
# NA_ERA40_sf.to_csv(directory+'/text_for_plots/Figure_8_NA_ERA40')

# x = scaling_factor.Siteprod_df
# EC_ERA40_sf = x[0][17::]
# EC_ERA40_sf.to_csv(directory+'/text_for_plots/Figure_8_EC_ERA40')


#temporarily: change time to 3 Ma bc there's some bug where it'll glitch if time is <2ma
# x = scaling_factor.Siteprod_df
# NA_climate_sf = x[0][0:17]
# NA_climate_sf.to_csv(directory+'/text_for_plots/Figure_8_NA_climate')

# x = scaling_factor.Siteprod_df
# EC_climate_sf = x[0][17::]
# EC_climate_sf.to_csv(directory+'/text_for_plots/Figure_8_EC_climate')


##when running below, change time --> 65-70 Ma
# x = scaling_factor.Siteprod_df
# NA_climate_sf_70 = x[20][0:17]
# NA_climate_sf_70.to_csv(directory+'/text_for_plots/Figure_8_NA_climate_70')

# x = scaling_factor.Siteprod_df
# EC_climate_sf_70 = x[20][17::]
# EC_climate_sf_70.to_csv(directory+'/text_for_plots/Figure_8_EC_climate_70')

#START RUN#
# from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,mark_inset)
# import matplotlib.patches as patches


# alt = np.arange(0,5001,500)


# fig, ax1 = plt.subplots()
# ax1.set_aspect('equal')
# plt.scatter(NA_STD.iloc[10:12][1],NA_climate.iloc[10:12][1],  linewidth = 2,  label = 'valdes', c = '#014636')
# #plt.scatter(EC_STD.iloc[6:12][1],EC_climate.iloc[6:12][1],   linewidth = 2,  label = 'Equator: 0N, 70W' , c = '#67a9cf')
# plt.grid()
# ax1.set_ylabel('Scaling factor')
# ax1.set_xlabel('Scaling factor using standard atmosphere')
# ax1.legend(loc=0)
# ax1.plot([26,40], [26,40], 'k-')

# # # ax1.set_ylim(0,46)
# # # ax1.set_xlim(0,46)

# # # rect = patches.Rectangle((0, 0), 5, 5, linewidth=1, edgecolor='k', facecolor='none')
# # # ax1.add_patch(rect)

# # # left, bottom, width, height = [0.53, 0.2, 0.20, 0.25] # modify to move the inset curve and change its size
# # # ax2 = fig.add_axes([left, bottom, width, height])
# # # ax2.plot(NA_STD.iloc[1:12][1],NA_climate.iloc[1:12][1], 'x-',  linewidth = 2, markersize = 6, label = 'High latitude: 65N,130W ', c = '#014636')
# # # ax2.plot(EC_STD.iloc[1:12][1],EC_climate.iloc[1:12][1], 'x-',  linewidth = 2,   markersize = 6,label = 'Equator: 0N, 70W' , c = '#67a9cf')

# # # ax2.set_xlim(0,5)
# # # ax2.set_ylim(0,5)
# # # ax2.set_xticks([0, 2,4])
# # # ax2.set_yticks([0,2,4])
# # # ax2.tick_params(axis='both', which='major', labelsize=8)

# plt.scatter(NA_STD.iloc[10:12][1],NA_ERA40.iloc[10:12][1], c='pink', linewidth = 2, label = 'era40')
# #ax1.plot(EC_STD.iloc[1:12][1],EC_ERA40.iloc[1:12][1], 'o-',   linewidth = 2,  markersize = 4,label = 'Equator: 0N, 70W' , c = '#67a9cf')
# plt.legend()

# ax1.legend(loc=0)
# ax1.set_ylim(0,46)
# ax1.set_xlim(0,46)

# rect = patches.Rectangle((0, 0), 5, 5, linewidth=1, edgecolor='k', facecolor='none')
# ax1.add_patch(rect)

# left, bottom, width, height = [0.53, 0.2, 0.20, 0.25] # modify to move the inset curve and change its size
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(NA_STD.iloc[1:12][1],NA_ERA40.iloc[1:12][1], 'o-',  linewidth = 2, markersize = 4, label = 'High latitude: 65N,130W ', c = '#014636')
# ax2.plot(EC_STD.iloc[1:12][1],EC_ERA40.iloc[1:12][1], 'o-',  linewidth = 2,   markersize = 4,label = 'Equator: 0N, 70W' , c = '#67a9cf')

# ax2.set_xlim(0,5)
# ax2.set_ylim(0,5)
# ax2.set_xticks([0, 2,4])
# ax2.set_yticks([0,2,4])
# ax2.tick_params(axis='both', which='major', labelsize=8)
# plt.grid()
#plt.savefig(Read.directory+'/plots_updated/Figure_8A_UPDATED.svg', dpi = 300, bbox_inches='tight')


# fig = plt.figure(figsize=(4,4))

# alt = np.arange(0,5001,500)


# fig, ax1 = plt.subplots()
# ax1.set_aspect('equal')
# ax1.plot(Read.NA_STD.iloc[1:12][1],Read.NA_climate_70.iloc[1:12][1], 'x-',  linewidth = 2, markersize = 6, label = 'High latitude: 75N,40E ', c = '#014636')
# ax1.plot(Read.EC_STD.iloc[1:12][1],Read.EC_climate_70.iloc[1:12][1], 'x-',   linewidth = 2,  markersize = 6,label = 'Equator: 0N, 78E' , c = '#67a9cf')


# #ax1.legend(loc=0)
# ax1.set_ylim(0,46)
# ax1.set_xlim(0,46)
# plt.grid()
# rect = patches.Rectangle((0, 0), 5, 5, linewidth=1, edgecolor='k', facecolor='none')
# ax1.add_patch(rect)

# left, bottom, width, height = [0.53, 0.2, 0.20, 0.25] # modify to move the inset curve and change its size
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(Read.NA_STD.iloc[1:12][1],Read.NA_climate_70.iloc[1:12][1], 'x-',  linewidth = 2, markersize = 6, label = 'High latitude: 75N,40E ', c = '#014636')
# ax2.plot(Read.EC_STD.iloc[1:12][1],Read.EC_climate_70.iloc[1:12][1], 'x-',  linewidth = 2,   markersize = 6,label = 'Equator: 0N, 78E' , c = '#67a9cf')

# ax2.set_xlim(0,5)
# ax2.set_ylim(0,5)
# ax2.set_xticks([0, 2,4])
# ax2.set_yticks([0,2,4])
# ax2.tick_params(axis='both', which='major', labelsize=8)

# ax1.plot(Read.NA_STD.iloc[1:12][1],Read.NA_ERA40.iloc[1:12][1], 'o-',  linewidth = 2, markersize = 4, label = 'High latitude: 75N,40E ', c = '#014636')
# ax1.plot(Read.EC_STD.iloc[1:12][1],Read.EC_ERA40.iloc[1:12][1], 'o-',   linewidth = 2,  markersize = 4,label = 'Equator: 0N, 78E' , c = '#67a9cf')


# #ax1.legend(loc=0)
# ax1.set_ylim(0,46)
# ax1.set_xlim(0,46)

# rect = patches.Rectangle((0, 0), 5, 5, linewidth=1, edgecolor='k', facecolor='none')
# ax1.add_patch(rect)

# left, bottom, width, height = [0.53, 0.2, 0.20, 0.25] # modify to move the inset curve and change its size
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(Read.NA_STD.iloc[1:12][1],Read.NA_ERA40.iloc[1:12][1], 'o-',  linewidth = 2, markersize = 4, label = 'High latitude: 75N,40E ', c = '#014636')
# ax2.plot(Read.EC_STD.iloc[1:12][1],Read.EC_ERA40.iloc[1:12][1], 'o-',  linewidth = 2,   markersize = 4,label = 'Equator: 0N, 78E' , c = '#67a9cf')

# ax2.set_xlim(0,5)
# ax2.set_ylim(0,5)
# ax2.set_xticks([0, 2,4])
# ax2.set_yticks([0,2,4])
# ax2.tick_params(axis='both', which='major', labelsize=8)
# plt.grid()
# plt.savefig(Read.directory+'/plots_updated/Figure_8B_UPDATED.svg', dpi = 300, bbox_inches='tight')


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

# sig75 = sf_sigma75.iloc[1][1:]
# sig25 = sf_sigma25.iloc[1][1:]
# median =sf_regular_sigma.iloc[1][1:]
# const = sf_constant_sigma.iloc[1][1:]

# tvfield_25 = sf_tvfieldonly_25sigma.iloc[1][1:]
# tvfield_75 = sf_tvfieldonly_75sigma.iloc[1][1:]
# tvfield_avg = sf_tvfieldonly_sigma.iloc[1][1:]
# tvlat = sf_tvlatonly_sigma.iloc[1][1:]

# # # # #BEGIN
# time = np.linspace(0,70,281)
# f = plt.figure(figsize=(15,6))
# ax = f.add_subplot(121)
# ax2 = f.add_subplot(122)
# ax.plot(time,median, linewidth = 2, c = '#016c59',label = 'time-varying field and latitude')
# ax.plot(time,const, '--',linewidth = 2.5,c = 'black', label = 'constant field and latitude')
# ax.fill_between(time, sig75, median,  color = '#a6bddb', alpha = 0.5)
# ax.fill_between(time, median, sig25, color =  '#a6bddb', alpha = 0.5)

# ax.set_xlim(0,70)
# ax.set_ylim(0.45,0.95)

# ax.plot(time, sig25, '#a6bddb')
# ax.plot(time,sig75,'#a6bddb')

# ax.vlines(66.052, 0.45, 0.95, linewidth = 2.5)
# ax.set_xlabel('Time (Ma)', fontsize = 15)
# ax.set_ylabel('Scaling Factor', fontsize = 15)
# ax.legend(loc = 'lower left', fontsize =13)

# ax2.plot(time,tvfield_avg, linewidth = 2.5,c = '#014636',label = 'time-varying field, constant latitude')
# ax2.plot(time,tvlat, '--',linewidth = 2.5,c = '#67a9cf', label = 'constant field, time-varying latitude')
# ax2.plot(time, tvfield_25, '#a6bddb')
# ax2.plot(time,tvfield_75,'#a6bddb')
# ax2.fill_between(time, tvfield_75, tvfield_avg,  color = '#a6bddb', alpha = 0.5)
# ax2.fill_between(time, tvfield_avg, tvfield_25, color =  '#a6bddb', alpha = 0.5)

# ax2.set_ylim(0.45,0.95)
# ax2.vlines(66.052, 0.45, 0.95, linewidth = 2.5)


# ax2.set_xlim(0,70)
# ax2.vlines(66.052, 0.50, 0.95,linewidth = 2.5)
# ax2.set_xlabel('Time (Ma)', fontsize = 15)
# ax2.legend(loc = 'lower left', fontsize = 13)
# plt.setp(ax2.get_yticklabels(), visible=False)
# plt.savefig(directory+'/plots_updated/Figure_8.pdf', dpi = 300, bbox_inches='tight')




# """

# FIGURE 9
# EVENSTAR DATASET

# """
# exp_ages_time_varying = [123764.70513124338,
#   999950.5881550129,
#   2809842.973923239,
#   1437709.5492099412,
#   1597412.2430487473,
#   2306374.286561611,
#   2811905.9936664747,
#   5205562.436422755,
#   804638.461019477,
#   1027097.292649448,
#   3243379.122532165,
#   5272036.169905982,
#   4814983.263867728,
#   5004348.192627103,
#   5798579.472430228,
#   3801760.946131991,
#   4043021.3848517216,
#   4190083.484928454,
#   3974482.253474694,
#   10867014.793712351,
#   7457939.823871471,
#   11504457.347719094,
#   10174352.548386587,
#   10034978.260752263,
#   2501601.075564036,
#   2442727.0967175965,
#   1917534.0170423328,
#   2085500.9806046379]

# exp_ages_constant= [114228.05791045129,
#   915946.3467122873,
#   2738524.329526318,
#   1337892.329096456,
#   1492716.4114716016,
#   2237688.836019829,
#   2737022.7304163054,
#   5020979.568684665,
#   730821.6829189667,
#   938896.583164952,
#   3152139.0098045915,
#   5070621.350176061,
#   4631739.899436452,
#   4825366.17480535,
#   5623508.560978162,
#   3695269.4978240505,
#   3950957.8542163633,
#   4083156.2323068194,
#   3882028.5922924485,
#   11323751.27282418,
#   7584169.781085953,
#   12086889.969182406,
#   10509988.870293442,
#   10352712.57702584,
#   2442963.7472036444,
#   2385523.147630269,
#   1834586.2395702424,
#   2009533.8964364766]


# exp_neon_tv = [893171.6042412941,
#   875306.5594295587,
#   257829.28728460363,
#   113891.21526679581,
#   302435.37394875474,
#   209844.55595393197,
#   247835.1756155724,
#   34726.29393051977,
#   2083043.0180226536,
#   2175843.36519608,
#   3066251.27098606,
#   6014867.565018561,
#   2981554.3122289614,
#   2154086.2918152586]



# exp_neon_const = [807709.0575222793,
#   791014.1341699025,
#   236324.26155541767,
#   104479.46561747165,
#   276128.5809262426,
#   193361.72654931567,
#   228368.15645606536,
#   31825.841032641998,
#   1995778.20589343,
#   2094232.3820456,
#   2967381.6952170026,
#   5867371.194278396,
#   2883651.1637155297,
#   2071981.4245235054]

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
    

# exp_ages_dunai =[15763888.284884367,
#   17076439.897954084,
#   13374151.996150088,
#   23883596.012271866,
#   15918675.374240698,
#   17660422.55280363,
#   11541398.822023429,
#   7955981.4814617345,
#   17571600.49200227,
#   11441483.741217585,
#   14631506.693484198,
#   18550832.147374067,
#   14064530.42373193,
#   69285.95320017869,
#   130873.53703242909,
#   88532.05131133944]
                         
# exp_ages_dunai_const = [17162844.505560774,
#   18533186.489756998,
#   14294878.008155053,
#   27155794.989833537,
#   17338807.22884569,
#   19258940.393708486,
#   12089588.878998378,
#   8055902.3665621765,
#   19143774.462789685,
#   11971567.401384685,
#   15860207.587445626,
#   20421186.017621815,
#   15138254.28251518,
#   64006.15963224702,
#   120900.58338250335,
#   81785.64841898231]



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


# fig = plt.figure(figsize=(14,9))


# gs = gridspec.GridSpec(2,2)

# ax1=fig.add_subplot(gs[:,0])
# ax2=fig.add_subplot(gs[0,1])
# ax3=fig.add_subplot(gs[1,1])


# ax2.set_ylim(-3.5,0.5)
# ax2.set_xlim(2,30)
# ax2.hlines(0,2,30)

# ax2.plot(updated_texp_const[0:4] ,diff_tv_pyx[0:4], 'o', c = 'limegreen', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 2')
# ax2.plot(updated_texp_const[4:17],diff_tv_pyx[4:17], 'o', c = 'royalblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 3')
# ax2.plot(updated_texp_const[17:26],diff_tv_pyx[17:26], 'o', c = 'deepskyblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 5')

# # ax2.plot(updated_neon_const[0:9], diff_tv_qtz[0:9], 's', c ='teal', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 1')
# # ax2.plot(updated_neon_const[9:11], diff_tv_qtz[9:11], 's', c='limegreen', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 2')
# # ax2.plot(updated_neon_const[11:14], diff_tv_qtz[11:14], 's', c='royalblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 3')
# # ax2.plot(updated_neon_const[13], diff_tv_qtz[13], 's', c='deepskyblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 5')

# # ax2.plot(updated_dunai_const[0:5], diff_tv_dunai[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# # ax2.plot(updated_dunai_const[5:9], diff_tv_dunai[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# # ax2.plot(updated_dunai_const[9:13],  diff_tv_dunai[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# # ax2.plot(updated_dunai_const[13:15], diff_tv_dunai[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# # ax2.plot(updated_dunai_const[15:16], diff_tv_dunai[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# ax2.set_ylabel('Exposure age difference (Ma)', fontsize = 14)
# ax2.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)

# ax3.set_xlim(2,30)
# ax3.set_ylim(-14,7.5)
# ax3.plot(updated_texp_const[0:4] ,perdif_ev[0:4], 'o', c = 'limegreen', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 2')
# ax3.plot(updated_texp_const[4:17],perdif_ev[4:17], 'o', c = 'royalblue', alpha = 0.7,markersize = 8, label = '$^{3}He$ - Surface 3')
# ax3.plot(updated_texp_const[17:26],perdif_ev[17:26], 'o', c = 'deepskyblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 5')

# # ax3.plot(updated_neon_const[0:9], perdifneon[0:9], 's', c ='teal', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 1')
# # ax3.plot(updated_neon_const[9:11], perdifneon[9:11], 's', c='limegreen', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 2')
# # ax3.plot(updated_neon_const[11:14], perdifneon[11:14], 's', c='royalblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 3')
# # ax3.plot(updated_neon_const[13], perdifneon[13], 's', c='deepskyblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 5')

# # ax3.plot(updated_dunai_const[0:5], perdif[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# # ax3.plot(updated_dunai_const[5:9], perdif[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# # ax3.plot(updated_dunai_const[9:13],  perdif[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# # ax3.plot(updated_dunai_const[13:15], perdif[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# # ax3.plot(updated_dunai_const[15:16], perdif[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# ax3.set_ylabel('Exposure age percent difference (%)', fontsize = 14)
# ax3.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)
# ax3.hlines(0,2,30)



# ax1.set_xlim(2,30)
# ax1.plot([2,30], [2,30], 'k-')
# # ax1.plot(updated_neon_const[0:9], updated_neon_tv[0:9],  's', c = 'teal', alpha = 0.7,markersize = 8)
# # ax1.plot(updated_neon_const[9:11], updated_neon_tv[9:11],  's', c='limegreen', alpha = 0.7,markersize = 8)
# # ax1.plot(updated_neon_const[11:14], updated_neon_tv[11:14], 's', c='royalblue',alpha = 0.7, markersize = 8)
# # ax1.plot(updated_neon_const[13], updated_neon_tv[13],  's', c='deepskyblue', alpha = 0.7,markersize = 8)

# ax1.plot(updated_texp_const[0:4],updated_texp_tv[0:4], 'o', c='limegreen', alpha = 0.7,markersize = 8)
# ax1.plot(updated_texp_const[4:17],updated_texp_tv[4:17], 'o', c = 'royalblue', alpha = 0.7,markersize = 8)
# ax1.plot(updated_texp_const[17:26],updated_texp_tv[17:26], 'o', c = 'deepskyblue',alpha = 0.7, markersize = 8)

# # ax1.plot(updated_dunai_const[0:5],updated_dunai[0:5], 's', c='midnightblue',alpha = 0.7, markersize = 8)
# # ax1.plot(updated_dunai_const[5:9],updated_dunai[5:9], 's', c='purple',alpha = 0.7,markersize =8)
# # ax1.plot(updated_dunai_const[9:13],updated_dunai[9:13], 's', c='mediumpurple',alpha = 0.7, markersize = 8)
# # ax1.plot(updated_dunai_const[13:15],updated_dunai[13:15], 's', c='skyblue', alpha = 0.7,markersize =8)
# # ax1.plot(updated_dunai_const[15:16],updated_dunai[15:16], 's', c='hotpink', alpha = 0.7,markersize = 8)
# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 14)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)

# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 13)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 13)
#plt.savefig(Read.directory+'/plots_updated/old_fig_9.png', dpi = 300, bbox_inches='tight')

"""
FIG 10
LIBARKIN DATASET

# """
# tempvals = []
# tempvalsmu = []
# lambdasp = 160 #effective attenuation length for spallation in at/g/yr = 160 g/cm2 Balco 2008, gosee and phillips 2001
# rho = 2.32
# erosion = (20*(10**-3)) #in cm/yr
# dt2 = 250000
# dt1 = 49000
# dt3 = 201000

# texp_bin1 = [10000,50000,100000,150000,200000,250000]
# texp_bin2 = [300000,350000,400000,450000,500000]
# texp_bin3 = [510000,520000,530000,540000,550000,600000]

# z0 = np.arange(0,102,2)
# concentrations = []
# a = 0.01036
# b = -9.697e-6
# htemp = atm_depth.x
# htemp[:] = htemp.values[:, ::-1] #reverse to get in correct time sequence
# h = (htemp) / 1.019716 # convert back from atmospheric depth to pressure
# lambdamu = 1 / (a + b*h) #muon attenuation length, equation 8 in Balco (@017)    
    
# for i in range(len(z0)):
#     Cspall = (shielding.S_thick[0][0]*(neutron_spallation.pn_df[0][i] + proton_spallation.pp_df[0][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt1)) + (shielding.S_thick[0][0]*(neutron_spallation.pn_df[1][i] + proton_spallation.pp_df[1][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt2))+ (shielding.S_thick[0][0]*(neutron_spallation.pn_df[2][i] + proton_spallation.pp_df[2][i])) / ((rho * erosion) / lambdasp) * np.exp(-(rho*z0[i]/lambdasp)) * (1-np.exp(-(rho*erosion/lambdasp)*dt3))
#     Cmuons = muons.pmuons_df[0][i] / ((rho * erosion) / lambdamu[0][i]) * np.exp(-(rho*z0[i]/lambdamu[0][i])) * (1-np.exp(-(rho*erosion/lambdamu[0][i])*dt1)) + muons.pmuons_df[1][i] / ((rho * erosion) / lambdamu[1][i]) * np.exp(-(rho*z0[i]/lambdamu[1][i])) * (1-np.exp(-(rho*erosion/lambdamu[1][i])*(dt2))) + muons.pmuons_df[2][i] / ((rho * erosion) / lambdamu[2][i]) * np.exp(-(rho*z0[i]/lambdamu[2][i])) * (1-np.exp(-(rho*erosion/lambdamu[2][i])*(dt3))) 
#     Ctot = Cspall + Cmuons
#     concentrations.append(Cspall + Cmuons)
# np.savetxt(directory+"/text_for_plots_updated/lib_20e3.csv", 
#             concentrations,
#             delimiter =", ", 
#             fmt ='% s')

# z0 = np.arange(0,102,2)
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
# plt.savefig(Read.directory+'/plots_updated/libarkin.pdf', dpi = 300, bbox_inches='tight')
"""
LIBARKIN V2

"""


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

# plt.plot(time,atm_2.iloc[0], '--', label = 'Climate data')
# plt.plot(time,atm_1.iloc[0],'-.', label = 'Standard atmosphere')
# plt.plot(time,atm_0.iloc[0], label = 'ERA40')
# plt.xlabel('Time (Ma)')
# plt.ylabel('Atmospheric Depth (g/cm2)')
# plt.legend()
# plt.savefig(Read.directory+'/plots/atm_depth_comparison_elevations.png', dpi = 300, bbox_inches='tight')

# """

# FIGURE 9
# ATACAMA DATASET
# UPLIFT

# """

# exp_ages_tv_uplift = [123764.70513124338,
#   1011721.3154752883,
#   2934967.3752608323,
#   1463523.9210383103,
#   1627495.22304928,
#   2379409.3664045176,
#   2933413.659577405,
#   5628517.284506589,
#   812312.3744830841,
#   1040974.4429489293,
#   3406667.4156682994,
#   5671102.087487514,
#   5156666.159387262,
#   5410559.460795641,
#   6243713.399592858,
#   4001738.9914335134,
#   4341101.961751757,
#   4506959.208549344,
#   4252356.466299975,
#   13049595.996737225,
#   8477795.64572071,
#   14031203.72585432,
#   12056498.933110522,
#   11845543.948775323,
#   2609554.820853299,
#   2546577.5222186195,
#   1976683.9716491036,
#   2154513.7377854045]

# exp_ages_constant_uplift = [114228.05791045129,
#   925683.4924972189,
#   2851567.1078528627,
#   1361983.204932554,
#   1520896.4900682927,
#   2308382.7616215744,
#   2846276.7023067386,
#   5421535.293460598,
#   737177.1652444504,
#   950281.2655596972,
#   3302153.253938878,
#   5449697.376729284,
#   4945321.536036997,
#   5206286.30833472,
#   6154030.817246244,
#   3885848.9901233376,
#   4214183.486464434,
#   4358970.864916163,
#   4130737.5225037164,
#   13950922.95605886,
#   8641300.496771319,
#   15175840.066833192,
#   12730664.759090213,
#   12482905.637024231,
#   2540004.4605131424,
#   2483550.646732441,
#   1891064.693892004,
#   2077722.472297793]
# exp_neon_tv_uplift = [901477.3619298406,
#   883413.0982569401,
#   257961.43805251978,
#   113959.20696139176,
#   302999.40117392206,
#   209994.54910795248,
#   248089.87060402642,
#   34762.279854703855,
#   2141601.013207391,
#   2240464.225536865,
#   3203064.493085238,
#   6453140.144192169,
#   3107996.480401831,
#   2218827.0455286833]
 
# exp_neon_const_uplift = [814523.7302475247,
#   797627.0714262014,
#   236399.26191033865,
#   104539.315520937,
#   276477.85401260597,
#   193496.09313945018,
#   228594.3357526747,
#   31857.884829358478,
#   2052899.4793962038,
#   2157714.310530949,
#   3092208.5330092534,
#   6403677.673500354,
#   2997992.20006065,
#   2135542.581971693]

# updated_texp_tv_uplift = []
# updated_texp_const_uplift = []


# updated_neon_tv_uplift = []
# updated_neon_const_uplift = []


# diff_tv_pyx_uplift = []
# diff_tv_qtz_uplift = []
# perdif_ev_uplift = []

# perdifneon_uplift = []
# for i in range(len(exp_ages_constant_uplift)): #convert ages from [yr] to [Ma]
#     updated = exp_ages_tv_uplift[i]/10**6
#     updated_texp_tv_uplift.append(updated) #Evenstar data
#     updated_const = exp_ages_constant_uplift[i]/10**6 
#     updated_texp_const_uplift.append(updated_const) #this model
#     temp = updated - updated_const
#     diff_tv_pyx_uplift.append(temp)
#     perdif_ev_uplift.append((temp/updated_const)*100)

# for i in range(len(exp_neon_tv_uplift)): #convert ages from [yr] to [Ma]
#     updatedneontv = exp_neon_tv_uplift[i]/10**6
#     updated_neon_tv_uplift.append(updatedneontv)
#     updatedneonconst = exp_neon_const_uplift[i]/10**6
#     updated_neon_const_uplift.append(updatedneonconst)
#     temp = updatedneontv - updatedneonconst
#     diff_tv_qtz_uplift.append(temp)
#     perdifneon_uplift.append((temp/updatedneonconst)*100)
    


# exp_ages_dunai_uplift = [21620883.698379427,
#   24056295.76201434,
#   17361363.196589906,
#   40069619.75631412,
#   21924929.188413106,
#   25543921.808545973,
#   14124650.763207203,
#   9106392.952987157,
#   25322648.87909743,
#   13978668.270522999,
#   19645764.316148702,
#   27952676.845142517,
#   18589950.22714381,
#   69378.698394077,
#   131094.04670745842,
#   88682.33937065522]

# exp_ages_dunai_const_uplift = [24814188.752465002,
#   27736727.057144716,
#   19030258.69177412,
#   46086717.902100146,
#   25205794.1053524,
#   29344893.444416832,
#   15229493.23631132,
#   9272744.911805676,
#   29115531.30299894,
#   15035437.472459888,
#   22128031.12508559,
#   31844129.630884707,
#   20684262.93627985,
#   64092.364079986764,
#   121102.18690494522,
#   81924.99928118107]
# updated_dunai_const_uplift = []
# updated_dunai_uplift = []
# diff_tv_dunai_uplift = []
# perdif_uplift = []



# for i in range(len(exp_ages_dunai_uplift)):
#     updated_dunaix = exp_ages_dunai_uplift[i]/10**6
#     updated_dunai_constx = exp_ages_dunai_const_uplift[i]/10**6
#     #x = perdif(updated_dunai_constx, updated_dunaix)
#     updated_dunai_uplift.append(updated_dunaix)
#     updated_dunai_const_uplift.append(updated_dunai_constx)
#     temp = updated_dunaix - updated_dunai_constx
#     diff_tv_dunai_uplift.append(temp)
#     perdif_uplift.append((temp/updated_dunai_constx)*100)
#     #perdif_uplift.append(x)


# fig = plt.figure(figsize=(14,9))


# gs = gridspec.GridSpec(2,2)

# ax1=fig.add_subplot(gs[:,0])
# ax2=fig.add_subplot(gs[0,1])
# ax3=fig.add_subplot(gs[1,1])


# ax2.set_ylim(-3.5,0.5)
# ax2.set_xlim(2,30)
# ax2.hlines(0,2,50)

# # ax2.plot(updated_texp_const_uplift[0:4] ,diff_tv_pyx_uplift[0:4], 'o', c = 'limegreen', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 2')
# # ax2.plot(updated_texp_const_uplift[4:17],diff_tv_pyx_uplift[4:17], 'o', c = 'royalblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 3')
# # ax2.plot(updated_texp_const_uplift[17:26],diff_tv_pyx_uplift[17:26], 'o', c = 'deepskyblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 5')

# # ax2.plot(updated_neon_const_uplift[0:9], diff_tv_qtz_uplift[0:9], 's', c ='teal', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 1')
# # ax2.plot(updated_neon_const_uplift[9:11], diff_tv_qtz_uplift[9:11], 's', c='limegreen', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 2')
# # ax2.plot(updated_neon_const_uplift[11:14], diff_tv_qtz_uplift[11:14], 's', c='royalblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 3')
# # ax2.plot(updated_neon_const_uplift[13], diff_tv_qtz_uplift[13], 's', c='deepskyblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 5')

# ax2.plot(updated_dunai_const_uplift[0:5], diff_tv_dunai_uplift[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# ax2.plot(updated_dunai_const_uplift[5:9], diff_tv_dunai_uplift[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# ax2.plot(updated_dunai_const_uplift[9:13],  diff_tv_dunai_uplift[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# ax2.plot(updated_dunai_const_uplift[13:15], diff_tv_dunai_uplift[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# ax2.plot(updated_dunai_const_uplift[15:16], diff_tv_dunai_uplift[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# ax2.set_ylabel('Exposure age difference (Ma)', fontsize = 14)
# ax2.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)


# # ax2.plot(updated_texp_const[0:4] ,diff_tv_pyx[0:4], 'o', c = 'limegreen', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 2')
# # ax2.plot(updated_texp_const[4:17],diff_tv_pyx[4:17], 'o', c = 'royalblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 3')
# # ax2.plot(updated_texp_const[17:26],diff_tv_pyx[17:26], 'o', c = 'deepskyblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 5')

# # ax2.plot(updated_neon_const[0:9], diff_tv_qtz[0:9], '*', c ='teal', alpha = 0.7,markersize = 10,label = '$^{21}Ne$ - Surface 1')
# # ax2.plot(updated_neon_const[9:11], diff_tv_qtz[9:11], '*', c='limegreen', alpha = 0.7,markersize = 10,label = '$^{21}Ne$ - Surface 2')
# # ax2.plot(updated_neon_const[11:14], diff_tv_qtz[11:14], '*', c='royalblue', alpha = 0.7,markersize = 10,label = '$^{21}Ne$ - Surface 3')
# # ax2.plot(updated_neon_const[13], diff_tv_qtz[13], '*', c='deepskyblue', alpha = 0.7,markersize = 10,label = '$^{21}Ne$ - Surface 5')

# ax2.plot(updated_dunai_const[0:5], diff_tv_dunai[0:5], '*', c = 'midnightblue',alpha = 0.7, markersize = 10, label = 'Surface A')
# ax2.plot(updated_dunai_const[5:9], diff_tv_dunai[5:9], '*', c = 'purple',alpha = 0.7, markersize = 10, label = 'Surface B')
# ax2.plot(updated_dunai_const[9:13],  diff_tv_dunai[9:13],'*', c = 'mediumpurple',alpha = 0.7, markersize = 10, label = 'Surface C')
# ax2.plot(updated_dunai_const[13:15], diff_tv_dunai[13:15], '*', c = 'skyblue',alpha = 0.7, markersize = 10, label = 'Surface D')
# ax2.plot(updated_dunai_const[15:16], diff_tv_dunai[15:16], '*', c = 'hotpink',alpha = 0.7, markersize = 10, label = 'Surface E')
# ax2.set_ylabel('Exposure age difference (Ma)', fontsize = 14)
# ax2.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)


# ax3.set_xlim(2,30)
# ax3.set_ylim(-14,7.5)
# # ax3.plot(updated_texp_const_uplift[0:4] ,perdif_ev_uplift[0:4], 'o', c = 'limegreen', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 2')
# # ax3.plot(updated_texp_const_uplift[4:17],perdif_ev_uplift[4:17], 'o', c = 'royalblue', alpha = 0.7,markersize = 8, label = '$^{3}He$ - Surface 3')
# # ax3.plot(updated_texp_const_uplift[17:26],perdif_ev_uplift[17:26], 'o', c = 'deepskyblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 5')

# # ax3.plot(updated_neon_const_uplift[0:9], perdifneon_uplift[0:9], 's', c ='teal', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 1')
# # ax3.plot(updated_neon_const_uplift[9:11], perdifneon_uplift[9:11], 's', c='limegreen', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 2')
# # ax3.plot(updated_neon_const_uplift[11:14], perdifneon_uplift[11:14], 's', c='royalblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 3')
# # ax3.plot(updated_neon_const_uplift[13], perdifneon_uplift[13], 's', c='deepskyblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 5')

# ax3.plot(updated_dunai_const_uplift[0:5], perdif_uplift[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# ax3.plot(updated_dunai_const_uplift[5:9], perdif_uplift[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# ax3.plot(updated_dunai_const_uplift[9:13],  perdif_uplift[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# ax3.plot(updated_dunai_const_uplift[13:15], perdif_uplift[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# ax3.plot(updated_dunai_const_uplift[15:16], perdif_uplift[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# ax3.set_ylabel('Exposure age percent difference (%)', fontsize = 14)
# ax3.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)
# ax3.hlines(0,2,50)

# ax3.set_ylim(-14,7.5)
# # ax3.plot(updated_texp_const[0:4] ,perdif_ev[0:4], '*', c = 'limegreen', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 2')
# # ax3.plot(updated_texp_const[4:17],perdif_ev[4:17], '*', c = 'royalblue', alpha = 0.7,markersize = 8, label = '$^{3}He$ - Surface 3')
# # ax3.plot(updated_texp_const[17:26],perdif_ev[17:26], '*', c = 'deepskyblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 5')

# # ax3.plot(updated_neon_const[0:9], perdifneon[0:9], '*', c ='teal', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 1')
# # ax3.plot(updated_neon_const[9:11], perdifneon[9:11], '*', c='limegreen', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 2')
# # ax3.plot(updated_neon_const[11:14], perdifneon[11:14], '*', c='royalblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 3')
# # ax3.plot(updated_neon_const[13], perdifneon[13], '*', c='deepskyblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 5')

# ax3.plot(updated_dunai_const[0:5], perdif[0:5], '*', c = 'midnightblue',alpha = 0.7, markersize = 10, label = 'Surface A')
# ax3.plot(updated_dunai_const[5:9], perdif[5:9], '*', c = 'purple',alpha = 0.7, markersize = 10, label = 'Surface B')
# ax3.plot(updated_dunai_const[9:13],  perdif[9:13],'*', c = 'mediumpurple',alpha = 0.7, markersize = 10, label = 'Surface C')
# ax3.plot(updated_dunai_const[13:15], perdif[13:15], '*', c = 'skyblue',alpha = 0.7, markersize = 10, label = 'Surface D')
# ax3.plot(updated_dunai_const[15:16], perdif[15:16], '*', c = 'hotpink',alpha = 0.7, markersize = 10, label = 'Surface E')
# ax3.set_ylabel('Exposure age percent difference (%)', fontsize = 14)
# # ax3.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)
# # ax3.hlines(0,2,30)


# # ax1.set_xlim(2,50)
# # ax1.plot([2,50], [2,50], 'k-')
# # ax1.plot(updated_neon_const_uplift[0:9], updated_neon_tv_uplift[0:9],  's', c = 'teal',alpha = 0.7, markersize = 8)
# # ax1.plot(updated_neon_const_uplift[9:11], updated_neon_tv_uplift[9:11],  's', c='limegreen', alpha = 0.7,markersize = 8)
# # ax1.plot(updated_neon_const_uplift[11:14], updated_neon_tv_uplift[11:14], 's', c='royalblue',alpha = 0.7, markersize = 8)
# # ax1.plot(updated_neon_const_uplift[13], updated_neon_tv_uplift[13],  's', c='deepskyblue', alpha = 0.7,markersize = 8)

# # ax1.plot(updated_texp_const_uplift[0:4],updated_texp_tv_uplift[0:4], 'o', c='limegreen', alpha = 0.7,markersize = 8)
# # ax1.plot(updated_texp_const_uplift[4:17],updated_texp_tv_uplift[4:17], 'o', c = 'royalblue', alpha = 0.7,markersize = 8)
# # ax1.plot(updated_texp_const_uplift[17:26],updated_texp_tv_uplift[17:26], 'o', c = 'deepskyblue',alpha = 0.7, markersize = 8)

# # ax1.plot(updated_dunai_const_uplift[0:5],updated_dunai_uplift[0:5], 's', c='midnightblue',alpha = 0.7, markersize = 8)
# # ax1.plot(updated_dunai_const_uplift[5:9],updated_dunai_uplift[5:9], 's', c='purple',alpha = 0.7,markersize =8)
# # ax1.plot(updated_dunai_const_uplift[9:13],updated_dunai_uplift[9:13], 's', c='mediumpurple',alpha = 0.7, markersize = 8)
# # ax1.plot(updated_dunai_const_uplift[13:15],updated_dunai_uplift[13:15], 's', c='skyblue',alpha = 0.7, markersize =8)
# # ax1.plot(updated_dunai_const_uplift[15:16],updated_dunai_uplift[15:16], 's', c='hotpink',alpha = 0.7, markersize = 8)
# # ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 14)
# # ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)
# plt.savefig(Read.directory+'/plots_updated/panel_bc.png', dpi = 300, bbox_inches='tight')






# #perdif

# # uplift_constant_temp=Read.uplift_constant
# # uplift_tv_temp= Read.uplift_tv


# # uplift_constant = uplift_constant_temp.iloc[1:][:]
# # uplift_tv = uplift_tv_temp.iloc[1:][:]

# # new_df = ((uplift_constant-uplift_tv).div((uplift_constant+uplift_tv)/2))*100




# static_constant_temp=Read.static_constant
# static_tv_temp= Read.static_tv


# static_constant = static_constant_temp.iloc[1:][:]
# static_tv = static_tv_temp.iloc[1:][:]

# new_df_static = ((static_constant-static_tv).div((static_constant+static_tv)/2))*100
# new_df_static.to_csv(directory+'/text_for_plots_updated/new_df_static.csv') 


#scaling factors
# uplift=Read.uplift_tv_sf
# static= Read.uplift_const_sf



# uplift = uplift.iloc[1:][:]
# static = static.iloc[1:][:]

# new_df = ((uplift-static).div((uplift+static)/2))*100


# new_df.to_csv(directory+'/text_for_plots_updated/perdifperdif.csv') 


# uplift_tv_sf = Read.uplift_tv_sf

# static_tv_sf = Read.static_tv_sf
# # # ###
# uplift_const_sf = Read.uplift_const_sf

# static_const_sf = Read.static_const_sf

# uplift_df = ((uplift_const_sf-uplift_tv_sf).div((uplift_tv_sf+uplift_const_sf)/2))*100

# static_df = ((static_const_sf-static_tv_sf).div((static_tv_sf+static_const_sf)/2))*100
# xaxis = np.arange(0,50.1,0.25)


# plt.plot(xaxis, uplift_tv_sf.iloc[1][1:], label = 'Uplift - time varying')
# plt.plot(xaxis, static_tv_sf.iloc[1][1:], label = 'No uplift - time varying')

# plt.plot(xaxis, uplift_const_sf.iloc[1][1:], label = 'Uplift - constant field')
# plt.plot(xaxis, static_const_sf.iloc[1][1:], label = 'No uplift - constant field')

# plt.axhline(-10.38342711488394,0,0.4, c = 'orange', label = 'average - no uplift 0-20Ma')

# plt.plot(xaxis,uplift_df.iloc[2][1:], label = 'uplift percent difference')
# plt.plot(xaxis,static_df.iloc[2][1:], label = 'no uplift percent difference')
# plt.axhline(-14.185977668175942,0,1, label = 'average - uplift 0-50Ma')
# plt.axhline(-9.550278180258353,0,0.4, label = 'average - uplift 0-20Ma')

# plt.xlabel('time')
# plt.ylabel('scaling factor')
# plt.legend()


# no = [15763888.284884367,
#   17076419.20354244,
#   13374161.294552842,
#   23883596.425344076,
#   15918685.926606067,
#   17660409.548891433,
#   11541407.566040298,
#   7955981.027963302,
#   17571620.08877715,
#   11441479.528158769,
#   14631504.274478512,
#   18550823.513116516,
#   14064538.456138527,
#   69285.95320017869,
#   130873.29079752268,
#   88532.09858076084]

# up = [21620883.698379427,
#   24055913.389574993,
#   17361613.516701892,
#   40070652.16999828,
#   21925671.14222829,
#   25541939.09866185,
#   14125145.069483079,
#   9106809.43571375,
#   25324744.29490823,
#   13977621.65892431,
#   19642333.40767994,
#   27952660.253182348,
#   18591584.940358467,
#   69383.06805338568,
#   131101.9020692805,
#   88689.67484872199]

##uplift 

# up = [21620883.698379427,
#   24056295.76201434,
#   17361363.196589906,
#   40069619.75631412,
#   21924929.188413106,
#   25543921.808545973,
#   14124650.763207203,
#   9106392.952987157,
#   25322648.87909743,
#   13978668.270522999,
#   19645764.316148702,
#   27952676.845142517,
#   18589950.22714381,
#   69378.698394077,
#   131094.04670745842,
#   88682.33937065522]

# no = [24814188.752465002,
#   27736727.057144716,
#   19030258.69177412,
#   46086717.902100146,
#   25205794.1053524,
#   29344893.444416832,
#   15229493.23631132,
#   9272744.911805676,
#   29115531.30299894,
#   15035437.472459888,
#   22128031.12508559,
#   31844129.630884707,
#   20684262.93627985,
#   64092.364079986764,
#   121102.18690494522,
#   81924.99928118107]

##no uplift
# up =[15763888.284884367,
#   17076439.897954084,
#   13374151.996150088,
#   23883596.012271866,
#   15918675.374240698,
#   17660422.55280363,
#   11541398.822023429,
#   7955981.4814617345,
#   17571600.49200227,
#   11441483.741217585,
#   14631506.693484198,
#   18550832.147374067,
#   14064530.42373193,
#   69285.95320017869,
#   130873.53703242909,
#   88532.05131133944]
                         
# no = [17162844.505560774,
#   18533186.489756998,
#   14294878.008155053,
#   27155794.989833537,
#   17338807.22884569,
#   19258940.393708486,
#   12089588.878998378,
#   8055902.3665621765,
#   19143774.462789685,
#   11971567.401384685,
#   15860207.587445626,
#   20421186.017621815,
#   15138254.28251518,
#   64006.15963224702,
#   120900.58338250335,
#   81785.64841898231]

# tempvals_uplift = Read.tempvals_uplift
# tempvals_static = Read.tempvals_static
# tempvals_uplift_const= Read.tempvals_uplift_const
# tempvals_static_const = Read.tempvals_static_const

# def perdif(a,b):
#     x = (a-b)/((a+b)/2)*100
#     return x

# lst = []
# for i in range(len(no)):
#     y = perdif(up[i],no[i])
#     lst.append(y)


#uPDATED SLHL
##Evenstar
# exp_ages_time_varying = [144983.2281236156,
#  1173042.5168646728,
#  3296753.479733703,
#  1660044.228652668,
#  1844203.7215091037,
#  2690484.135880749,
#  3299448.535973061,
#  6009823.89328057,
#  938002.3550705574,
#  1204874.6583443254,
#  3788931.9927694774,
#  6061045.696206524,
#  5632872.747655558,
#  5822361.3274903055,
#  6571843.023966717,
#  4485508.43420602,
#  4783857.192612417,
#  4954112.497759416,
#  4702246.838064122,
#  12489077.938449884,
#  8679198.589871358,
#  13221167.907005921,
#  11693730.108354347,
#  11534832.348870195,
#  2940314.482025803,
#  2865164.2601110777,
#  2217342.626614907,
#  2414276.3947902]

# exp_ages_constant = [124415.5182278017,
#  997635.2700000198,
#  2982760.364398058,
#  1457212.6192325512,
#  1625844.729374425,
#  2437257.7216031,
#  2981124.8447642648,
#  5468776.992941866,
#  796000.2128702761,
#  1022632.3295136057,
#  3433263.3820873713,
#  5522846.090175795,
#  5044822.878250542,
#  5255717.76548942,
#  6125042.696787047,
#  4024833.109949104,
#  4303325.101735422,
#  4447313.628021082,
#  4228248.3648968525,
#  12333663.100493345,
#  8260566.01943776,
#  13164862.528409122,
#  11447325.077443585,
#  11276022.055315902,
#  2660840.1314005414,
#  2598276.6763793626,
#  1998204.3107890561,
#  2188754.7218694557]

# exp_neon_tv = [972480.4235659479,
#  952976.087724448,
#  282097.35725954035,
#  124327.24456520952,
#  330789.9677605628,
#  229014.97328645727,
#  271019.79901667073,
#  37910.794523412944,
#  2255505.566966592,
#  2358902.1829043366,
#  3348866.0792458323,
#  6433979.980551361,
#  3256581.7502254983,
#  2334804.830010265]

# exp_neon_const = [772749.7430859036,
#  756777.2951421886,
#  226107.54364586118,
#  99962.66296896077,
#  264190.9889103578,
#  185023.02502292232,
#  218519.75356919228,
#  30449.09367920325,
#  1909540.4312698185,
#  2003740.515337338,
#  2838829.533478482,
#  5613188.29519167,
#  2758608.725266527,
#  1982503.8550429493]


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
    
# exp_ages_dunai = [17247117.412727457,
#  18398238.04278796,
#  14419620.408127125,
#  26143180.11554556,
#  17396340.102117803,
#  19010916.034524135,
#  12470612.22673141,
#  8613953.87220469,
#  18914925.173530705,
#  12364150.481662944,
#  15900923.299707763,
#  19980583.317925557,
#  15201352.069258908,
#  75621.62350226798,
#  142840.92763334894,
#  96627.63003067576]
                         
# exp_ages_dunai_const = [16422498.38763968,
#  17733728.131539553,
#  13678246.106836824,
#  25984388.806494284,
#  16590870.683880834,
#  18428372.516637336,
#  11568209.25751027,
#  7708480.630050803,
#  18318173.69313886,
#  11455253.71897883,
#  15176184.659430362,
#  19540454.41428692,
#  14485367.933942908,
#  61243.84191298591,
#  115682.8670989324,
#  78256.02022214868]



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


# fig = plt.figure(figsize=(14,9))


# gs = gridspec.GridSpec(2,2)

# ax1=fig.add_subplot(gs[:,0])
# ax2=fig.add_subplot(gs[0,1])
# ax3=fig.add_subplot(gs[1,1])


# #ax2.set_ylim(-1,1)
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
# #ax3.set_ylim(-5,15)
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
# ax1.plot(updated_neon_const[0:9], updated_neon_tv[0:9],  's', c = 'teal', alpha = 0.7,markersize = 8)
# ax1.plot(updated_neon_const[9:11], updated_neon_tv[9:11],  's', c='limegreen', alpha = 0.7,markersize = 8)
# ax1.plot(updated_neon_const[11:14], updated_neon_tv[11:14], 's', c='royalblue',alpha = 0.7, markersize = 8)
# ax1.plot(updated_neon_const[13], updated_neon_tv[13],  's', c='deepskyblue', alpha = 0.7,markersize = 8)

# ax1.plot(updated_texp_const[0:4],updated_texp_tv[0:4], 'o', c='limegreen', alpha = 0.7,markersize = 8)
# ax1.plot(updated_texp_const[4:17],updated_texp_tv[4:17], 'o', c = 'royalblue', alpha = 0.7,markersize = 8)
# ax1.plot(updated_texp_const[17:26],updated_texp_tv[17:26], 'o', c = 'deepskyblue',alpha = 0.7, markersize = 8)

# ax1.plot(updated_dunai_const[0:5],updated_dunai[0:5], 's', c='midnightblue',alpha = 0.7, markersize = 8)
# ax1.plot(updated_dunai_const[5:9],updated_dunai[5:9], 's', c='purple',alpha = 0.7,markersize =8)
# ax1.plot(updated_dunai_const[9:13],updated_dunai[9:13], 's', c='mediumpurple',alpha = 0.7, markersize = 8)
# ax1.plot(updated_dunai_const[13:15],updated_dunai[13:15], 's', c='skyblue', alpha = 0.7,markersize =8)
# ax1.plot(updated_dunai_const[15:16],updated_dunai[15:16], 's', c='hotpink', alpha = 0.7,markersize = 8)
# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 14)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)

# ax1.set_xlim(2,30)
# ax1.plot([2,30], [2,30], 'k-')
# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 13)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 13)
# plt.savefig(Read.directory+'/plots_updated/nouplift_newslhl.png', dpi = 300, bbox_inches='tight')





##UPLIFT WITH NEW SLHL

# exp_ages_tv_uplift = [144983.2281236156,
#  1190071.5371676113,
#  3468813.6312247925,
#  1695913.9786014399,
#  1886646.4906149844,
#  2800913.7725531026,
#  3465769.813417348,
#  6474272.646724874,
#  948824.3869951426,
#  1224279.7441953535,
#  4008725.7359628878,
#  6488420.721355995,
#  6018795.514098521,
#  6270645.634599504,
#  7250115.829444345,
#  4791677.478163087,
#  5180496.433107149,
#  5365315.883353746,
#  5082505.540522843,
#  15603634.63865798,
#  10091557.292198913,
#  17049076.028758008,
#  14307430.758604964,
#  14060124.507848147,
#  3086863.6366207614,
#  3013837.3942850726,
#  2296603.4272113345,
#  2511149.5718965046]

# exp_ages_constant_uplift = [124415.5182278017,
#  1009331.9975648309,
#  3118610.0314274537,
#  1486080.1454902478,
#  1659913.2054546974,
#  2522007.8702279353,
#  3112157.0071080043,
#  5950461.776844486,
#  803811.8715729876,
#  1036291.3999628819,
#  3613050.988111661,
#  5977854.557000819,
#  5420894.840699209,
#  5713178.054875442,
#  6763103.552411586,
#  4252468.182924881,
#  4618955.428532844,
#  4777641.833942556,
#  4525878.630904905,
#  15557648.877287868,
#  9539042.673732297,
#  16969301.570279185,
#  14162535.89575378,
#  13878034.069018835,
#  2776376.8236526847,
#  2715141.101665013,
#  2065242.281591577,
#  2269642.1180312997]

# exp_neon_tv_uplift = [982512.445954843,
#  962800.2084838838,
#  282415.7591511918,
#  124403.47822999391,
#  331581.34477182425,
#  229178.98361570507,
#  271416.91566504835,
#  37950.265931142894,
#  2327087.428928443,
#  2438036.420512498,
#  3512987.1436768277,
#  7003718.9123381,
#  3408360.5855686096,
#  2413934.9052379355]
 
# exp_neon_const_uplift = [778794.4602149348,
#  762625.4942371708,
#  226178.87831883878,
#  100019.22512976744,
#  264443.23517445696,
#  185151.48504191294,
#  218734.538964495,
#  30479.686676858288,
#  1961497.9724124814,
#  2061501.5866479815,
#  2952450.761242099,
#  6100669.585005386,
#  2862977.4898303016,
#  2040330.76098448]


# updated_texp_tv_uplift = []
# updated_texp_const_uplift = []


# updated_neon_tv_uplift = []
# updated_neon_const_uplift = []


# diff_tv_pyx_uplift = []
# diff_tv_qtz_uplift = []
# perdif_ev_uplift = []

# perdifneon_uplift = []
# for i in range(len(exp_ages_constant_uplift)): #convert ages from [yr] to [Ma]
#     updated = exp_ages_tv_uplift[i]/10**6
#     updated_texp_tv_uplift.append(updated) #Evenstar data
#     updated_const = exp_ages_constant_uplift[i]/10**6 
#     updated_texp_const_uplift.append(updated_const) #this model
#     temp = updated - updated_const
#     diff_tv_pyx_uplift.append(temp)
#     perdif_ev_uplift.append((temp/updated_const)*100)

# for i in range(len(exp_neon_tv_uplift)): #convert ages from [yr] to [Ma]
#     updatedneontv = exp_neon_tv_uplift[i]/10**6
#     updated_neon_tv_uplift.append(updatedneontv)
#     updatedneonconst = exp_neon_const_uplift[i]/10**6
#     updated_neon_const_uplift.append(updatedneonconst)
#     temp = updatedneontv - updatedneonconst
#     diff_tv_qtz_uplift.append(temp)
#     perdifneon_uplift.append((temp/updatedneonconst)*100)
    
# exp_ages_dunai_uplift = [24415905.752183124,
#  27442891.09306456,
#  19214390.499043625,
#  44398310.253074974,
#  24801554.40243952,
#  29174918.470955934,
#  15647003.146367976,
#  10022344.89364451,
#  28929667.252090547,
#  15452312.697551738,
#  21928060.24061816,
#  31521955.738282025,
#  20656467.857115395,
#  75727.97567924544,
#  143094.06993327953,
#  96801.7697015583]

# exp_ages_dunai_const_uplift = [23246340.495556008,
#  26044310.2023921,
#  17913623.40031618,
#  43611381.15275605,
#  23621082.751148492,
#  27582304.925880548,
#  14392033.849750554,
#  8810911.868443776,
#  27362319.625571623,
#  14211566.432506615,
#  20755874.557585835,
#  29975501.606458947,
#  19433966.86166299,
#  61326.1987636971,
#  115874.39239248243,
#  78388.61295555996]

# updated_dunai_const_uplift = []
# updated_dunai_uplift = []
# diff_tv_dunai_uplift = []
# perdif_uplift = []



# for i in range(len(exp_ages_dunai_uplift)):
#     updated_dunaix = exp_ages_dunai_uplift[i]/10**6
#     updated_dunai_constx = exp_ages_dunai_const_uplift[i]/10**6
#     #x = perdif(updated_dunai_constx, updated_dunaix)
#     updated_dunai_uplift.append(updated_dunaix)
#     updated_dunai_const_uplift.append(updated_dunai_constx)
#     temp = updated_dunaix - updated_dunai_constx
#     diff_tv_dunai_uplift.append(temp)
#     perdif_uplift.append((temp/updated_dunai_constx)*100)
#     #perdif_uplift.append(x)


# fig = plt.figure(figsize=(14,9))


# gs = gridspec.GridSpec(2,2)

# ax1=fig.add_subplot(gs[:,0])
# ax2=fig.add_subplot(gs[0,1])
# ax3=fig.add_subplot(gs[1,1])


# #ax2.set_ylim(-3.5,0.5)
# ax2.set_xlim(2,50)
# ax2.hlines(0,2,50)

# ax2.plot(updated_texp_const_uplift[0:4] ,diff_tv_pyx_uplift[0:4], 'o', c = 'limegreen', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 2')
# ax2.plot(updated_texp_const_uplift[4:17],diff_tv_pyx_uplift[4:17], 'o', c = 'royalblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 3')
# ax2.plot(updated_texp_const_uplift[17:26],diff_tv_pyx_uplift[17:26], 'o', c = 'deepskyblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 5')

# ax2.plot(updated_neon_const_uplift[0:9], diff_tv_qtz_uplift[0:9], 's', c ='teal', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 1')
# ax2.plot(updated_neon_const_uplift[9:11], diff_tv_qtz_uplift[9:11], 's', c='limegreen', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 2')
# ax2.plot(updated_neon_const_uplift[11:14], diff_tv_qtz_uplift[11:14], 's', c='royalblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 3')
# ax2.plot(updated_neon_const_uplift[13], diff_tv_qtz_uplift[13], 's', c='deepskyblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 5')

# ax2.plot(updated_dunai_const_uplift[0:5], diff_tv_dunai_uplift[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# ax2.plot(updated_dunai_const_uplift[5:9], diff_tv_dunai_uplift[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# ax2.plot(updated_dunai_const_uplift[9:13],  diff_tv_dunai_uplift[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# ax2.plot(updated_dunai_const_uplift[13:15], diff_tv_dunai_uplift[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# ax2.plot(updated_dunai_const_uplift[15:16], diff_tv_dunai_uplift[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# ax2.set_ylabel('Exposure age difference (Ma)', fontsize = 14)
# ax2.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)



# ax2.set_ylabel('Exposure age difference (Ma)', fontsize = 14)
# ax2.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)


# ax3.set_xlim(2,50)
# #ax3.set_ylim(-14,7.5)
# ax3.plot(updated_texp_const_uplift[0:4] ,perdif_ev_uplift[0:4], 'o', c = 'limegreen', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 2')
# ax3.plot(updated_texp_const_uplift[4:17],perdif_ev_uplift[4:17], 'o', c = 'royalblue', alpha = 0.7,markersize = 8, label = '$^{3}He$ - Surface 3')
# ax3.plot(updated_texp_const_uplift[17:26],perdif_ev_uplift[17:26], 'o', c = 'deepskyblue', alpha = 0.7, markersize = 8,label = '$^{3}He$ - Surface 5')

# ax3.plot(updated_neon_const_uplift[0:9], perdifneon_uplift[0:9], 's', c ='teal', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 1')
# ax3.plot(updated_neon_const_uplift[9:11], perdifneon_uplift[9:11], 's', c='limegreen', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 2')
# ax3.plot(updated_neon_const_uplift[11:14], perdifneon_uplift[11:14], 's', c='royalblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 3')
# ax3.plot(updated_neon_const_uplift[13], perdifneon_uplift[13], 's', c='deepskyblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 5')

# ax3.plot(updated_dunai_const_uplift[0:5], perdif_uplift[0:5], 's', c = 'midnightblue',alpha = 0.7, markersize = 8, label = 'Surface A')
# ax3.plot(updated_dunai_const_uplift[5:9], perdif_uplift[5:9], 's', c = 'purple',alpha = 0.7, markersize = 8, label = 'Surface B')
# ax3.plot(updated_dunai_const_uplift[9:13],  perdif_uplift[9:13],'s', c = 'mediumpurple',alpha = 0.7, markersize = 8, label = 'Surface C')
# ax3.plot(updated_dunai_const_uplift[13:15], perdif_uplift[13:15], 's', c = 'skyblue',alpha = 0.7, markersize = 8, label = 'Surface D')
# ax3.plot(updated_dunai_const_uplift[15:16], perdif_uplift[15:16], 's', c = 'hotpink',alpha = 0.7, markersize = 8, label = 'Surface E')
# ax3.set_ylabel('Exposure age percent difference (%)', fontsize = 14)
# ax3.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)
# ax3.hlines(0,2,50)

# #ax3.set_ylim(-14,7.5)

# ax3.set_ylabel('Exposure age percent difference (%)', fontsize = 14)
# # ax3.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)
# # ax3.hlines(0,2,30)

# ax1.set_title('Uplift')
# ax1.set_xlim(2,50)
# ax1.plot([2,50], [2,50], 'k-')
# ax1.plot(updated_neon_const_uplift[0:9], updated_neon_tv_uplift[0:9],  's', c = 'teal',alpha = 0.7, markersize = 8)
# ax1.plot(updated_neon_const_uplift[9:11], updated_neon_tv_uplift[9:11],  's', c='limegreen', alpha = 0.7,markersize = 8)
# ax1.plot(updated_neon_const_uplift[11:14], updated_neon_tv_uplift[11:14], 's', c='royalblue',alpha = 0.7, markersize = 8)
# ax1.plot(updated_neon_const_uplift[13], updated_neon_tv_uplift[13],  's', c='deepskyblue', alpha = 0.7,markersize = 8)

# ax1.plot(updated_texp_const_uplift[0:4],updated_texp_tv_uplift[0:4], 'o', c='limegreen', alpha = 0.7,markersize = 8)
# ax1.plot(updated_texp_const_uplift[4:17],updated_texp_tv_uplift[4:17], 'o', c = 'royalblue', alpha = 0.7,markersize = 8)
# ax1.plot(updated_texp_const_uplift[17:26],updated_texp_tv_uplift[17:26], 'o', c = 'deepskyblue',alpha = 0.7, markersize = 8)

# ax1.plot(updated_dunai_const_uplift[0:5],updated_dunai_uplift[0:5], 's', c='midnightblue',alpha = 0.7, markersize = 8)
# ax1.plot(updated_dunai_const_uplift[5:9],updated_dunai_uplift[5:9], 's', c='purple',alpha = 0.7,markersize =8)
# ax1.plot(updated_dunai_const_uplift[9:13],updated_dunai_uplift[9:13], 's', c='mediumpurple',alpha = 0.7, markersize = 8)
# ax1.plot(updated_dunai_const_uplift[13:15],updated_dunai_uplift[13:15], 's', c='skyblue',alpha = 0.7, markersize =8)
# ax1.plot(updated_dunai_const_uplift[15:16],updated_dunai_uplift[15:16], 's', c='hotpink',alpha = 0.7, markersize = 8)
# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 14)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)
# plt.savefig(Read.directory+'/plots_updated/uplift_newslhl.png', dpi = 300, bbox_inches='tight')
