# -*- coding: utf-8 -*-
__author__ = 'sergio'

from inferencia import Inferencia

class Equiparar(Inferencia):
    '''
    '''
    def __init__(self,candidata,nuevos_valores):
        Inferencia.__init__(self)
        self.candidata = candidata
        self.nuevos_valores = nuevos_valores
        self.explicacion=u''

    def execute(self):
        '''
        Equipara una clase candidata con el conjunto de nuevos
        valores devolviendo False si es rechazada la clase candidata.
        '''
        explicacion = ""

        print "*** Ejecución de la inferencia equiparar"
        print
        #Para cada valor comprobar que es compatible con la definición de la clase

        for nv in self.nuevos_valores:
            print "Equiparando el atributo/valor del objeto %s=%s con la clase candidata %s" \
                  % (nv.atributo.nombre, nv.valor, self.candidata.nombre)

            explicacion += "\t  Equiparar el atributo %s=%s" % (nv.atributo.nombre, nv.valor)

            for idRegla, regla in self.candidata.reglas.iteritems():
                print "Regla: %s Tipo: %s" % (regla.idRegla, regla.get_type())
                if regla.atributo.nombre == nv.atributo.nombre:
                    if regla.execute(nv):
                        continue
                    else:
                        return False, explicacion
                else:
                    print 'Regla no aplicable a este atributo\n'
        return True, explicacion
