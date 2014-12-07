# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import classification.method as method

def eventGenerar(clasificacionDlg):
    '''
    '''
    print 'ctrl', 'event generar'
        
def eventClasificar(clasificacionDlg):
    print 'Objeto:', clasificacionDlg.objeto.identificador
    print '================================\n'
    mp = method.Poda(clasificacionDlg.objeto) #Se crea la instancia del método de la poda
    r, exp = mp.execute() #se ejecuta el método
    clasificacionDlg.plainTextEditExplicacion.clear() #Se borra la explicación
    clasificacionDlg.plainTextEditExplicacion.appendPlainText(exp)# Se presenta la nueva explicación
    clasificacionDlg.plainTextEditExplicacion.moveCursor(QtGui.QTextCursor.Start)
    cs=[]
    for cc in r:
        print '\t ->',cc.nombre
        cs.append(cc.nombre)
    clasificacionDlg.listWidgetClasesSeleccionadas.clear()
    clasificacionDlg.listWidgetClasesSeleccionadas.addItems(cs) #Se añaden las clases resultado de la clasificación 
                                                                # al control listbox para que lo presente.
    return
        


