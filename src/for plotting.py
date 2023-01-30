#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:57:00 2022

@author: mmijjum
"""
import numpy as np

import matplotlib.pyplot as plt
import Read
import Pmag_paleolat
import scaling_factor
import glob
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)

"""
Figure 1
Rc vs. Scaling Factor
"""
# # FOR FIG 3.
# # create figure and axis objects with subplots()
# # in excel sheet: set every lat to 0-90, lon = 0, elevation = 0. Uncomment out the part of pmag that hard-codes the latitudes (so it doesn't vary w time)
# # only run for like 1 Ma, bc you're only gonna use the first value anyways.
# # note: make sure you hard code atm depth to 1033 g/cm2
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


"""
Figure 2
PALEOLAT FIGURE
"""

time = np.linspace(0,70,len(Pmag_paleolat.pl_df.iloc[0]))
# IN = Pmag_paleolat.pl_df.iloc[0]
# IN.to_csv(directory+'/plots/IN.csv') 
# sf_india = scaling_factor.Siteprod_df.iloc[0]
# sf_india.to_csv(directory+'/plots/sf_IN.csv') 

# SA = Pmag_paleolat.pl_df.iloc[1]
# SA.to_csv(directory+'/plots/SA.csv') 
# sf_sa = scaling_factor.Siteprod_df.iloc[1]
# sf_sa.to_csv(directory+'/plots/sf_SA.csv') 

# GL = Pmag_paleolat.pl_df.iloc[2]
# GL.to_csv(directory+'/plots/GL.csv') 
# sf_GL = scaling_factor.Siteprod_df.iloc[2]
# sf_GL.to_csv(directory+'/plots/sf_GL.csv') 

# AF = Pmag_paleolat.pl_df.iloc[3]
# AF.to_csv(directory+'/plots/AF.csv') 
# sf_AF = scaling_factor.Siteprod_df.iloc[3]
# sf_AF.to_csv(directory+'/plots/sf_AF.csv') 

fig, axs = plt.subplots(2, 2, figsize = (10,5), sharex = True)

axs[0, 1].plot(time,Read.IN.iloc[:,1]/Read.IN.iloc[0,1], 'royalblue')
axs[0, 1].set_title('India: 20N, 73E')
axs[1,1].plot(time,(Read.SA.iloc[:,1]+90)/(Read.SA.iloc[0,1]+90), 'mediumseagreen')
axs[1,1].set_title('South America: 19S, 69W')
axs[0,0].plot(time,Read.GL.iloc[:,1]/Read.GL.iloc[0,1], 'darkblue')
axs[0,0].set_title('Greenland: 75N, 42W')
axs[1,0].plot(time,(Read.AF.iloc[:,1]+90)/(Read.AF.iloc[0,1]+90), 'seagreen')
axs[1, 0].set_title('Africa: 0N, 20W')

fig.text(0.5,0.04, "Time [Ma]",size = 15, ha="center", va="center")
fig.text(0.05,0.5, "Change in paleolatitude (normalized)",size = 15, ha="center", va="center", rotation=90)
plt.savefig(directory+'/plots/paleolat_subplots.png', dpi = 300, bbox_inches='tight')


"""
Figure 3
MCADAM Model

"""



"""
Figure 4
Time varying field vs. Constant 
For present - 25 Ma and 40-65Ma
Including Muons

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
# exp_ages_time_varying_40 = [2168943.0556243784,
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
# exp_ages_constant_40 = [2990674.9547791057,
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
#  2056795.4435907109,
#  2555151.201061768,
#  5023786.798965172,
#  3036213.925069018,
#  5024321.868726578,
#  4531786.161718714,
#  4786715.492061025,
#  5546595.182462663,
#  3536620.176497739,
#  3802736.2381327846,
#  4025090.5900709876,
#  3784680.5793326064,
#  10552959.960047904,
#  7278845.120270775,
#  11285533.425735576,
#  10018403.433793591,
#  9791145.702431163,
#  2298236.0942358165,
#  2286441.4922106797]

