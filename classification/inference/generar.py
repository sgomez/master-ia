# -*- coding: utf-8 -*-
__author__ = 'sergio'

from .inferencia import Inferencia
import services

class Generar(Inferencia):
    '''
    Dado un objeto genera un conjunto de clases candidatas
    Esta inferencia es básica se devuelven todas las clases
    candidatas que ofrece la base de conocimiento.
    '''
    def __init__(self, objeto):
        Inferencia.__init__(self)
        self.objeto = objeto


    def execute(self):
        print("*** Ejecución de la inferencia Generar")
        print()
        return services.Container().get('clases')
