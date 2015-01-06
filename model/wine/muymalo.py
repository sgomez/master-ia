# -*- coding: utf-8 -*-
__author__ = 'jmoyano'

from model.wine import Vino
import rules

class MuyMalo(Vino):
    def __init__(self):
        Vino.__init__(self,nombre='Muy malo')

        self.add_rule(rules.ReglaRango('r1', self.get_attribute('Acided fija'), [6.7, 11.6]))
        self.add_rule(rules.ReglaRango('r2', self.get_attribute('Acided volatil'), [0.44, 1.58]))
        self.add_rule(rules.ReglaRango('r3', self.get_attribute('Acido citrico'), [0, 0.66]))
        self.add_rule(rules.ReglaRango('r4', self.get_attribute('Azucar residual'), [1.2, 5.7]))
        self.add_rule(rules.ReglaRango('r5', self.get_attribute('Cloruros'), [0.05, 0.66]))
        self.add_rule(rules.ReglaRango('r6', self.get_attribute('Dioxido de azufre libre'), [3, 34]))
        self.add_rule(rules.ReglaRango('r7', self.get_attribute('Dioxido de azufre total'), [9, 49]))
        self.add_rule(rules.ReglaRango('r8', self.get_attribute('Densidad'), [0.9947, 1.0008]))
        self.add_rule(rules.ReglaRango('r9', self.get_attribute('pH'), [3.16, 3.63]))
        self.add_rule(rules.ReglaRango('r10', self.get_attribute('Sulfatos'), [0.4, 0.86]))
        self.add_rule(rules.ReglaRango('r11', self.get_attribute('Alcohol'), [8.4, 11]))
