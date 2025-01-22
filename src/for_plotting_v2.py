#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:43:47 2024

@author: mmijjum
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)

"""
Figure 1
Rc vs. Scaling Factor

Before running this code: 
    
1) in excel sheet: set every lat to 0-90, lon = 0, elevation = 0
2) Make sure pmag_paleolat is hard-coded to not vary w/ time. 
3) Only run for ~1 Ma, bc you're only gonna use the first value anyways.
4) In atmospheric depth plot - hard code to 1033 g/cm2
5) You need to run it for Rc: M_modern, then M_half. 
    Save the Rc dataframes as Rc_full and Rc_half.
"""

##Read in necessary dataframes
# Rc_full = pd.read_csv(directory+'/text_for_plots/Rc_full.csv', header = None)
# Rc_half = pd.read_csv(directory+'/text_for_plots/Rc_half.csv', header = None)

# sf_full = pd.read_csv(directory+'/text_for_plots/sf_full.csv', header = None)
# sf_half = pd.read_csv(directory+'/text_for_plots/sf_half.csv', header = None)

# paleolatitudes = np.arange(0,91,2) #set x-axis
# fig,ax = plt.subplots()

# #make a plot with different y-axis using second axis object
# ax.plot(paleolatitudes, Rc_full[1][1:],linewidth = 2.5, color="#016c59")
# ax.plot(paleolatitudes, Rc_half[1][1:],linewidth = 2.5, color="#016c59", linestyle = '-.')

# ax.set_ylim(top = 15)

# ax.set_ylabel("Cutoff Rigidity (GV)",
#               color="#016c59",
#               fontsize=13)
# ax.set_xlabel("Geomagnetic Latitude", fontsize = 13)
# ax.spines['left'].set_color('#016c59')
# ax.tick_params(axis='y', colors='#016c59')

# # twin object for two different y-axis on the sample plot
# ax2=ax.twinx()
# ax2.plot(paleolatitudes, sf_half[1][1:], linewidth = 2.5,
#         color="#67a9cf", linestyle = '-.', label = "$M_{half}$")
# ax2.plot(paleolatitudes, sf_full[1][1:],linewidth =2.5,
#         color="#67a9cf", label = "$M_{present}$")


# # set x-axis label
# # set y-axis label
# ax2.set_xlim(left=0)
# ax2.set_xlim(right=90)
# ax2.set_ylabel("Scaling Factor",color="#67a9cf",fontsize=13)
# ax2.tick_params(axis='y', colors='#67a9cf')

# ax2.legend(loc = 'right')

# plt.savefig(directory+'/plots_updated/Figure_2.pdf', dpi = 300, bbox_inches='tight')

"""
Figure 2
Paleolatitude 

Before running this code: 
    1)The relevant CSV files are already saved. Unless you are changing them, you don't need to re-run the code at all. If you are re-running:
    2)Set inputs to 'Figure 2' sheet.
    3) Make sure pmag_paleolat is time-varying.
    4) You'll need to change the plate variable in the spreadsheet as needed. 
"""
## The following lines will re-make the necessary CSV files. Unless you are changing them- DO NOT RE-RUN
## IN = Pmag_paleolat.pl_df.iloc[0]
## IN.to_csv(directory+'/text_for_plots/IN.csv') 


## SA = Pmag_paleolat.pl_df.iloc[1]
## SA.to_csv(directory+'/text_for_plots/SA.csv') 
 

## GL = Pmag_paleolat.pl_df.iloc[2]
## GL.to_csv(directory+'/text_for_plots/GL.csv') 


## AF = Pmag_paleolat.pl_df.iloc[3]
## AF.to_csv(directory+'/text_for_plots/AF.csv') 
    
#Begin uncommenting!

##Read in text files:
# IN = pd.read_csv(directory+'/text_for_plots/IN.csv')
# SA = pd.read_csv(directory+'/text_for_plots/SA.csv')
# GL = pd.read_csv(directory+'/text_for_plots/GL.csv')
# AF = pd.read_csv(directory+'/text_for_plots/AF.csv')

# time = np.linspace(0,70,281) #set X-axis

# fig = plt.figure(figsize=(10.5, 8.5))
# spec = fig.add_gridspec(3,3)
# fig.text(0.06, 0.65, 'Normalized paleolatitude', va='center', rotation='vertical', size =15)
# fig.text(0.45, 0.34, 'Time (Ma)', va='center', rotation='horizontal', size =15)

