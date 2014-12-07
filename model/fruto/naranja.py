# -*- coding: utf-8 -*-
__author__ = 'sergio'

from model.fruto import Fruto
import rules

class Naranja(Fruto):
    '''
    El objeto es una naranja si su color es naranja, el peso
    debe de estar en un rango determinado y el diametro debe
    de estar en un rango determinado.

    '''
    def __init__(self):
        Fruto.__init__(self,nombre='naranja')# Se inicia con el nombre naranja

        self.add_rule(rules.ReglaIgual('r1', self.get_attribute('color'), 'naranja'))
        self.add_rule(rules.ReglaRango('r2', self.get_attribute('diametro'), [10, 30]))
        self.add_rule(rules.ReglaRango('r3', self.get_attribute('peso'), [100, 200]))