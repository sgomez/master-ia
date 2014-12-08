#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import Objeto
from PyQt4 import QtGui
import ckVtsClasificacion
import services
import sys
from model.fruto import Fruto , classes as cfruto
from model.zoo import Animal , classes as canimal
from model.wine import Vino, classes as cvino

fruto = Fruto('fruto')
ob1 = Objeto('Fruto', fruto, cfruto)
ob1.add_feature("color", "verde")
ob1.add_feature("diametro", 180)
ob1.add_feature("peso", 6000)

#ZOO
animal = Animal('animal')
ob2 = Objeto('Animal', animal, canimal)
ob2.add_feature("pelo", False)
ob2.add_feature("plumas", False)
ob2.add_feature("huevos", True)
ob2.add_feature("leche", False)
ob2.add_feature("vuela", False)
ob2.add_feature("acuatico", True)
ob2.add_feature("dentado", True)
ob2.add_feature("columna", True)
ob2.add_feature("venenoso", False)
ob2.add_feature("aletas", True)
ob2.add_feature("patas", 0)

#WINE
vino = Vino('vino')
ob3 = Objeto('Vino', vino, cvino)
ob3.add_feature("Acided fija", 7.1)
ob3.add_feature("Acided volatil", 1)
ob3.add_feature("Acido citrico", 0.5)
ob3.add_feature("Azucar residual", 2.4)
ob3.add_feature("Cloruros", 0.12)
ob3.add_feature("Dioxido de azufre libre", 21)
ob3.add_feature("Dioxido de azufre total", 33)
ob3.add_feature("Densidad", 1)
ob3.add_feature("pH", 3.3)
ob3.add_feature("Sulfatos", 0.6)
ob3.add_feature("Alcohol", 9)

app = QtGui.QApplication(sys.argv)
form = ckVtsClasificacion.ClasificacionDlg([ob1, ob2, ob3])
sys.exit(app.exec_())