# time = np.arange(0,70+0.25,0.25)
# ax0 = fig.add_subplot(spec[0, :])
# ax0.plot(time,IN.iloc[:,1]/IN.iloc[0,1], linewidth = 2.5, c = 'royalblue', label = 'India (20N, 73E)')
# ax0.plot(time,GL.iloc[:,1]/GL.iloc[0,1], linewidth = 2.5, c = 'mediumorchid')
# ax0.plot(time,(SA.iloc[:,1]+90)/(SA.iloc[0,1]+90), linewidth = 2.5, c = 'darkblue')
# ax0.plot(time,(AF.iloc[:,1]+90)/(AF.iloc[0,1]+90), linewidth = 2.5, c = 'mediumseagreen')
# ax0.text(65,0, 'A', fontsize = 22)

# plt.axhspan(0.85, 1.1, xmin=0, xmax=1, color = 'gray', alpha = 0.5)

# ax0.set_xlim(0, 70)
# plt.legend()
# #annotate_axes(ax0, 'ax0')

# ax10 = fig.add_subplot(spec[1, :])
# ax10.plot(time,GL.iloc[:,1]/GL.iloc[0,1], linewidth = 2.5, c = 'mediumorchid', label = 'Greenland (75N, 42W)')
# ax10.plot(time,(SA.iloc[:,1]+90)/(SA.iloc[0,1]+90), linewidth = 2.5, c = 'darkblue', label = 'Northern Chile (19S, 69W)')
# ax10.plot(time,(AF.iloc[:,1]+90)/(AF.iloc[0,1]+90), linewidth = 2.5, c = 'mediumseagreen', label = 'South Africa (31S, 22E)')
# ax10.set_xlim(0, 70)
# ax10.text(65,0.93, 'B', fontsize = 22)

# plt.legend()
# plt.savefig(directory+'/plots/Figure_4.png', dpi = 300, bbox_inches='tight')

"""
Figure 3
Workflow figure - not coded
"""


"""
Figure 4
MCADAM Model - Katie Bristol

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

##Read in necessary text:
# sf_50kyr = pd.read_csv(directory+'/text_for_plots/sf_50kyr.csv')
# sf_250ka = pd.read_csv(directory+'/text_for_plots/sf_250ka.csv')
# sf_1ma = pd.read_csv(directory+'/text_for_plots/sf_1ma.csv')

# #Start uncommenting:
# time1 =  np.arange(2,70.05,0.05)
# time2=  np.arange(2,70.05,0.25)

# x_temp = sf_50kyr.iloc[:,1]
# x = x_temp[40::] # remove first 2 Ma post LSDn update
# plt.rcParams["figure.figsize"] = [5,4] #update figure size 

# w = 0.02
# plt.ylim(0,0.6)
# data = sf_250ka.iloc[8:,1].repeat(5).reset_index(drop=True).iloc[4:].reset_index(drop=True)/x.reset_index(drop=True)
# data2= sf_250ka.iloc[8:,1].reset_index(drop=True)/sf_1ma.iloc[2:,1].repeat(4).reset_index(drop=True).iloc[3:].reset_index(drop=True)
# x, bins, p = plt.hist(data,  bins=np.arange(min(data), max(data) + w, w), density = True,color = '#014636', label = 'SF(250 kyr) : SF(50 kyr)')
# y, bins, q = plt.hist(data2,bins=np.arange(min(data2), max(data2) + w, w), density = True, color = '#3690c0', alpha = 0.7, label = 'SF(250 kyr): SF(1000 kyr)')

# for item in p:
#     item.set_height(item.get_height()/sum(x))
# for item in q:
#     item.set_height(item.get_height()/sum(y))
# plt.legend(bbox_to_anchor=(0, 0.2), prop={'size':9}, loc = 'lower left')
# plt.xlabel('Scaling factor ratio', fontsize = 13)
# plt.ylabel('Normalized number of occurrences', fontsize = 13)
# plt.savefig(directory+'/plots_updated/Figure_5_newbins.svg', dpi = 300, bbox_inches='tight')

"""
FIGURE 6

Scaling factor TV and Constant

