# -*- coding: utf-8 -*-
__author__ = 'sergio'

from rules import Regla

class ReglaIgual(Regla):
    '''
    Esta regla verifica si los valores de un atributo satisfacen
    las restricciones de la regla de la clase. P.e.
    -  La clase naranja debe de tener el atributo cuyo nombre es color rojo
    '''
    def __init__(self, idRegla, atributo, valorEsperado):
        Regla.__init__(self, idRegla, atributo, valorEsperado)

    def get_type(self):
        return "igual"

    def execute(self, caracteristica):
        Regla.execute(self, caracteristica)
        if self.atributo.nombre == caracteristica.atributo.nombre:
            if self.valorEsperado == caracteristica.valor:
                return True
            else:
                return False
        else:
            return False
