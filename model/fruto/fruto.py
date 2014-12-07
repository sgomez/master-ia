# -*- coding: utf-8 -*-
__author__ = 'sergio'

from model import Atributo, Clase

class Fruto(Clase):
    '''
    Describe los atributos por los que se caracterizara a un fruto.
    '''
    def __init__(self, nombre):
        '''
        @param nombre: Nombre del fruto
        '''
        Clase.__init__(self, nombre)

        self.add_attribute(Atributo('color', 'str', None))
        self.add_attribute(Atributo('diametro', 'int', 'cm'))
        self.add_attribute(Atributo('peso', 'int', 'gr'))
