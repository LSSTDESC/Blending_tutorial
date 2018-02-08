#!/usr/bin/env bash
export OMP_NUM_THREADS=4
INST_DIR=/global/common/software/lsst/cori-haswell-gcc/stack/
source $INST_DIR/setup_w_2017_46_py3_gcc6.sh
setup meas_algorithms
setup lsst_apps
#setup lsst_sims # In the case that we need it in the future
export PYTHONPATH=$PYTHONPATH:/global/projecta/projectdirs/lsst/groups/WL/projects/wl-btf/WeakLensingDeblending/descwl
exec python -m ipykernel $@
