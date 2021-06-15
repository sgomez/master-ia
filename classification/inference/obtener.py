# -*- coding: utf-8 -*-
__author__ = 'sergio'

from .inferencia import Inferencia

class Obtener(Inferencia):
    '''
    Dado un atributo obtener un valor para ese atributo en el objeto a clasificar.
    '''
    def __init__(self, objeto, atributo):
        Inferencia.__init__(self)
        self.objeto = objeto
        self.atributo = atributo


    def execute(self):
        print("*** Ejecución de la inferencia Obtener")
        print()
        for caracteristica in self.objeto.caracteristicas:
            if self.atributo.nombre == caracteristica.atributo.nombre:
                return caracteristica
        return None

