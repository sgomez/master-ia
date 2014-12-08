# -*- coding: utf-8 -*-
__author__ = 'jmoyano'

from model import Atributo, Clase

class Vino(Clase):
    '''
    Describe los atributos por los que se caracterizara un vino
    '''
    def __init__(self, nombre):
        '''
        @param nombre: Calidad del vino
        '''
        Clase.__init__(self, nombre)

#        self.add_attribute(Atributo('Acided fija', 'float', 'g/dm3'))
#        self.add_attribute(Atributo('Acided volatil', 'float', 'g/dm3'))
#        self.add_attribute(Atributo('Acido citrico', 'float', 'g/dm3'))
#        self.add_attribute(Atributo('Azucar residual', 'float', 'g/dm3'))
#        self.add_attribute(Atributo('Cloruros', 'float', 'g/dm3'))
#        self.add_attribute(Atributo('Dioxido de azufre libre', 'int', 'mg/dm3'))
#        self.add_attribute(Atributo('Dioxido de azufre total', 'int', 'mg/dm3'))
#        self.add_attribute(Atributo('Densidad', 'float', 'g/cm3'))
#        self.add_attribute(Atributo('pH', 'float', None))
#        self.add_attribute(Atributo('Sulfatos', 'float', 'g/dm3'))
#        self.add_attribute(Atributo('Alcohol', 'float', '% vol'))

        self.add_attribute(Atributo('Acided fija', 'int', 'g/dm3'))
        self.add_attribute(Atributo('Acided volatil', 'int', 'g/dm3'))
        self.add_attribute(Atributo('Acido citrico', 'int', 'g/dm3'))
        self.add_attribute(Atributo('Azucar residual', 'int', 'g/dm3'))
        self.add_attribute(Atributo('Cloruros', 'int', 'g/dm3'))
        self.add_attribute(Atributo('Dioxido de azufre libre', 'int', 'mg/dm3'))
        self.add_attribute(Atributo('Dioxido de azufre total', 'int', 'mg/dm3'))
        self.add_attribute(Atributo('Densidad', 'int', 'g/cm3'))
        self.add_attribute(Atributo('pH', 'int', None))
        self.add_attribute(Atributo('Sulfatos', 'int', 'g/dm3'))
        self.add_attribute(Atributo('Alcohol', 'int', '% vol'))