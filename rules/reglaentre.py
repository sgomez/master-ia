# -*- coding: utf-8 -*-
from rules import Regla

class ReglaEntre(Regla):
    '''
    Esta regla verifica si los valores de un atributo satisfacen
    las restricciones de la regla de la clase. P.e.
    -  La clase naranja debe de tener el atributo cuyo nombre es color rojo
    '''
    def __init__(self, idRegla, atributo, valorEsperado):
        Regla.__init__(self, idRegla, atributo, valorEsperado)

        if not isinstance(valorEsperado, list):
            raise AttributeError("ReglaEntre requiere una lista como valor esperado")

    def get_type(self):
        return "entre"

    def execute(self, caracteristica):
        Regla.execute(self, caracteristica)
        if self.atributo.nombre == caracteristica.atributo.nombre:
            if caracteristica.valor in self.valorEsperado:
                return True
            else:
                return False
        else:
            return False
