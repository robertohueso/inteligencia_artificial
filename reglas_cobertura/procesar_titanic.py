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

entr = random.sample(entr_bruto, 600)
valid = random.sample(entr_bruto,10)
test = random.sample(entr_bruto, 5)

titanicpy = open('titanic.py', 'w+')
titanicpy.write('atributos = ' + str(atributos) + '\n')
titanicpy.write('atributo_clasificacion = "' + str(atributo_clasificacion) + '"\n')
titanicpy.write('clases = ' + str(clases) + '\n')
titanicpy.write('entr = ' + str(entr) + '\n')
titanicpy.write('valid = ' + str(valid) + '\n')
titanicpy.write('test = ' + str(test) + '\n')
