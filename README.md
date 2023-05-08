# SPRITE: Scaling Production Rates In deep TimE
**Please note: This calculator is still under development! The following README is a draft.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)

[![DOI](https://img.shields.io/badge/DOI-10.1130%2Fabs%2F2021AM--364512-red)](https://gsa.confex.com/gsa/2021AM/webprogram/Paper364512.html)

This repository contains the manuscript, code, and data associated with the project: *A model framework for scaling pre-Quaternary cosmogenic nuclide production rates*.
 
GSA 2021 Abstract: Multiple scaling schemes for cosmogenic nuclide production rates have been developed for the late Quaternary, the period over which most cosmogenic nuclide measurements are applicable. Applications of cosmogenic nuclide measurements on longer timescales to address questions regarding landscape evolution and surface exposure durations are becoming more prevalent. However, production rate calculations through deep time (i.e., pre-late Quaternary) have primarily utilized Quaternary or present-day scaling factors. To increase the accuracy of scaling schemes through deep time, spatiotemporal variations in physical parameters (e.g. geomagnetic field intensity and paleogeography) beyond the Quaternary should be accounted for. We present a production rate scaling scheme model for the past 70 My. This model builds on existing scaling schemes while incorporating effects relevant to deep time applications, specifically by, (1) accounting for site-specific changes in paleolatitude, and (2) integrating geomagnetic field intensity data from two global paleomagnetic databases. We evaluate the efficacy of our model by applying it to existing datasets from paleo exposure sites, and from sites with apparent continuous million-year exposure histories. Our model will enable measurements of stable cosmogenic nuclides to be applied to research questions such as constraining paleoexposure durations between lava flows, quantifying sediment storage on ~Ma timescales, and calculating the formation timescales of paleosurfaces.

*Mijjum, M, Bristol, K.E., Bono, R.K., Sprain, C.J., Tremblay, M.M, 2023. A model framework for scaling pre-Quaternary cosmogenic nuclide production rates. In preparation.*

SPRITE is published under the [MIT license](LICENSE.txt).


## Folders 
### Manuscript

The manuscript and reference files and will be included within this folder.


### Data
All the data needed to run the code are included within this folder. 

The following .csv files are adapted from LSD:

* Spreadsheet with user-provided sample-specific information: 
    * inputs.xlsx

* Integrated neutron flux < 15 MeV:
    * a_values.csv
    * b_values.csv

* Basic Spectrum
    * basic_spectrum_protons.csv
    * basic_spectrum.csv 
    * c_values.csv

* Ground level spectrum
    * ground_level_spectrum.csv

* Thermal neutron spectrum 
    * thermal_neutron_spectrum.csv

* Primary spectrum (for protons)
    * primary_spectrum.csv

* Secondary spectrum (for protons)
    * secondary_spectrum.csv
    * h_values_protons.csv

* Reaction cross sections
    * Alnx3HeT.csv
    * Alpx3HeT.csv
    * Canx3HeT.csv
    * Capx3HeT.csv
    * Capx3HeT.csv
    * Fenx3HeT.csv
    * Fepx3HeT.csv
    * Mgnx3HeT.csv
    * Mgpx3HeT.csv
    * Onx3HeT.csv
    * Opx3HeT.csv
    * Sinx3HeT.csv
    * Sipx3HeT.csv
    * SinxNe21.csv
    * SipxNe21.csv

* ERA40 reanalysis data
    * ERA40lat.csv
    * ERA40lon.csv
    * meanP.csv
    * meanT.csv

* Muon flux
    * mfluxRef_neg.csv
    * mfluxRef_pos.csv

The following .csv files are what make up the magnetic data compilation:

* Geomagnetic data
    * archeo010.csv - Excerpt from the GEOMAGIA50.v3 paleointensity database (Brown et al., 2015)
    * MCADAM_1b.csv - Excerpt from the MCADAM1.b dipole moment model (Bono et al., 2021)
	
### Code

Description of each of the scripts:

1) Read.py
- All .csv / .xlsx files from 'Data' are read into the code here.

2) mcadam.py 
- MCADAM and GEOMAGIA data is compiled into a contineous geomagnetic model.  

3) Pmag_paleolat.py
- Present day site latitude is converted to paleolatitude for the specified time duration in User_Interface. 

4) Rc.py
- Cutoff rigidity is calculated following Dunai (2001). 

5) atm_depth.py
- Elevation is converted to atmospheric depth either using ERA40 reanalysis data or a standard atmosphere conversion.
- Conversion method is specified in excel spreadsheet - 1 = standard atmosphere, 0 = ERA40. 

6) neutrons.py
- Production via spallation from neutrons is calculated. 

7) protons.py
- Production via spallation from protons is calculated.

8) muons.py
- Production via muons (only for 21Ne) is calculated. 

9) shielding.py
- Shielding (due to sample thickness) scaling factor is calculated.

10) scaling_factor.py
- Scaling factor due to spallation is calculated.

11) expage.py
- Exposure ages are calculated. 
- If 21Ne: incorporates muons into calculation. 

12) expage_modified.py
- Tests a range of exposure ages and erosion rates to minimize chi-square values (of nuclide concentration)

13) for_plotting.py ##NOTE FOR TYPICAL USE
- code for generating plots in Mijjum et al. (2023)

### Outputs

SPRITE calculates exposure ages using 3He and 21Ne measurements. The following are relevant outputs from individual scripts:

- expage.py: when run, will return the exposure age of each sample specified in 'inputs.xlsx'
- scaling_factor.py: when run, 'Siteprod_df' will generate a dataframe of site-specific & time varying spallogenic scaling factors.
- Pmag_paleolat.py: when run, 'pl_df' will generate a dataframe of site-specific & time varying paleolatitudes.

## How to use

1) Input sample-specific information into 'inputs.xlsx'. This includes:
- Sample name
- Latitude (degrees, positive if N hemisphere, negative if S)
- Longitude (degrees, positive if E hemisphere, negative if W)
- Elevation (MASL)
- Sample thickness (cm)
- Sample density (g/cm3)
- Topographic shielding correction (0 - 1)
- Erosion rate (cm/yr)
- Nuclide concentration (at/g)
- Nuclide uncertainty (at/g)
- Nuclide - mineral system 
- Atmospheric conversion preference
- Tectonic plate
- Start and stop duration
- Mineral nuclide pair
- Atmospheric pressure conversion
- Tectonic plate

* NOTE: only 'Active' tab is read into code. All other tabs are reference tables that can be copy-pasted into 'Active' to generate certain figures, or for specific datasets. 

2) Run 'expage.py' 

3) Will output exposure ages for each sample. For ~20 samples, takes ~3 minutes to run for 20 Ma. 

### Dependencies

Use of SPRITE requires PmagPy (https://github.com/PmagPy) which can be installed using pip: 

```pip install pmagpy```

To see additional dependencies, see requirements.txt.

