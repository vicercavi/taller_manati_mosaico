#http://www.pcigeomatics.com/geomatica-help/references/pciFunction_r/python/P_fexport.html
from pci.fexport import fexport
from pci.exceptions import *
from time import time

# The following locale settings are used to ensure that Python is configured
# the same way as PCI's C/C++ code.
import locale
locale.setlocale(locale.LC_ALL, "")
locale.setlocale(locale.LC_NUMERIC, "C")

fili = r"05.3_runmos/DEFMOS_MOSAICO_LANDSAT8_v2_1_1.pix"
filo = r"08_export/DEFMOS_MOSAICO_LANDSAT8_v2_1_1.tif"
dbiw = []      # Integer
dbic = [1,2,3,4]      # Integer
dbib = []      # Integer
dbvs = []      # Integer
dblut = []      # Integer
dbpct = []      # Integer
ftype = u"tif"
foptions = u""

try:
    tiempo_inicial = time()
    print "INICIO---->"
    fexport(fili, filo, dbiw, dbic, dbib, dbvs, dblut, dbpct, ftype, foptions)
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print "FINAL---->"
    print tiempo_ejecucion
except PCIException, e:
    print e
except Exception, e:
    print e