# exp_ages_muons_const = [2804694.601454547,
#  2291451.7704243823,
#  2801180.6267542527,
#  5296654.495290533,
#  3288119.3619893105,
#  5303227.6317730425,
#  5001584.898952547,
#  5055488.738484894,
#  6024849.306097686,
#  3806980.741328083,
#  4262879.589419506,
#  4293269.676632794,
#  4050497.5906659523,
#  12263282.93816918,
#  8254035.283485948,
#  13040516.707969276,
#  11297650.29089213,
#  11257175.75048956,
#  2537307.567803689,
#  2518794.2504755203]
# exp_ages_muons_tv_40 = [2038507.3868198807,
#  1552945.6876126726,
#  2027140.7487187046,
#  3779870.455732829,
#  2292547.402327704,
#  3760589.539642837,
#  3300870.4321572417,
#  3750615.814442533,
#  4275850.4963406045,
#  2556564.699971064,
#  3033088.4983339314,
#  3047344.437869694,
#  3011135.556944223,
#  8531592.629825767,
#  5785438.910213004,
#  9052583.660561532,
#  8015061.925196326,
#  7791861.157506797,
#  1788967.6358008967,
#  1784318.6862023794]
# exp_ages_muons_const_40 = [2804694.601454547,
#  2291451.7704243823,
#  2801180.6267542527,
#  5296654.495290533,
#  3288119.3619893105,
#  5303227.6317730425,
#  5001584.898952547,
#  5055488.738484894,
#  6024849.306097686,
#  3806980.741328083,
#  4262879.589419506,
#  4293269.676632794,
#  4050497.5906659523,
#  12263282.93816918,
#  8254035.283485948,
#  13040516.707969276,
#  11297650.29089213,
#  11257175.75048956,
#  2537307.567803689,
#  2518794.2504755203]

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
    
#     updated_40 = exp_ages_time_varying_40[i]/10**6
#     updated_texp_tv_40.append(updated_40) #Evenstar data
#     updated_const_40 = exp_ages_constant_40[i]/10**6 
#     updated_texp_const_40.append(updated_const_40) #this model
    
#     updatedmuons = exp_ages_muons_tv[i]/10**6
#     updated_muons_tv.append(updatedmuons)
#     updatedmuonsconst = exp_ages_muons_const[i]/10**6
#     updated_muons_const.append(updatedmuonsconst)
    
#     updatedmuons_40 = exp_ages_muons_tv_40[i]/10**6
#     updated_muons_tv_40.append(updatedmuons_40)
#     updatedmuonsconst_40 = exp_ages_muons_const_40[i]/10**6
#     updated_muons_const_40.append(updatedmuonsconst_40)
#     #wmuons = agemuons[i]/10**6 
    

# plt.plot([0,18], [0,18], 'k-') #1:1 line
# plt.rcParams["figure.figsize"] = [6,4] #update figure size
# plt.plot(updated_texp_const,updated_texp_tv, 'o', c = 'darkblue', alpha = 0.7, label = '0-25 Ma')
# plt.plot(updated_texp_const_40,updated_texp_tv_40, 'o', c = 'darkgreen', alpha = 0.7, label = '40-65 Ma')
# plt.plot(updated_muons_const,updated_muons_tv, 'x', markersize = 3, c = 'cornflowerblue', label = '0-25 Ma w muons')
# plt.plot(updated_muons_const_40,updated_muons_tv_40, 'x', markersize = 3, c = 'mediumaquamarine', label = '40-65 Ma w muons')
# plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
# plt.xlabel('Exposure Age [Ma] constant field', fontsize = 10)
# plt.ylabel('Exposure Age [Ma] time-varying field', fontsize = 10)
# plt.savefig(Read.directory+'/plots/tv_constant_comparison.png', dpi = 300, bbox_inches='tight')


# #Age comparison plot: Evenstar data, CPX.

# texp = [3060943,2420867,2996038,5626876,3466142,5550019,5054803,5421151,6343026,3975730,4503242,4602262,4368152,13030241,8703075,13958527,12118011,11914337,2696545,2660317]

# age250 = [2768814.7852780037,
#  2248207.300541437,
#  2741539.525003936,
#  5107076.41764413,
#  3159569.0728202676,
#  5108018.95259798,
#  4640289.046260925,
#  4913645.370893386,
#  5706446.686550266,
#  3660411.029096094,
#  3983111.2540024156,
#  4112798.331950483,
#  3904084.2200530013,
#  10737925.276977753,
#  7381647.68935432,
#  11412837.334886586,
#  10087786.024035417,
#  9936179.90547212,
#  2461604.0058712866,
#  2411367.4649931323]

# # #FOR QUARTZ BELOW
# # texp = [3482009,2760335,3411507,6389973,3943729,6310070,5748965,6155450,7198966,4528601,5113348,5227171,4962226,14765193
# # ,9867669,15815179,13732297,13502759,3070545,3026159]
# # age250 = [3472423.4290153407,
# #   2803426.12703357,
# #   3440260.0089757773,
# #   6210468.883134722,
# #   3941471.677105054,
# #   6199931.158187177,
# #   5784984.334458705,
# #   6036594.47367114,
# #   6840152.114310803,
# #   4621753.219224201,
# #   5044878.742110162,
# #   5208934.969623533,
# #   4941923.281071253,
# #   13047183.38954281,
# #   9169206.641035197,
# #   13862570.084416265,
# #   12278962.150294438,
# #   12099327.172749909,
# #   3085828.2737018084,
# #   3017938.615948302]

