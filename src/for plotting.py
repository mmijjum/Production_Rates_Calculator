#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:57:00 2022

@author: mmijjum
"""
import numpy as np

import matplotlib.pyplot as plt
import User_Interface
import Pmag_paleolat
import Read
import scaling_factor
import Rc
import atm_depth
import expage
import pandas as pd

# # time = User_Interface.time
# # #This is testing using the Evenstar Dataset. 
# # #FOR 0-25MA
# # age50 = [2446582.051843587,
#  # 2004314.7353869148,
#  # 2423194.5340497126,
#  # 4535972.506898869,
#  # 2795229.12301331,
#  # 4539397.58713876,
#  # 4106453.091722328,
#  # 4351934.179543529,
#  # 5128416.108848863,
#  # 3259093.6636512275,
#  # 3553278.3979254076,
#  # 3654274.4142123642,
#  # 3480292.242302103,
#  # 9797321.47007983,
#  # 6655131.16099609,
#  # 10433859.672708213,
#  # 9155427.32999988,
#  # 9010333.353256276,
#  # 2182009.839645,
#  # 2136281.964589597] #using 50 ka bins

# # age250 = [2466573.812240755,
# #   2023299.0465562146,
# #   2444888.3224641937,
# #   4553730.093643763,
# #   2815661.742382576,
# #   4558046.30932169,
# #   4129536.130928539,
# #   4370703.18758535,
# #   5147929.74150341,
# #   3284304.210058709,
# #   3574064.8522674884,
# #   3678847.610658329,
# #   3503468.9083244572,
# #   9826447.766671108,
# #   6690999.3511465965,
# #   10466508.118817024,
# #   9186317.233039252,
# #   9039952.58829612,
# #   2203962.164205366,
# #   2156751.2442309437] #using 250 ka bins.


# # # #FOR 40-65MA
# # age50z = [2322222.0197343845,
# #  1827003.7180525255,
# #  2236332.73211175,
# #  4088426.636282565,
# #  2576783.4195228834,
# #  3921153.933296707,
# #  3587126.381608773,
# #  3981091.0425009327,
# #  4623998.620604362,
# #  2814588.7760927277,
# #  3382878.185449054,
# #  3425614.41611594,
# #  3258087.635618077,
# #  9197530.90823805,
# #  6275536.489532302,
# #  9819943.027370123,
# #  8570076.817017611,
# #  8410296.476118937,
# #  2045676.7612999033,
# #  2092838.0987445342]


# # age250z = [2104071.4747958337,
#  # 1688590.7537658196,
#  # 2067916.1273260734,
#  # 3779146.8719433253,
#  # 2377461.5747988084,
#  # 3730277.133714455,
#  # 3414259.340207927,
#  # 3652250.384898707,
#  # 4237039.14064651,
#  # 2713396.8940542364,
#  # 3039615.707531209,
#  # 3113495.2378157135,
#  # 2961420.937027323,
#  # 8224269.327877105,
#  # 5678036.31749751,
#  # 8770084.468422879,
#  # 7693400.381483267,
#  # 7571956.359234414,
#  # 1866300.7930147112,
#  # 1838465.8121254023]
# #  2091393.189669876]
# # #plt.plot([0,15*10**4], [0,15*10**4], 'k-') #1:1 line

# # # plt.ylabel('250ka resolution_evenstar')
# # # plt.xlabel('50ka resolution_evenstar')

# # # plt.plot(age50,age250, 'o', c = 'darkmagenta', label = '0-25Ma')
# # # plt.plot(age50z,age250z, 'x', c = 'blue', label = '40-65Ma')

# # # plt.legend()


# # # plt.savefig(Read.directory+'/plots/exposure_age_residual_50_250.png', dpi = 300, bbox_inches='tight')

# # xx = []

# # for i in range(len(age50)):
# #     xaxis = age250[i]-age50[i]
# #     xx.append(xaxis)
# # plt.xlabel('sample')
# # plt.ylabel('Exposure Age Difference (250ka - 50ka)')
# # plt.plot(xx, 'o-',  c = 'darkmagenta', label = '0-25Ma')
# # plt.savefig(Read.directory+'/plots/exposure_age_difference_50_250.png', dpi = 300, bbox_inches='tight')


# # PALEOLAT FIGURE
# # Excel sheet: change inputs to be: 
# #     20N, 73E
# #     19S, 69W

# # # Run sheet with plate = SA for the second sample and palte = IN for first. 
# # # save values:
# # SA = pl_df.iloc[1] #COMMENT THIS OUT WHEN YOU RUN THE NEXT SAMPLE SO DATA DOESN'T GET UPDATED W NEW PLATE.
# # #IN = Pmag_paleolat.pl_df.iloc[0]

# # plt.figure()p
# # plt.subplot(211)
# # plt.plot(time,IN,color='blue',c = 'blue', label = '20N, 73E')
# # plt.legend(loc = 'lower left', frameon=True)
# # plt.subplot(212)
# # plt.plot(time,SA, color='green', label = '19S, 69W')
# # plt.xlabel('Time [Ma]')
# # plt.legend(frameon=True)
# #plt.savefig(directory+'/plots/paleolat_subplots.png', dpi = 300, bbox_inches='tight')

    
# # # FOR FIG 3.
# # # create figure and axis objects with subplots()
# # # in excel sheet: set every lat to 0-90, lon = 0, elevation = 0. Uncomment out the part of pmag that hard-codes the latitudes (so it doesn't vary w time)
# # # only run for like 1 Ma, bc you're only gonna use the first value anyways.
# # #note: make sure you hard code atm depth to 1033 g/cm2
# # paleolatitudes = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
# # fig,ax = plt.subplots()
# # # make a plot
# # ax.plot(paleolatitudes, scaling_factor.Siteprod_df[0],
# #         color="green")
# # ax.set_ylim(top = 1.1)
# # # set x-axis label
# # ax.set_xlabel("Geomagnetic Latitude", fontsize = 13)
# # # set y-axis label
# # ax.set_ylabel("Scaling Factor",
# #               color="green",
# #               fontsize=13)


# # # twin object for two different y-axis on the sample plot
# # ax2=ax.twinx()
# # # make a plot with different y-axis using second axis object
# # ax2.plot(paleolatitudes, Rc.Rc.iloc[:,0],color="blue")
# # ax2.set_ylim(top = 19)

# # ax2.set_ylabel("Cutoff Rigidty [GV]",color="blue",fontsize=13)
# # plt.savefig(Read.directory+'/plots/rc_vs_sf.png', dpi = 300, bbox_inches='tight')


    
# # #atmospheric depth plot
# # x_standard = x.iloc[0]
# # #x_era = atm_depth.x.iloc[0]
# # plt.ticklabel_format(useOffset=False)
# # plt.ylabel('standard - ERA40')
# # plt.xlabel('time [ma]')
# # plt.plot(time,x_standard-x_era, c = 'blue')
# # plt.savefig(Read.directory+'/plots/atm_residual', dpi = 300, bbox_inches='tight')

# #exposure age comparison w different atmospheric depth calculation

# # expage_std = [2466573.812240755,
# #   2023299.0465562146,
# #   2444888.3224641937,
# #   4553730.093643763,
# #   2815661.742382576,
# #   4558046.30932169,
# #   4129536.130928539,
# #   4370703.18758535,
# #   5147929.74150341,
# #   3284304.210058709,
# #   3574064.8522674884,
# #   3678847.610658329,
# #   3503468.9083244572,
# #   9826447.766671108,
# #   6690999.3511465965,
# #   10466508.118817024,
# #   9186317.233039252,
# #   9039952.58829612,
# #   2203962.164205366,
# #   2156751.2442309437]

# # expage_era40 = [1938440.7781959225,
# #   1580978.8403407035,
# #   1887920.3635395293,
# #   3423590.8721212395,
# #   2157731.039071558,
# #   3359987.614138326,
# #   3062171.5156887756,
# #   3318756.522474874,
# #   3863429.0543755232,
# #   2413123.865511337,
# #   2748475.9238908947,
# #   2816235.434936107,
# #   2673858.5996476803,
# #   7587676.481013189,
# #   5365592.334366433,
# #   8141846.771045497,
# #   7072698.131225801,
# #   6967076.575171458,
# #   1731835.9645246845,
# #   1737999.832930422]
# # plt.ylabel('exp_age era40')
# # plt.xlabel('exp_age std atm')

# # plt.plot([0,15*10**6], [0,15*10**6], 'k-') #1:1 line
# # plt.plot(expage_std,expage_era40,'o', color = 'darkmagenta')
# # plt.savefig(Read.directory+'/plots/atm_depth_expage_residual', dpi = 300, bbox_inches='tight')


# #Age comparison plot: Evenstar data, CPX.

# texp = [3060943,2420867,2996038,5626876,3466142,5550019,5054803,5421151,6343026,3975730,4503242,4602262
#   ,4368152,13030241,8703075,13958527,12118011,11914337,2696545,2660317]

# age250 = [2839161.7976549855,
#  2301862.116779193,
#  2811301.826025699,
#  5238892.278703601,
#  3239322.4409733815,
#  5240686.691514916,
#  4764029.0054370975,
#  5041761.411336673,
#  5822777.130696475,
#  3747196.379156443,
#  4086671.677934946,
#  4220536.545408334,
#  4001351.54136129,
#  10971879.937392477,
#  7566920.79039923,
#  11662836.030671537,
#  10313452.203257067,
#  10159133.243373051,
#  2521636.8086418966,
#  2469205.3393815313]


#FOR QUARTZ BELOW
texp = [3482009,2760335,3411507,6389973,3943729,6310070,5748965,6155450,7198966,4528601,5113348,5227171,4962226,14765193
,9867669,15815179,13732297,13502759,3070545,3026159]
age250 = [3472423.4290153407,
  2803426.12703357,
  3440260.0089757773,
  6210468.883134722,
  3941471.677105054,
  6199931.158187177,
  5784984.334458705,
  6036594.47367114,
  6840152.114310803,
  4621753.219224201,
  5044878.742110162,
  5208934.969623533,
  4941923.281071253,
  13047183.38954281,
  9169206.641035197,
  13862570.084416265,
  12278962.150294438,
  12099327.172749909,
  3085828.2737018084,
  3017938.615948302]

# # agemuons =[2299376.4962355015,
# #   2005097.1553156185,
# #   2294512.4758100417,
# #   4511658.6546481615,
# #   2764697.7612026543,
# #   4512914.162611268,
# #   4029413.1513461927,
# #   4277003.556080146,
# #   5033158.675264351,
# #   3257644.270266324,
# #   3516324.441128348,
# #   3540522.9335363014,
# #   3500185.831999511,
# #   9766021.61571931,
# #   6542896.4724914115,
# #   10298131.506059371,
# #   9041251.02480929,
# #   9007658.906741863,
# #   2046583.114626112,
# #   2035542.1304661129]

# updated_texp_qtz = []
# updated_texp_cpx = []
# muons_list = []
# for i in range(len(texp_qtz)): #convert ages from [yr] to [Ma]
#     updated_qtz = texp_qtz[i]/10**6
#     updated_texp_qtz.append(updated_qtz) #Evenstar data
#     updated_cpx = texp_cpx[i]/10**6 
#     updated_texp_cpx.append(updated_cpx)
    


# plt.plot([0,18], [0,18], 'k-') #1:1 line
# plt.rcParams["figure.figsize"] = [6,4] #update figure size
# # plt.axhline(y=1, color='k', linestyle='-')
# # plt.plot(ratio, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')

# plt.plot(updated_texp_qtz,updated_texp_cpx, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')
# #plt.plot(updated_texp,muons_list, 'x', c = 'black', label = 'w muons')
# plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
# plt.xlabel('CRONUS quartz', fontsize = 10)
# plt.ylabel('CRONUS cpx', fontsize = 10)
# plt.savefig(Read.directory+'CRONUs_comparison.png', dpi = 300, bbox_inches='tight')

updated_texp = []
updated_model_ages = []
for i in range(len(texp)): #convert ages from [yr] to [Ma]
    updated = texp[i]/10**6
    updated_texp.append(updated) #Evenstar data
    updated_model = age250[i]/10**6 
    updated_model_ages.append(updated_model) #this model
    #wmuons = agemuons[i]/10**6 
    
    #muons_list.append(wmuons) #con muons
ratio = []    
for i in range(len(updated_model_ages)):
    ratio.append(updated_model_ages[i]/updated_texp[i])


plt.plot([0,18], [0,18], 'k-') #1:1 line
plt.rcParams["figure.figsize"] = [6,4] #update figure size
# plt.axhline(y=1, color='k', linestyle='-')
# plt.plot(ratio, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')

plt.plot(updated_texp,updated_model_ages, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')
#plt.plot(updated_texp,muons_list, 'x', c = 'black', label = 'w muons')
plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
plt.title('Qtz')
plt.xlabel('Exposure Age [Ma] recalculated from Evenstar (2017)', fontsize = 10)
plt.ylabel('Exposure Age [Ma] from this Model', fontsize = 10)
plt.savefig(Read.directory+'expage_comparison_qtz.png', dpi = 300, bbox_inches='tight')


#USING ERA 40
# texp = [3188863,2560853,3166922,5939087,3670960,5942367,5413382,5710884,6680445,4267817,4712387,4825234,4580202,13646406,9082561,14562636,12643455,12447934,2823366,2784350]
# age250 = [2238677.182960314,
#  1744026.5586148114,
#  2179578.6323638153,
#  4260561.527570254,
#  2558132.410063256,
#  4164931.793416893,
#  3749418.3450232707,
#  4111740.7152837734,
#  4899611.557819584,
#  2924374.291220311,
#  3343289.3609476616,
#  3436760.939126842,
#  3243999.771813855,
#  9492375.017043112,
#  6422328.049597673,
#  10111423.73670608,
#  8863780.125665246,
#  8699638.116029948,
#  1962031.7206746638,
#  1984285.3107075954]
#SET DIRECTORY

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)

lifton_tm = pd.read_csv(directory+'/t_m.csv') #excel sheet with all pmag data. 0-70 Ma, all criteria

lifton_tm * 8.0648




