# Dissertation: Antarctic Megadunes
This work is the code used as part of my undergraduate dissertation. 

## Megadunes (MD)
These are low amplitude, high wavelength features constructed from aelian drift snow, formed from tens thousands of years. They occupy vast fields +500,000km2 (see image below for segmnet example). These features are previously thought to occupy ~18% of Eastern Antartrica. Due to there geomorphology altimeter accuracy in picking up these features is difficult and this work aims to assess this comparing between various forms of altimters ICESat-2 (IS2), CryoSat-2 (CS2) and Sentinel-3 (S3). Therefore assessing Radar vs laser based approaches. This was weighted and assessed against REMA a DEM for antartica constructed from ICESat-1 and CryoSat alongside the Worldview product series and Geoeye data. 

<img src="3D MD fig copy.png" alt="Simply Easy Learning" width="800" height="320">
- 3D image of megadunes East of Lake Vostok.

##Quantifying MD.
These scripts illustrate the code used to investigate Antarcticas megadunes. Megadunes are a unique wave landfrom expression formed by wind laid snow deposits. 

## REMA

### Extract elevation data from line shape file off tif.ipynb
code based from: https://portailsig.org/content/python-utilisation-des-couches-vectorielles-et-matricielles-dans-une-perspective-geologique-.html .

These REMA extracted elevations from a flightpath aligned with various altimeter satellite products to assess how well REMA accurately represents megadune features. The altimeter products used were ICESat-2, CryoSat-2 and Sentinnel-3.

### Calculate wave landform expression charachteristics
Calculating: amplitude, wavelength, length and frequency.

see/ use Waveform.py

This script extracts the peak, trough points along transect lines and stores these values. These values are then used to calculate amplitude and wavelengths.
Plots can be created showing all transects for each site. But adds 12mins runtime to the script.
