#!/usr/bin/env bash
export OMP_NUM_THREADS=4
setup lsst_sims
INST_DIR=/global/common/software/lsst/cori-haswell-gcc/stack/
source $INST_DIR/setup_w_2017_46_py3_gcc6.sh
setup meas_algorithms
setup lsst_apps
export PYTHONPATH=$PYTHONPATH:/global/homes/j/jsanch87/WeakLensingDeblending/descwl
exec python -m ipykernel $@