# # # # agemuons =[2299376.4962355015,
# # # #   2005097.1553156185,
# # # #   2294512.4758100417,
# # # #   4511658.6546481615,
# # # #   2764697.7612026543,
# # # #   4512914.162611268,
# # # #   4029413.1513461927,
# # # #   4277003.556080146,
# # # #   5033158.675264351,
# # # #   3257644.270266324,
# # # #   3516324.441128348,
# # # #   3540522.9335363014,
# # # #   3500185.831999511,
# # # #   9766021.61571931,
# # # #   6542896.4724914115,
# # # #   10298131.506059371,
# # # #   9041251.02480929,
# # # #   9007658.906741863,
# # # #   2046583.114626112,
# # # #   2035542.1304661129]

# # # updated_texp_qtz = []
# # # updated_texp_cpx = []
# # # muons_list = []
# # # for i in range(len(texp_qtz)): #convert ages from [yr] to [Ma]
# # #     updated_qtz = texp_qtz[i]/10**6
# # #     updated_texp_qtz.append(updated_qtz) #Evenstar data
# # #     updated_cpx = texp_cpx[i]/10**6 
# # #     updated_texp_cpx.append(updated_cpx)
    


# # # plt.plot([0,18], [0,18], 'k-') #1:1 line
# # # plt.rcParams["figure.figsize"] = [6,4] #update figure size
# # # # plt.axhline(y=1, color='k', linestyle='-')
# # # # plt.plot(ratio, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')

# # # plt.plot(updated_texp_qtz,updated_texp_cpx, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')
# # # #plt.plot(updated_texp,muons_list, 'x', c = 'black', label = 'w muons')
# # # plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
# # # plt.xlabel('CRONUS quartz', fontsize = 10)
# # # plt.ylabel('CRONUS cpx', fontsize = 10)
# # # plt.savefig(Read.directory+'CRONUs_comparison.png', dpi = 300, bbox_inches='tight')
# expage_ERA40 = [1.031612, #north pole
# 0.991611, #greenland
# 0.992812,
# 0.910905,
# 0.646370,  
# 0.536337,  
# 0.528077, 
# 0.494504,  
# 0.646370,  
# 0.851704,  
# 1.008682]

# expage_STD = [1.000002,
# 0.997904,
# 0.969559,
# 0.857090,
# 0.650230,
# 0.507475,
# 0.467342,
# 0.507475,
# 0.650230,
# 0.857090,
# 1.000002]

# expage_ERA40_high = [2.432631 
# ,2.465787  
# ,2.383925  
# ,2.508120  
# ,1.667130  
# ,1.349848  
# ,1.266194  
# ,1.127579  
# ,1.667130  
# ,2.306703
# ,2.414015]
# expage_std_high = [2.471401  
# ,2.466886  
# ,2.403441  
# ,2.106326  
# ,1.529240  
# ,1.151732  
# ,1.052648  
# ,1.151732  
# ,1.529240 
# ,2.106326  
# ,2.471401]
  
# lat = [90,75
# ,60
# ,45
# ,30
# ,15
# ,0
# ,15
# ,30
# ,45
# ,90]

# plt.subplot(211)
# plt.scatter(expage_ERA40, expage_STD,c = lat, cmap = 'summer')
# plt.plot([0.4,1.1], [0.4,1.1], 'k-') #1:1 line

# plt.legend(loc = 'lower left', frameon=True)
# plt.subplot(212)
# plt.scatter(expage_ERA40_high, expage_std_high,c = lat, cmap = 'summer')
# plt.plot([1.1,2.5], [1.1,2.5], 'k-') #1:1 line

# plt.xlabel('Time [Ma]')
# plt.colorbar(orientation = 'horizontal')

# fig, ax = plt.subplots(2, 1, figsize=(10,7))
# fig.tight_layout()

# #define data
# x = [1, 2, 3]
# y = [7, 13, 24]

# #create subplots
# ax[0, 0].plot(x, y, color='red')
# ax[0, 1].plot(x, y, color='blue')
# ax[1, 0].plot(x, y, color='green')
# #ax[1, 1].plot(x, y, color='purple')
# # plt.rcParams["figure.figsize"] = [6,4] #update figure size

