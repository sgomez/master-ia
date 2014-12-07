# -*- coding: utf-8 -*-
__author__ = 'sergio'

from rules import Regla

class ReglaRango(Regla):
    '''
    Esta regla verifica si los valores de un atributo satisfacen
    las restricciones de la regla de la clase. P.e.
    -  La clase naranja debe de tener el atributo cuyo diametro está entre dos valores
    '''
    def __init__(self, idRegla, atributo, valorEsperado):
        Regla.__init__(self, idRegla, atributo, valorEsperado)

    def get_type(self):
        return "rango"

    def execute(self, caracteristica):
        Regla.execute(self, caracteristica)
        if self.atributo.nombre == caracteristica.atributo.nombre:
            if caracteristica.valor < self.valorEsperado[1] and caracteristica.valor >= self.valorEsperado[0]:
                return True
            else:
                return False
        else:
            return False
