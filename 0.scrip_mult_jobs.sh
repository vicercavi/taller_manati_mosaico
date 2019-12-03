#!/bin/bash
while IFS=, read col1 col2 col3 col4
do
  qsub -v ID_IMG=${col1},DIR_IMG=${col2},NAME_IMG=${col3} -N ${col1}_pros_ispot_${col1}  1.qsub_eje_pre_procesamiento.sh
done < bd_landsat_loreto.csv