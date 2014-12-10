#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller import CtrlMainWindow
from model import Objeto
from model.fruto import Fruto, classes as cfruto
from model.wine import Vino, classes as cvino
from model.zoo import Animal, classes as canimal
from PyQt4 import QtGui
import resources
import sys


fruto = Fruto('fruto')
ob1 = Objeto('Fruto', fruto, cfruto)
ob1.add_feature("color", "verde")
ob1.add_feature("diametro", 180)
ob1.add_feature("peso", 6000)

#ZOO
animal = Animal('animal')
ob2 = Objeto('Animal', animal, canimal)
ob2.add_feature("pelo", True)
ob2.add_feature("plumas", False)
ob2.add_feature("huevos", False)
ob2.add_feature("leche", True)
ob2.add_feature("vuela", False)
ob2.add_feature("acuatico", False)
ob2.add_feature("dentado", True)
ob2.add_feature("columna", True)
ob2.add_feature("venenoso", False)
ob2.add_feature("aletas", False)
ob2.add_feature("patas", 2)

#WINE
vino = Vino('vino')
ob3 = Objeto('Vino', vino, cvino)
ob3.add_feature("Acided fija", 7.1)
ob3.add_feature("Acided volatil", 0.13)
ob3.add_feature("Acido citrico", 0.5)
ob3.add_feature("Azucar residual", 7.4)
ob3.add_feature("Cloruros", 0.12)
ob3.add_feature("Dioxido de azufre libre", 21)
ob3.add_feature("Dioxido de azufre total", 103)
ob3.add_feature("Densidad", 1.001)
ob3.add_feature("pH", 3.3)
ob3.add_feature("Sulfatos", 0.6)
ob3.add_feature("Alcohol", 11.1)

app = QtGui.QApplication(sys.argv)
form = CtrlMainWindow([ob1, ob2, ob3])
sys.exit(app.exec_())
