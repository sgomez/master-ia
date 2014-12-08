# -*- coding: utf-8 -*-
__author__ = 'sergio'

from model import Atributo
from rules import Regla

class Clase():
    u'''
    Clase en la jerarquía más alta.
    '''

    def __init__(self, nombre):
        u'''
        @param: Nombre de la clase.
        '''
        self.atributos = {}
        self.nombre = nombre #La clase tiene un nombre
        self.reglas = []

    def add_attribute(self, atributo):
        if not isinstance(atributo, Atributo):
            raise TypeError()

        self.atributos[atributo.nombre] = atributo


    def get_attribute(self, nombre):
        return self.atributos[nombre]


    def add_rule(self, regla):
        if not isinstance(regla, Regla):
            raise TypeError()

        self.reglas.append(regla)


    def get_rule(self, idRegla):
        return self.reglas[idRegla]


    def description(self):
        u'''
        Devuelve el texto de la descripción de una clase.
        '''

        msg = "Clase: %s\n" % (self.nombre)

        for r in self.reglas:
            msg += "- Regla: %s\tTipo: %s\tAtributo: %s\tValor esperado: %s\n" \
                   % (r.idRegla, r.get_type(), r.atributo.nombre, r.valorEsperado)

        return msg