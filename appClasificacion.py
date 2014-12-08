#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import Caracteristica, Objeto
from PyQt4 import QtGui
import ckVtsClasificacion
import services
import sys
#from model.fruto import Fruto as mc, classes
#from model.zoo import Animal as mc, classes
from model.wine import Vino as mc, classes

services.Container().set('clases', classes)

#clase = mc('fruto')
#ob = Objeto('ob1', clase)
#ob.add_feature("color", "verde")
#ob.add_feature("diametro", 180)
#ob.add_feature("peso", 6000)

#ZOO
#clase = mc('animal')
#ob = Objeto('ob1', clase)
#ob.add_feature("pelo", False)
#ob.add_feature("plumas", False)
#ob.add_feature("huevos", True)
#ob.add_feature("leche", False)
#ob.add_feature("vuela", False)
#ob.add_feature("acuatico", True)
#ob.add_feature("dentado", True)
#ob.add_feature("columna", True)
#ob.add_feature("venenoso", False)
#ob.add_feature("aletas", True)
#ob.add_feature("patas", 0)

#WINE
clase = mc('vino')
ob = Objeto('ob1', clase)
ob.add_feature("Acided fija", 7.1)
ob.add_feature("Acided volatil", 1)
ob.add_feature("Acido citrico", 0.5)
ob.add_feature("Azucar residual", 2.4)
ob.add_feature("Cloruros", 0.12)
ob.add_feature("Dioxido de azufre libre", 21)
ob.add_feature("Dioxido de azufre total", 33)
ob.add_feature("Densidad", 1)
ob.add_feature("pH", 3.3)
ob.add_feature("Sulfatos", 0.6)
ob.add_feature("Alcohol", 9)



app = QtGui.QApplication(sys.argv)
form = ckVtsClasificacion.ClasificacionDlg(ob)
sys.exit(app.exec_())
