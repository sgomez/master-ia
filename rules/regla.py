# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from model import Caracteristica

class Regla():
    '''
    Describe aspectos generales de una regla
    '''
    __metaclass__ = ABCMeta

    idRegla = None
    atributo = None
    valorEsperado = None
    tipo = None

    def __init__(self, idRegla, atributo, valorEsperado):
        self.idRegla = idRegla
        self.atributo = atributo
        self.valorEsperado = valorEsperado

    @abstractmethod
    def get_type(self):
        raise NotImplemented()

    @abstractmethod
    def execute(self, caracteristica):
        if not isinstance(caracteristica, Caracteristica):
            raise AttributeError("El tipo de dato %s no es de tipo Caracteristica" % caracteristica)