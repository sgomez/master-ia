# -*- coding: utf-8 -*-
__author__ = 'sergio'

from model.fruto import Fruto
import rules

class Limon(Fruto):
    def __init__(self):
        Fruto.__init__(self,nombre='limon')

        self.add_rule(rules.ReglaIgual('r1', self.get_attribute('color'), 'amarillo'))
        self.add_rule(rules.ReglaRango('r2', self.get_attribute('diametro'), [10, 30]))
        self.add_rule(rules.ReglaRango('r3', self.get_attribute('peso'), [100, 200]))