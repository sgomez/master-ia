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