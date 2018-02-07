# Blending tutorial (SLAC February 2018)
Repo containing the tutorial for the Blending Task Force session at the LSST DESC collaboration meeting at SLAC on February 2018.

# Quick start

1. Please if you don't have a NERSC account or don't remember how to access NERSC follow the instructions [here](https://confluence.slac.stanford.edu/display/LSSTDESC/Getting+Started+at+NERSC)

2. Clone this repo into your favorite location on NERSC

## Setup the DM stack

3. The next step is to configure a custom kernel at jupyter-dev (NERSC). More info [here](https://github.com/LSSTDESC/Monitor/blob/master/doc/jupyter-dev.md). First create a new kernel with the command `ipython kernel install --user --name KERNEL_NAME`. This will generate a directory `~/.local/share/jupyter/kernels/KERNEL_NAME`. We chose `KERNEL_NAME=lsst2`. This directory contains a file called `kernel.json` that we will modify in a different step.

4. Copy the script `lsst-kernel2.sh` from this repo in your favorite location and change the permissions with `chmod ug+rx lsst-kernel2.sh`

4. Modify the `kernel.json` file to link to `lsst-kernel2.sh` (check the file `kernel.json` to see an example).

5. Start your session in https://jupyter-dev.nersc.gov and you should be able to open and execute the notebooks in this repo. 

## Run the analysis notebooks

You can find two different tutorial notebooks in this repository. In `Two_galaxy_blends.ipynb` you can create simple two-galaxy blends with the DESC Weak Lensing Deblending package (WLD), analyze the images with the LSST DM stack, and then develop metrics on the output. If you are not able to install the LSST DM stack, you can run an example analysis on a pre-generated catalog using `Two_galaxy_blends_catalog.ipynb`.

The second tutorial is based on generating and analyzing an LSST 10-year depth i-band like image of a chip (4096 x 4096 pixels). You can also use the pre-generated catalog or use WLD to generate your own. Then you can run the DM-stack on the image using the notebook `Process.ipynb`. Finally, you can run some analysis in these catalogs, an example is made on `Example_analysis.ipynb`. You can use our pre-generated WLD and DM catalogs and run this notebook.

All our data products can be found at NERSC in `/global/projecta/projectdirs/lsst/groups/WL/projects/wl-btf`.