"""


# # #DONT RUN THIS PART UNLESS YOU CHANGE DATA
# sf_india = scaling_factor.Siteprod_df.iloc[0]
# sf_india.to_csv(directory+'/text_for_plots/sf_IN.csv') 
# sf_india_const = scaling_factor.Siteprod_df.iloc[0]
# sf_india_const.to_csv(directory+'/text_for_plots/sf_IN_const.csv') 
# sf_india_tvfieldonly = scaling_factor.Siteprod_df.iloc[0]
# sf_india_tvfieldonly.to_csv(directory+'/text_for_plots/sf_india_tvfieldonly.csv') 
# sf_india_tvlatonly = scaling_factor.Siteprod_df.iloc[0]
# sf_india_tvlatonly.to_csv(directory+'/text_for_plots/sf_india_tvlatonly.csv') 

##RELEVANT TEXT FILES
sf_sigma75 = pd.read_csv(directory+'/text_for_plots_updated/sf_sigma75.csv', header = None)
sf_sigma25= pd.read_csv(directory+'/text_for_plots_updated/sf_sigma25.csv', header = None)
sf_regular_sigma = pd.read_csv(directory+'/text_for_plots_updated/sf_regular_sigma.csv', header = None)
sf_constant_sigma= pd.read_csv(directory+'/text_for_plots_updated/sf_constant_sigma.csv', header = None)

sf_tvfieldonly_25sigma = pd.read_csv(directory+'/text_for_plots_updated/sf_tvfield_only_25sigma.csv', header = None)
sf_tvfieldonly_75sigma = pd.read_csv(directory+'/text_for_plots_updated/sf_tvfield_only_75sigma.csv', header = None)
sf_tvfieldonly_sigma = pd.read_csv(directory+'/text_for_plots_updated/sf_tvfield_only_sigma.csv', header = None)
sf_tvlatonly_sigma= pd.read_csv(directory+'/text_for_plots_updated/sf_tvlatonly_sigma.csv', header = None)

sig75 = sf_sigma75.iloc[1][9:].reset_index(drop=True)
sig25 = sf_sigma25.iloc[1][9:]
median =sf_regular_sigma.iloc[1][9:]
const = sf_constant_sigma.iloc[1][9:]

tvfield_25 = sf_tvfieldonly_25sigma.iloc[1][9:]
tvfield_75 = sf_tvfieldonly_75sigma.iloc[1][9:]
tvfield_avg = sf_tvfieldonly_sigma.iloc[1][9:]
tvlat = sf_tvlatonly_sigma.iloc[1][9:]

# # #coding
# time = np.linspace(2,70,273)
# f = plt.figure(figsize=(15,6))
# ax = f.add_subplot(121)
# ax2 = f.add_subplot(122)
# ax.plot(time,median, linewidth = 2, c = '#016c59',label = 'time-varying field and latitude')
# ax.plot(time,const, '--',linewidth = 2.5,c = 'black', label = 'constant field and latitude')
# ax.fill_between(time, sig75, median,  color = '#a6bddb', alpha = 0.5)
# ax.fill_between(time, median, sig25, color =  '#a6bddb', alpha = 0.5)

# ax.set_xlim(2,70)
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


# ax2.set_xlim(2,70)
# ax2.vlines(66.052, 0.50, 0.95,linewidth = 2.5)
# ax2.set_xlabel('Time (Ma)', fontsize = 15)
# ax2.legend(loc = 'lower left', fontsize = 13)
# plt.setp(ax2.get_yticklabels(), visible=False)
# plt.savefig(directory+'/plots_updated/Figure_8_LSDn.svg', dpi = 300, bbox_inches='tight')


"""
Figure 7: Atmospheric depth comparison

