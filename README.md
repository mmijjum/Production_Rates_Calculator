# SPRITE: Scaling Production Rates In deep TimE

SPRITE is published under the [MIT license](LICENSE.txt).

This repository contains the manuscript, code, and data associated with the project: *A model framework for scaling pre-Quaternary cosmogenic nuclide production rates*.
 
Mijjum et al. (2023) abstract: Cosmogenic nuclide dating is an essential component of studying Earth surface processes. Most scaling schemes for terrestrial cosmogenic nuclide production rates have been developed for the late Quaternary. However, applications of cosmogenic nuclides that extend beyond the late Quaternary are becoming more prevalent. For these deeper time applications, production rate calculations using scaling models optimized for the late Quaternary neglect spatiotemporal variations in geomagnetic field intensity and paleogeography beyond the Quaternary. We present a production rate scaling scheme for the past 70 million years, SPRITE (Scaling Production Rates In deep TimE). This model extends existing scaling schemes into deeper time by (1) accounting for site-specific changes in paleolatitude, and (2) integrating a geomagnetic field intensity model rooted in data from a global paleomagnetic database. We evaluate the efficacy of our model by applying it to existing datasets from paleoexposure sites, and from sites with apparent continuous million-year exposure histories. This scaling model enables measurements of stable cosmogenic nuclides to be applied to research questions such as constraining hiatus durations between ancient lava flows, quantifying sediment transport and storage timescales in the geologic past, and calculating the formation timescales of stable landforms in arid environments over millions of years.


* Mijjum, M, Bristol, K.E., Bono, R.K., Sprain, C.J., Tremblay, M.M, 2023. A model framework for scaling pre-Quaternary cosmogenic nuclide production rates.



## Folders 

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
    * MCADAM_1b_cosmo.csv - Excerpt from the MCADAM1.b dipole moment model, designed for use in SPRITE by implementing 250ka bins (Bono et al., 2022).
	
### Code

Description of each of the scripts:

1) Read.py
    * All .csv / .xlsx files from 'Data' are read into the code here.

2) mcadam.py 
    * MCADAM_1b_cosmo.csv is read in only for the time period specified by the user in 'Inputs.xlsx'. 

3) Pmag_paleolat.py
    * Present day site latitude is converted to paleolatitude for the specified time duration 'Inputs.xlsx'. 

4) Rc.py
    * Cutoff rigidity is calculated following Eq. 2 of Mijjum et al. (2023).

5) atm_depth.py
    * Elevation is converted to atmospheric depth either using ERA40 reanalysis data or a standard atmosphere conversion.
    * Conversion method is specified in excel spreadsheet. 1 = standard atmosphere, 0 = ERA40. 

6) neutrons.py
    * Production via spallation from neutrons is calculated. 

7) protons.py
    * Production via spallation from protons is calculated.

8) muons.py
    * Production via muons (only for 21Ne) is calculated. 

9) shielding.py
    * Shielding (due to sample thickness) scaling factor is calculated.

10) scaling_factor.py
    * Scaling factor due to spallation is calculated.

11) expage.py
    * Exposure ages are calculated. 
    * If 21Ne: incorporates muons into calculation. 


### Outputs

SPRITE calculates exposure ages using 3He and 21Ne measurements. The following are relevant outputs from individual scripts:

* expage.py: when run, will return the exposure age of each sample specified in 'inputs.xlsx'
* scaling_factor.py: when run, 'Siteprod_df' will generate a dataframe of site-specific & time varying spallogenic scaling factors.
* Pmag_paleolat.py: when run, 'pl_df' will generate a dataframe of site-specific & time varying paleolatitudes.

## How to use

1) Input sample-specific information into 'inputs.xlsx'. This includes:
* Sample name
* Latitude (degrees, positive if N hemisphere, negative if S)
* Longitude (degrees, positive if E hemisphere, negative if W)
* Elevation (MASL)
* Sample thickness (cm)
* Sample density (g/cm3)
* Topographic shielding correction (0 - 1)
* Erosion rate (g/cm2/yr)
* Nuclide concentration (at/g)
* Nuclide uncertainty (at/g)
* Nuclide - mineral system 
* Atmospheric conversion preference
* Time 1 and Time 2 (exposure duration)(Ma)
* Tectonic plate
* Depth below paleosurface
* Paleoduration

The user may also refer to Figure 3 of Mijjum et al. (2023) for a workflow diagaram of how each calculation within the model is executed. 

* NOTE: Details on how to format spreadsheet are in 'README' tab of 'inputs.xlsx'. Only 'Active' tab is read into code. All other tabs are reference tables that can be copy-pasted into 'Active' to generate certain figures, or for specific datasets. 

2) Run 'expage.py' 

3) Will output exposure ages for each sample. For ~20 samples, takes ~3 minutes to run for 20 Ma. 

### Dependencies

Use of SPRITE requires PmagPy (https://github.com/PmagPy) which can be installed using pip: 

```pip install pmagpy```

To see additional dependencies, see requirements.txt.

