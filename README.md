# Blending tutorial (SLAC February 2018)
Repo containing the tutorial for the Blending Task Force session at the LSST DESC collaboration meeting at SLAC on February 2018.

## Generate your simulated image with WeakLensingDeblending

1. Using the [WeakLensingDeblending package](https://github.com/LSSTDESC/WeakLensingDeblending/) (WLD) you can generate your own LSST-like images. To do that, you can download the CatSim instance catalog [here](ftp://ftp.slac.stanford.edu/groups/desc/WL/OneDegSq.fits.gz). Once you have the file you can go to the folder where you have the WeakLensingDeblending package and run `./simulate.py --survey-name LSST --filter-band i --catalog-name INPUT_CATALOG --output-name OUTPUT_CATALOG`. You can test it using the catalog at `/global/projecta/projectdirs/lsst/groups/WL/projects/wl-btf/OneDegSq.fits`. This will generate a LSST 10-year i-band like image and a catalog containing true shapes, positions and fluxes of galaxies, and Fisher-matrix predictions for their uncertainties (it also has the capability to produce predictions for the bias). If you are not interested in the individual, un-blended postage stamps you can add the option `--no-stamps` and it will produce a more lightweight output. You can see more options by executing `./simulate.py --help`.

## Setup the DM stack
1. The first step is to configure a custom kernel at jupyter-dev (NERSC). More info [here](https://github.com/LSSTDESC/Monitor/blob/master/doc/jupyter-dev.md). First create a new kernel with the command `ipython kernel install --user --name KERNEL_NAME`. This will generate a directory `~/.local/share/jupyter/kernels/KERNEL_NAME`. I chose `KERNEL_NAME=lsst2`. This directory contains a file called `kernel.json` that we will modify in step 3.

2. Copy the script `lsst-kernel2.sh` from this repo in your favorite location and change the permissions with `chmod ug+rx lsst-kernel2.sh`

3. Modify the `kernel.json` file to link to `lsst-kernel2.sh` (check the file `kernel.json` to see an example).

4. Start your session in https://jupyter-dev.nersc.gov and you should be able to open and execute the notebook. 

## Run the notebook

1. Just point to the path where you have the image generated with WLD, set a seed for the noise and save the results in a FITS file if you want to.

## Analyze the results and compare with the true catalog

One of the advantages of this approach is that you have a truth-table to compare with. Perform your favorite analysis to test the effects of blending. You can find the outputs of WLD at `/global/projecta/projectdirs/lsst/groups/WL/projects/wl-btf/LSST_i_lite.fits` and a processed catalog by the DM stack at the same folder in the file `LSST_i_DM.fits.gz` and perform your favorite analysis. You can also check an example in `Example_analysis.ipynb` 
