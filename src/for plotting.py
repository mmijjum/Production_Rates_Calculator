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
# age50 = [2092440.7163792772,
 1725318.990309885,
 2080936.2183514563,
 3792000.2983032307,
 2373118.5224286295,
 3790654.0591238867,
 3473432.2435856927,
 3656462.421640884,
 4287476.291783117,
 2747731.9629505384,
 3006449.5761132357,
 3100075.947847032,
 2946292.5112709007,
 8286325.188444292,
 5786596.529530387,
 8825054.684539936,
 7728948.953306702,
 7598486.571212875,
 1879297.0764446724,
 1846749.2127140833] #using 50 ka bins

# age250 = [2119590.634889613,
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
 1868307.506440616] #using 250 ka bins.


# #FOR 40-65MA
# age50z = [2689659.114906265,
#  2155694.603761782,
#  2637707.013669703,
#  4804033.939075664,
#  3037099.10099234,
#  4704307.533596549,
#  4307603.32974832,
#  4646317.658072593,
#  5390202.859364487,
#  3410603.6101067797,
#  3904993.8667768147,
#  3983063.6655656835,
#  3789593.1432980974,
#  10712479.57992168,
#  7247101.444131516,
#  11452567.652469862,
#  9931314.2597088,
#  9766406.740785452,
#  2384958.7529432024,
#  2372482.2537648976]


# age250z = [1640794.5347412296,
 1313967.71432156,
 1608705.019250512,
 2954805.801212531,
 1853970.1883031263,
 2894466.101604687,
 2644408.2908202913,
 2855951.362842375,
 3325841.3437333032,
 2084036.146086675,
 2390277.3022556105,
 2439571.565762161,
 2319183.0918199196,
 6640797.558613795,
 4507741.727392904,
 7064266.8599011395,
 6181270.891445461,
 6081971.016792731,
 1454199.8407673405,
 1446355.9266932283]
# plt.plot([0,15*10**6], [0,15*10**6], 'k-') #1:1 line

# plt.ylabel('250ka resolution_evenstar')
# plt.xlabel('50ka resolution_evenstar')

# plt.plot(age50,age250, 'o', c = 'darkmagenta', label = '0-25Ma')
# plt.plot(age50z,age250z, 'x', c = 'blue', label = '40-65Ma')

# plt.legend()


# plt.savefig(Read.directory+'/plots/exposure_age_residual.png', dpi = 300, bbox_inches='tight')


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

# expage_std = [3438985.747690098,
#   2793365.6583587048,
#   3418691.4562739925,
#   6197079.767436442,
#   3947296.9780319743,
#   6192199.908251557,
#   5773331.872040842,
#   6019121.413486346,
#   6820032.170606625,
#   4598993.155508901,
#   5026263.482989186,
#   5183519.5905606,
#   4925618.939848194,
#   13017786.842042197,
#   9108387.593166394,
#   13788637.378882773,
#   12207476.794415213,
#   12037778.436894862,
#   3067407.9322499265,
#   3015213.471865391]
# expage_era40 = [2655178.095662571,
#  2145412.4476588825,
#  2593334.6762203546,
#  4820500.531826417,
#  2992475.500430216,
#  4728629.986740357,
#  4286959.064097682,
#  4666395.684401184,
#  5442138.891194208,
#  3373327.9793261257,
#  3841786.2947979905,
#  3942285.9766430752,
#  3750269.717795015,
#  10309336.739507422,
#  7064920.908953373,
#  10945690.49249853,
#  9656848.168775728,
#  9500656.170884604,
#  2357769.506722916,
#  2380470.5189771415]
# plt.ylabel('exp_age era40')
# plt.xlabel('exp_age std atm')

# plt.plot([0,15*10**6], [0,15*10**6], 'k-') #1:1 line
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


plt.plot([0,20], [0,20], 'k-') #1:1 line
plt.rcParams["figure.figsize"] = [5,5] #update figure size
plt.plot(updated_texp,updated_model_ages, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')
plt.plot(updated_texp,muons_list, 'x', c = 'black', label = 'w muons')
plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
plt.xlabel('Exposure Age [Ma] recalculated from Evenstar (2017)', fontsize = 10)
plt.ylabel('Exposure Age [Ma] This Work', fontsize = 10)
plt.savefig(Read.directory+'/plots/exposure_age_residual.png', dpi = 300, bbox_inches='tight')



