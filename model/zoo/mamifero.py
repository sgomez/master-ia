# -*- coding: utf-8 -*-
__author__ = 'jmoyano'

from model.zoo import Animal
import rules

class Mamifero(Animal):
    def __init__(self):
        Animal.__init__(self,nombre='mamifero')
        
        self.add_rule(rules.ReglaIgual('r1', self.get_attribute('plumas'), False))
        self.add_rule(rules.ReglaIgual('r2', self.get_attribute('huevos'), False))
        self.add_rule(rules.ReglaIgual('r3', self.get_attribute('leche'), True))
        self.add_rule(rules.ReglaIgual('r4', self.get_attribute('dentado'), True))
        self.add_rule(rules.ReglaIgual('r5', self.get_attribute('columna'), True))
        self.add_rule(rules.ReglaIgual('r6', self.get_attribute('venenoso'), False))
        self.add_rule(rules.ReglaEntre('r7', self.get_attribute('patas'), [0, 2, 4])) #0, 2, 4
