# SPRITE: Scaling Production Rates In deep TimE

SPRITE is published under the [MIT license](LICENSE.txt).

This repository contains the manuscript, code, and data associated with the project: *A model framework for scaling pre-Quaternary cosmogenic nuclide production rates*.
 
Mijjum et al. (2024) abstract: Cosmogenic nuclide dating is an essential component of studying Earth surface processes, but it requires knowledge of how nuclide production rates vary in time and space. Typically, production rates are calibrated at sites with independently well-constrained exposure histories and then scaled to other sites of interest using scaling frameworks that account for spatial and temporal variation in the secondary cosmic-ray flux at Earth’s surface. To date,  scaling schemes for terrestrial cosmogenic nuclide production rates have been developed for the Quaternary, yet cosmogenic nuclide applications that extend beyond the Quaternary are becoming more prevalent. For these deeper time applications, production rate calculations using scaling models optimized for the latest Quaternary neglect longer term spatiotemporal variations in geomagnetic field intensity, paleogeography, and paleoatmospheric depth. We present a production rate scaling scheme for the past 70 million years, SPRITE (Scaling Production Rates In deep TimE). This model extends existing scaling schemes into deeper time by (1) accounting for site-specific changes in paleolatitude, (2) integrating a geomagnetic field intensity model rooted in data from a global paleomagnetic database, and (3) incorporating climate-driven, time-varying atmospheric depths. We evaluate the efficacy of our model by applying it to existing datasets from paleoexposure sites, and from sites with apparent continuous million-year exposure histories. This scaling model can be applied with measurements of stable cosmogenic nuclides to research questions such as constraining hiatus durations between ancient lava flows, quantifying sediment transport and storage timescales in the geologic past, and calculating the formation timescales of stable landforms in arid environments over millions of years.

* Mijjum, M, Bristol, K.E., Bono, R.K., Sprain, C.J., Lifton, N., Tremblay, M.M, 2024. A model framework for scaling pre-Quaternary cosmogenic nuclide production rates.



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
	* "lsdn_rc.xlsx" - Magnetic model as implemented in LSDn from 0-2Ma. Designed for use in SPRITE using the same temporal resolution as LSDn (Lifton et al., 2014; Lifton, 2016).
	
### Code

Description of each of the scripts. Note: corresponding "MCADAM" scripts will run a low-resolution version of the model, where the magnetic field from 0-2 Ma is taken from MCADAM magnetic model, not the same high-resolution magnetic model as implemented as LSDn (see Table 1 in Mijjum et al., 2024). 

1) Read.py
    * All .csv / .xlsx files from 'Data' are read into the code here.

2) mcadam.py 
    * MCADAM_1b_cosmo.csv is read in only for the time period specified by the user in 'Inputs.xlsx'. 
	* Magnetic model implemented in SPRITE from 2-70 Ma (Bono et al., 2022)

3) Pmag_paleolat.py || Pmag_paleolat_MCADAM.py
    * Present day site latitude is converted to paleolatitude for the specified time duration 'Inputs.xlsx'. 

4) Rc.py || Rc_MCADAM.py
    * Cutoff rigidity is calculated following Eq. 2 of Mijjum et al. (2024).

5) atm_depth.py || atm_depth_MCADAM.py
    * Elevation is converted to atmospheric depth either using ERA40 reanalysis data, standard atmosphere, or Valdes et al. (2021) paleoclimate-based conversion.
    * Conversion method is specified in excel spreadsheet. 

6) neutron_spallation.py || neutron_spallation_MCADAM.py
    * Production via spallation from neutrons is calculated. 


7) proton_spallation.py || neutron_spallation_MCADAM.py
    * Production via spallation from protons is calculated.

8) Muons_v2.py || Muons_v2_MCADAM.py
    * Production via muons (only for 21Ne) is calculated, after Balco (2017).

9) shielding.py
    * Shielding (due to sample thickness) scaling factor is calculated.

10) scaling_factor.py || scaling_factor_MCADAM.py
    * Scaling factor due to spallation is calculated.
	
11) expage.py || expage_MCADAM.py
    * Exposure ages are calculated. 
    * If 21Ne: incorporates muons into calculation. 
	* If expage_MCADAM.py is run, all preceding scripts with the ending _MCADAM.py will run. This will implement a lower resolution magnetic model from 0-2Ma (directly from MCADAM, 8 time bins), as opposed to using the same magnetic model as LSDn from 0-2Ma (see Table 1, Mijjum et al., 2024, >1700 time bins). 

### Outputs

SPRITE calculates exposure ages using 3He and 21Ne measurements. The following are relevant outputs from individual scripts:

* expage.py: when run, will return the exposure age of each sample specified in 'inputs.xlsx'
* scaling_factor.py: when run, 'Siteprod_df' will generate a dataframe of site-specific & time varying spallogenic scaling factors.
* Pmag_paleolat.py: when run, 'pl_df' will generate a dataframe of site-specific & time varying paleolatitudes.
* atm_depth.py: when run, will return a dataframe of site-specific atmospheric depths (and time-varying, if using Valdes et al. (2021) conversion method.)

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
* Uplift/Subsidence rate (cm/yr)
	- Uplift: will be negative values (e.g., if you have a continuously exposed surface and input a modern day elevation of 500 MASL but you know the surface has been uplifted, in the past it should be lower than 500 MASL.)
* Nuclide concentration (at/g)
* Nuclide uncertainty (at/g)
* Nuclide - mineral system 
* Atmospheric conversion preference
* Time 1 and Time 2 (exposure duration)(Ma)
* Tectonic plate
* Depth below paleosurface
* Paleoduration

The user may also refer to Figure 3 of Mijjum et al. (2023) for a workflow diagaram of how each calculation within the model is executed. 

* NOTE: Details on how to format spreadsheet are in 'README' tab of 'inputs.xlsx'. Only 'Active' tab is read into code. See "inputs_archive.xlsx" for example input parameters used to generate figures in Mijjum et al. (2024).

2) Run 'expage.py' OR "expage_MCADAM.py"
	- If you run "expage.py", computational time will be much longer but more accurate for Quaternary timescales. It will run the latest iteration of SPRITE where the magnetic model from 0-2Ma is identical to what is currently implemented in LSDn (higher temporal resolution), which spans >1700 time bins. 
	- If you run 'expage_MCADAM.py', computational time will be much faster because the LSDn magnetic model is not added to this version. It will run earlier iterations of this SPRITE where 0-2Ma is derived from MCADAM and is only 8 time bins.
3) Will output exposure ages for each sample.

### Dependencies

Use of SPRITE requires PmagPy (https://github.com/PmagPy) which can be installed using pip: 

```pip install pmagpy```

To see additional dependencies, see requirements.txt.

