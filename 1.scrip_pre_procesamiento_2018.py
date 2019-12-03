"""
 * -------------------------------------
 * www.iiap.org.pe | Instituto de Investigaciones de la Amazonia Peruana
 * Scrip para realizar pre procesamiento de imagenes satelitales usando PIC GEOMATICA 2018
 *
 * 1.scrip_pre_procesamiento_2018.py
 * -------------------------------------
 * Modificado por:
 * @vicercavi | Rodolfo Cardenas |
 * -------------------------------------
 """
from pci.fimport import fimport
from pci.masking import masking
from pci.hazerem import hazerem
from pci.atcor import atcor
from pci.ortho import ortho
from pci.exceptions import *
from time import time
import os

# The following locale settings are used to ensure that Python is configured
# the same way as PCI's C/C++ code.
import locale
locale.setlocale(locale.LC_ALL, "")
locale.setlocale(locale.LC_NUMERIC, "C")

def _blash():
        sistemaop = os.name
        if sistemaop=='posix':
                return '/'
        else:
                return '\\'

dir_proyect=".."
# Rutas archivos
dir_dataset=dir_proyect+_blash()+"01_dataset"
dir_import=dir_proyect+_blash()+"02_import"
dir_orto=dir_proyect+_blash()+"03_orthoimg"
dir_mask=dir_proyect+_blash()+"04.1_mask"
dir_haze=dir_proyect+_blash()+"04.2_haze"
dir_atcor=dir_proyect+_blash()+"04.3_atcor"
dir_premos=dir_proyect+_blash()+"05.1_premos"
dir_defmos=dir_proyect+_blash()+"05.2_defmos"
dir_runmos=dir_proyect+_blash()+"05.3_runmos"
dir_dem=dir_proyect+_blash()+"06_dem30mt"+_blash()+"dem_peru_utm_ok.pix"
id_imagen="000"



def _fimport(dir_imagen,name_file):

        fili=r""+dir_imagen+_blash()+name_file

        name_file=name_file.replace(".txt-MS",".PIX")
        dir_ouput=dir_import
        filo = r""+dir_ouput+_blash()+"IMPORT_"+name_file
        if not os.path.isfile(filo):
                try:
                        tiempo_inicial = time()
                        print "Fimport----> "+id_imagen
                        fimport(fili=fili,
                        filo=filo)
                        tiempo_final = time()
                        tiempo_ejecucion = tiempo_final - tiempo_inicial
                        print "Tiempo Ej.---> "+id_imagen
                        print tiempo_ejecucion
                except PCIException, e:
                    print "Error Fimport PCI----> "+id_imagen
                    print e
                except Exception, e:
                    print "Error Fimport ----> "+id_imagen
                    print e
        else:
                print "El archivo existe "+filo

        return "IMPORT_"+name_file

def _ortho(dir_imagen,name_file):

        name_file=name_file.replace(".txt-MS",".PIX")

        dir_ouput=dir_orto

        mfile = r""+dir_imagen+_blash()+"IMPORT_"+name_file
        dbic = []      # Integer #usa_metadata imagen importada
        mmseg = []      # Integer  #usa_metadata
        dbiw = []      # Integer  #usa_metadata
        srcbgd = u""
        filo = r""+dir_ouput+_blash()+"ORTO_"+name_file
        ftype = u"" #dejar vacio por defecto pix
        foptions = u"" #dejar vacio
        outbgd = []     # Float #dejar vacio
        ulx = u""  #usa_metadata
        uly = u""  #usa_metadata
        lrx = u""  #usa_metadata
        lry = u""  #usa_metadata
        edgeclip = []      # Integer -> dejar vacio por defecto 0%
        tipostrn = u"" #dejar vacio
        mapunits = u"UTM 18 C D000"  #Reproyecta a todas las imagenes a UTM 18 sona sur WGS98
        bxpxsz = u"6"  #usa_metadata dfine el ancho de salida de la imagen
        bypxsz = u"6"  #usa_metadata dfine el alto de salida de la imagen
        filedem=r""
        #filedem=r""+dir_dem
        #filedem = r"F:\SRTM_UTM\dem_peru_utm1.pix"
        dbec = []      # Integer #dejar vacio
        backelev = []     # Float #dejar vacio
        elevref = u"MSL"
        elevunit = u"METER"
        elfactor = []     # Float
        proc = u""
        sampling = [1]      # Integer # valor 1
        resample = u"NEAR"  #NEAR

        if not os.path.isfile(filo):
                try:
                        tiempo_inicial = time()
                        print "Ortho----> "+id_imagen
                        ortho(mfile, dbic, mmseg, dbiw, srcbgd, filo, ftype, foptions, outbgd, ulx, uly, lrx, lry, edgeclip, tipostrn, mapunits, bxpxsz, bypxsz, filedem, dbec, backelev, elevref, elevunit, elfactor, proc, sampling, resample)
                        tiempo_final = time()
                        tiempo_ejecucion = tiempo_final - tiempo_inicial
                        print "FINAL ----> "+id_imagen
                        print tiempo_ejecucion
                except PCIException, e:
                        print "Error Ortho PCI----> "+id_imagen
                        print e
                except Exception, e:
                        print "Error Ortho ----> "+id_imagen
                        print e
        else:
                print "El archivo existe "+filo


