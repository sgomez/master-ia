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
        msg = '<p class="head">Se generan las clases candidatas que son: %s</p>' % ([clase.nombre for clase in clases_candidatas])

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

                obtener = inference.Obtener(self.obj, nuevo_atributo[0])
                caracteristica = obtener.execute()

                print " Atributo y valor del objeto: %s= %s" % (caracteristica.atributo.nombre, caracteristica.valor)
                msg += '<p class="select">Seleccionamos el atributo <strong>%s</strong> con el valor <strong>%s</strong></p>' % (caracteristica.atributo.nombre, caracteristica.valor)

                nuevos_valores.append(caracteristica)

                nuevas_candidatas = []

                msg += '<table>'
                msg += '<thead><tr><th>Clase</th><th>Atributo</th><th>Valor</th><th>Regla</th><th>Valor esperado</th><th>Resultado</th></tr></thead>'
                msg += '<tbody>'

                for clase in clases_candidatas:
                    print "Probamos a equipara la clase %s con el conjunto de nuevos pares atributos/valores %s" \
                        % (clase.nombre, [item.atributo.nombre for item in nuevos_valores])

                    equiparar = inference.Equiparar(clase, nuevos_valores)
                    resultado, explicacion = equiparar.execute()

                    for item in explicacion:
                        estado = 'pass' if item[5] else 'nopass'
                        msg += '<tr class="%s"><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' \
                               % (estado, item[0], item[1], item[2], item[3], item[4], item[5])

                    if resultado == True:
                        nuevas_candidatas.append(clase)
                        print "Clase aceptada: %s" % clase.nombre
            else:
                print "No quedan más atributos por especificar"
                found = True
                continue

            clases_candidatas = nuevas_candidatas
            msg += '</tbody>'
            msg += '</table>'
            msg += '<p class="head">Clases candidatas tras la equiparaci&oacute;n: %s</p>' % ([clase.nombre for clase in clases_candidatas])

        return clases_candidatas, msg