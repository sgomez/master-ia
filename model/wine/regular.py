# -*- coding: utf-8 -*-
__author__ = 'jmoyano'

from model.wine import Vino
import rules

class Regular(Vino):
    def __init__(self):
        Vino.__init__(self,nombre='Regular')

        self.add_rule(rules.ReglaRango('r1', self.get_attribute('Acided fija'), [4.7, 15.9]))
        self.add_rule(rules.ReglaRango('r2', self.get_attribute('Acided volatil'), [0.16, 1.33]))
        self.add_rule(rules.ReglaRango('r3', self.get_attribute('Acido citrico'), [0, 0.79]))
        self.add_rule(rules.ReglaRango('r4', self.get_attribute('Azucar residual'), [0.9, 15.5]))
        self.add_rule(rules.ReglaRango('r5', self.get_attribute('Cloruros'), [0.034, 0.611]))
        self.add_rule(rules.ReglaRango('r6', self.get_attribute('Dioxido de azufre libre'), [1, 72]))
        self.add_rule(rules.ReglaRango('r7', self.get_attribute('Dioxido de azufre total'), [6, 165]))
        self.add_rule(rules.ReglaRango('r8', self.get_attribute('Densidad'), [0.9901, 1.0037]))
        self.add_rule(rules.ReglaRango('r9', self.get_attribute('pH'), [2.86, 4.01]))
        self.add_rule(rules.ReglaRango('r10', self.get_attribute('Sulfatos'), [0.37, 1.98]))
        self.add_rule(rules.ReglaRango('r11', self.get_attribute('Alcohol'), [8.4, 14.9]))

