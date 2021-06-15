# -*- coding: utf-8 -*-
__author__ = 'sergio'

from abc import ABCMeta, abstractmethod

class Inferencia(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    def execute(self): pass
