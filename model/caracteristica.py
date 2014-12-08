# -*- coding: utf-8 -*-
__author__ = 'sergio'

from model import Atributo

class Caracteristica():
    u'''Clase característica que establece el valor para un atributo'''

    def __init__(self, atributo, valor):
        if not isinstance(atributo, Atributo):
            raise AttributeError("El tipo %s no es de tipo Atributo" % atributo)

        self.atributo = atributo
        self.valor = valor

    def set_valor(self, valor):
        if self.atributo.tipo == 'int':
            self.valor = int(valor)
        elif self.atributo.tipo == 'str':
            self.valor = str(valor)
        elif self.atributo.tipo == 'bool' or self.atributo.tipo == 'boleano':
            self.valor = bool(valor)
        else:
            raise TypeError('Tipo de atributo desconocido')