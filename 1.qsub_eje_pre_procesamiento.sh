#!/bin/bash
#PBS -l nodes=1:ppn=10
#PBS -e 07_pbsout/${PBS_JOBNAME}.e${PBS_JOBID}
#PBS -o 07_pbsout/${PBS_JOBNAME}.o${PBS_JOBID}

cd $PBS_O_WORKDIR

##Print HOST EXEC
echo "Nodo de Procesamiento: " $HOSTNAME
echo "\n"
echo "Inicio: " `date "+%d/%m/%Y %H:%M"`
echo "\n"
##source $ANACONDA3/bin/activate Python27
python 1.scrip_pre_procesamiento_2018.py ${DIR_IMG} ${NAME_IMG} ${ID_IMG} | tee log_preprocesamiento.txt
echo "\n"
echo "Fin: " `date "+%d/%m/%Y %H:%M"`