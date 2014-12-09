# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import appResources
import classification.method as method
import services
import views

class ctrlClasificacion(QtGui.QMainWindow, views.Ui_MainWindow):

    def __init__(self, objetos):
        QtGui.QMainWindow.__init__(self)

        self.objetos = objetos
        self.objeto = objetos[0]
        services.Container().set('clases', self.objeto.clases_candidatas)

        # Configura UI
        self.setupUi(self)
        self.generarListaClasesCandidatas()
        self.generarTablaAtributos()
        self.show()

        # Señales
        self.boxBaseConocimiento.activated.connect(self.boxBaseConocimientoActivatedEvent)
        self.btnClasificar.clicked.connect(self.btnGenerarClickedEvent)
        self.btnSalir.clicked.connect(self.close)
        self.lstClasesCandidatas.itemClicked.connect(self.lstClasesCandidatasItemClickedEvent)


    def boxBaseConocimientoActivatedEvent(self, item):
        self.objeto = self.objetos[item]
        services.Container().set('clases', self.objeto.clases_candidatas)
        self.generarTablaAtributos()
        self.generarListaClasesCandidatas()


    def btnGenerarClickedEvent(self):
        print 'Objeto:', self.objeto.identificador
        print '================================\n'
        metodo = method.Poda(self.objeto)
        clasesCandidatas, explicacion = metodo.execute()

        self.txtJustificacionClasificacion.clear()
        self.htmlExplication.setHtml(explicacion)
        self.txtJustificacionClasificacion.setDocument(self.htmlExplication)
        self.txtJustificacionClasificacion.moveCursor(QtGui.QTextCursor.Start)

        clasesSeleccionadas=[]
        for clase in clasesCandidatas:
            print '\t ->', clase.nombre
            clasesSeleccionadas.append(clase.nombre)

        self.lstClasesSeleccionadas.clear()
        self.lstClasesSeleccionadas.addItems(clasesSeleccionadas)


    def cambiaValorAtributoEvent(self, *args):
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


    def generarListaClasesCandidatas(self):
        self.lstClasesCandidatas.clear()
        clases_candidatas=services.Container().get('clases')
        for clase in clases_candidatas:
            self.lstClasesCandidatas.addItem(clase.nombre)

        self.lstClasesCandidatas.setCurrentRow(0)


    def generarTablaAtributos(self):
        self.tblObjeto.clear()
        self.tblObjeto.setRowCount(len(self.objeto.caracteristicas))
        self.tblObjeto.setHorizontalHeaderLabels(['Atributo', 'Valor'])

        #print observables
        for i, at in enumerate(self.objeto.caracteristicas):
            print "Característica: Atributo=%s Valor=%s" % (at.atributo.nombre, at.valor)
            print  at.atributo.nombre,at.atributo.tipo, at.valor,type(at.valor),at.atributo.unidad#,

            # Atributo
            celda_nombre = QtGui.QTableWidgetItem(at.atributo.nombre)
            celda_nombre.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            self.tblObjeto.setItem(i, 0, celda_nombre)

            # Valor
            celda_valor = QtGui.QLineEdit()
            celda_valor.row = i

            if at.atributo.tipo == 'boleano':
                celda_valor = QtGui.QComboBox()
                celda_valor.row = i
                celda_valor.addItem('False')
                celda_valor.addItem('True')
                celda_valor.activated.connect(self.cambiaValorAtributoEvent)
                if at.valor == True:
                    celda_valor.setCurrentIndex(1)
            elif at.atributo.tipo in ['int', 'float', 'str']:
                celda_valor.setText(str(at.valor))
                celda_valor.editingFinished.connect(self.cambiaValorAtributoEvent)
            else:
                raise AttributeError('Tupo de atributo desconocido')

            self.tblObjeto.setCellWidget(i, 1, celda_valor)


    def lstClasesCandidatasItemClickedEvent(self):
        row = self.lstClasesCandidatas.currentRow()
        self.txtDescripcionTareas.clear()
        self.htmlDescripcionClase.setHtml(self.objeto.clases_candidatas[row].description())
        self.txtDescripcionTareas.setDocument(self.htmlDescripcionClase)


    def setupUi(self, MainWindow):
        views.Ui_MainWindow.setupUi(self, MainWindow)

        # Dominios de conocimiento
        for objeto in self.objetos:
            self.boxBaseConocimiento.addItem(objeto.identificador)

        # Cargas hojas de estilo
        self.htmlDescripcionClase = QtGui.QTextDocument()
        self.htmlExplication = QtGui.QTextDocument()
        css = QtCore.QFile(':/resources/css/style.css')
        css.open(QtCore.QIODevice.ReadOnly)
        if css.isOpen():
            style = QtCore.QVariant(css.readAll()).toString()
            self.htmlExplication.setDefaultStyleSheet(style)
            self.htmlDescripcionClase.setDefaultStyleSheet(style)
        else:
            raise IOError("Fichero no encontrado")
        css.close()

        # Ancho de las columnas
        self.tblObjeto.setColumnWidth(0, 150)
        self.tblObjeto.setColumnWidth(1, 200)