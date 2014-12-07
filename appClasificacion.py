#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import Caracteristica, Objeto
from PyQt4 import QtGui
import ckVtsClasificacion
import services
import sys
from model.fruto import Fruto as mc, classes

services.Container().set('clases', classes)

clase = mc('fruto')
ob = Objeto('ob1', clase)
ob.add_feature("color", "verde")
ob.add_feature("diametro", 180)
ob.add_feature("peso", 6000)

app = QtGui.QApplication(sys.argv)
form = ckVtsClasificacion.ClasificacionDlg(ob)
sys.exit(app.exec_())
