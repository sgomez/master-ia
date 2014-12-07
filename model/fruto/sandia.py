# -*- coding: utf-8 -*-
__author__ = 'sergio'

from model.fruto import Fruto
import rules

class Sandia(Fruto):
    def __init__(self):
        Fruto.__init__(self,nombre='sandia')

        self.add_rule(rules.ReglaIgual('r1', self.get_attribute('color'), 'verde'))
        self.add_rule(rules.ReglaRango('r2', self.get_attribute('diametro'), [100, 300]))
        self.add_rule(rules.ReglaRango('r3', self.get_attribute('peso'), [1000, 8000]))
