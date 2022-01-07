# Dissertation: Antarctic Megadunes
This work is the code used as part of my undergraduate dissertation. Appologies for poor commenting throughout scripts.

## Megadunes (MD)
These are low amplitude, high wavelength features constructed from aelian drift snow, formed from tens thousands of years. They occupy vast fields +500,000km2 (see image below for segmnet example). These features are previously thought to occupy ~18% of Eastern Antartrica. It is unknown how well modern altimters will represent the megadune morphology and if so how accurately. This work aims to assess this comparing between various forms of altimters ICESat-2 (IS2), CryoSat-2 (CS2). Therefore, assessing Radar vs laser based approaches. This was weighted and assessed against REMA a DEM for antartica constructed from ICESat-1 and CryoSat-2 alongside the Worldview product series and Geoeye data. 

<img src="3D MD fig copy.png" alt="Simply Easy Learning" width="800" height="320">
- 3D image of megadunes East of Lake Vostok.

## Quantifying MD.
These scripts illustrate the code used to investigate Antarcticas megadunes. Megadunes are a unique wave landfrom expression formed by wind laid snow deposits. 

### REMA

### Extract elevation data from line shape file off tif.ipynb
code based from: https://portailsig.org/content/python-utilisation-des-couches-vectorielles-et-matricielles-dans-une-perspective-geologique-.html .

These REMA extracted elevations from a flightpath aligned with various altimeter satellite products to assess how well REMA accurately represents megadune features. The altimeter products used were ICESat-2, CryoSat-2 and Sentinnel-3.

### Calculate wave landform expression charachteristics
Calculating: amplitude, wavelength.

see/ use Waveform.py

This script extracts the peak, trough points along transect lines and stores these values. These values are then used to calculate amplitude and wavelengths.
Plots can be created showing all transects for each site. But adds 12mins runtime to the script.

### Extract altimter representation of megadunes

HDF5 and netcdf files containing transect paths were generated and extracted over 5-sites and contrasted with REMA. See individual site scripts clean_site[x].py