"""
# NA_ERA40 =  pd.read_csv(directory+'/text_for_plots_updated/sf_ERA40_NA.csv', header = None)
# NA_STD = pd.read_csv(directory+'/text_for_plots_updated/sf_STD_NA.csv', header = None)
# NA_climate = pd.read_csv(directory+'/text_for_plots_updated/sf_climate_NA.csv', header = None)

# EC_ERA40 =  pd.read_csv(directory+'/text_for_plots_updated/sf_ERA40_EQ.csv', header = None)
# EC_STD = pd.read_csv(directory+'/text_for_plots_updated/sf_STD_EQ.csv', header = None)
# EC_climate = pd.read_csv(directory+'/text_for_plots_updated/sf_climate_EQ.csv', header = None)

#START RUN#
# from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,mark_inset)
# import matplotlib.patches as patches


# alt = np.arange(0,5001,500)


# fig, ax1 = plt.subplots()
# ax1.set_aspect('equal')
# ax1.plot(NA_STD.iloc[1:][1],NA_ERA40.iloc[1:][1], 'o-',  linewidth = 2, markersize = 4, label = 'High latitude: 65N,130W ', c = '#014636')
# ax1.plot(EC_STD.iloc[1:][1],EC_ERA40.iloc[1:][1], 'o-',  linewidth = 2,   markersize = 4,label = 'Equator: 0N, 70W' , c = '#67a9cf')
# ax1.plot(NA_STD.iloc[1:][1],NA_climate.iloc[1:][1], 'x-',  linewidth = 2, markersize = 4, label = 'High latitude: 65N,130W ', c = '#014636')
# ax1.plot(EC_STD.iloc[1:][1],EC_climate.iloc[1:][1], 'x-',  linewidth = 2,   markersize = 4,label = 'Equator: 0N, 70W' , c = '#67a9cf')


# plt.grid()
# ax1.set_ylabel('Scaling factor')
# ax1.set_xlabel('Scaling factor using standard atmosphere')

# ax1.set_ylim(0,46)
# ax1.set_xlim(0,46)

# rect = patches.Rectangle((0, 0), 5, 5, linewidth=1, edgecolor='k', facecolor='none')
# ax1.add_patch(rect)

# left, bottom, width, height = [0.53, 0.2, 0.20, 0.25] # modify to move the inset curve and change its size
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(NA_STD.iloc[1:][1],NA_ERA40.iloc[1:12][1], 'o-',  linewidth = 2, markersize = 4, label = 'High latitude: 65N,130W ', c = '#014636')
# ax2.plot(EC_STD.iloc[1:][1],EC_ERA40.iloc[1:12][1], 'o-',  linewidth = 2,   markersize = 4,label = 'Equator: 0N, 70W' , c = '#67a9cf')
# ax2.plot(NA_STD.iloc[1:][1],NA_climate.iloc[1:][1], 'x-',  linewidth = 2, markersize = 4, label = 'High latitude: 65N,130W ', c = '#014636')
# ax2.plot(EC_STD.iloc[1:][1],EC_climate.iloc[1:][1], 'x-',  linewidth = 2,   markersize = 4,label = 'Equator: 0N, 70W' , c = '#67a9cf')

# ax2.set_xlim(0,5)
# ax2.set_ylim(0,5)
# ax2.set_xticks([0, 2,4])
# ax2.set_yticks([0,2,4])
# ax2.tick_params(axis='both', which='major', labelsize=8)
# plt.grid()
# plt.savefig(directory+'/plots_updated/Figure_8A_UPDATED_LSDn.svg', dpi = 300, bbox_inches='tight')


"""
Figure 8

