# -*- coding: utf-8 -*-
__author__ = 'jmoyano'

from model.zoo import Animal
import rules

class Mamifero(Animal):
    def __init__(self):
        Animal.__init__(self,nombre='mamifero')

#        self.add_rule(rules.ReglaIgual('r1', self.get_attribute('pelo'), True))
#        self.add_rule(rules.ReglaIgual('r2', self.get_attribute('plumas'), False))
#        self.add_rule(rules.ReglaIgual('r3', self.get_attribute('huevos'), False))
#        self.add_rule(rules.ReglaIgual('r4', self.get_attribute('leche'), True))
#        self.add_rule(rules.ReglaIgual('r5', self.get_attribute('vuela'), False))
#        self.add_rule(rules.ReglaIgual('r6', self.get_attribute('acuatico'), False))
#        self.add_rule(rules.ReglaIgual('r7', self.get_attribute('dentado'), True))
#        self.add_rule(rules.ReglaIgual('r8', self.get_attribute('columna'), True))
#        self.add_rule(rules.ReglaIgual('r9', self.get_attribute('venenoso'), False))
#        self.add_rule(rules.ReglaIgual('r10', self.get_attribute('aletas'), False))
#        self.add_rule(rules.ReglaIgual('r11', self.get_attribute('patas'), 2))
        
        
        self.add_rule(rules.ReglaIgual('r1', self.get_attribute('plumas'), False))
        self.add_rule(rules.ReglaIgual('r2', self.get_attribute('huevos'), False))
        self.add_rule(rules.ReglaIgual('r3', self.get_attribute('leche'), True))
        self.add_rule(rules.ReglaIgual('r4', self.get_attribute('dentado'), True))
        self.add_rule(rules.ReglaIgual('r5', self.get_attribute('columna'), True))
        self.add_rule(rules.ReglaIgual('r6', self.get_attribute('venenoso'), False))
        self.add_rule(rules.ReglaIgual('r7', self.get_attribute('patas'), 2)) #0, 2, 4
        
#        self.add_rule(rules.ReglaIgual('r1', self.get_attribute('patas'), int in [2, 4]))


#        self.add_rule(rules.ReglaRango('r2', self.get_attribute('diametro'), [10, 30]))
#        self.add_rule(rules.ReglaRango('r3', self.get_attribute('peso'), [100, 200]))