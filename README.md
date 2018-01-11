# Deblending_tutorial_SLAC2018
Repo containing the the tutorial for the deblending session at the LSST DESC collaboration meeting at SLAC 2018.

# Setup the DM stack
1. The first step is to configure a custom kernel at jupyter-dev (NERSC). More info [here] (https://github.com/LSSTDESC/Monitor/blob/master/doc/jupyter-dev.md) first you should create a new kernel with the command `ipython kernel install --user --name KERNEL_NAME`. This will generate a directory `~/.local/share/jupyter/kernels/KERNEL_NAME`. I chose `KERNEL_NAME=lsst2`. This directory contains a file called `kernel.json` that we will modify in step 3.

2. Copy the script `lsst-kernel2.sh` from this repo in your favorite location and change the permissions with `chmod ug+rx lsst-kernel2.sh`

3. Modify the `kernel.json` file to link to `lsst-kernel2.sh` (check the file `kernel.json` to see an example).

4. Start your session in https://jupyter-dev.nersc.gov and you should be able to open and execute the notebook. 
