# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/mainWindow.ui'
#
# Created: Wed Dec 10 10:00:31 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 800)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblDescripcionTareas = QtGui.QLabel(self.centralwidget)
        self.lblDescripcionTareas.setObjectName(_fromUtf8("lblDescripcionTareas"))
        self.gridLayout.addWidget(self.lblDescripcionTareas, 0, 2, 1, 1)
        self.boxBaseConocimiento = QtGui.QComboBox(self.centralwidget)
        self.boxBaseConocimiento.setObjectName(_fromUtf8("boxBaseConocimiento"))
        self.gridLayout.addWidget(self.boxBaseConocimiento, 1, 0, 1, 1)
        self.lblMetodo = QtGui.QLabel(self.centralwidget)
        self.lblMetodo.setObjectName(_fromUtf8("lblMetodo"))
        self.gridLayout.addWidget(self.lblMetodo, 6, 0, 1, 1)
        self.lstClasesSeleccionadas = QtGui.QListWidget(self.centralwidget)
        self.lstClasesSeleccionadas.setObjectName(_fromUtf8("lstClasesSeleccionadas"))
        self.gridLayout.addWidget(self.lstClasesSeleccionadas, 5, 0, 1, 1)
        self.lblBaseConocimiento = QtGui.QLabel(self.centralwidget)
        self.lblBaseConocimiento.setObjectName(_fromUtf8("lblBaseConocimiento"))
        self.gridLayout.addWidget(self.lblBaseConocimiento, 0, 0, 1, 1)
        self.lblClasesSeleccionadas = QtGui.QLabel(self.centralwidget)
        self.lblClasesSeleccionadas.setObjectName(_fromUtf8("lblClasesSeleccionadas"))
        self.gridLayout.addWidget(self.lblClasesSeleccionadas, 4, 0, 1, 1)
        self.lblClasesCandidatas = QtGui.QLabel(self.centralwidget)
        self.lblClasesCandidatas.setObjectName(_fromUtf8("lblClasesCandidatas"))
        self.gridLayout.addWidget(self.lblClasesCandidatas, 0, 1, 1, 1)
        self.boxMetodo = QtGui.QComboBox(self.centralwidget)
        self.boxMetodo.setObjectName(_fromUtf8("boxMetodo"))
        self.boxMetodo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.boxMetodo, 7, 0, 1, 1)
        self.lstClasesCandidatas = QtGui.QListWidget(self.centralwidget)
        self.lstClasesCandidatas.setObjectName(_fromUtf8("lstClasesCandidatas"))
        self.gridLayout.addWidget(self.lstClasesCandidatas, 1, 1, 3, 1)
        self.txtDescripcionTareas = QtGui.QTextEdit(self.centralwidget)
        self.txtDescripcionTareas.setObjectName(_fromUtf8("txtDescripcionTareas"))
        self.gridLayout.addWidget(self.txtDescripcionTareas, 1, 2, 3, 1)
        self.txtJustificacionClasificacion = QtGui.QTextEdit(self.centralwidget)
        self.txtJustificacionClasificacion.setObjectName(_fromUtf8("txtJustificacionClasificacion"))
        self.gridLayout.addWidget(self.txtJustificacionClasificacion, 5, 1, 3, 2)
        self.lblJustificacionClasificacion = QtGui.QLabel(self.centralwidget)
        self.lblJustificacionClasificacion.setObjectName(_fromUtf8("lblJustificacionClasificacion"))
        self.gridLayout.addWidget(self.lblJustificacionClasificacion, 4, 1, 1, 1)
        self.lblObjeto = QtGui.QLabel(self.centralwidget)
        self.lblObjeto.setObjectName(_fromUtf8("lblObjeto"))
        self.gridLayout.addWidget(self.lblObjeto, 2, 0, 1, 1)
        self.tblObjeto = QtGui.QTableWidget(self.centralwidget)
        self.tblObjeto.setObjectName(_fromUtf8("tblObjeto"))
        self.tblObjeto.setColumnCount(2)
        self.tblObjeto.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblObjeto.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblObjeto.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tblObjeto, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnClasificar = QtGui.QPushButton(self.centralwidget)
        self.btnClasificar.setEnabled(True)
        self.btnClasificar.setObjectName(_fromUtf8("btnClasificar"))
        self.horizontalLayout.addWidget(self.btnClasificar)
        self.btnBorrar = QtGui.QPushButton(self.centralwidget)
        self.btnBorrar.setObjectName(_fromUtf8("btnBorrar"))
        self.horizontalLayout.addWidget(self.btnBorrar)
        self.btnSalir = QtGui.QPushButton(self.centralwidget)
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        self.horizontalLayout.addWidget(self.btnSalir)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Clasificador", None))
        self.lblDescripcionTareas.setText(_translate("MainWindow", "Descripción de las tareas", None))
        self.lblMetodo.setText(_translate("MainWindow", "Método", None))
        self.lblBaseConocimiento.setText(_translate("MainWindow", "Base de conocimiento", None))
        self.lblClasesSeleccionadas.setText(_translate("MainWindow", "Clases seleccionadas", None))
        self.lblClasesCandidatas.setText(_translate("MainWindow", "Clases candidatas", None))
        self.boxMetodo.setItemText(0, _translate("MainWindow", "Poda", None))
        self.lblJustificacionClasificacion.setText(_translate("MainWindow", "Justificación de la clasificación", None))
        self.lblObjeto.setText(_translate("MainWindow", "Objeto", None))
        item = self.tblObjeto.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Atributo", None))
        item = self.tblObjeto.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Valor", None))
        self.btnClasificar.setText(_translate("MainWindow", "Clasificar", None))
        self.btnBorrar.setText(_translate("MainWindow", "Borrar", None))
        self.btnSalir.setText(_translate("MainWindow", "Salir", None))

