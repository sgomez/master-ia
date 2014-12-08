# -*- coding: utf-8 -*-
__author__ = 'jmoyano'

from model.zoo import Animal
import rules

class Ave(Animal):
    def __init__(self):
        Animal.__init__(self,nombre='ave')

        self.add_rule(rules.ReglaIgual('r1', self.get_attribute('pelo'), False))
        self.add_rule(rules.ReglaIgual('r2', self.get_attribute('plumas'), True))
        self.add_rule(rules.ReglaIgual('r3', self.get_attribute('huevos'), True))
        self.add_rule(rules.ReglaIgual('r4', self.get_attribute('leche'), False))
        self.add_rule(rules.ReglaIgual('r5', self.get_attribute('dentado'), False))
        self.add_rule(rules.ReglaIgual('r6', self.get_attribute('columna'), True))
        self.add_rule(rules.ReglaIgual('r7', self.get_attribute('venenoso'), False))
        self.add_rule(rules.ReglaIgual('r8', self.get_attribute('aletas'), False))
        self.add_rule(rules.ReglaIgual('r9', self.get_attribute('patas'), 2))