#!/bin/bash
#PBS -N Taller_mosaico
#PBS -l nodes=n009:ppn=5
#PBS -e 07_pbsout/${PBS_JOBNAME}.e${PBS_JOBID}
#PBS -o 07_pbsout/${PBS_JOBNAME}.o${PBS_JOBID}

cd $PBS_O_WORKDIR

##source $ANACONDA3/bin/activate Python27

python 2.scrip_procesamiento_mosaico_2018.py atcor