# Funcion para paso 1.1_mask
def _masking(dir_imagen,name_file,from_other=""):

        name_file_out=name_file.replace(".txt-MS",".PIX")

        dir_ouput=dir_mask

        if from_other=="":
                fili = r""+dir_imagen+_blash()+name_file
        else:
                name_file=name_file.replace(".txt-MS",".PIX")
                fili = r""+dir_imagen+_blash()+from_other+name_file

        srcbgd = u"" #usa_metadados
        asensor = u"" #usa_metadados -> PlatformName
        visirchn = [] #Integer #usa_metadados --> MinWavelength , MaxWavelength , y WavelengthUnits
        cfile = u""   #usa_metadados --> RadiometricTransOffset, RadiometricTransGain, RadiometricTransUnits
        znangle = [] # Float #usa_metadados SOLAR_ZENITH o AngleOfSolarElevation o (Acquisition_DateTime, NominalLocation_Latitude, NominalLocation_Longitude)
        hazecov = [25]     # Float #Se pone manualmente y se definira de acuerdo a la zona de la imagen
        clthresh = [10,20,10]     # Float #Se pone manualmente y se definira de acuerdo a la zona de la imagen
        wuthresh = []      # Integer ##Es agua no se pone nada .
        filo = r""+dir_ouput+_blash()+"MASK_"+name_file_out
        if not os.path.isfile(filo):
                try:
                        tiempo_inicial = time()
                        print "Masking----> "+id_imagen
                        masking(fili, srcbgd, asensor, visirchn, cfile, znangle, hazecov, clthresh, wuthresh, filo)
                        tiempo_final = time()
                        tiempo_ejecucion = tiempo_final - tiempo_inicial
                        print "Tiempo Ej.---> "+id_imagen
                        print tiempo_ejecucion
                except PCIException, e:
                    print "Error Masking PCI----> "+id_imagen
                    print e
                except Exception, e:
                    print "Error Masking ----> "+id_imagen
                    print e
        else:
                print "El archivo existe "+filo

# Funcion para paso 1.1_mask
def _hazerem(dir_imagen,name_file,from_other=""):

        name_file=name_file.replace(".txt-MS",".PIX")

        if from_other=="":
                fili = r""+dir_imagen+_blash()+name_file
        else:
                fili = r""+dir_imagen+_blash()+from_other+name_file

        dir_ouput=dir_haze

        fili_pan = u"" #no se pone
        srcbgd = u""  #usa_metadados
        asensor = u"" #usa_metadados -> PlatformName
        visirchn = []      # Integer
        chanopt = u""
        maskfili = r""+dir_mask+_blash()+"MASK_"+name_file
        maskseg = []      # In
        hazecov = [40]      # Integer
        hazeflsz = []      # Integer
        filo = r""+dir_ouput+_blash()+"HAZE_"+name_file
        filo_pan = u""
        ftype = u""
        foptions = u""
        if not os.path.isfile(filo):
                try:
                        tiempo_inicial = time()
                        print "Hazerem----> "+id_imagen
                        hazerem(fili, fili_pan, srcbgd, asensor, visirchn, chanopt, maskfili, maskseg, hazecov, hazeflsz, filo, filo_pan, ftype, foptions)
                        tiempo_final = time()
                        tiempo_ejecucion = tiempo_final - tiempo_inicial
                        print "Tiempo Ej.---> "+id_imagen
                        print tiempo_ejecucion
                except PCIException, e:
                    print "Error Hazerem PCI----> "+id_imagen
                    print e
                except Exception, e:
                    print "Error Hazerem ----> "+id_imagen
                    print e
        else:
                print "El archivo existe "+filo


