# -*- coding: utf-8 -*-
__author__ = 'sergio'

from abc import ABCMeta, abstractmethod

class Inferencia():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    def execute(self): pass
