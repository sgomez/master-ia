# -*- coding: utf-8 -*-
__author__ = 'jmoyano'

from model import Atributo, Clase

class Animal(Clase):
    '''
    Describe los atributos por los que se caracterizara a una especie animal.
    '''
    def __init__(self, nombre):
        '''
        @param nombre: Nombre de la especie animal
        '''
        Clase.__init__(self, nombre)

        self.add_attribute(Atributo('pelo', 'boleano', None))
        self.add_attribute(Atributo('plumas', 'boleano', None))
        self.add_attribute(Atributo('huevos', 'boleano', None))
        self.add_attribute(Atributo('leche', 'boleano', None))
        self.add_attribute(Atributo('vuela', 'boleano', None))
        self.add_attribute(Atributo('acuatico', 'boleano', None))
        self.add_attribute(Atributo('dentado', 'boleano', None))
        self.add_attribute(Atributo('columna', 'boleano', None))
        self.add_attribute(Atributo('venenoso', 'boleano', None))
        self.add_attribute(Atributo('aletas', 'boleano', None))
        self.add_attribute(Atributo('patas', 'int', None))
