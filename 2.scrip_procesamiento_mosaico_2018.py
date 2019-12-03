"""
 * -------------------------------------
 * www.iiap.org.pe | Instituto de investagaciones de la Amazonia Peruana
 * Scrip para generar mosaico con imagenes ortorectificadas, haciendo correccion Atmosferica
 *
 * scrip_procesamiento_mosaico_2015.py
 * -------------------------------------
 * Modificado por:
 * @vicercavi | Rodolfo Cardenas |
 * -------------------------------------
 """
from pci.mosprep import mosprep
from pci.mosdef import mosdef
from pci.mosrun import mosrun
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

dir_proyect="..."
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

def _mosprep(dir_imagen,dir_ouput,name_file):

        out_name_file="PREMOS_MOSAICO_LANDSAT8_v2.xml"
        dir_ouput=dir_premos

        mfile = r""+dir_imagen
        silfile = r""+dir_ouput+_blash()+out_name_file
        nodatval = [0]     # Float
        sortmthd = u""
        normaliz = u"ADAPTIVE"
        balspec = u"BUNDLE"
        loclmask = u""
        globfile = u""
        globmask = []      # Integer
        cutmthd = u"MINSQDIFF"

        try:
                tiempo_inicial = time()
                print "Mosprep---->"
                mosprep(mfile, silfile, nodatval, sortmthd, normaliz, balspec, loclmask, globfile, globmask, cutmthd)
                tiempo_final = time()
                tiempo_ejecucion = tiempo_final - tiempo_inicial
                print "Tiempo Ej.--->"
                print tiempo_ejecucion
        except PCIException, e:
                print "Error Mosprep PCI----> "
                print e
        except Exception, e:
                print "Error Mosprep ----> "
                print e

        return out_name_file

def _mosdef(dir_imagen,dir_ouput,name_file):

        out_name_file="DEFMOS_MOSAICO_LANDSAT8_v2.xml"
        dir_ouput=dir_defmos

        silfile = r""+dir_imagen+_blash()+name_file
        mdfile =r""+dir_ouput+_blash()+out_name_file
        dbic = []      # Integer
        tispec = u"" #En espera para poner ruta de archivo de grilla
        tipostrn = u""  #vacio
        mapunits = u"LONG/LAT D000"  #vacio por ahora E012 #UTM 18 C D000
        pxszout = []     # Float
        blend = [6]      # Integer #Output pixel size, same for x and y
        nodatval = []     # Float
        ftype = u"PIX"
        foptions = u""

        try:
                tiempo_inicial = time()
                print "Mosdef---->"
                mosdef(silfile, mdfile, dbic, tispec, tipostrn, mapunits, pxszout, blend, nodatval, ftype, foptions)
                tiempo_final = time()
                tiempo_ejecucion = tiempo_final - tiempo_inicial
                print "Tiempo Ej.--->"
                print tiempo_ejecucion
        except PCIException, e:
                print "Error Mosprep PCI----> "
                print e
        except Exception, e:
                print "Error Mosprep ----> "
                print e

        return out_name_file

def _mosrun(dir_img_premos,dir_img_defmos):

        out_name_file="MOSAICO_LANDSAT8_v2"
        dir_ouput=dir_runmos

        silfile = r""+dir_img_premos
        mdfile = r""+dir_img_defmos
        outdir = r""+dir_ouput
        tilist = u""
        crsrcmap = u""
        extirule = u""
        delempti = u""
        proc = u""
        resample = u""

        try:
                tiempo_inicial = time()
                print "Mosrun---->"
                mosrun(silfile, mdfile, outdir, tilist, crsrcmap, extirule, delempti, proc, resample)
                tiempo_final = time()
                tiempo_ejecucion = tiempo_final - tiempo_inicial
                print "Tiempo Ej.--->"
                print tiempo_ejecucion
        except PCIException, e:
                print "Error Mosrun PCI----> "
                print e
        except Exception, e:
                print "Error Mosrun ----> "
                print e

if __name__ == '__main__':
        from sys import argv

        if len(argv) == 2:

                dir_img_proce=""

                if str(argv[1])=="atcor":
                        dir_img_proce=dir_atcor
                if str(argv[1])=="ortho":
                        dir_img_proce=dir_orto
                if str(argv[1])=="import":
                        dir_img_proce=dir_import



                tiempo_total_inicial = time()
                print "===== INICIANDO PROCESAMIENTO DE DATOS ====="

                dir_ouput=""
                img_mosprep= _mosprep(dir_img_proce,dir_ouput,"")
                #img_mosprep="PREMOS_MOSAICO_RAPIDEYE_v2.xml"
                img_mosdef=_mosdef(dir_premos,dir_ouput,img_mosprep)
                ##img_mosdef="DEFMOS_MOSAICO_RAPIDEYE_v2.xml"
                _mosrun(dir_premos+_blash()+img_mosprep,dir_defmos+_blash()+img_mosdef)

                tiempo_total_final = time()
                tiempo_total_ejecucion = tiempo_total_final - tiempo_total_inicial

                print "===== TIEMPO TOTAL DE PROCESAMIENTO ====="
                print tiempo_total_ejecucion

        else:
                print "No se especificaron todos los parametros:"
                for x in xrange(0,len(argv)):
                        print "Argunento "+str(x)+": "+str(argv[x])
