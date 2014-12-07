# -*- coding: utf-8 -*-
__author__ = 'sergio'

class Atributo():
    '''
    Clase Atributo. permite especificar las propiedades
    de los atributos que van a usarse en la base de conocimiento para
    describir un objeto.
    '''

    def __init__(self,nombre,tipo,unidad):
        self.nombre = nombre
        self.tipo = tipo
        self.unidad = unidad

    def __str__(self):
        return self.nombre