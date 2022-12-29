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

# time = User_Interface.time
# #This is testing using the Evenstar Dataset. 
# #FOR 0-25MA
# age50 = [2971311.246952437,
#  2362277.701548732,
#  2901703.541346414,
#  5415056.032983044,
#  3349631.9695656137,
#  5320983.353249119,
#  4846143.258819517,
#  5257945.032297412,
#  5987385.230717548,
#  3758573.2692336785,
#  4323651.450348153,
#  4437378.819503102,
#  4199954.225754401,
#  11400320.014650974,
#  7919416.911722029,
#  12103090.11544189,
#  10709149.041244345,
#  10534169.563039424,
#  2623464.7847683122,
#  2649455.685785593] #using 50 ka bins

# age250 = [2993214.8424117323,
#  2395932.918747693,
#  2923483.550604781,
#  5423396.039378376,
#  3369167.539136676,
#  5337558.104944664,
#  4868379.949897415,
#  5280608.276862493,
#  6033284.631505403,
#  3794518.978712607,
#  4341883.120046434,
#  4456443.562712103,
#  4227777.278522666,
#  11440236.98287091,
#  7929865.373103894,
#  12139811.440195149,
#  10745168.442814156,
#  10571245.699758459,
#  2646646.032687678,
#  2673997.688186752] #using 250 ka bins.


# # #FOR 40-65MA
# age50z = [2322222.0197343845,
#  1827003.7180525255,
#  2236332.73211175,
#  4088426.636282565,
#  2576783.4195228834,
#  3921153.933296707,
#  3587126.381608773,
#  3981091.0425009327,
#  4623998.620604362,
#  2814588.7760927277,
#  3382878.185449054,
#  3425614.41611594,
#  3258087.635618077,
#  9197530.90823805,
#  6275536.489532302,
#  9819943.027370123,
#  8570076.817017611,
#  8410296.476118937,
#  2045676.7612999033,
#  2092838.0987445342]


# age250z = [2320533.4945277083,
#  1825404.4705576631,
#  2234695.3313709847,
#  4088606.2961509074,
#  2575048.4839829234,
#  3920450.4433039473,
#  3586202.038521137,
#  3980404.076482722,
#  4624808.763162866,
#  2812797.8861436825,
#  3381735.5368374395,
#  3424265.079602525,
#  3257230.4243190503,
#  9202774.434686912,
#  6279701.375988659,
#  9823559.688011322,
#  8575417.423164926,
#  8415798.656272536,
#  2044203.986013726,
#  2091393.189669876]
# #plt.plot([0,15*10**4], [0,15*10**4], 'k-') #1:1 line

# # plt.ylabel('250ka resolution_evenstar')
# # plt.xlabel('50ka resolution_evenstar')

# # plt.plot(age50,age250, 'o', c = 'darkmagenta', label = '0-25Ma')
# # plt.plot(age50z,age250z, 'x', c = 'blue', label = '40-65Ma')

# # plt.legend()


# # plt.savefig(Read.directory+'/plots/exposure_age_residual_50_250.png', dpi = 300, bbox_inches='tight')

# xx = []

# for i in range(len(age50)):
#     xaxis = age250[i]-age50[i]
#     xx.append(xaxis)
# plt.xlabel('sample')
# plt.ylabel('Exposure Age Difference (250ka - 50ka)')
# plt.plot(xx, 'o-',  c = 'darkmagenta', label = '0-25Ma')
# plt.savefig(Read.directory+'/plots/exposure_age_difference_50_250.png', dpi = 300, bbox_inches='tight')


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



texp = [3060943,2420867,2996038,5626876,3466142,5550019,5054803,5421151,6343026,3975730,4503242,4602262
,4368152,13030241,8703075,13958527,12118011,11914337,2696545,2660317]
# texp = [4197679.828104344,
#  3455424.000412428,
#  4226492.030579648,
#  7753362.767842709,
#  4856950.376209599,
#  7938710.364720283,
#  7251584.965039427,
#  7452892.006529261,
#  8685641.769860847,
#  5823325.782328345,
#  5974112.762194599,
#  6240883.63318949,
#  5933470.90506114,
#  17307741.84581011,
#  11657446.497614004,
#  18578470.314534005,
#  16154653.24253609,
#  15909366.330485975,
#  3754185.6684603393,
#  3627425.916630392]
age250 = [2466573.812240755,
 2023299.0465562146,
 2444888.3224641937,
 4553730.093643763,
 2815661.742382576,
 4558046.30932169,
 4129536.130928539,
 4370703.18758535,
 5147929.74150341,
 3284304.210058709,
 3574064.8522674884,
 3678847.610658329,
 3503468.9083244572,
 9826447.766671108,
 6690999.3511465965,
 10466508.118817024,
 9186317.233039252,
 9039952.58829612,
 2203962.164205366,
 2156751.2442309437]

