# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import classification.method as method
import services
import views


class CtrlMainWindow(QtGui.QMainWindow, views.Ui_MainWindow):

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
        self.boxBaseConocimiento.activated.connect(
            self.boxBaseConocimientoActivatedEvent)
        self.btnClasificar.clicked.connect(self.btnGenerarClickedEvent)
        self.btnSalir.clicked.connect(self.close)
        self.lstClasesCandidatas.itemClicked.connect(
            self.lstClasesCandidatasItemClickedEvent)

    def boxBaseConocimientoActivatedEvent(self, item):
        """
        Actualiza la tabla de atributos y la lista de clases candidatas cuando
        se selecciona una nueva base de datos de conocimiento
        :param item: Índice de la base de conocimiento
        """
        self.objeto = self.objetos[item]
        services.Container().set('clases', self.objeto.clases_candidatas)
        self.generarTablaAtributos()
        self.generarListaClasesCandidatas()

    def btnGenerarClickedEvent(self):
        """
        Ejecuta la clasificación y actualiza la justificación de las clases
        seleccionadas
        """
        metodo = method.Poda(self.objeto)
        clasesSeleccionadas, explicacion = metodo.execute()

        self.txtJustificacionClasificacion.clear()
        self.htmlExplication.setHtml(explicacion)
        self.txtJustificacionClasificacion.setDocument(self.htmlExplication)
        self.txtJustificacionClasificacion.moveCursor(QtGui.QTextCursor.Start)

        self.lstClasesSeleccionadas.clear()
        for clase in clasesSeleccionadas:
            self.lstClasesSeleccionadas.addItem(clase.nombre)

    def cambiaValorAtributoEvent(self, *args):
        """
        Actualiza el valor del atributo de una característica del objeto a
        clasificar
        :param args: Para QComboBox el índice seleccionado
        """
        # item: Corresponde al elemento que envió la señal
        item = self.sender()
        index = item.row

        if isinstance(item, QtGui.QLineEdit):
            print "Cambia QLineEdit"
            value = item.text()
        elif isinstance(item, QtGui.QComboBox):
            print "Cambia QComboBox"
            value = args[0]
        else:
            raise AttributeError('Tipo de Widget desconocido')
            value = None

        self.objeto.caracteristicas[index].set_valor(value)

        for caracteristica in self.objeto.caracteristicas:
            print caracteristica.atributo.nombre, caracteristica.valor

    def generarListaClasesCandidatas(self):
        """
        Para la base de conocimiento activa genera la lista de clases
        candidatas
        :return:
        """
        self.lstClasesCandidatas.clear()
        clases_candidatas = services.Container().get('clases')

        for clase in clases_candidatas:
            self.lstClasesCandidatas.addItem(clase.nombre)

        self.lstClasesCandidatas.setCurrentRow(0)

    def generarTablaAtributos(self):
        """
        Para la base de conocimiento activa genera la tabla de atributos
        :return:
        """
        self.tblObjeto.clear()
        self.tblObjeto.setRowCount(len(self.objeto.caracteristicas))
        self.tblObjeto.setHorizontalHeaderLabels(['Atributo', 'Valor'])

        for i, at in enumerate(self.objeto.caracteristicas):
            # Atributo
            celda_nombre = QtGui.QTableWidgetItem(at.atributo.nombre)
            celda_nombre.setFlags(
                QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)

            # Valor
            celda_valor = QtGui.QLineEdit()
            celda_valor.row = i

            if at.atributo.tipo == 'boleano':
                celda_valor = QtGui.QComboBox()
                celda_valor.activated.connect(self.cambiaValorAtributoEvent)
                celda_valor.addItems(['False', 'True'])
                celda_valor.row = i
                celda_valor.setCurrentIndex(1 if at.valor is True else 0)
            elif at.atributo.tipo in ['int', 'float', 'str']:
                celda_valor.setText(str(at.valor))
                celda_valor.editingFinished.connect(
                    self.cambiaValorAtributoEvent)
            else:
                raise AttributeError('Tipo de atributo desconocido')

            self.tblObjeto.setItem(i, 0, celda_nombre)
            self.tblObjeto.setCellWidget(i, 1, celda_valor)

    def lstClasesCandidatasItemClickedEvent(self):
        row = self.lstClasesCandidatas.currentRow()
        self.txtDescripcionTareas.clear()
        self.htmlDescripcionClase.setHtml(
            self.objeto.clases_candidatas[row].description())
        self.txtDescripcionTareas.setDocument(self.htmlDescripcionClase)

    def setupUi(self, MainWindow):
        views.Ui_MainWindow.setupUi(self, MainWindow)

        # Dominios de conocimiento
        for objeto in self.objetos:
            self.boxBaseConocimiento.addItem(objeto.identificador)

        # Cargas hojas de estilo
        self.htmlDescripcionClase = QtGui.QTextDocument()
        self.htmlExplication = QtGui.QTextDocument()
        css = QtCore.QFile(':/style.css')
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