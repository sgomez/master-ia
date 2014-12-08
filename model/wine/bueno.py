# -*- coding: utf-8 -*-
__author__ = 'jmoyano'

from model.wine import Vino
import rules

class Bueno(Vino):
    def __init__(self):
        Vino.__init__(self,nombre='Bueno')

        self.add_rule(rules.ReglaRango('r1', self.get_attribute('Acided fija'), [4.9, 15.6]))
        self.add_rule(rules.ReglaRango('r2', self.get_attribute('Acided volatil'), [0.12, 0.915]))
        self.add_rule(rules.ReglaRango('r3', self.get_attribute('Acido citrico'), [0, 0.76]))
        self.add_rule(rules.ReglaRango('r4', self.get_attribute('Azucar residual'), [1.2, 8.9]))
        self.add_rule(rules.ReglaRango('r5', self.get_attribute('Cloruros'), [0.012, 0.358]))
        self.add_rule(rules.ReglaRango('r6', self.get_attribute('Dioxido de azufre libre'), [3, 54]))
        self.add_rule(rules.ReglaRango('r7', self.get_attribute('Dioxido de azufre total'), [7, 289]))
        self.add_rule(rules.ReglaRango('r8', self.get_attribute('Densidad'), [0.9907, 1.0032]))
        self.add_rule(rules.ReglaRango('r9', self.get_attribute('pH'), [2.92, 3.78]))
        self.add_rule(rules.ReglaRango('r10', self.get_attribute('Sulfatos'), [0.39, 1.36]))
        self.add_rule(rules.ReglaRango('r11', self.get_attribute('Alcohol'), [9.2, 14]))