# Funcion para paso 1.1_mask
def _atcor(dir_imagen,name_file,from_file):

        name_file=name_file.replace(".txt-MS",".PIX")

        dir_ouput=dir_atcor

        #if(dir_imagen=="04.2_haze"):
                #fili = r""+dir_haze+_blash()+"HAZE_"+name_file
        #if(dir_imagen=="03_orthoimg"):
        fili = r""+dir_imagen+_blash()+from_file+name_file


        dbic = []      # Integer
        srcbgd = u""
        asensor = u""
        cfile = u""
        #if(dir_imagen=="04.2_haze"):
        #       maskfili = r""+dir_mask+_blash()+"MASK_"+name_file
        #else:
        maskfili = u""
        #terfile = u""+dir_dem+_blash()+"dem_peru_utm.pix" #quitar
        terfile = u""
        illufile = u""
        meanelev = []     # Float #Si tiene dem no se pone nada
        vistype = "Constant, 30.0"
        visfilo = u""
        atmdef = "Rural"
        atmcond = "tropical"
        satilaz = []     # Float
        sazangl = []     # Float
        adjacen = u"ON"
        brdffun = []     # Float
        terrefl = []      # Integer
        outunits = u""
        filo = r""+dir_ouput+_blash()+"ATCOR_"+name_file
        ftype = u""
        foptions = u""

        if not os.path.isfile(filo):
                try:
                        tiempo_inicial = time()
                        print "Atcor----> "+id_imagen
                        atcor(fili, dbic, srcbgd, asensor, cfile, maskfili, terfile, illufile, meanelev, vistype, visfilo, atmdef, atmcond, satilaz, sazangl, adjacen, brdffun, terrefl, outunits, filo, ftype, foptions)
                        tiempo_final = time()
                        tiempo_ejecucion = tiempo_final - tiempo_inicial
                        print "Tiempo Ej.---> "+id_imagen
                        print tiempo_ejecucion
                except PCIException, e:
                    print "Error Atco PCI----> "+id_imagen
                    print e
                except Exception, e:
                    print "Error Atco ----> "+id_imagen
                    print e
        else:
                print "El archivo existe "+filo


# Funcion principal
if __name__ == '__main__':
        from sys import argv

        if len(argv) == 4:

                dir_imagen=argv[1]
                name_file=argv[2]
                id_imagen=argv[3]

                tiempo_total_inicial = time()
                print "===== INICIANDO PROCESAMIENTO DE DATOS ====="

                _fimport(dir_imagen,name_file)
                #_ortho(dir_import,name_file)
                dir_imagen=dir_import
                #_masking(dir_imagen,name_file,"IMPORT_")# pasa "ORTO_" o "IMPORT_" si la fuente de la imagen vienen desde la carpeta ortho
                #_hazerem(dir_imagen,name_file,"IMPORT_")
                #dir_imagen=dir_haze;
                _atcor(dir_imagen,name_file,"IMPORT_") #pasa "ORTO_" o "IMPORT_" si la fuente de la imagen vienen desde la carpeta ortho

                tiempo_total_final = time()
                tiempo_total_ejecucion = tiempo_total_final - tiempo_total_inicial

                print "===== TIEMPO TOTAL DE PROCESAMIENTO ====="
                print tiempo_total_ejecucion
        else:
                print "No se especificaron todos los parametros:"
                for x in xrange(0,len(argv)):
                        print "Argunento "+str(x)+": "+str(argv[x])