#  ages = 2251001.4948168835,
#  2746021.498019962,
#  5120846.0270699505,
#  3165211.6838768465,
#  5122645.927791952,
#  4652986.125227776,
#  4926242.573040874,
#  5720592.830853811,
#  3667993.691417608,
#  3991804.6579179233,
#  4122233.649873024,
#  3912322.928939883,
#  10786092.630398773,
#  7405516.385962273,
#  11465464.134077815,
#  10131692.238997385,
#  9979440.229284357,
#  2465042.7311924705,
#  2414299.133596048]

# ages_winc = [3017907.2222434254,
#  2446110.5750196436,
#  2998014.9641851885,
#  5581701.545085265,
#  3450635.580592478,
#  5601260.664281315,
#  5129254.571045523,
#  5361960.623092524,
#  6101296.302822712,
#  4017309.468494362,
#  4402782.894985831,
#  4524441.991818928,
#  4281140.839805374,
#  11662939.301209481,
#  8054193.267043953,
#  12358978.265612938,
#  10934511.109933846,
#  10790756.226796174,
#  2682791.360075334,
#  2587139.9225765336]

# updated_texp = []
# updated_texp_inc = []
# for i in range(len(ages)): #convert ages from [yr] to [Ma]
#     updated = ages[i]/10**6
#     updated_texp.append(updated) #Evenstar data
#     updated_winc = ages_winc[i]/10**6 
#     updated_texp_inc.append(updated_winc) #this model
#     #wmuons = agemuons[i]/10**6 
    

# plt.plot([0,18], [0,18], 'k-') #1:1 line
# plt.rcParams["figure.figsize"] = [6,4] #update figure size
# # plt.axhline(y=1, color='k', linestyle='-')
# # plt.plot(ratio, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')

# plt.plot(updated_texp_inc,updated_texp, 'o', c = 'darkmagenta', alpha = 0.5)
# plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
# #plt.title('Qtz')
# plt.xlabel('Exposure Age [Ma] using Rc w Inc', fontsize = 10)
# plt.ylabel('Exposure Age [Ma] using Rc without Inc', fontsize = 10)
# plt.savefig(Read.directory+'inc_comparison.png', dpi = 300, bbox_inches='tight')


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



# updated_texp = []
# updated_model_ages = []
# for i in range(len(texp)): #convert ages from [yr] to [Ma]
#     updated = texp[i]/10**6
#     updated_texp.append(updated) #Evenstar data
#     updated_model = age250[i]/10**6 
#     updated_model_ages.append(updated_model) #this model
#     #wmuons = agemuons[i]/10**6 
    
#     #muons_list.append(wmuons) #con muons
# ratio = []    
# for i in range(len(updated_model_ages)):
#     ratio.append(updated_model_ages[i]/updated_texp[i])


# plt.plot([0,18], [0,18], 'k-') #1:1 line
# plt.rcParams["figure.figsize"] = [6,4] #update figure size
# # plt.axhline(y=1, color='k', linestyle='-')
# # plt.plot(ratio, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')

# plt.plot(updated_texp,updated_model_ages, 'o', c = 'darkmagenta', alpha = 0.5, label = 'without muons')
# #plt.plot(updated_texp,muons_list, 'x', c = 'black', label = 'w muons')
# plt.legend(frameon = True,facecolor='white',framealpha=1, fontsize = 10)
# plt.xlabel('Exposure Age [Ma] recalculated from Evenstar (2017)', fontsize = 10)
# plt.ylabel('Exposure Age [Ma] from this Model', fontsize = 10)
# plt.savefig(Read.directory+'expage_comparison_updated.png', dpi = 300, bbox_inches='tight')


# #USING ERA 40
# # texp = [3188863,2560853,3166922,5939087,3670960,5942367,5413382,5710884,6680445,4267817,4712387,4825234,4580202,13646406,9082561,14562636,12643455,12447934,2823366,2784350]
# # age250 = [2238677.182960314,
# #  1744026.5586148114,
# #  2179578.6323638153,
# #  4260561.527570254,
# #  2558132.410063256,
# #  4164931.793416893,
# #  3749418.3450232707,
# #  4111740.7152837734,
# #  4899611.557819584,
# #  2924374.291220311,
# #  3343289.3609476616,
# #  3436760.939126842,
# #  3243999.771813855,
# #  9492375.017043112,
# #  6422328.049597673,
# #  10111423.73670608,
# #  8863780.125665246,
# #  8699638.116029948,
# #  1962031.7206746638,
# #  1984285.3107075954]
# #SET DIRECTORY

# import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# directory = os.path.dirname(__file__)

# lifton_tm = pd.read_csv(directory+'/t_m.csv') #excel sheet with all pmag data. 0-70 Ma, all criteria

# lifton_tm * 8.0648




