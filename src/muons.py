#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:01:48 2022

@author: mmijjum
"""
import numpy as np
import pandas as pd
import Pmag_paleolat
import Rc
import Read
import User_Interface
import atm_depth



time = User_Interface.time 


s = 624.5718; #Solar modulation- uses constant value that Lifton (2008)/code uses for samples beyond 10 Ma
smin = 400; #Units of MV
smax = 1200; #Units of MV
w = 0.2

if User_Interface.system == 4: 

    Emu = 105.658 # in Mev, Rest energy of muon
    E_muons = np.logspace(1,5.9030,200) #Energy spectrum [MeV]. From LSD, data from Sato & Nita (2008) 
    E_m_temp = pd.DataFrame(E_muons)
    E_m = pd.concat([E_m_temp.T]*len(Rc), ignore_index=True)

    alpha3 = 3.7 # Muon spectrum power law exponent
    Beta = np.sqrt(1-(Emu/(Emu + E_m))**2) #  Particle speed relative to light
    c = 3.0e8 #speed of light, in m/s
    p = np.sqrt((E_m**2 + (2*E_m*Emu))) #in MeV/c

smin = 400 #units of MV
smax = 1200 #units of MV


if User_Interface.system == 4: 
    def Phimnfun(x):
        return Read.u1n*(np.exp(-Read.u2n*x) - Read.u3n*np.exp(-Read.u4n*x)) + Read.u5n

    Phimn = Phimnfun(atm_depth.x)

    def Phimpfun(x):
        return Read.u1p*(np.exp(-Read.u2p*x) - Read.u3p*np.exp(-Read.u4p*x)) + Read.u5p

    Phimp = Phimpfun(atm_depth.x)

if User_Interface.system == 4 :
    def minmax(w1,w2,w3,w4,w5):
        return w1 + w2*Rc.iloc[: , 1:] + w3/(1 + np.exp((Rc.iloc[: , 1:] - w4)/w5))

    #Negative Muons:
    v11nmin = minmax(Read.w111nmin, Read.w112nmin, Read.w113nmin, Read.w114nmin, Read.w115nmin)
    v11nmax = minmax(Read.w111nmax, Read.w112nmax, Read.w113nmax, Read.w114nmax, Read.w115nmax)

    v12nmin = minmax(Read.w121nmin, Read.w122nmin, Read.w123nmin, Read.w124nmin, Read.w125nmin)
    v12nmax = minmax(Read.w121nmax, Read.w122nmax, Read.w123nmax, Read.w124nmax, Read.w125nmax)

    v13nmin = minmax(Read.w131nmin, Read.w132nmin, Read.w133nmin, Read.w134nmin, Read.w135nmin)
    v13nmax = minmax(Read.w131nmax, Read.w132nmax, Read.w133nmax, Read.w134nmax, Read.w135nmax)

    v14nmin = minmax(Read.w141nmin, Read.w142nmin, Read.w143nmin, Read.w144nmin, Read.w145nmin)
    v14nmax = minmax(Read.w141nmax, Read.w142nmax, Read.w143nmax, Read.w144nmax, Read.w145nmax)

    v15nmin = minmax(Read.w151nmin, Read.w152nmin, Read.w153nmin, Read.w154nmin, Read.w155nmin)
    v15nmax = minmax(Read.w151nmax, Read.w152nmax, Read.w153nmax, Read.w154nmax, Read.w155nmax)


    v21nmin = minmax(Read.w211nmin, Read.w212nmin, Read.w213nmin, Read.w214nmin, Read.w215nmin)
    v21nmax = minmax(Read.w211nmax, Read.w212nmax, Read.w213nmax, Read.w214nmax, Read.w215nmax)

    v22nmin = minmax(Read.w221nmin, Read.w222nmin, Read.w223nmin, Read.w224nmin, Read.w225nmin)
    v22nmax = minmax(Read.w221nmax, Read.w222nmax, Read.w223nmax, Read.w214nmax, Read.w225nmax)

    v23nmin = minmax(Read.w231nmin, Read.w232nmin, Read.w233nmin, Read.w234nmin, Read.w235nmin)
    v23nmax = minmax(Read.w231nmax, Read.w232nmax, Read.w233nmax, Read.w234nmax, Read.w235nmax)

    v24nmin = minmax(Read.w241nmin, Read.w242nmin, Read.w243nmin, Read.w244nmin, Read.w245nmin)
    v24nmax = minmax(Read.w241nmax, Read.w242nmax, Read.w243nmax, Read.w244nmax, Read.w245nmax)

    v25nmin = minmax(Read.w251nmin, Read.w252nmin, Read.w253nmin, Read.w254nmin, Read.w255nmin)
    v25nmax = minmax(Read.w251nmax, Read.w252nmax, Read.w253nmax, Read.w254nmax, Read.w255nmax)


    v31nmin = minmax(Read.w311nmin, Read.w312nmin, Read.w313nmin, Read.w314nmin, Read.w315nmin)
    v31nmax = minmax(Read.w311nmax, Read.w312nmax, Read.w313nmax, Read.w314nmax, Read.w315nmax)

    v32nmin = minmax(Read.w321nmin, Read.w322nmin, Read.w323nmin, Read.w324nmin, Read.w325nmin)
    v32nmax = minmax(Read.w321nmax, Read.w322nmax, Read.w323nmax, Read.w324nmax, Read.w325nmax)

    v33nmin = minmax(Read.w331nmin, Read.w332nmin, Read.w333nmin, Read.w334nmin, Read.w335nmin)
    v33nmax = minmax(Read.w331nmax, Read.w332nmax, Read.w333nmax, Read.w334nmax, Read.w335nmax)

    v34nmin = minmax(Read.w341nmin,Read.w342nmin, Read.w343nmin, Read.w344nmin, Read.w345nmin)
    v34nmax = minmax(Read.w341nmax, Read.w342nmax, Read.w343nmax, Read.w344nmax,Read. w345nmax)

    v35nmin = minmax(Read.w351nmin, Read.w352nmin, Read.w353nmin, Read.w354nmin, Read.w355nmin)
    v35nmax = minmax(Read.w351nmax, Read.w352nmax, Read.w353nmax, Read.w354nmax, Read.w355nmax)

    t1nmin = []
    t1nmax = []
    t2nmin = []
    t2nmax = []
    t3nmin = []
    t3nmax = []
    for i in range(len(Rc.Rc)):
        for j in range(len(time)):    
            t1nmin_temp = v11nmin.iloc[i,j] + v12nmin.iloc[i,j]*atm_depth.x.iloc[i,j] + v13nmin.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v14nmin.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v15nmin.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t1nmax_temp = v11nmax.iloc[i,j] + v12nmax.iloc[i,j]*atm_depth.x.iloc[i,j] + v13nmax.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v14nmax.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v15nmax.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t2nmin_temp = v21nmin.iloc[i,j] + v22nmin.iloc[i,j]*atm_depth.x.iloc[i,j] + v23nmin.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v24nmin.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v25nmin.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t2nmax_temp = v21nmax.iloc[i,j] + v22nmax.iloc[i,j]*atm_depth.x.iloc[i,j] + v23nmax.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v24nmax.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v25nmax.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t3nmin_temp = v31nmin.iloc[i,j] + v32nmin.iloc[i,j]*atm_depth.x.iloc[i,j] + v33nmin.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v34nmin.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v35nmin.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t3nmax_temp = v31nmax.iloc[i,j] + v32nmax.iloc[i,j]*atm_depth.x.iloc[i,j] + v33nmax.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v34nmax.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v35nmax.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t1nmin.append(t1nmin_temp)
            t1nmax.append(t1nmax_temp)
            t2nmin.append(t2nmin_temp)
            t2nmax.append(t2nmax_temp)
            t3nmin.append(t3nmin_temp)
            t3nmax.append(t3nmax_temp)
    t1nmin_df = pd.DataFrame([(t1nmin[n:n+len(time)]) for n in range(0, len(t1nmin), len(time))])
    t1nmax_df = pd.DataFrame([(t1nmax[n:n+len(time)]) for n in range(0, len(t1nmax), len(time))])
    t2nmin_df = pd.DataFrame([(t2nmin[n:n+len(time)]) for n in range(0, len(t2nmin), len(time))])
    t2nmax_df = pd.DataFrame([(t2nmax[n:n+len(time)]) for n in range(0, len(t2nmax), len(time))])
    t3nmin_df = pd.DataFrame([(t3nmin[n:n+len(time)]) for n in range(0, len(t3nmin), len(time))])
    t3nmax_df = pd.DataFrame([(t3nmax[n:n+len(time)]) for n in range(0, len(t3nmax), len(time))])

    phimunmin = []
    phimunmax = []
    phimun = []
    g5n = []
    g6n = []
    
    for i in range(len(Rc)):
        for j in range(len(time)):
            for n in range(len(E_m)):
                phimunmin_temp = Phimn.iloc[i,j]*(E_m.iloc[i,n] + (t1nmin_df.iloc[i,j] + t2nmin_df.iloc[i,j]*np.log10(E_m.iloc[i,n]))/(Beta.iloc[i,n]**t3nmin_df.iloc[i,j]))**-alpha3;
                phimunmin.append(phimunmin_temp)
                phimunmax_temp = Phimn.iloc[i,j]*(E_m.iloc[i,n] + (t1nmax_df.iloc[i,j] + t2nmax_df.iloc[i,j]*np.log10(E_m.iloc[i,n]))/(Beta.iloc[i,n]**t3nmax_df.iloc[i,j]))**-alpha3;
                phimunmax.append(phimunmax_temp)
    phimunmin_df = pd.DataFrame([(phimunmin[n:n+200]) for n in range(0, len(phimunmin), len(E_m))])
    phimunmax_df = pd.DataFrame([(phimunmax[n:n+200]) for n in range(0, len(phimunmax), len(E_m))])

    def gnfun(h1,h2,h3,h4,h5):
        return h1 + h2*Rc.iloc[: , 1:]+ h3/(1 + np.exp((Rc.iloc[: , 1:] - h4)/h5));

    g5n = gnfun(Read.h51n, Read.h52n, Read.h53n, Read.h54n, Read.h55n)
    g6n = gnfun(Read.h61n, Read.h62n, Read.h63n, Read.h64n, Read.h65n)


    phimun = []
    f3n = []
    for i in range(len(Rc)):
        for j in range(len(time)):
            f3n_temp = g5n.iloc[i,j] + g6n.iloc[i,j]*atm_depth.x.iloc[i,j];
            f3n.append(f3n_temp)
    f3n_df = pd.DataFrame([(f3n[n:n+len(time)]) for n in range(0, len(f3n), len(time))])


    f3n_updated = f3n_df.stack().tolist() #this flattens pressure df into a list so you can incorporate it into the for loop below
    phimun = []
    for i in range(len(phimunmin_df)):
        for j in range(len(E_m)):
            f2n = (phimunmin_df.iloc[i,j]- phimunmax_df.iloc[i,j])/(smin**f3n_updated[i] - smax**f3n_updated[i])
            f1n = phimunmin_df.iloc[i,j] - f2n*smin**f3n_updated[i]
            phimun_temp = f1n + f2n*s**f3n_updated[i]
            phimun.append(phimun_temp)
    Phimun_df = pd.DataFrame([(phimun[n:n+200]) for n in range(0, len(phimun), len(E_m))])
    
    #Positive Muons:
    v11pmin = minmax(Read.w111pmin, Read.w112pmin, Read.w113pmin, Read.w114pmin, Read.w115pmin)
    v11pmax = minmax(Read.w111pmax, Read.w112pmax, Read.w113pmax, Read.w114pmax, Read.w115pmax)

    v12pmin = minmax(Read.w121pmin, Read.w122pmin, Read.w123pmin, Read.w124pmin, Read.w125pmin)
    v12pmax = minmax(Read.w121pmax, Read.w122pmax, Read.w123pmax, Read.w124pmax, Read.w125pmax)

    v13pmin = minmax(Read.w131pmin, Read.w132pmin, Read.w133pmin, Read.w134pmin, Read.w135pmin)
    v13pmax = minmax(Read.w131pmax, Read.w132pmax, Read.w133pmax, Read.w134pmax, Read.w135pmax)

    v14pmin = minmax(Read.w141pmin, Read.w142pmin, Read.w143pmin, Read.w144pmin, Read.w145pmin)
    v14pmax = minmax(Read.w141pmax, Read.w142pmax, Read.w143pmax, Read.w144pmax, Read.w145pmax)

    v15pmin = minmax(Read.w151pmin, Read.w152pmin, Read.w153pmin, Read.w154pmin, Read.w155pmin)
    v15pmax = minmax(Read.w151pmax, Read.w152pmax, Read.w153pmax, Read.w154pmax, Read.w155pmax)


    v21pmin = minmax(Read.w211pmin, Read.w212pmin, Read.w213pmin, Read.w214pmin, Read.w215pmin)
    v21pmax = minmax(Read.w211pmax, Read.w212pmax, Read.w213pmax, Read.w214pmax, Read.w215pmax)

    v22pmin = minmax(Read.w221pmin, Read.w222pmin, Read.w223pmin, Read.w224pmin, Read.w225pmin)
    v22pmax = minmax(Read.w221pmax, Read.w222pmax, Read.w223pmax, Read.w214pmax, Read.w225pmax)

    v23pmin = minmax(Read.w231pmin, Read.w232pmin, Read.w233pmin, Read.w234pmin, Read.w235pmin)
    v23pmax = minmax(Read.w231pmax, Read.w232pmax, Read.w233pmax, Read.w234pmax, Read.w235pmax)

    v24pmin = minmax(Read.w241pmin, Read.w242pmin, Read.w243pmin, Read.w244pmin, Read.w245pmin)
    v24pmax = minmax(Read.w241pmax, Read.w242pmax, Read.w243pmax, Read.w244pmax, Read.w245pmax)

    v25pmin = minmax(Read.w251pmin, Read.w252pmin, Read.w253pmin, Read.w254pmin, Read.w255pmin)
    v25pmax = minmax(Read.w251pmax, Read.w252pmax, Read.w253pmax, Read.w254pmax, Read.w255pmax)


    v31pmin = minmax(Read.w311pmin, Read.w312pmin, Read.w313pmin, Read.w314pmin, Read.w315pmin)
    v31pmax = minmax(Read.w311pmax, Read.w312pmax, Read.w313pmax, Read.w314pmax, Read.w315pmax)

    v32pmin = minmax(Read.w321pmin, Read.w322pmin, Read.w323pmin, Read.w324pmin, Read.w325pmin)
    v32pmax = minmax(Read.w321pmax, Read.w322pmax, Read.w323pmax, Read.w324pmax, Read.w325pmax)

    v33pmin = minmax(Read.w331pmin, Read.w332pmin, Read.w333pmin, Read.w334pmin, Read.w335pmin)
    v33pmax = minmax(Read.w331pmax, Read.w332pmax, Read.w333pmax, Read.w334pmax, Read.w335pmax)

    v34pmin = minmax(Read.w341pmin, Read.w342pmin, Read.w343pmin, Read.w344pmin, Read.w345pmin)
    v34pmax = minmax(Read.w341pmax, Read.w342pmax, Read.w343pmax, Read.w344pmax, Read.w345pmax)

    v35pmin = minmax(Read.w351pmin, Read.w352pmin, Read.w353pmin, Read.w354pmin, Read.w355pmin)
    v35pmax = minmax(Read.w351pmax, Read.w352pmax, Read.w353pmax, Read.w354pmax, Read.w355pmax)


    t1pmin = []
    t1pmax=[]
    t2pmin=[]
    t2pmax=[]
    t3pmin=[]
    t3pmax=[]
    for i in range(len(Rc)):
        for j in range(len(time)):    
            t1pmin_temp = v11pmin.iloc[i,j] + v12pmin.iloc[i,j]*atm_depth.x.iloc[i,j] + v13pmin.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v14pmin.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v15pmin.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t1pmax_temp = v11pmax.iloc[i,j] + v12pmax.iloc[i,j]*atm_depth.x.iloc[i,j] + v13pmax.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v14pmax.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v15pmax.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t2pmin_temp = v21pmin.iloc[i,j] + v22pmin.iloc[i,j]*atm_depth.x.iloc[i,j] + v23pmin.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v24pmin.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v25pmin.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t2pmax_temp = v21pmax.iloc[i,j] + v22pmax.iloc[i,j]*atm_depth.x.iloc[i,j] + v23pmax.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v24pmax.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v25pmax.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t3pmin_temp = v31pmin.iloc[i,j] + v32pmin.iloc[i,j]*atm_depth.x.iloc[i,j] + v33pmin.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v34pmin.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v35pmin.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t3pmax_temp = v31pmax.iloc[i,j] + v32pmax.iloc[i,j]*atm_depth.x.iloc[i,j] + v33pmax.iloc[i,j]*atm_depth.x.iloc[i,j]**2 + v34pmax.iloc[i,j]*atm_depth.x.iloc[i,j]**3 + v35pmax.iloc[i,j]*atm_depth.x.iloc[i,j]**4;
            t1pmin.append(t1pmin_temp)
            t1pmax.append(t1pmax_temp)
            t2pmin.append(t2pmin_temp)
            t2pmax.append(t2pmax_temp)
            t3pmin.append(t3pmin_temp)
            t3pmax.append(t3pmax_temp)
    #all correct above this
    t1pmin_df = pd.DataFrame([(t1pmin[n:n+len(time)]) for n in range(0, len(t1pmin), len(time))])
    t1pmax_df = pd.DataFrame([(t1pmax[n:n+len(time)]) for n in range(0, len(t1pmax), len(time))])
    t2pmin_df = pd.DataFrame([(t2pmin[n:n+len(time)]) for n in range(0, len(t2pmin), len(time))])
    t2pmax_df = pd.DataFrame([(t2pmax[n:n+len(time)]) for n in range(0, len(t2pmax), len(time))])
    t3pmin_df = pd.DataFrame([(t3pmin[n:n+len(time)]) for n in range(0, len(t3pmin), len(time))])
    t3pmax_df = pd.DataFrame([(t3pmax[n:n+len(time)]) for n in range(0, len(t3pmax), len(time))])

    phimupmin = []
    phimupmax = []
    phimup = []
    g5n = []
    g6n = []
    for i in range(len(Rc)):
        for j in range(len(time)):
            for n in range(len(E_m)):
                phimupmin_temp = Phimp.iloc[i,j]*(E_m.iloc[i,n] + (t1pmin_df.iloc[i,j] + t2pmin_df.iloc[i,j]*np.log10(E_m.iloc[i,n]))/(Beta.iloc[i,n]**t3pmin_df.iloc[i,j]))**-alpha3;
                phimupmin.append(phimupmin_temp)
                phimupmax_temp = Phimp.iloc[i,j]*(E_m.iloc[i,n] + (t1pmax_df.iloc[i,j] + t2pmax_df.iloc[i,j]*np.log10(E_m.iloc[i,n]))/(Beta.iloc[i,n]**t3pmax_df.iloc[i,j]))**-alpha3;
                phimupmax.append(phimupmax_temp)
    phimupmin_df = pd.DataFrame([(phimupmin[n:n+200]) for n in range(0, len(phimupmin), len(E_m))])
    phimupmax_df = pd.DataFrame([(phimupmax[n:n+200]) for n in range(0, len(phimupmax), len(E_m))])

    def gpfun(h1,h2,h3,h4,h5):
        return h1 + h2*Rc.iloc[: , 1:]+ h3/(1 + np.exp((Rc.iloc[: , 1:] - h4)/h5));

    g5p = gpfun(Read.h51p, Read.h52p, Read.h53p, Read.h54p, Read.h55p)
    g6p = gpfun(Read.h61p, Read.h62p, Read.h63p, Read.h64p, Read.h65p)


    f3p = []
    for i in range(len(Rc)):
        for j in range(len(time)):
            f3p_temp = g5p.iloc[i,j] + g6p.iloc[i,j]*atm_depth.x.iloc[i,j];
            f3p.append(f3p_temp)
    f3p_df = pd.DataFrame([(f3p[n:n+len(time)]) for n in range(0, len(f3p), len(time))])


    f3p_updated = f3p_df.stack().tolist() #this flattens pressure df into a list so you can incorporate it into the for loop below


    phimup = []
    for i in range(len(phimupmin_df)):
        for j in range(len(E_m)):
            f2p = (phimupmin_df.iloc[i,j]- phimupmax_df.iloc[i,j])/(smin**f3p_updated[i] - smax**f3p_updated[i])
            f1p = phimupmin_df.iloc[i,j] - f2p*smin**f3p_updated[i]
            phimup_temp = f1p + f2p*s**f3p_updated[i]
            phimup.append(phimup_temp)
    Phimup_df = pd.DataFrame([(phimup[n:n+200]) for n in range(0, len(phimup), len(E_m))])


    Site_muE = E_m #muon flux energy bins in MeV
    Site_mup = p #muon flux momentu bins in MeV/c

    #Differential fluxes for negative and positive muons
    mflux_neg = Phimun_df
    mflux_pos = Phimup_df
    mfluxRef_total = 0.0157 #from LSD
    mfluxRef_nint = 0.0071
    mfluxRef_pint = 0.0085

    muRef = Read.mfluxRef_neg + Read.mfluxRef_pos
    modified_muRef = pd.concat([muRef.T]*len(Rc), ignore_index=True)
    muSite = mflux_neg + mflux_pos
    Site_muSF = []

    #Total ground level flux = Phimu
    Phimu = Phimun_df + Phimup_df 

    #Differential muon flux SF as f(E,Rc)
    for i in range(len(Rc)):
        for j in range(len(E_m)):
            Site_muSF_temp = muSite.iloc[i,j]/modified_muRef.iloc[i,j]
            Site_muSF.append(Site_muSF_temp)
    mu_df = pd.DataFrame([(Site_muSF[n:n+len(time)]) for n in range(0, len(Site_muSF), len(E_m))])


    #Total integral flux
    mflux_total = []
    mflux_nint = []
    mflux_pint = []

    for i in range(len(Rc)*len(time)):
        mflux_total_temp = np.trapz(Phimu.T.iloc[:,i], E_m.T[0])
        mflux_total.append(mflux_total_temp)

        #Integral fluxes for pos and neg muons
        mflux_nint_temp = np.trapz(Phimun_df.T.iloc[:,i],  E_m.T[0])
        mflux_nint.append(mflux_nint_temp)
        mflux_pint_temp = np.trapz(Phimup_df.T.iloc[:,i], E_m.T[0])
        mflux_pint.append(mflux_pint_temp)

    mflux_total_df = pd.DataFrame([(mflux_total[n:n+len(time)]) for n in range(0, len(mflux_total), len(time))])
    mflux_nint_df = pd.DataFrame([(mflux_nint[n:n+len(time)]) for n in range(0, len(mflux_nint), len(time))])
    mflux_pint_df = pd.DataFrame([(mflux_pint[n:n+len(time)]) for n in range(0, len(mflux_pint), len(time))])


    Site_muTotal = mflux_total_df/mfluxRef_total
    Site_mn = mflux_nint_df/mfluxRef_nint
    Site_mp = mflux_pint_df/mfluxRef_pint
    Site_mnabs = mflux_nint
    Site_mpabs = mflux_pint

