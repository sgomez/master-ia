# -*- coding: utf-8 -*-
__author__ = 'sergio'

import classification.inference as inference

class Poda():
    '''
    Dado un objeto clasificarlo como perteneciente a una clase
    '''

    def __init__(self,obj):
        self.obj=obj


    def execute(self):
        # Se generan las posibles clases candidatas
        generar = inference.Generar(self.obj)
        clases_candidatas = generar.execute()
        atributos_usados = []
        nuevos_valores = []
        msg = u"Se generan las clases candidatas que son: %s\n" % ([clase.nombre for clase in clases_candidatas])

        found = False

        while not found and len(clases_candidatas) > 0:
            print "inicio while-> Lista de atributos usados: %s\n" % ([item.nombre for item in atributos_usados])
            print " Clases candidatas: %s\n" % ([clase.nombre for clase in clases_candidatas])

            especificar = inference.Especificar(clases_candidatas, atributos_usados)
            nuevo_atributo = especificar.execute()

            if not nuevo_atributo == (None, None):
                atributos_usados = nuevo_atributo[1]
                print " Nuevo atributo seleccionado: %s\n" % (nuevo_atributo[0].nombre)
                print " Atributos usados: %s\n" % ([item.nombre for item in atributos_usados])
                msg += "Seleccionamos el atributo %s " % nuevo_atributo[0].nombre

                obtener = inference.Obtener(self.obj, nuevo_atributo[0])
                caracteristica = obtener.execute()
                print " Atributo y valor del objeto: %s= %s" % (caracteristica.atributo.nombre, caracteristica.valor)
                msg += "con el valor: %s\n" % (caracteristica.valor)

                nuevos_valores.append(caracteristica)

                nuevas_candidatas = []
                for clase in clases_candidatas:
                    print "Probamos a equipara la clase %s con el conjunto de nuevos pares atributos/valores %s" \
                        % (clase.nombre, [item.atributo.nombre for item in nuevos_valores])
                    msg += "\t- Probamos la clase candidata %s\n" % clase.nombre

                    equiparar = inference.Equiparar(clase, nuevos_valores)
                    resultado, explicacion = equiparar.execute()
                    msg += explicacion
                    msg += "\t  Resultado de equiparar la clase %s: %s\n" % (clase.nombre, resultado)

                    if resultado == True:
                        nuevas_candidatas.append(clase)
                        print "Clase aceptada: %s" % clase.nombre
            else:
                print "No quedan más atributos por especificar"
                found = True
                continue

            clases_candidatas = nuevas_candidatas
            msg += u"Clases candidatas tras la equiparación:\n"
            for clase in clases_candidatas:
                msg += u"Nombre: %s Descripción: %s\n" % (clase.nombre, clase.description())
            msg += "\n"

        return clases_candidatas, msg