"""
# t_cpx_tv = [127752.60582088573,
#   984162.1262581163,
#   2846306.534078561,
#   1389258.6673328548,
#   1549441.746161166,
#   2294728.6111806347,
#   2844070.84976501,
#   5353463.085910166,
#   807436.4674610357,
#   1002228.8745564914,
#   3293469.9260718096,
#   5413073.649512974,
#   4943551.208225091,
#   5135940.5731570255,
#   5882650.872377071,
#   3873433.6755535025,
#   4182366.18996209,
#   4324353.079607126,
#   4089837.416285006,
#   11246508.157481706,
#   7743930.472061706,
#   11913493.74941639,
#   10516680.128945855,
#   10377958.617091846,
#   2522442.7358753113,
#   2445980.9338783138,
#   1881330.9255949694,
#   2051482.2947345783]

# t_cpx_const = [127752.60582088573,
#   982938.6283601706,
#   2823872.504616442,
#   1386949.4050687125,
#   1547454.4614787283,
#   2298908.187435368,
#   2821797.558898027,
#   5213497.319342755,
#   806348.433833418,
#   1000877.8486951116,
#   3256422.9995765956,
#   5267882.395433342,
#   4807325.211794432,
#   4998631.612932419,
#   5832825.882157335,
#   3825717.167711228,
#   4109260.5920640165,
#   4234613.111664737,
#   4024083.97419149,
#   11813662.060701597,
#   7888245.238179045,
#   12595789.920927303,
#   10947157.078291597,
#   10789453.634880532,
#   2514814.5419891,
#   2440636.963800355,
#   1877862.9480487357,
#   2049646.747968753]

# t_qtz_tv = [896206.7939181189,
#   878362.8383798527,
#   264920.88340950105,
#   119327.3182085496,
#   305815.4862325982,
#   214126.51362611144,
#   254566.77723230896,
#   38432.06112115359,
#   2067064.7696490448,
#   2166753.3414753093,
#   3120090.070754946,
#   6117941.457308308,
#   3030371.057439765,
#   2141039.718231983]

# t_qtz_const = [894741.236792822,
#   877261.2605537559,
#   264536.2818474675,
#   119169.91504834245,
#   305328.05832091457,
#   213764.21265166433,
#   254112.23894512616,
#   38381.03331259172,
#   2066166.0363766595,
#   2169267.513283057,
#   3084961.8988671782,
#   6128553.283178382,
#   2999279.319739138,
#   2142478.114128847]

# t_dunai_tv = [16524682.549915295,
#   17721159.12246139,
#   13845053.762400333,
#   25122608.267600313,
#   16711310.349630775,
#   18319319.274463803,
#   11937258.750470864,
#   8186263.304041222,
#   18225857.87550319,
#   11832166.288678875,
#   15234183.823739847,
#   19261987.023456745,
#   14561757.108731031,
#   75460.79868235035,
#   134862.2990977344,
#   95322.09078681619] 

# t_dunai_const = [17870040.916582223,
#   19299357.1962142,
#   14878644.337580388,
#   28293127.746684644,
#   18053607.726645924,
#   20054493.351199094,
#   12577398.339739406,
#   8370530.568907558,
#   19934403.834506948,
#   12454699.876934445,
#   16510438.676682878,
#   21267356.52900423,
#   15757445.146939285,
#   75335.3700115672,
#   134624.70173269822,
#   95187.07363615221]

# updated_texp_tv = []
# updated_texp_const = []
# diff_tv_pyx = []
# perdif_ev = []

# for i in range(len(t_cpx_const)): #convert ages from [yr] to [Ma]
#     updated = t_cpx_tv[i]/10**6
#     updated_texp_tv.append(updated) #Evenstar data
#     updated_const = t_cpx_const[i]/10**6 
#     updated_texp_const.append(updated_const) #this model
#     temp = updated - updated_const
#     diff_tv_pyx.append(temp)
#     perdif_ev.append((temp/updated_const)*100)

# updated_neon_tv = []
# updated_neon_const = []
# diff_tv_qtz = []
# perdifneon = []

# for i in range(len(t_qtz_tv)): #convert ages from [yr] to [Ma]
#     updatedneontv = t_qtz_tv[i]/10**6
#     updated_neon_tv.append(updatedneontv)
#     updatedneonconst = t_qtz_const[i]/10**6
#     updated_neon_const.append(updatedneonconst)
#     temp = updatedneontv - updatedneonconst
#     diff_tv_qtz.append(temp)
#     perdifneon.append((temp/updatedneonconst)*100)
    
# updated_dunai_const = []
# updated_dunai = []
# diff_tv_dunai = []
# perdif = []

# for i in range(len(t_dunai_tv)):
#     updated_dunaix = t_dunai_tv[i]/10**6
#     updated_dunai_constx = t_dunai_const[i]/10**6
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

# ax2.plot(updated_neon_const[0:9], diff_tv_qtz[0:9], 's', c ='teal', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 1')
# ax2.plot(updated_neon_const[9:11], diff_tv_qtz[9:11], 's', c='limegreen', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 2')
# ax2.plot(updated_neon_const[11:14], diff_tv_qtz[11:14], 's', c='royalblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 3')
# ax2.plot(updated_neon_const[13], diff_tv_qtz[13], 's', c='deepskyblue', alpha = 0.7,markersize = 8,label = '$^{21}Ne$ - Surface 5')

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

# ax1.plot(updated_texp_const[0:4],updated_texp_tv[0:4], 'o', c='limegreen', alpha = 0.7,markersize = 8)
# ax1.plot(updated_texp_const[4:17],updated_texp_tv[4:17], 'o', c = 'royalblue', alpha = 0.7,markersize = 8)
# ax1.plot(updated_texp_const[17:26],updated_texp_tv[17:26], 'o', c = 'deepskyblue',alpha = 0.7, markersize = 8)

# ax1.plot(updated_neon_const[0:9], updated_neon_tv[0:9],  's', c = 'teal', alpha = 0.7,markersize = 8)
# ax1.plot(updated_neon_const[9:11], updated_neon_tv[9:11],  's', c='limegreen', alpha = 0.7,markersize = 8)
# ax1.plot(updated_neon_const[11:14], updated_neon_tv[11:14], 's', c='royalblue',alpha = 0.7, markersize = 8)
# ax1.plot(updated_neon_const[13], updated_neon_tv[13],  's', c='deepskyblue', alpha = 0.7,markersize = 8)

# ax1.plot(updated_dunai_const[0:5],updated_dunai[0:5], 's', c='midnightblue',alpha = 0.7, markersize = 8)
# ax1.plot(updated_dunai_const[5:9],updated_dunai[5:9], 's', c='purple',alpha = 0.7,markersize =8)
# ax1.plot(updated_dunai_const[9:13],updated_dunai[9:13], 's', c='mediumpurple',alpha = 0.7, markersize = 8)
# ax1.plot(updated_dunai_const[13:15],updated_dunai[13:15], 's', c='skyblue', alpha = 0.7,markersize =8)
# ax1.plot(updated_dunai_const[15:16],updated_dunai[15:16], 's', c='hotpink', alpha = 0.7,markersize = 8)

# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 14)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)

# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 13)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 13)
#plt.savefig(directory+'/plots_updated/new_fig_9.svg', dpi = 300, bbox_inches='tight')

"""
FIGURE 10
"""
# t_cpx_tv = [127752.60582088573,
#  984162.1262581163,
#  2917654.856010612,
#  1389258.6673328548,
#  1549441.746161166,
#  2317451.8236946194,
#  2912232.1579089137,
#  5709151.519200945,
#  807436.4674610357,
#  1002228.8745564914,
#  3403825.34572112,
#  5735978.882425856,
#  5261345.939071056,
#  5507852.277797063,
#  6326798.495530824,
#  4053538.195650597,
#  4444421.154333873,
#  4597641.267148721,
#  4333813.174187148,
#  13661842.769868333,
#  8794225.62368942,
#  14684237.760250501,
#  12559749.300963627,
#  12343283.44760367,
#  2566516.5531185577,
#  2485182.724490686,
#  1881330.9255949694,
#  2055648.3511814296]

# t_cpx_const = [127550.45010137597,
#  982938.6283601706,
#  2892533.284129768,
#  1386949.4050687125,
#  1547454.4614787283,
#  2320195.1854633987,
#  2887366.2274679984,
#  5610810.65823586,
#  806348.433833418,
#  1000877.8486951116,
#  3367072.9957549083,
#  5643674.368107751,
#  5108166.707665575,
#  5367513.285908491,
#  6369548.715392036,
#  3986607.675189789,
#  4345129.1923235245,
#  4483380.746670333,
#  4241518.437283093,
#  14722557.689984877,
#  9014137.937643,
#  16015494.804875465,
#  13383289.576190414,
#  13126751.946490193,
#  2556318.703268875,
#  2477661.307038694,
#  1877862.9480487357,
#  2053632.7608103429]

# t_qtz_tv = [896206.7939181189,
#  878362.8383798527,
#  264920.88340950105,
#  119327.3182085496,
#  305815.4862325982,
#  214126.51362611144,
#  254566.77723230896,
#  38432.06112115359,
#  2071967.0797841568,
#  2178789.309577073,
#  3212028.48382731,
#  6597036.167599809,
#  3111192.799787036,
#  2151408.051484728]

# t_qtz_const= [894741.236792822,
#  877261.2605537559,
#  264536.2818474675,
#  119169.91504834245,
#  305328.05832091457,
#  213764.21265166433,
#  254112.23894512616,
#  38381.03331259172,
#  2070953.3186181409,
#  2181359.342203705,
#  3172570.571774715,
#  6686821.764808734,
#  3076217.9311023173,
#  2152845.5387340374]

# t_dunai_tv = [23105312.356544875,
#  25915968.896820262,
#  18259749.858322594,
#  42593963.196708575,
#  23459409.68677945,
#  27586986.83357753,
#  14780555.123567522,
#  9434646.130985275,
#  27348505.884927094,
#  14605800.102705868,
#  20805187.30944283,
#  30041612.254961908,
#  19616162.37370307,
#  75460.80000488897,
#  134862.3567647821,
#  95322.11590645289]

# t_dunai_const = [26349936.171570845,
#  29374739.693126243,
#  20160896.67886079,
#  48397595.90337271,
#  26750926.399538074,
#  31041130.784294575,
#  16045835.090211656,
#  9678282.715581302,
#  30796967.176567987,
#  15841816.86615897,
#  23535458.89918671,
#  33622890.86429601,
#  21958673.489488207,
#  75335.37133153905,
#  134624.75913290796,
#  95187.09864418964]

# updated_texp_tv = []
# updated_texp_const = []
# diff_tv_pyx = []
# perdif_ev = []

# for i in range(len(t_cpx_const)): #convert ages from [yr] to [Ma]
#     updated = t_cpx_tv[i]/10**6
#     updated_texp_tv.append(updated) #Evenstar data
#     updated_const = t_cpx_const[i]/10**6 
#     updated_texp_const.append(updated_const) #this model
#     temp = updated - updated_const
#     diff_tv_pyx.append(temp)
#     perdif_ev.append((temp/updated_const)*100)

# updated_neon_tv = []
# updated_neon_const = []
# diff_tv_qtz = []
# perdifneon = []

# for i in range(len(t_qtz_tv)): #convert ages from [yr] to [Ma]
#     updatedneontv = t_qtz_tv[i]/10**6
#     updated_neon_tv.append(updatedneontv)
#     updatedneonconst = t_qtz_const[i]/10**6
#     updated_neon_const.append(updatedneonconst)
#     temp = updatedneontv - updatedneonconst
#     diff_tv_qtz.append(temp)
#     perdifneon.append((temp/updatedneonconst)*100)
    
# updated_dunai_const = []
# updated_dunai = []
# diff_tv_dunai = []
# perdif = []

# for i in range(len(t_dunai_tv)):
#     updated_dunaix = t_dunai_tv[i]/10**6
#     updated_dunai_constx = t_dunai_const[i]/10**6
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


# ax2.set_ylim(-7,1)
# ax2.set_xlim(2,50)
# ax2.hlines(0,2,50)

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

# ax3.set_xlim(2,50)
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
# ax3.hlines(0,2,50)



# ax1.set_xlim(2,50)
# ax1.plot([2,50], [2,50], 'k-')

# ax1.plot(updated_texp_const[0:4],updated_texp_tv[0:4], 'o', c='limegreen', alpha = 0.7,markersize = 8)
# ax1.plot(updated_texp_const[4:17],updated_texp_tv[4:17], 'o', c = 'royalblue', alpha = 0.7,markersize = 8)
# ax1.plot(updated_texp_const[17:26],updated_texp_tv[17:26], 'o', c = 'deepskyblue',alpha = 0.7, markersize = 8)

# ax1.plot(updated_neon_const[0:9], updated_neon_tv[0:9],  's', c = 'teal', alpha = 0.7,markersize = 8)
# ax1.plot(updated_neon_const[9:11], updated_neon_tv[9:11],  's', c='limegreen', alpha = 0.7,markersize = 8)
# ax1.plot(updated_neon_const[11:14], updated_neon_tv[11:14], 's', c='royalblue',alpha = 0.7, markersize = 8)
# ax1.plot(updated_neon_const[13], updated_neon_tv[13],  's', c='deepskyblue', alpha = 0.7,markersize = 8)

# ax1.plot(updated_dunai_const[0:5],updated_dunai[0:5], 's', c='midnightblue',alpha = 0.7, markersize = 8)
# ax1.plot(updated_dunai_const[5:9],updated_dunai[5:9], 's', c='purple',alpha = 0.7,markersize =8)
# ax1.plot(updated_dunai_const[9:13],updated_dunai[9:13], 's', c='mediumpurple',alpha = 0.7, markersize = 8)
# ax1.plot(updated_dunai_const[13:15],updated_dunai[13:15], 's', c='skyblue', alpha = 0.7,markersize =8)
# ax1.plot(updated_dunai_const[15:16],updated_dunai[15:16], 's', c='hotpink', alpha = 0.7,markersize = 8)

# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 14)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 14)

# ax1.set_ylabel('SPRITE exposure age (Ma)', fontsize = 13)
# ax1.set_xlabel('LSDn average exposure age (Ma)', fontsize = 13)
# plt.savefig(directory+'/plots_updated/new_fig_10.svg', dpi = 300, bbox_inches='tight')
