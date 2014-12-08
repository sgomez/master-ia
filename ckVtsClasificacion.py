# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
import ckCtrlClasificacion as ctrl
import services

class ClasificacionDlg(QtGui.QWidget):
    def __init__(self, objetos):
        super(ClasificacionDlg, self).__init__()
        self.objetos = objetos
        self.objeto=objetos[0]
        services.Container().set('clases', self.objeto.clases_candidatas)

        # Selección de la base de datos de conocimiento
        lblBaseConocimiento = QtGui.QLabel("Base de conocimiento", self)

        boxBaseConocimiento = QtGui.QComboBox()
        for objeto in objetos:
            boxBaseConocimiento.addItem(objeto.identificador)

        boxBaseConocimiento.activated.connect(self.changeBaseConocimiento)

        #Label
        lblObjeto=QtGui.QLabel("Objeto",self)
        labelClasesCandidatas=QtGui.QLabel("Clases candidatas",self)
        labelTextDescripcionClases=QtGui.QLabel(u"Descripción de las clases",self)

        
        labelListClasesSeleccionadas=QtGui.QLabel("Clases seleccionadas",self)
        labelTextjustificacionR=QtGui.QLabel(u"Justificación de la clasificación",self)
        labelComboxMetodo=QtGui.QLabel(u"Método",self)
        
        #Widget
        header = ['ATRIBUTO', 'VALOR']
        #posiblesFallos = Fallos(self,   observables_list, header)
        self.tableWidgetObjeto = QtGui.QTableWidget(len(self.objeto.caracteristicas),2) #Crea la tabla de elementos observables de dps columnas
        self.tableWidgetObjeto.setColumnWidth(0, 140) #Asignan ancho a las columnas
        self.tableWidgetObjeto.setColumnWidth(1, 200) #Asignan ancho a las columnas
        self.tableWidgetObjeto.setHorizontalHeaderLabels(header) #Asigna etiquetas a las columnas
        self.generaTablaAtributos()
        
        #List
        self.listWidgetClasesCandidatas = QtGui.QListWidget()
        self.generaListaClasesCandidatas()

        self.plainTextEditDescripcionClases = QtGui.QPlainTextEdit()#Cuadro de texto de descripcion de la clase
        self.listWidgetClasesSeleccionadas = QtGui.QListWidget()
        self.plainTextEditExplicacion = QtGui.QPlainTextEdit()#Cuadro de texto    de la explicación
        
        #Método
        self.comboboxWidgetMetodo = QtGui.QComboBox()
        self.comboboxWidgetMetodo.addItem('Poda')
        self.comboboxWidgetMetodo.addItem('Semi Poda') 
        
        #Botones
        self.clasificarButtom=QtGui.QPushButton('Clasificar')
        self.borrarButtom=QtGui.QPushButton('Borrar')
        self.salirButtom=QtGui.QPushButton('Salir') 
        self.buttomsLayout = QtGui.QHBoxLayout()
        self.buttomsLayout.addStretch()
        self.buttomsLayout.addWidget(self.clasificarButtom)
        self.buttomsLayout.addWidget(self.borrarButtom)
        self.buttomsLayout.addWidget(self.salirButtom)
        self.buttomsLayout.addStretch()
        
        #Rejilla de distribución de los controles
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(lblBaseConocimiento, 0, 0)
        grid.addWidget(boxBaseConocimiento, 1, 0)
        grid.addWidget(lblObjeto, 2, 0)
        grid.addWidget(self.tableWidgetObjeto, 3, 0)
        grid.addWidget(labelListClasesSeleccionadas, 4, 0)
        grid.addWidget(self.listWidgetClasesSeleccionadas, 5, 0)
        grid.addWidget(labelComboxMetodo, 6, 0)
        grid.addWidget(self.comboboxWidgetMetodo, 7, 0)

        grid.addWidget(labelClasesCandidatas, 0, 1)
        grid.addWidget(labelTextDescripcionClases, 0, 2)
        grid.addWidget(self.listWidgetClasesCandidatas, 1, 1, 3, 1)
        grid.addWidget(self.plainTextEditDescripcionClases, 1, 2, 3, 1)
        grid.addWidget(labelTextjustificacionR, 4, 1)
        grid.addWidget(self.plainTextEditExplicacion, 5, 1, 3, 2)


        #Diseño principal
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttomsLayout)
        self.setLayout(mainLayout)
        
    
        self.setGeometry(300, 300, 1200, 800)
        self.setWindowTitle(u"TAREA DE CLASIFICACION")
        self.show()
 
        self.center()
        #Conexiones:
        #==========
        self.listWidgetClasesCandidatas.itemClicked.connect(self.showCc)
        #self.generarButtom.clicked.connect(self.generar)
        self.clasificarButtom.clicked.connect(self.clasificar)
        self.salirButtom.clicked.connect(self.close)


    def generar(self):
        print 'generar'
        ckCtrlClasificacion.eventGenerar(self)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showCc(self):
        row = self.listWidgetClasesCandidatas.currentRow()
        #print row
        #print self.cc[row].nombre
        #print self.cc[row].descripcion()
        self.plainTextEditDescripcionClases.clear()
        self.plainTextEditDescripcionClases.appendPlainText(self.objeto.clases_candidatas[row].description())
        pass

    def change_table_cell(self, *args):
        item = self.sender()
        index = item.row
        value = None

        if isinstance(item, QtGui.QLineEdit):
            print "Cambia QLineEdit"
            value = item.text()
        elif isinstance(item, QtGui.QComboBox):
            print "Cambia QComboBox"
            value = args[0]
        else:
            raise AttributeError('Tipo de Widget desconocido')

        self.objeto.caracteristicas[index].set_valor(value)

        for at in self.objeto.caracteristicas:
            print at.atributo.nombre, at.valor

    def changeBaseConocimiento(self, item):
        self.objeto = self.objetos[item]
        services.Container().set('clases', self.objeto.clases_candidatas)
        self.generaTablaAtributos()
        self.generaListaClasesCandidatas()

    def generaListaClasesCandidatas(self):
        self.listWidgetClasesCandidatas.clear()
        clases_candidatas=services.Container().get('clases')
        for clase in clases_candidatas:
            self.listWidgetClasesCandidatas.addItem(clase.nombre)

        self.listWidgetClasesCandidatas.setCurrentRow(0)


    def generaTablaAtributos(self):
        self.tableWidgetObjeto.clear()
        self.tableWidgetObjeto.setRowCount(len(self.objeto.caracteristicas))

        #print observables
        for i, at in enumerate(self.objeto.caracteristicas):
            print "Característica: Atributo=%s Valor=%s" % (at.atributo.nombre, at.valor)
            print  at.atributo.nombre,at.atributo.tipo, at.valor,type(at.valor),at.atributo.unidad#,

            # Atributo
            celda_nombre = QtGui.QTableWidgetItem(at.atributo.nombre)
            celda_nombre.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            self.tableWidgetObjeto.setItem(i, 0, celda_nombre)

            # Valor
            celda_valor = QtGui.QLineEdit()
            celda_valor.row = i

            if at.atributo.tipo == 'boleano':
                celda_valor = QtGui.QComboBox()
                celda_valor.row = i
                celda_valor.addItem('False')
                celda_valor.addItem('True')
                celda_valor.activated.connect(self.change_table_cell)
                if at.valor == True:
                    celda_valor.setCurrentIndex(1)
            elif at.atributo.tipo in ['int', 'float', 'str']:
                celda_valor.setText(str(at.valor))
                celda_valor.editingFinished.connect(self.change_table_cell)
            else:
                raise AttributeError('Tupo de atributo desconocido')

            self.tableWidgetObjeto.setCellWidget(i, 1, celda_valor)

    def clasificar(self):
        print 'clasificar'
        ctrl.eventClasificar(self)
