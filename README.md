# High Performance Computing aplicado a generación de mosaicos
Códigos para el taller de uso de Supercomputadora manatí para generación de mosaicos

## Pasos

### 1. Configurar espacio de trabajo
#### Crear la carpeta del proyecto
```bash
mkdir taller
cd taller 
mkdir 01_dataset
mkdir 02_import
mkdir 03_orthoimg
mkdir 04.1_mask
mkdir 04.2_haze
mkdir 04.3_atcor
mkdir 05.1_premos
mkdir 05.2_defmos
mkdir 05.3_runmos
mkdir 06_dem30mt
mkdir 07_pbsout
mkdir 08_export
```
#### Extraer Imagenes landsat
```bash
cd 01_dataset
mkdir LC08_L1TP_006063_20181029_20181115_01_T1 & tar xvzf /opt/shared/repositorio/landsat/LC08_L1TP_006063_20181029_20181115_01_T1.tar.gz -C LC08_L1TP_006063_20181029_20181115_01_T1/

mkdir LC08_L1TP_006064_20180911_20180927_01_T1 & tar xvzf /opt/shared/repositorio/landsat/LC08_L1TP_006064_20180911_20180927_01_T1.tar.gz -C LC08_L1TP_006064_20180911_20180927_01_T1/

mkdir LC08_L1TP_007063_20170713_20170726_01_T1 & tar xvzf /opt/shared/repositorio/landsat/LC08_L1TP_007063_20170713_20170726_01_T1.tar.gz -C LC08_L1TP_007063_20170713_20170726_01_T1/

mkdir LC08_L1TP_007064_20170713_20170726_01_T1 & tar xvzf /opt/shared/repositorio/landsat/LC08_L1TP_007064_20170713_20170726_01_T1.tar.gz -C LC08_L1TP_007064_20170713_20170726_01_T1/
```
#### Codificando para automatizacion del procesamiento 
Regresar al directorio de taller
```bash
cd ..
```
Crear base datos de las imagenes 

Script para leer la base datos y ejecutar el preprocesamiento

Script del gestor de colas

Script de preprocesamiento

Scrip de Procesamiento de mosaico. 

#### Ejecucion de preprocesamiento 
```bash
./0.scrip_mult_jobs.sh
```
#### Ejecucion de procesamiento
```bash
qsub 2.qsub_eje_procesamiento_mosaico.sh
```
#### Monitoreo de procesos
```bash
qstat
```

#### Comandos utiles
Para listar contenido
```bash
ls
```
Para para acceder a un carpeta
```bash
cd carpeta
```
Para crear un archivo
```bash
touch archivo.txt
``` 
Para ver contenido de un arhivo
```bash
cat archivo.txt
```
Para elimnar un archivo
```bash
rm archivo.txt
``` 
Para editar un archivo
```bash
nano archivo.txt
#para cerrar y guardar
ctr+x 
y
enter
``` 
