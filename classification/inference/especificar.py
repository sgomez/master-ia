# -*- coding: utf-8 -*-
__author__ = 'sergio'

from inferencia import Inferencia

class Especificar(Inferencia):
    '''Dado un conjunto de clases candidatas no vacío
       especifica un atributo para extraer su valor en otra inferencia.
    '''
    def __init__(self, clases_candidatas, atributos_usados):
        '''
        @param clases_candidatas: Lista de clases candidatas
        @param atributos_usados: Lista de atributos ya seleccionados
        '''
        Inferencia.__init__(self)
        self.clases_candidatas = clases_candidatas
        self.atributos_usados = atributos_usados


    def execute(self):
        '''
        Ejecución del método de la inferencia
        @return: Devuelve en una tupla el atributo especificado y la lista de atributos ya usados.
        '''
        print "*** Ejecución de la inferencia Especificar"
        print
        if len(self.clases_candidatas) > 0:
            clase = self.clases_candidatas[0]
            for nombre, atributo in clase.atributos.iteritems():
                if not nombre in [item.nombre for item in self.atributos_usados]:
                    self.atributos_usados.append(atributo)
                    return (atributo, self.atributos_usados)

            return None,None

