#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:01:08 2022

@autfhor: mmijjum
    

This script will read in all the necessary files (inputs spreadsheet, and .csv files).


"""
import numpy as np
import pandas as pd
import glob
import os
import matplotlib.pyplot as plt

#SET DIRECTORY
os.chdir(os.path.dirname(os.path.abspath(__file__)))
directory = os.path.dirname(__file__)


#Read in excel sheet with data, set variable names.
Exposure_Age_Inputs = pd.read_excel(directory+'/Data/inputs.xlsx') #excel sheet with all pmag data. 0-70 Ma, all criteria
site_lat = Exposure_Age_Inputs['Latitude']
site_lon = Exposure_Age_Inputs['Longitude']
site_elevation = Exposure_Age_Inputs['Elevation']
s_topo = Exposure_Age_Inputs['Topographic shielding correction']
zmax = Exposure_Age_Inputs['Sample Thickness']
rho = Exposure_Age_Inputs['Sample Density']
erosion = Exposure_Age_Inputs['Erosion']

nuclide_concentration = Exposure_Age_Inputs['Nuclide Concentration']
nuclide_uncertainty = Exposure_Age_Inputs['Nuclide Uncertainty']
Nuclide = Exposure_Age_Inputs['Nuclide']
atm = Exposure_Age_Inputs['Atmospheric conversion']
start = Exposure_Age_Inputs['Start']
stop = Exposure_Age_Inputs['Stop']
plate = Exposure_Age_Inputs['Plate']
z_from_surface = Exposure_Age_Inputs['Depth below paleosurface']
paleo = Exposure_Age_Inputs['Paleoduration?']

delta = Exposure_Age_Inputs['Uplift/Subsidence']

if plate[0] == 1:
    plate = 'NA'
if plate[0] == 2:
    plate = 'SA'
if plate[0] == 3:
    plate = 'AF'
if plate[0] == 4:
    plate = 'IN'
if plate[0] == 5:
    plate = 'EU'
if plate[0] == 6:
    plate = 'AU'
if plate[0] == 7:
    plate = 'ANT'
if plate[0] == 8:
    plate = 'GL'
if Nuclide[0] == 1:
    system = 1
if Nuclide[0] == 2:
    system = 2
if Nuclide[0] == 3:
    system = 3
if Nuclide[0] == 4:
    system = 4
    
if atm[0] == 0:
    stdatm = 0
if atm[0] == 1:
    stdatm = 1
    
if Nuclide[0] != 4:
    muons = 'False'
else:
    muons = 'True'


resolution = int(250000)/10**6 #change from 250000 to 50000 for MCADAM full resolution
if paleo[0] ==0: 
    timerange = [start[0],stop[0]+0.05]
    
    time_1 = np.arange(timerange[0], timerange[1], resolution)
    def round_down(num):
        return num - (num%0.25)
    
    time1 = round_down(timerange[0])
    
    def myround(x, base=0.25):
        return base * round(x/base)
    
    time2 = myround(timerange[1])
    time = np.arange(time1,time2+.25,resolution)

if paleo[0] == 1:
    timerange = [start[0]+0.05,stop[0]]
    def round_down(num):
        return num - (num%0.25)

    time1 = round_down(timerange[1])
    
    def myround(x, base=0.25):
        return base * round(x/base)

    time2 = myround(timerange[0])

    
    time = np.arange(time2,time1+0.5,resolution)
#convert lat/lon/altitude to lists for use later.
lat = site_lat.tolist()
lon = site_lon.tolist()
alt = site_elevation.tolist()

#Add files to compute ERA40 reanalysis
ERA40lat = pd.read_csv(directory+'/Data/ERA40lat.csv', header=None) 
ERA40lon = pd.read_csv(directory+'/Data/ERA40lon.csv', header=None)
meanT = pd.read_csv(directory+'/Data/meanT.csv', header=None)
meanP = pd.read_csv(directory+'/Data/meanP.csv', header=None)

#Reaction Cross Sections: naming scheme is Element_nucleon_x_nuclide_T
#e.g: Oxygen_neutron_x_3He_T = Onx3HeT
Onx3HeT = pd.read_csv(directory+'/Data/Onx3HeT.csv', header = None) 
Sinx3HeT = pd.read_csv(directory+'/Data/Sinx3HeT.csv', header=None) 
Fenx3HeT = pd.read_csv(directory+'/Data/Fenx3HeT.csv', header=None)
Canx3HeT = pd.read_csv(directory+'/Data/Canx3HeT.csv', header=None)
Mgnx3HeT = pd.read_csv(directory+'/Data/Mgnx3HeT.csv', header=None)
Alnx3HeT = pd.read_csv(directory+'/Data/Alnx3HeT.csv', header=None)
Sinx21Ne = pd.read_csv(directory+'/Data/SinxNe21.csv', header = None)

Opx3HeT = pd.read_csv(directory+'/Data/Opx3HeT.csv', header = None)
Sipx3HeT = pd.read_csv(directory+'/Data/Sipx3HeT.csv', header = None)
Fepx3HeT = pd.read_csv(directory+'/Data/Fepx3HeT.csv', header=None)
Capx3HeT = pd.read_csv(directory+'/Data/Capx3HeT.csv', header=None)
Mgpx3HeT = pd.read_csv(directory+'/Data/Mgpx3HeT.csv', header=None)
Alpx3HeT = pd.read_csv(directory+'/Data/Alpx3HeT.csv', header=None)
Sipx21Ne = pd.read_csv(directory+'/Data/SipxNe21.csv', header = None)


#Integrated neutron flux < 15 MeV
a_values = pd.read_csv(directory+'/Data/a_values.csv', header=None)

#Basic Spectrum
b_values = pd.read_csv(directory+'/Data/b_values.csv', header=None)
basic_spectrum = pd.read_csv(directory+'/Data/basic_spectrum.csv',header=None)

#C values are also part of basic spectrum.
#c1, c7 are in units of inverse lethargy
#c2,5,5,6,8, 10 are in units of MeV
c_values = pd.read_csv(directory+'/Data/c_values.csv', header=None)

ground_level_spectrum = pd.read_csv(directory+'/Data/ground_level_spectrum.csv',header=None)
thermal_neutron_spectrum = pd.read_csv(directory+'/Data/thermal_neutron_spectrum.csv',header=None)

#convert to numpy arrays
c = Onx3HeT.to_numpy()
d = Sinx3HeT.to_numpy()
e = Fenx3HeT.to_numpy()
f = Canx3HeT.to_numpy()
g = Mgnx3HeT.to_numpy()
h = Alnx3HeT.to_numpy()
i = Sinx21Ne.to_numpy()

#reshape the arrays to convert to dataframe in preferred format.
Onx3HeT_array = np.reshape(c,200)
Sinx3HeT_array = np.reshape(d,200)
Fenx3HeT_array = np.reshape(e,200)
Canx3HeT_array = np.reshape(f,200)
Mgnx3HeT_array = np.reshape(g,200)
Alnx3HeT_array = np.reshape(h,200)
Sinx21Ne_array = np.reshape(i,200)

#convert to dataframe. Using length of 'lat' because that will tell the dataframe how many rows (sample #) it needs.
Onx3 = pd.DataFrame(data=Onx3HeT_array)
Onx3df = pd.DataFrame(np.repeat(Onx3.values, len(lat), axis=1))

Sinx3 = pd.DataFrame(data=Sinx3HeT_array)
Sinx3df = pd.DataFrame(np.repeat(Sinx3.values,len(lat), axis=1))


Fenx3 = pd.DataFrame(data=Fenx3HeT_array)
Fenx3df = pd.DataFrame(np.repeat(Fenx3.values, len(lat), axis=1))

Canx3 = pd.DataFrame(data=Canx3HeT_array)
Canx3df = pd.DataFrame(np.repeat(Canx3.values, len(lat), axis=1))

Mgnx3 = pd.DataFrame(data=Mgnx3HeT_array)
Mgnx3df = pd.DataFrame(np.repeat(Mgnx3.values, len(lat), axis=1))

Alnx3 = pd.DataFrame(data=Alnx3HeT_array)
Alnx3df = pd.DataFrame(np.repeat(Alnx3.values, len(lat), axis=1))

Sinx21 = pd.DataFrame(data=Sinx21Ne_array)
Sinx21df = pd.DataFrame(np.repeat(Sinx21.values, len(lat), axis=1))

#Proton Spectra
basic_spectrum_protons = pd.read_csv(directory+'/Data/basic_spectrum_protons.csv', header = None)
primary_spectrum = pd.read_csv(directory+'/Data/primary_spectrum.csv', header = None)
secondary_spectrum = pd.read_csv(directory+'/Data/secondary_spectrum.csv', header = None)
#h values are part of the secondary spectrum
h_values_protons = pd.read_csv(directory+'/Data/h_values_protons.csv', header = None)

basic_spectrum_protons.columns = ['variable','values']
primary_spectrum.columns = ['variable','values']
secondary_spectrum.columns = ['variable','values']
h_values_protons.columns = ['variable','values']


cp = Opx3HeT.to_numpy()
dp = Sipx3HeT.to_numpy()
ep = Fepx3HeT.to_numpy()
fp = Capx3HeT.to_numpy()
gp = Mgpx3HeT.to_numpy()
hp = Alpx3HeT.to_numpy()
ip = Sipx21Ne.to_numpy() 

Opx3HeT_array = np.reshape(cp,200)
Sipx3HeT_array = np.reshape(dp,200)
Fepx3HeT_array = np.reshape(ep,200)
Capx3HeT_array = np.reshape(fp,200)
Mgpx3HeT_array = np.reshape(gp,200)
Alpx3HeT_array = np.reshape(hp,200)
Sipx21NeT_array = np.reshape(ip,200)

Opx3 = pd.DataFrame(data=Opx3HeT_array)
Opx3df = pd.DataFrame(np.repeat(Opx3.values, len(lat), axis=1))

Sipx3 = pd.DataFrame(data=Sipx3HeT_array)
Sipx3df = pd.DataFrame(np.repeat(Sipx3.values,len(lat), axis=1))


Fepx3 = pd.DataFrame(data=Fepx3HeT_array)
Fepx3df = pd.DataFrame(np.repeat(Fepx3.values, len(lat), axis=1))

Capx3 = pd.DataFrame(data=Capx3HeT_array)
Capx3df = pd.DataFrame(np.repeat(Capx3.values, len(lat), axis=1))

Mgpx3 = pd.DataFrame(data=Mgpx3HeT_array)
Mgpx3df = pd.DataFrame(np.repeat(Mgpx3.values, len(lat), axis=1))

Alpx3 = pd.DataFrame(data=Alpx3HeT_array)
Alpx3df = pd.DataFrame(np.repeat(Alpx3.values, len(lat), axis=1))

Sipx21 = pd.DataFrame(data=Sipx21NeT_array)
Sipx21df = pd.DataFrame(np.repeat(Sipx21.values, len(lat), axis=1))


#Assign column names to text files
a_values.columns = ['variable','values']
b_values.columns = ['variable','values']
basic_spectrum.columns = ['variable', 'values']
c_values.columns = ['variable', 'values']
ground_level_spectrum.columns = ['variable' , 'values']
thermal_neutron_spectrum.columns = ['variable' , 'values']

#Number densities

#Quartz
NatomsQtzO = 2.0046e22
NatomsQtzSi = 1.0023e22

#Pyroxene
NatomsOPxEnMg = 5.998e21
NatomsOPxEnSi = 5.9988e21
NatomsOPxEnO = 1.7997e22
NatomsOPxFsFe = 4.5647e21
NatomsOPxFsSi = 4.5647e21
NatomsOPxFsO = 1.3694e22
NatomsCPxWoCa = 5.1843e21
NatomsCPxWoSi = 5.1843e21
NatomsCPxWoO = 1.5553e22
NatomsCpxAuCa = 2.5521e21
NatomsCpxAuMg = 2.2969e21
NatomsCpxAuFe = 5.1041e20
NatomsCpxAuAl = 1.2760e21
NatomsCpxAuSi = 4.8489e21
NatomsCpxAuO= 1.5312e22

#Olivine
NatomsOlFoMg = 8.5607e21
NatomsOlFoSi = 4.2803e21
NatomsOlFoO = 1.7121e22
NatomsOlFaFe = 5.9106e21
NatomsOlFaSi = 2.9553e21
NatomsOlFaO = 1.1821e22
NatomsOlFo80Fe = 6.2850e21
NatomsOlFo80Mg = 1.5712e21
NatomsOlFo80Si = 3.9821e21
NatomsOlFo80O = 1.5712e22


# # Muons
# - only for 21Ne qtz
mfluxRef_neg = pd.read_csv(directory+'/Data/mfluxRef_neg.csv', header = None)
mfluxRef_pos = pd.read_csv(directory+'/Data/mfluxRef_pos.csv', header = None)


u1n = 5.8214e9;
u2n = 3.6228e-3;
u3n = 1.0240;
u4n = 4.5141e-3;
u5n = 3.1992e8;


#Negative muon coefficients
w111nmin = 2.0899e3;
w112nmin = 1.2110e2;
w113nmin = -9.2925e2;
w114nmin = 6.8558;
w115nmin = 3.2929;
w111nmax = 2.4185e3;
w112nmax = 1.1240e2;
w113nmax = -8.9497e2;
w114nmax = 7.4497;
w115nmax = 3.5522;
w121nmin = -5.6641;
w122nmin = -6.4998e-1;
w123nmin = 3.5830;
w124nmin = 8.8799e-1;
w125nmin = 3.7337;
w121nmax = -5.6115;
w122nmax = -6.5095e-1;
w123nmax = 3.3115;
w124nmax = 7.7616e-1;
w125nmax = 3.7607;
w131nmin = 1.1807e-2;
w132nmin = 1.5847e-3;
w133nmin = -1.2543e-2;
w134nmin = 3.4411;
w135nmin = 3.6455;
w131nmax = 1.1804e-2;
w132nmax = 1.5798e-3;
w133nmax = -1.2480e-2;
w134nmax = 3.4818;
w135nmax = 3.5926;
w141nmin = -2.5853e-6;
w142nmin = -7.9871e-7;
w143nmin = 2.5370e-5;
w144nmin = 4.9450;
w145nmin = 3.7213;
w141nmax = -2.5196e-6;
w142nmax = -7.9341e-7;
w143nmax = 2.5343e-5;
w144nmax = 4.9219;
w145nmax = 3.7354;
w151nmin = 1.8671e-9;
w152nmin = -1.9787e-10;
w153nmin = -1.7061e-8;
w154nmin = 5.1157;
w155nmin = 4.2354;
w151nmax = 1.8602e-9;
w152nmax = -2.0122e-10;
w153nmax = -1.7016e-8;
w154nmax = 5.1424;
w155nmax = 4.2718;

w211nmin = 8.5946e1;
w212nmin = -5.8637;
w213nmin = 3.6872e2;
w214nmin = 4.8178;
w215nmin = 3.2984;
w211nmax = 8.6974e1;
w212nmax = -5.8773;
w213nmax = 3.7230e2;
w214nmax = 4.6802;
w215nmax = 3.2996;
w221nmin = 3.4175;
w222nmin = 7.9022e-2;
w223nmin = -5.2936e-1;
w224nmin = 6.8789;
w225nmin = 1.0647;
w221nmax = 3.4184;
w222nmax = 7.8730e-2;
w223nmax = -5.3162e-1;
w224nmax = 6.8578;
w225nmax = 1.0891;
w231nmin = -3.3253e-3;
w232nmin = -1.4941e-4;
w233nmin = 1.8630e-3;
w234nmin = 7.0358;
w235nmin = 6.0158e-1;
w231nmax = -3.3203e-3;
w232nmax = -1.4962e-4;
w233nmax = 1.8556e-3;
w234nmax = 7.0391;
w235nmax = 6.0068e-1;
w241nmin = -2.6862e-6;
w242nmin = -8.9985e-8;
w243nmin = -2.7068e-6;
w244nmin = 7.0511;
w245nmin = 4.6369e-1;  
w241nmax = -2.6832e-6;
w242nmax = -8.9349e-8;
w243nmax = -2.7056e-6;
w244nmax = 7.0489;
w245nmax = 4.6511e-1;
w251nmin = 2.3372e-9;
w252nmin = 1.5003e-10;
w253nmin = 1.1941e-9;
w254nmin = 7.0490;
w255nmin = 3.5646e-1;
w251nmax = 2.3300e-9;
w252nmax = 1.4973e-10;
w253nmax = 1.1994e-9;
w254nmax = 7.0449;
w255nmax = 3.6172e-1;

w311nmin = 7.8736e-1;
w312nmin = -1.8004e-2;
w313nmin = -3.0414e-1;
w314nmin = 1.4479e1;
w315nmin = 5.6128;
w311nmax = 8.1367e-1;
w312nmax = -2.4784e-2;
w313nmax = -3.1104e-1;
w314nmax = 1.0553e1;
w315nmax = 3.6057;
w321nmin = 2.1362e-3;
w322nmin = 4.9866e-5;
w323nmin = 1.4331e-3;
w324nmin = 8.1043;
w325nmin = 3.4619;
w321nmax = 6.6470e-4;
w322nmax = 1.3546e-4;
w323nmax = 1.8371e-3;
w324nmax = 9.2913;
w325nmax = 2.3906;
w331nmin = -6.0480e-6;
w332nmin = -1.3554e-7;
w333nmin = -3.9433e-6;
w334nmin = 7.8291;
w335nmin = 4.3398;
w331nmax = -3.7978e-6;
w332nmax = -2.9193e-7;
w333nmax = -2.5834e-6;
w334nmax = 9.6668;
w335nmax = 1.3763;
w341nmin = 6.6770e-9;
w342nmin = 1.0885e-12;
w343nmin = 1.5756e-9;
w344nmin = 2.2697e1;
w345nmin = 1.9922;
w341nmax = 2.7492e-9;
w342nmax = 3.3458e-10;
w343nmax = 2.3109e-9;
w344nmax = 1.0281e1;
w345nmax = 1.3660;
w351nmin = -3.0952e-12;
w352nmin = 3.8044e-14;
w353nmin = 7.4580e-13;
w354nmin = 7.8473;
w355nmin = 2.0013;
w351nmax = -1.8076e-12;
w352nmax = -4.1711e-14;
w353nmax = 4.6284e-13;
w354nmax = 4.5439;
w355nmax = 4.7886e-1;

h51n = 5.6500e-1;
h52n = 1.2100e-2;
h53n = -3.5700e-1;
h54n = 4.7300;
h55n = 1.4600;
h61n = 8.8000e-5;
h62n = -3.8900e-6;
h63n = 4.9100e-4;
h64n = 4.5100;
h65n = 1.7200;

# Positive muon coefficients
u1p = 6.2603e9;
u2p = 3.4320e-3;
u3p = 1.0131;
u4p = 4.1817e-3;
u5p = 3.7543e8;


w111pmin = 2.0538e3;
w112pmin = 1.2598e2;
w113pmin = -1.0131e3;
w114pmin = 6.1791;
w115pmin = 3.4718;
w111pmax = 2.3945e3;
w112pmax = 1.1790e2;
w113pmax = -9.4920e2;
w114pmax = 7.0369;
w115pmax = 3.8446;
w121pmin = -5.6688;
w122pmin = -6.5475e-1;
w123pmin = 3.5933;
w124pmin = 1.3137;
w125pmin = 3.2223;
w121pmax = -5.6246;
w122pmax = -6.5784e-1;
w123pmax = 3.2754;
w124pmax = 1.0604;
w125pmax = 3.3353;
w131pmin = 1.1700e-2;
w132pmin = 1.5748e-3;
w133pmin = -1.2521e-2;
w134pmin = 3.2601;
w135pmin = 3.6451;
w131pmax = 1.1736e-2;
w132pmax = 1.5714e-3;
w133pmax = -1.2383e-2;
w134pmax = 3.3054;
w135pmax = 3.5833;
w141pmin = -2.3130e-6;
w142pmin = -7.5964e-7;
w143pmin = 2.4832e-5;
w144pmin = 4.9409;
w145pmin = 3.7979;
w141pmax = -2.2412e-6;
w142pmax = -7.5644e-7;
w143pmax = 2.4834e-5;
w144pmax = 4.8875;
w145pmax = 3.8034;
w151pmin = 1.7430e-9;
w152pmin = -2.2205e-10;
w153pmin = -1.6916e-8;
w154pmin = 5.1206;
w155pmin = 4.3875;
w151pmax = 1.7462e-9;
w152pmax = -2.2603e-10;
w153pmax = -1.6852e-8;
w154pmax = 5.1768;
w155pmax = 4.3997;

w211pmin = 8.4834e1;
w212pmin = -5.7723;
w213pmin = 3.7035e2;
w214pmin = 4.8084;
w215pmin = 3.3589;
w211pmax = 8.7301e1;
w212pmax = -5.9021;
w213pmax = 3.7664e2;
w214pmax = 4.5920;
w215pmax = 3.3933;
w221pmin = 3.4086;
w222pmin = 7.8728e-2;
w223pmin = -5.2000e-1;
w224pmin = 6.8730;
w225pmin = 1.0869;
w221pmax = 3.4070;
w222pmax = 7.8501e-2;
w223pmax = -5.2268e-1;
w224pmax = 6.8422;
w225pmax = 1.0916;
w231pmin = -3.3162e-3;
w232pmin = -1.4917e-4;
w233pmin = 1.8524e-3;
w234pmin = 7.0237;
w235pmin = 6.0692e-1;
w231pmax = -3.3141e-3;
w232pmax = -1.4904e-4;
w233pmax = 1.8518e-3;
w234pmax = 7.0237;
w235pmax = 6.1137e-1;
w241pmin = -2.6781e-6;
w242pmin = -8.8820e-8;
w243pmin = -2.7098e-6;
w244pmin = 7.0420;
w245pmin = 4.6845e-1;
w241pmax = -2.6774e-6;
w242pmax = -8.8086e-8;
w243pmax = -2.7055e-6;
w244pmax = 7.0422;
w245pmax = 4.7162e-1;
w251pmin = 2.3267e-9;
w252pmin = 1.4896e-10;
w253pmin = 1.2010e-9;
w254pmin = 7.0431;
w255pmin = 3.6378e-1;
w251pmax = 2.3187e-9;
w252pmax = 1.4872e-10;
w253pmax = 1.2045e-9;
w254pmax = 7.0488;
w255pmax = 3.6659e-1;

w311pmin = 7.6040e-1;
w312pmin = -1.8020e-2;
w313pmin = -2.7253e-1;
w314pmin = 1.1292e1;
w315pmin = 5.3901;
w311pmax = 9.2327e-1;
w312pmax = -2.9590e-2;
w313pmax = -4.2838e-1;
w314pmax = 9.6573;
w315pmax = 4.0023;
w321pmin = 2.0613e-3;
w322pmin = 6.1719e-5;
w323pmin = 1.7751e-3;
w324pmin = 7.5508;
w325pmin = 3.9262;
w321pmax = 8.4438e-4;
w322pmax = 1.3392e-4;
w323pmax = 1.8096e-3;
w324pmax = 9.2554;
w325pmax = 2.4406;
w331pmin = -5.9644e-6;
w332pmin = -1.4795e-7;
w333pmin = -4.1301e-6;
w334pmin = 7.5298;
w335pmin = 4.3879;
w331pmax = -3.9078e-6;
w332pmax = -2.8780e-7;
w333pmax = -2.4920e-6;
w334pmax = 9.7445;
w335pmax = 1.4865;
w341pmin = 6.4640e-9;
w342pmin = -9.2764e-12;
w343pmin = 1.7352e-9;
w344pmin = 2.3633e1;
w345pmin = 1.6729;
w341pmax = 1.9852e-9;
w342pmax = 3.5716e-10;
w343pmax = 2.9465e-9;
w344pmax = 1.0431e1;
w345pmax = 1.9364;
w351pmin = -3.2101e-12;
w352pmin = 5.4637e-14;
w353pmin = 9.2092e-13;
w354pmin = 7.5423;
w355pmin = 2.6570;
w351pmax = -1.7751e-12;
w352pmax = -3.1711e-14;
w353pmax = 4.7927e-13;
w354pmax = 4.2050;
w355pmax = 7.4704e-1;

h51p = 5.0600e-1;
h52p = 1.3000e-2;
h53p = -3.9400e-1;
h54p = 4.1200;
h55p = 1.3300;
h61p = 1.3900e-4;
h62p = 6.9500e-6;
h63p = 7.4700e-4;
h64p = 3.7200;
h65p = 1.9700;


data_muons = pd.read_csv(directory+'/Data/data_muons.txt', header = None)

##EVERYTHING BELOW ARE TEXT FILES FOR PLOTS MADE IN MANUSCRIPT. 
#NOT RELEVANT FOR REGULAR USER

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

GL_ERA40 =  pd.read_csv(directory+'/text_for_plots/Figure_7_GL_ERA40', header = None)
GL_STD = pd.read_csv(directory+'/text_for_plots/Figure_7_GL_STD', header = None)

EC_ERA40 =  pd.read_csv(directory+'/text_for_plots/Figure_7_EC_ERA40', header = None)
EC_STD = pd.read_csv(directory+'/text_for_plots/Figure_7_EC_STD', header = None)

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
lib3e3 = pd.read_csv(directory+'/text_for_plots/lib_3e3.csv', header = None)
lib10e3 = pd.read_csv(directory+'/text_for_plots/lib_10e3.csv', header = None)
lib20e3 = pd.read_csv(directory+'/text_for_plots/lib_20e3.csv', header = None)

Rc_const = pd.read_csv(directory+'/text_for_plots/Rc_const.csv', header = None)
Rc_tv_latonly = pd.read_csv(directory+'/text_for_plots/Rc_tv_latonly.csv', header = None)
Rc_tv_fieldonly = pd.read_csv(directory+'/text_for_plots/Rc_tv_fieldonly.csv', header = None)
Rc_tv_both = pd.read_csv(directory+'/text_for_plots/Rc_tv_both.csv', header = None)

north_america = pd.read_csv(directory+'/text_for_plots/north_america.csv', header = None)
poles = pd.read_csv(directory+'/text_for_plots/poles.csv', header = None)
equator = pd.read_csv(directory+'/text_for_plots/equator.csv', header = None)


