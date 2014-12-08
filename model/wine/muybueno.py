# -*- coding: utf-8 -*-
__author__ = 'jmoyano'

from model.wine import Vino
import rules

class MuyBueno(Vino):
    def __init__(self):
        Vino.__init__(self,nombre='Muy bueno')

        self.add_rule(rules.ReglaRango('r1', self.get_attribute('Acided fija'), [5, 12.6]))
        self.add_rule(rules.ReglaRango('r2', self.get_attribute('Acided volatil'), [0.26, 0.85]))
        self.add_rule(rules.ReglaRango('r3', self.get_attribute('Acido citrico'), [0.03, 0.72]))
        self.add_rule(rules.ReglaRango('r4', self.get_attribute('Azucar residual'), [1.4, 6.4]))
        self.add_rule(rules.ReglaRango('r5', self.get_attribute('Cloruros'), [0.044, 0.086]))
        self.add_rule(rules.ReglaRango('r6', self.get_attribute('Dioxido de azufre libre'), [3, 42]))
        self.add_rule(rules.ReglaRango('r7', self.get_attribute('Dioxido de azufre total'), [12, 88]))
        self.add_rule(rules.ReglaRango('r8', self.get_attribute('Densidad'), [0.9908, 0.9988]))
        self.add_rule(rules.ReglaRango('r9', self.get_attribute('pH'), [2.88, 3.72]))
        self.add_rule(rules.ReglaRango('r10', self.get_attribute('Sulfatos'), [0.63, 1.1]))
        self.add_rule(rules.ReglaRango('r11', self.get_attribute('Alcohol'), [9.8, 14]))

