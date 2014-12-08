# -*- coding: utf-8 -*-
__author__ = 'jmoyano'

from model.wine import Vino
import rules

class Malo(Vino):
    def __init__(self):
        Vino.__init__(self,nombre='Malo')

        self.add_rule(rules.ReglaRango('r1', self.get_attribute('Acided fija'), [4.6, 12.5]))
        self.add_rule(rules.ReglaRango('r2', self.get_attribute('Acided volatil'), [0.23, 1.13]))
        self.add_rule(rules.ReglaRango('r3', self.get_attribute('Acido citrico'), [0, 1]))
        self.add_rule(rules.ReglaRango('r4', self.get_attribute('Azucar residual'), [1.3, 12.9]))
        self.add_rule(rules.ReglaRango('r5', self.get_attribute('Cloruros'), [0.045, 0.61]))
        self.add_rule(rules.ReglaRango('r6', self.get_attribute('Dioxido de azufre libre'), [3, 41]))
        self.add_rule(rules.ReglaRango('r7', self.get_attribute('Dioxido de azufre total'), [7, 119]))
        self.add_rule(rules.ReglaRango('r8', self.get_attribute('Densidad'), [0.9934, 1.001]))
        self.add_rule(rules.ReglaRango('r9', self.get_attribute('pH'), [2.74, 3.9]))
        self.add_rule(rules.ReglaRango('r10', self.get_attribute('Sulfatos'), [0.33, 2]))
        self.add_rule(rules.ReglaRango('r11', self.get_attribute('Alcohol'), [9, 13.1]))

