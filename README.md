# Production Rates Calculator
**Please note: This calculator is still under development! The following README is a draft.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)

[![DOI](https://img.shields.io/badge/DOI-10.1130%2Fabs%2F2021AM--364512-red)](https://gsa.confex.com/gsa/2021AM/webprogram/Paper364512.html)

This repository contains the manuscript, code, and data associated with the project: *A model framework for scaling pre-Quaternary cosmogenic nuclide production rates*.
 
GSA 2021 Abstract: Multiple scaling schemes for cosmogenic nuclide production rates have been developed for the late Quaternary, the period over which most cosmogenic nuclide measurements are applicable. Applications of cosmogenic nuclide measurements on longer timescales to address questions regarding landscape evolution and surface exposure durations are becoming more prevalent. However, production rate calculations through deep time (i.e., pre-late Quaternary) have primarily utilized Quaternary or present-day scaling factors. To increase the accuracy of scaling schemes through deep time, spatiotemporal variations in physical parameters (e.g. geomagnetic field intensity and paleogeography) beyond the Quaternary should be accounted for. We present a production rate scaling scheme model for the past 70 My. This model builds on existing scaling schemes while incorporating effects relevant to deep time applications, specifically by, (1) accounting for site-specific changes in paleolatitude, and (2) integrating geomagnetic field intensity data from two global paleomagnetic databases. We evaluate the efficacy of our model by applying it to existing datasets from paleo exposure sites, and from sites with apparent continuous million-year exposure histories. Our model will enable measurements of stable cosmogenic nuclides to be applied to research questions such as constraining paleoexposure durations between lava flows, quantifying sediment storage on ~Ma timescales, and calculating the formation timescales of paleosurfaces.

*Mijjum, M, Bristol, K.E., Bono, R.K., Sprain, C.J., Tremblay, M.M, 2023. A model framework for scaling pre-Quaternary cosmogenic nuclide production rates. In preparation.*

This Production Rate Calculator is published under the [MIT license](LICENSE.txt).


## Folders 
### Manuscript

The manuscript and reference files and will be included within this folder.


### Data

All the data needed to run the code will be included within this folder. 
-ERA40 data
-etc. etc.
-Excerpt from the GEOMAGIA50.v3 paleointensity database (Brown et al., 2015)
-Excerpt from the MCADAM1.b dipole moment model (Bono et al., 2021)
-Complete PINT model compilation

### Code

The code that estimates production rates and creates the figures for the manuscript will be included in the Jupyter notebooks within this folder.

-Notebook 1: The code that estimates production rates.
-Notebook 2: The code that recreates the figures from the manuscript. 
-Notebook 3: abcd xyz

You can try a preview of the code here (link needs updating):

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mmijjum/Production_Rates_Calculator/tree/main?filepath=demo.ipynb)

### Outputs

Description of outputs will go here. 

## How to use

General walkthrough on usage will go here.

### Dependencies

Use of this code requires PmagPy (https://github.com/PmagPy) which can be installed using pip: 

```pip install pmagpy```

