#PBS -N Export mosaico
#PBS -l nodes=1:ppn=24
#PBS -e 07_pbsout/${PBS_JOBNAME}.e${PBS_JOBID}
#PBS -o 07_pbsout/${PBS_JOBNAME}.o${PBS_JOBID}

cd $PBS_O_WORKDIR

python 3.scrip_fexport.py | tee log_export.txt