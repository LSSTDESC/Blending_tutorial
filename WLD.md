# Simulate Realistic Galaxies

We simulate realistic galaxies using the WeakLensingDeblending package and the LSST DM CatSim catalog.

For a general tutorial introduction to the WeakLensingDeblending package, start [here](http://weaklensingdeblending.readthedocs.io/en/latest/quickstart.html).

The file `/global/projecta/projectdirs/lsst/groups/WL/projects/wl-btf/LSST_i_lite.fits` can be reproduced with the following steps:
```
mkdir tutorial
cd tutorial
ln -s /global/projecta/projectdirs/lsst/groups/WL/projects/wl-btf/WeakLensingDeblending WLD
WLD/simulate.py --survey-name LSST --filter-band i --catalog-name WLD/OneDegSq.fits --no-stamps
```
Note that this will take ~20 minutes to run.
