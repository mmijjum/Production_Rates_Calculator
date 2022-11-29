#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:57:00 2022

@author: mmijjum
"""
import numpy as np
import matplotlib.pyplot as plt
import User_Interface
#import Pmag_paleolat
import Read
#import scaling_factor
#import Rc
import atm_depth
#import expage

time = User_Interface.time
#This is testing using the Evenstar Dataset. 
#FOR 0-25MA
# age50 = [2093772.4256661092,
#   1726165.1427583196,
#   2081887.164883334,
#   3794010.627343578,
#   2374363.7614730676,
#   3791900.9065173003,
#   3474506.99921253,
#   3658587.261596599,
#   4290251.866445129,
#   2748483.971594672,
#   3008785.9841243965,
#   3102199.997681156,
#   2948188.5658668843,
#   8291082.744689552,
#   5789721.38242785,
#   8830771.09504759,
#   7734194.788864596,
#   7603683.4355172785,
#   1880453.2621676903,
#   1848520.0425761389] #using 50 ka bins

# age250 = [2119590.634889613,
#   1762255.7986143497,
#   2107807.655974157,
#   3827058.939207,
#   2407049.049635731,
#   3827384.4932132033,
#   3504150.9877329734,
#   3696091.6962375473,
#   4312343.256852603,
#   2772698.267747615,
#   3030374.8776484244,
#   3127042.2952194544,
#   2969982.649205427,
#   8335259.328754014,
#   5826142.719464731,
#   8862280.727973185,
#   7759364.3585272785,
#   7625234.756910009,
#   1898838.5359503585,
#   1868307.506440616] #using 250 ka bins.


# # #FOR 40-65MA
# age50z = [1641715.3620027953,
#   1314498.3069084424,
#   1609358.3240256277,
#   2956001.030059968,
#   1854727.1280713787,
#   2895166.820680435,
#   2645049.671025622,
#   2857271.909595606,
#   3327361.9130364996,
#   2084456.3941086568,
#   2391713.6306608147,
#   2440823.66680588,
#   2320383.8364273356,
#   6644021.436928393,
#   4510091.790629581,
#   7067792.7393099675,
#   6184382.977237228,
#   6084899.1555786645,
#   1454945.563913008,
#   1447490.6318393145]


# age250z = [1640367.6527764683,
#   1313149.8654674513,
#   1607891.0802430166,
#   2954299.724546143,
#   1853193.3764866616,
#   2893354.18320825,
#   2643045.9779880107,
#   2855721.3486434543,
#   3326239.74462353,
#   2082727.8854659325,
#   2390202.8394402456,
#   2439088.883007017,
#   2318773.3358721477,
#   6648201.600721818,
#   4511154.639028694,
#   7072798.146107502,
#   6187826.864755532,
#   6088562.993477617,
#   1453706.4418546127,
#   1446249.2598376216]
# plt.plot([0,10*10**6], [0,10*10**6], 'k-') #1:1 line

# plt.ylabel('250ka resolution_evenstar')
# plt.xlabel('50ka resolution_evenstar')

# plt.plot(age50,age250, 'o', c = 'darkmagenta', label = '0-25Ma')
# plt.plot(age50z,age250z, 'x', c = 'blue', label = '40-65Ma')

# plt.legend()


# plt.savefig(Read.directory+'/plots/exposure_age_residual_50_250.png', dpi = 300, bbox_inches='tight')


# PALEOLAT FIGURE
# Excel sheet: change inputs to be: 
#     20N, 73E
#     19S, 69W

# # Run sheet with plate = SA for the second sample and palte = IN for first. 
# # save values:
# SA = pl_df.iloc[1] #COMMENT THIS OUT WHEN YOU RUN THE NEXT SAMPLE SO DATA DOESN'T GET UPDATED W NEW PLATE.
# #IN = Pmag_paleolat.pl_df.iloc[0]

# plt.figure()
# plt.subplot(211)
# plt.plot(time,IN,color='blue',c = 'blue', label = '20N, 73E')
# plt.legend(loc = 'lower left', frameon=True)
# plt.subplot(212)
# plt.plot(time,SA, color='green', label = '19S, 69W')
# plt.xlabel('Time [Ma]')
# plt.legend(frameon=True)
#plt.savefig(directory+'/plots/paleolat_subplots.png', dpi = 300, bbox_inches='tight')

    
# # FOR FIG 3.
# # create figure and axis objects with subplots()
# # in excel sheet: set every lat to 0-90, lon = 0, elevation = 0. Uncomment out the part of pmag that hard-codes the latitudes (so it doesn't vary w time)
# # only run for like 1 Ma, bc you're only gonna use the first value anyways.
# #note: make sure you hard code atm depth to 1033 g/cm2
# paleolatitudes = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
# fig,ax = plt.subplots()
# # make a plot
# ax.plot(paleolatitudes, scaling_factor.Siteprod_df[0],
#         color="green")
# ax.set_ylim(top = 1.1)
# # set x-axis label
# ax.set_xlabel("Geomagnetic Latitude", fontsize = 13)
# # set y-axis label
# ax.set_ylabel("Scaling Factor",
#               color="green",
#               fontsize=13)


# # twin object for two different y-axis on the sample plot
# ax2=ax.twinx()
# # make a plot with different y-axis using second axis object
# ax2.plot(paleolatitudes, Rc.Rc.iloc[:,0],color="blue")
# ax2.set_ylim(top = 19)

# ax2.set_ylabel("Cutoff Rigidty [GV]",color="blue",fontsize=13)
# plt.savefig(Read.directory+'/plots/rc_vs_sf.png', dpi = 300, bbox_inches='tight')


    
# #atmospheric depth plot
# x_standard = x.iloc[0]
# #x_era = atm_depth.x.iloc[0]
# plt.ticklabel_format(useOffset=False)
# plt.ylabel('standard - ERA40')
# plt.xlabel('time [ma]')
# plt.plot(time,x_standard-x_era, c = 'blue')
# plt.savefig(Read.directory+'/plots/atm_residual', dpi = 300, bbox_inches='tight')

#exposure age comparison w different atmospheric depth calculation

# expage_std = [2119590.634889613,
#   1762255.7986143497,
#   2107807.655974157,
#   3827058.939207,
#   2407049.049635731,
#   3827384.4932132033,
#   3504150.9877329734,
#   3696091.6962375473,
#   4312343.256852603,
#   2772698.267747615,
#   3030374.8776484244,
#   3127042.2952194544,
#   2969982.649205427,
#   8335259.328754014,
#   5826142.719464731,
#   8862280.727973185,
#   7759364.3585272785,
#   7625234.756910009,
#   1898838.5359503585,
#   1868307.506440616]
# expage_era40 = [1682336.27346274,
#  1369654.4967578787,
#  1651209.9744326228,
#  2903141.8451572447,
#  1859501.4579053859,
#  2845571.184447717,
#  2596830.5238763257,
#  2815120.777458704,
#  3288404.102596038,
#  2081043.1392238676,
#  2345687.503652107,
#  2403545.6562206727,
#  2284213.9644163325,
#  6505348.968571195,
#  4496809.454798173,
#  6886705.126891983,
#  6133158.26957023,
#  6045048.644731383,
#  1510154.7796044361,
#  1518470.5483525007]
# plt.ylabel('exp_age era40')
# plt.xlabel('exp_age std atm')

# plt.plot([0,10*10**6], [0,10*10**6], 'k-') #1:1 line
# plt.plot(expage_std,expage_era40,'o', color = 'darkmagenta')
# plt.savefig(Read.directory+'/plots/atm_depth_expage_residual', dpi = 300, bbox_inches='tight')



texp = [3188863,2560853,3166922,5939087,3670960,5942367,5413382,5710884,6680445,4267817,4712387,4825234,4580202,13646406,9082561,14562636,
12643455,12447934,2823366,2784350] #these are the re-calculated exposure ages from CRONUS.


age250 = [2119590.634889613,
  1762255.7986143497,
  2107807.655974157,
  3827058.939207,
  2407049.049635731,
  3827384.4932132033,
  3504150.9877329734,
  3696091.6962375473,
  4312343.256852603,
  2772698.267747615,
  3030374.8776484244,
  3127042.2952194544,
  2969982.649205427,
  8335259.328754014,
  5826142.719464731,
  8862280.727973185,
  7759364.3585272785,
  7625234.756910009,
  1898838.5359503585,
  1868307.506440616]

agemuons = [2118177.4565160577,
  1761518.7896895926,
  2106793.627392337,
  3824966.750524062,
  2405849.062068012,
  3826082.5196715537,
  3503005.227813785,
  3693985.496784637,
  4309608.55254154,
  2771935.9494826896,
  3028035.362593929,
  3125022.193753847,
  2968118.1408135714,
  8330218.072443537,
  5823071.607679994,
  8856730.933292668,
  7754617.960505956,
  7620386.360666843,
  1897781.1319129309,
  1866650.506910643]

updated_texp = []
updated_model_ages = []
muons_list = []

for i in range(len(texp)): #convert ages from [yr] to [Ma]
    updated = texp[i]/10**6
    updated_texp.append(updated) #Evenstar data
    updated_model = age250[i]/10**6 
    updated_model_ages.append(updated_model) #this model
    wmuons = agemuons[i]/10**6 
    muons_list.append(wmuons) #con muons
diff = []    
for i in range(len(updated_model_ages)):
    diff.append(updated_model_ages[i] - updated_texp[i])


plt.plot([0,18], [0,18], 'k-') #1:1 line
plt.rcParams["figure.figsize"] = [6,4] #update figure size
plt.plot(updated_texp,updated_model_ages, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')
plt.plot(updated_texp,muons_list, 'x', c = 'black', label = 'w muons')
plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
plt.xlabel('Exposure Age [Ma] recalculated from Evenstar (2017)', fontsize = 10)
plt.ylabel('Exposure Age [Ma] This Work', fontsize = 10)
plt.savefig(Read.directory+'/plots/exposure_age_residual.png', dpi = 300, bbox_inches='tight')



