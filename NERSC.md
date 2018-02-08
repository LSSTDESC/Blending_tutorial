# Prepare to Run at NERSC

For general information about creating your account and logging in, see [here](https://confluence.slac.stanford.edu/display/LSSTDESC/Getting+Started+at+NERSC).

Once you are logged in, there are two initial setup task you need to perform to prepare to run tutorials at NERSC.

## Clone the Tutorial Repository

Clone the [tutorial github repository](https://github.com/LSSTDESC/Blending_tutorial)
using either of these commands (not sure which? details [here](https://help.github.com/articles/which-remote-url-should-i-use/)):
```
git clone https://github.com/LSSTDESC/Blending_tutorial.git
git clone git@github.com:LSSTDESC/Blending_tutorial.git
```
This will create a subdirectory called `Blending_tutorial`.  Stay in the parent (current) directory for the steps below.

## Initialize a Custom Jupyter Kernel for Running DM

Setup an LSST environment:
```
source /global/common/software/lsst/cori-haswell-gcc/stack/setup_w_2017_46_py3_gcc6.sh
```
Initialize a new jupyter kernel:
```
ipython kernel install --user --name lsst2
```
Customize the new kernel (paths assume that you are in the same directory where you ran `git clone...` above):
```
cp Blending_tutorial/kernel.json ~/.local/share/jupyter/kernels/lsst2/
cp Blending_tutorial/lsst-kernel2.sh ~/.local/share/jupyter/kernels/lsst2/
chmod ug+rx ~/.local/share/jupyter/kernels/lsst2/lsst-kernel2.sh
```
## Launch Jupyter at NERSC

Once the two steps above are completed, you can launch a jupyter kernel at NERSC directly from your browser by visiting
https://jupyter-dev.nersc.gov/. This should display a list of files and directories on your nersc account.

To start one of blending tutorials, navigate to the `Blending_tutorial` directory and click on its name.

You can also launch a new notebook with DM configured by selecting `lsst2` from the "New" menu in the upper-right corner.
