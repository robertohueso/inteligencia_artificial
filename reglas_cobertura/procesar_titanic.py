#Dado que el archivo es un CSV
import csv
import random

def clasificar(clase, edad, sexo, sobrevive):
    if clase == '1st':
        clase = 'Primera'
    elif clase == '2nd':
        clase = 'Segunda'
    else:
        clase = 'Tercera'

    if edad != 'NA':
        edad = float(edad)

    if sexo == 'male':
        sexo = 'Masculino'
    else:
        sexo = 'Femenino'

    if int(sobrevive) == 1:
        sobrevive = 'Si'
    else:
        sobrevive = 'No'

    return [clase, edad, sexo, sobrevive]

def procesar_edad(entr_bruto):
    edades_si = []
    edades_no = []
    for muestra in entr_bruto:
        if muestra[1] != 'NA':
            if muestra[-1] == 'Si':
                edades_si.append(muestra[1])
            else:
                edades_no.append(muestra[1])
    #Tomamos como valor por defecto las medias.
    valor_si = sum(edades_si) / len(edades_si)
    valor_no = sum(edades_no) / len(edades_no)

    if valor_si <= 13:
        valor_si = 'Menor'
    else:
        valor_si = 'Mayor'

    if valor_no <= 13:
        valor_no = 'Menor'
    else:
        valor_no = 'Mayor'

    for muestra in entr_bruto:
        if muestra[1] == 'NA':
            if muestra[-1] == 'Si':
                muestra[1] = valor_si
            else:
                muestra[1] = valor_no
        elif muestra[1] <= 13:
            muestra[1] = 'Menor'
        else:
            muestra[1] = 'Mayor'
    return entr_bruto

def comprobar_proporcion(lista, dif_max):
    for i, numero in enumerate(lista):
        if abs(lista[i-1] - lista[i]) > dif_max:
            return False
    return True

def estratificar(entr_bruto, cantidad, dif_max):
    nuevo_entr = []
    clase = [0, 0, 0]
    edad = [0, 0]
    sexo = [0 ,0]
    while cantidad != 0:
        muestra = random.choice(entr_bruto)
        if 'Primera' in muestra:
            clase[0] += 1
        elif 'Segunda' in muestra:
            clase[1] += 1
        else:
            clase[2] += 1
        if 'Menor' in muestra:
            edad[0] += 1
        else:
            edad[1] += 1
        if 'Femenino' in muestra:
            sexo[0] += 1
        else:
            sexo[1] += 1

        if comprobar_proporcion(clase, dif_max) and comprobar_proporcion(edad, dif_max) and comprobar_proporcion(sexo, dif_max):
            nuevo_entr.append(muestra)
            cantidad -= 1
        else:
            if 'Primera' in muestra:
                clase[0] -= 1
            elif 'Segunda' in muestra:
                clase[1] -= 1
            else:
                clase[2] -= 1
            if 'Menor' in muestra:
                edad[0] -= 1
            else:
                edad[1] -= 1
            if 'Femenino' in muestra:
                sexo[0] -= 1
            else:
                sexo[1] -= 1
    return nuevo_entr

#Generamos el archivo titanic.py-----------------------------

atributos=[('Clase',['Primera', 'Segunda', 'Tercera']),
           ('Edad',['Menor', 'Mayor']),
           ('Sexo', ['Femenino', 'Masculino'])
           ]

atributo_clasificacion = 'Sobrevive'
clases = ['Si', 'No']

entr = []
valid = []
test = []

archivo = open('titanic.txt', 'r')
tabla = csv.DictReader(archivo)
entr_bruto = []
for fila in tabla:
    clase = fila['pclass']
    edad = fila['age']
    sexo = fila['sex']
    sobrevive = fila['survived']

    muestra = clasificar(clase, edad, sexo, sobrevive)
    entr_bruto.append(muestra)
entr_bruto = procesar_edad(entr_bruto)
    
entr = estratificar(entr_bruto, 10, 1)
valid = estratificar(entr_bruto, 5, 1)
test = random.sample(entr_bruto, 5)

titanicpy = open('titanic.py', 'w+')
titanicpy.write('atributos = ' + str(atributos) + '\n')
titanicpy.write('atributo_clasificacion = "' + str(atributo_clasificacion) + '"\n')
titanicpy.write('clases = ' + str(clases) + '\n')
titanicpy.write('entr = ' + str(entr) + '\n')
titanicpy.write('valid = ' + str(valid) + '\n')
titanicpy.write('test = ' + str(test) + '\n')