# age250 = [2143960.738490931,
#  1699470.2343283473,
#  2078702.1797437218,
#  3813311.8362104376,
#  2388567.9931456954,
#  3669361.8154165945,
#  3351764.675811082,
#  3678873.26543266,
#  4287379.351837229,
#  2633145.231430142,
#  3144082.165634465,
#  3172574.5417126417,
#  3016300.2298713233,
#  8798449.768000104,
#  5895084.059390719,
#  9394994.368748724,
#  8169288.088480698,
#  8031861.911606273,
#  1895304.9576729217,
#  1868696.6720632373]

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
agemuons = [3052380.7599469335,
 2524705.0518794283,
 3045508.6863120026,
 5776838.289361357,
 3541264.30894785,
 5776158.621180296,
 5286899.057752335,
 5540581.670815879,
 6295060.323451763,
 4255440.531700552,
 4540282.009104363,
 4768279.0658564605,
 4518056.7015403705,
 12252882.68380556,
 8512187.238517111,
 13005016.133362273,
 11506267.366353476,
 11275084.089055385,
 2776825.1058773575,
 2762188.5260250615]

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
#plt.plot(updated_texp,muons_list, 'x', c = 'black', label = 'w muons')
plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
plt.xlabel('Exposure Age [Ma] recalculated from Evenstar (2017)', fontsize = 10)
plt.ylabel('Exposure Age [Ma] This Work', fontsize = 10)
plt.savefig(Read.directory+'/plots/exposure_age_residual_cpx.png', dpi = 300, bbox_inches='tight')

# field_10 = [4137561.470427894,
#  3389188.9681463917,
#  4187909.0315092714,
#  7800267.218141239,
#  4849928.224001935,
#  8014626.742578083,
#  7314357.959473717,
#  7486193.693488222,
#  8735362.047513835,
#  5846523.41695823,
#  5973237.424855271,
#  6256325.052575388,
#  5942671.373624589,
#  17163743.871485114,
#  11672630.785640502,
#  18299675.89058697,
#  16044053.834104,
#  15816970.335515054,
#  3686254.7695530704,
#  3555621.7932638833]

# field_5 = [2656072.472504465,
#  2104813.529893542,
#  2624197.2342243255,
#  4985950.33306519,
#  3055130.745687083,
#  4946352.7170157535,
#  4502553.7076829905,
#  4808611.028005859,
#  5633744.570280622,
#  3526117.08461439,
#  3932690.8870730386,
#  4051360.1106643374,
#  3842204.149559848,
#  11497242.778787952,
#  7685129.533408722,
#  12287564.987748863,
#  10684080.92060481,
#  10506944.724692479,
#  2336599.4324931167,
#  2309136.3981573954]

# field_6 = [2979237.865790831,
#  2379528.210993337,
#  2960081.637857734,
#  5597242.303310371,
#  3440870.1581671736,
#  5598211.788069728,
#  5098256.782149096,
#  5386618.69125854,
#  6306200.353625106,
#  4012772.3630608553,
#  4390884.667344007,
#  4536517.111710038,
#  4302760.58977406,
#  12796269.736636773,
#  8571042.214202344,
#  13668397.696695087,
#  11895292.955342965,
#  11704882.67847606,
#  2629322.3182272064,
#  2577671.193280687]

# field_9 = [3802866.6403219053,
#  3104256.2605916546,
#  3839038.4158065817,
#  7158046.475407847,
#  4445744.207286981,
#  7329218.751358475,
#  6688870.092038802,
#  6888387.292543329,
#  8038380.712525239,
#  5334235.435065418,
#  5489668.809697852,
#  5747201.633983728,
#  5457427.030292566,
#  15880623.534001261,
#  10753337.616795797,
#  16953492.92917807,
#  14820464.401073366,
#  14598984.144014277,
#  3382309.2075525736,
#  3289871.926608834]

# updated_9 = []
# updated_6 = []

# for i in range(len(field_6)): #convert ages from [yr] to [Ma]
#     updated = field_9[i]/10**6
#     updated_9.append(updated) #Evenstar data
#     updated_model = field_6[i]/10**6 
#     updated_6.append(updated_model) #this model
   

# plt.plot([0,18], [0,18], 'k-') #1:1 line
# plt.rcParams["figure.figsize"] = [6,4] #update figure size
# plt.plot(updated_9,updated_6, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')
# #plt.plot(updated_texp,muons_list, 'x', c = 'black', label = 'w muons')
# plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
# plt.xlabel('Exposure Age [Ma] recalculated from Evenstar (2017)', fontsize = 10)
# plt.ylabel('Exposure Age [Ma] This Work', fontsize = 10)
# plt.savefig(Read.directory+'/plots/hard_coded_paleointensity_6v9.png', dpi = 300, bbox_inches='tight')

