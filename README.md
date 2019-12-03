# High Performance Computing aplicado a generación de mosaicos
Códigos para el taller de uso de Supercomputadora manatí para generación de mosaicos

## Requisitos
### Tener cuenta en a la Supercomputadora Manatí del IIAP. 
Puede solicitar la cuenta en el siguiente [link](https://docs.google.com/forms/d/e/1FAIpQLSetIRziYnWZbAeiRBg9jeNXnCWJQ0EPYaASL9cFLmL8YFv3SA/viewform)

### Acceder a Supercomputador
Inicie sesíon con el usuario y contraseña proporcionado
### Descargar código
```bash
git clone https://github.com/vicercavi/taller_manati_mosaico.git
```
## Pasos

### Configurar espacio de trabajo
#### 1. Crear la carpeta del proyecto
```bash
cd taller_manati_mosaico/ 
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
#### 2. Extraer Imagenes landsat
```bash
cd 01_dataset
mkdir LC08_L1TP_006063_20181029_20181115_01_T1
tar xvzf /opt/shared/repositorio/landsat/LC08_L1TP_006063_20181029_20181115_01_T1.tar.gz -C LC08_L1TP_006063_20181029_20181115_01_T1/

mkdir LC08_L1TP_006064_20180911_20180927_01_T1
tar xvzf /opt/shared/repositorio/landsat/LC08_L1TP_006064_20180911_20180927_01_T1.tar.gz -C LC08_L1TP_006064_20180911_20180927_01_T1/

mkdir LC08_L1TP_007063_20170713_20170726_01_T1
tar xvzf /opt/shared/repositorio/landsat/LC08_L1TP_007063_20170713_20170726_01_T1.tar.gz -C LC08_L1TP_007063_20170713_20170726_01_T1/

mkdir LC08_L1TP_007064_20170713_20170726_01_T1
tar xvzf /opt/shared/repositorio/landsat/LC08_L1TP_007064_20170713_20170726_01_T1.tar.gz -C LC08_L1TP_007064_20170713_20170726_01_T1/
```
#### 3. Codificando para la automatización del procesamiento 
Regresar al directorio de taller
```bash
cd ..
```
Crear base datos de las imagenes.
```bash
cat bd_landsat_loreto.csv 
```
Script para leer la base datos y ejecutar el preprocesamiento
```bash
cat 0.scrip_mult_jobs.sh
```
Script del gestor de colas para el preprocesamiento
```bash
cat 1.qsub_eje_pre_procesamiento.sh
```
Script Python de preprocesamiento utilizando PCI-GEOMATICA. Editar la direccion del proyecto 
```bash
cat 1.scrip_pre_procesamiento_2018.py
pwd
nano 1.scrip_pre_procesamiento_2018.py
```
Script del gestor de colas para el procesamiento
```bash
cat 2.qsub_eje_procesamiento_mosaico.sh
```
Script Python de procesamiento de mosaico utilizando PCI-GEOMATICA. Editar la direccion del proyecto 
```bash
cat 2.scrip_procesamiento_mosaico_2018.py
pwd
nano 2.scrip_procesamiento_mosaico_2018.py
```

#### 4. Ejecución de preprocesamiento 
```bash
sh 0.scrip_mult_jobs.sh
```
#### 5. Ejecucion de procesamiento
```bash
qsub 2.qsub_eje_procesamiento_mosaico.sh
```
#### 6. Monitoreo de procesos
```bash
qstat
```

### Comandos útiles
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
Para ver la ruta actual
```bash
pwd
``` 