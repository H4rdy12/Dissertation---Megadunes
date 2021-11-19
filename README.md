# Dissertation: Antarctic Megadunes
These scripts illustrate the code used to investigate Antarcticas megadunes. Megadunes are a unique wave landfrom expression formed by wind laid snow deposits. 

<img src="3D MD fig copy.png" alt="Simply Easy Learning" width="800" height="320">
- 3D image of megadunes East of Lake Vostok.

## REMA

### Extract elevation data from line shape file off tif.ipynb
code based from: https://portailsig.org/content/python-utilisation-des-couches-vectorielles-et-matricielles-dans-une-perspective-geologique-.html .

These REMA extracted elevations from a flightpath aligned with various altimeter satellite products to assess how well REMA accurately represents megadune features. The altimeter products used were ICESat-2, CryoSat-2 and Sentinnel-3.

### Calculate wave landform expression charachteristics
Calculating: amplitude, wavelength, length and frequency.

see/ use Waveform.py

This script extracts the peak, trough points along transect lines and stores these values. These values are then used to calculate amplitude and wavelengths.
Plots can be created showing all transects for each site. But adds 12mins runtime to the script.
