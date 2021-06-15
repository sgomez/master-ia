# -*- coding: utf-8 -*-
__author__ = 'sergio'

from model import Caracteristica

class Objeto():
    def __init__(self, id, clase, clases_candidatas):
        '''Se inicia la clase especificando el nombre y los atributos del objeto'''

        self.caracteristicas = []
        self.clase = clase
        self.identificador = id
        self.clases_candidatas = clases_candidatas

    def describeObjeto(self):
        print(("Identificador: %s\n" % self.identificador))
        for item in self.caracteristicas:
            print(("- Atributo: %s\tTipo: %s\tValor: %s\tUnidad: %s\n" \
                  % (item.atributo.nombre, item.atributo.tipo, item.valor, item.atributo.unidad)))


    def add_feature(self, nombre, valor):
        self.caracteristicas.append(Caracteristica(self.clase.get_attribute(nombre), valor))