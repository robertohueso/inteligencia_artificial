# ==========================================================
# Inteligencia Artificial. Tercer curso. Grupo 2.
# Grado en Ingeniería Informática - Tecnologías Informáticas
# Curso 2016-17
# Universidad de Sevilla
# Trabajo práctico
# Profesor: José Luis Ruiz Reina
# ===========================================================

# --------------------------------------------------------------------------
# Primer componente del grupo (o único autor): 
#
# APELLIDOS: HUESO GOMEZ
# NOMBRE: ROBERTO
# 
# Segundo componente (si se trata de un grupo):
#
# APELLIDOS
# NOMBRE:
# ----------------------------------------------------------------------------

# *****************************************************************************
# HONESTIDAD ACADÉMICA Y COPIAS: un trabajo práctico es un examen, por lo que
# debe realizarse exclusivamente por cada estudiante o grupo. La discusión y
# el intercambio de información de carácter general con los compañeros se
# permite (e incluso se recomienda), pero NO AL NIVEL DE CÓDIGO. Igualmente el
# remitir código de terceros, obtenido a través de la red o cualquier otro
# medio, se considerará plagio.

# Cualquier plagio o compartición de código que se detecte significará
# automáticamente la calificación de CERO EN LA ASIGNATURA para TODOS los
# alumnos involucrados. Por tanto a estos alumnos NO se les conservará, para
# futuras convocatorias, ninguna nota que hubiesen obtenido hasta el
# momento. Sin perjuicio de OTRAS MEDIDAS DE CARÁCTER DISCIPLINARIO. 
# *****************************************************************************


# IMPORTANTE: NO CAMBIAR EL NOMBRE NI A ESTE ARCHIVO NI A LAS FUNCIONES QUE SE
# PIDEN 





# ---------------------------------------------------------------------------
# PARTE 0: Conjuntos de datos
# ---------------------------------------------------------------------------

# EN ESTA PARTE NO SE PIDE NADA, PERO ES NECESARIO LEERLA PARA ENTENDER LA
# ESTRUCTURA DE LOS CONJUNTOS DE DATOS QUE SE PROPORCIONAN 
#
# Los archivos jugar_tenis.py, lentes.py, votos.py y credito.py (que se pueden
# descargar desde la página del trabajo) contienen los conjuntos de datos que
# vamos a usar para probar los algoritmos implementados.

# Cada archivo contiene la definición correspondiente de las siguientes
# variables:

# * atributos: es una lista de pares (Atributo,Valores) para cada atributo o
#   característica del conjunto de datos. Atributo es el nombre del atributo y
#   Valores es la lista de sus posibles valores.

# * atributo_clasificación: nombre del atributo de clasificación

# * clases: posibles valores (o clases) del atributo de clasificación

# * entr: conjunto de entrenamiento, una lista de ejemplos en los que cada
#   ejemplo es una lista de valores (cada valor indica el valor del atributo
#   correspondiente, en el mismo orden en el que aparecen en la lista de
#   atributos). El último valor del ejemplo es su clase.

# Además, votos.py y credito.py contienen las siguientes variables adicionales:

# * valid: conjunto de validación, una lista de ejemplos con el mismo formato
#     que la de entrenamiento. Este conjunto de ejemplo se usará para
#     generalizar el modelo aprendido con el de entrenamiento (en nuestro
#     caso, para hacer la poda). 

# * test: conjunto de test, una lista de ejemplos con el mismo formato
#     que la de entrenamiento. Este conjunto de ejemplo se usará para
#     medir el rendimiento final del clasificador aprendido. 

# Cargamos los cuatro conjuntos de datos:

import jugar_tenis
import lentes
import votos
import credito


# ---------------------------------------------------------------------------
# PARTE 1: Aprendizaje de reglas mediante cobertura
# ---------------------------------------------------------------------------

# En esta parte se trata de implementar el algoritmo de aprendizaje de reglas
# mediante cobertura, tal y como se explica en las diapositivas 34 a 45 del
# tema 7.


# Representación de reglas:
# =========================

# Para implementar el algoritmo de cobertura, lo primero que hay que decidir
# es cómo se va a repesentar una regla en python. En lo que sigue
# describirimos una representación que NO ES OBLIGATORIA, pero que será la que
# usemos en nuestros ejemplos de ejecución. 

# Puesto que el algoritmo aprende todas las reglas a la vez para cada clase,
# no será necesario que representemos la conclusión de una regla (ya que para una
# clase dada será siempre la misma), sino que sólo necesitamos representar las
# condiciones de la regla.

# Si tenemos una regla 

#     Si Atr1=v1 y Atr2=v2 y ... y Atrn=vn Entonces Clase=c

# representaremos la regla mediante la lista de pares:

#  [(i1,v1),(i2,v2),...,(in,vn)]

# donde i1,i2,..,in son las posiciones de los atributos Atr1,...,Atrn
# en la lista atributos que aparece en el archivo de datos.

# Ejemplos:
# ---------

# Por ejemplo, en el ejemplo de las lentes de contacto, las condiciones de la regla:

# Si (Astigmatismo = +) y (Lagrima = Normal) y (Diagnóstico = Miope) Entonces [Lente = Rígida]

# se representan por la lista:

# [(2, '+'), (3, 'Normal'), (1, 'Miope')]

# ya que en la lista lentes.atributos, "Astigmatismo" está en la posición 2,
# "Lagrima" en la posición 3, y "Diagnóstico" en la posición 1. 

# Otro ejemplo. En jugar_tenis, las condiciones de la regla:

# Si (Humedad = Normal) y (Viento = Débil) Entonces [Jugar Tenis = si]

# se representan por la lista:

# [(2, 'Normal'), (3, 'Débil')]

# ya que en jugar_tenis.atributos, "Humedad" está en la posición 2 y "Viento"
# en la posición 3.
# -------------

# Función que se pide
# ===================

# Implementar una función "cobertura(entr,atributos,clase)" que recibiendo
# como entrada un conjunto de entrenamiento (en forma de lista de ejemplos),
# la lista de los atributos del problema (tal y como se representa en los
# archivos ded datos) y un valor de clasificación, devuelve la lista de las
# condicones de la reglas aprendidas por el algoritmo de cobertura, tal y como
# se describe en la diapositiva 43 del tema 7.


# Ejemplos:
# ---------

# >>> cobertura(lentes.entr,lentes.atributos,"Rígida")
# [[(2, '+'), (3, 'Normal'), (1, 'Miope')],
#  [(0, 'Joven'), (2, '+'), (3, 'Normal')]]


# >>> cobertura(lentes.entr,lentes.atributos,"Blanda")
# [[(2, '-'), (3, 'Normal'), (1, 'Hipermétrope')],
#  [(2, '-'), (3, 'Normal'), (0, 'Joven')],
#  [(0, 'Prepresbicia'), (2, '-'), (3, 'Normal')]]

# >>> cobertura(jugar_tenis.entr,jugar_tenis.atributos,"no")
# [[(0, 'Soleado'), (2, 'Alta')], 
#  [(0, 'Lluvia'), (3, 'Fuerte')]]

# >>> cobertura(credito.entr,credito.atributos,"conceder") 
# [[(0, 'funcionario'), (5, 'altos')],
#  [(2, 'dos o más'), (5, 'medios')],
#  [(0, 'laboral'), (5, 'altos'), (1, 'ninguno')],
#  [(2, 'dos o más'), (0, 'funcionario'), (4, 'soltero')],
#  [(2, 'dos o más'), (0, 'funcionario'), (1, 'uno')],
#  [(0, 'laboral'), (5, 'altos'), (2, 'dos o más')],
#  [(0, 'laboral'), (5, 'altos'), (3, 'dos o más')],
#  [(2, 'dos o más'), (0, 'funcionario'), (3, 'uno')],
#  [(0, 'laboral'), (5, 'altos'), (4, 'viudo')],
#  [(2, 'dos o más'), (0, 'funcionario'), (4, 'divorciado')],
#  [(2, 'dos o más'), (0, 'funcionario'), (1, 'dos o más'), (3, 'dos o más')],
#  [(5, 'altos'), (0, 'laboral'), (4, 'casado')],
#  [(2, 'dos o más'), (0, 'parado'), (3, 'dos o más'), (4, 'divorciado')],
#  [(0, 'laboral'), (5, 'altos'), (2, 'una'), (3, 'uno')],
#  [(3, 'ninguno'), (2, 'dos o más'), (4, 'casado'), (1, 'uno'), (5, 'bajos')],
#  [(3, 'ninguno'), (0, 'parado'), (4, 'viudo'), (1, 'ninguno')],
#  [(2, 'dos o más'), (0, 'parado'), (1, 'dos o más'), (3, 'ninguno')],
#  [(3, 'ninguno'), (2, 'ninguna'), (4, 'viudo'), (0, 'parado')],
#  [(1, 'uno'),(2, 'dos o más'),(3, 'dos o más'),(0, 'parado'),(4, 'soltero')],
#  [(0, 'laboral'), (4, 'divorciado'), (2, 'ninguna'), (3, 'ninguno')]]
# ---------

def contiene_clase(entr, clase):
    for muestra in entr:
        if muestra[-1] == clase:
            return True
    return False

def muestra_compatible(muestra, regla):
    for atomo in regla:
        if muestra[atomo[0]] != atomo[1]:
            return False
    return True

def muestras_que_cumplen(entr, regla):
    cumplidoras = []
    for muestra in entr:
        if muestra_compatible(muestra, regla):
            cumplidoras.append(muestra)
    return cumplidoras

def muestras_que_cumplen_clase(entr, regla, clase):
    cumplidoras = muestras_que_cumplen(entr, regla)
    cumplidoras_de_clase = []
    for muestra in cumplidoras:
        if muestra[-1] == clase:
            cumplidoras_de_clase.append(muestra)
    return cumplidoras_de_clase

def contiene_ejemplo_incorrecto(entr, regla, clase):
    muestras_ajustadas = muestras_que_cumplen(entr, regla)
    for muestra in muestras_ajustadas:
        if muestra[-1] != clase:
            return True
    return False

def atributo_en_regla(index, regla):
    for atomo in regla:
        if atomo[0] == index:
            return True
    return False

def mejor_prox_atributo(entr, atributos, regla, clase):
    atributos_asignables = []
    #Comprueba que atributos no estan aun en la regla
    for i, atributo in enumerate(atributos):
        if not atributo_en_regla(i, regla):
            atributos_asignables.append((i, atributo[1]))
    #Comprueba cual es el mejor proximo atributo a elegir
    mejor_actual = (0, -1, '') #Mejor(proporcion, numero_atributo, valor)
    for atributo in atributos_asignables:
        for valor in atributo[1]:
            nueva_regla = regla + [(atributo[0], valor)]
            n_cumplidoras_regla = len(muestras_que_cumplen(entr, nueva_regla))

            if n_cumplidoras_regla != 0:
                proporcion = len(muestras_que_cumplen_clase(entr, nueva_regla, clase))/n_cumplidoras_regla
            else:
                proporcion = 0
            if proporcion > mejor_actual[0] or (n_cumplidoras_regla > len(muestras_que_cumplen(entr, regla + [(mejor_actual[1], mejor_actual[2])])) and proporcion == mejor_actual[0]):
                mejor_actual = (proporcion, atributo[0], valor)

    return mejor_actual

def quitar_muestras(original, eliminar):
    for muestra in eliminar:
        if muestra in original:
            original.remove(muestra)

def cobertura(entr,atributos,clase):
    conjunto = entr.copy()
    reglas_aprendidas = []
    while contiene_clase(conjunto, clase):
        regla = []
        while contiene_ejemplo_incorrecto(conjunto, regla, clase) or len(regla) < len(atributos):
            mejor_atrib = mejor_prox_atributo(conjunto, atributos, regla, clase)
            regla.append((mejor_atrib[1], mejor_atrib[2]))
            if mejor_atrib[0] == 1.0:
                break
        reglas_aprendidas.append(regla)
        muestras_cubiertas = muestras_que_cumplen_clase(conjunto, regla, clase)
        quitar_muestras(conjunto, muestras_cubiertas)
    return reglas_aprendidas

# ---------------------------
# PARTE 2: Reglas de decisión
# ---------------------------

# El algoritmo de aprendizaje de reglas por cobertura nos permite aprender un
# conjunto de reglas por cada valor de clasificación. Si a partir de estas
# reglas queremos tener un clasificador para nuevos ejemplos, de los cuales no
# conocemos su clasificación, lo natural sería buscar una regla de las
# aprendididas que cubra al ejemplo (es decir, tal que el ejemplo cumple las
# condiciones de la regla), y entonces clasificar el ejemplo según el valor de
# clasificación que aparece en la conclusión de esa regla.

# Sin embargo, esta manera natural de clasificar usando reglas, a veces
# presenta algunos problemas:
# (1) Un mismo ejemplo podría ser cubierto con varias reglas distintas, 
#     con distintos valores de clasificación en sus conclusiones 
# (2) O por el contrario, puede que ninguna regla cubra al ejemplo. 

# En ambas situaciones, debemos decidir qué valor de clasificación le damos al
# ejemplo. Existen varias maneras de tratar esto, pero nosotros en este
# trabajo veremos la manera más simple, que pasamos a describir.  

# Para evitar el problema (1), el conjunto de reglas lo daremos ORDENADO, y
# consideraremos sólo la PRIMERA regla, en ese orden, que cubra al ejemplo que
# se quiere clasificar. Para ordenar el conjunto de reglas, colocaremos en
# primer lugar las reglas aprendidas para el valor de clasificación menos
# frecuente en el conjunto de entrenamiento, a continuación las reglas
# apendidas para la segunda clase menos frecuente, etc. La idea intuitiva es
# que las clases menos frecuentes se tratan primero, ya que son más
# específicas.  Además, para evitar el problema (2), en último lugar no
# incluiremos las reglas de la clase más frecuente, sino que colocaremos al
# final una sola regla para dicha clase, sin condiciones (es decir,
# devolveríamos el valor de clasificación más frecuente en ejemplos que no
# cumplen las condiciones de ninguna de las reglas de las restantes clases).

# Los conjuntos de reglas ordenados que clasifican los ejemplos como se han
# descrito, los llamaremos REGLAS DE DECISIÓN. Por ejemplo, lo que sigue es un
# conjunto de reglas de decisión para el ejemplo de las lentes:

# Ejemplo:
# --------

# * Si (Astigmatismo = +) y (Lagrima = Normal) y (Diagnóstico = Miope) Entonces [Lente = Rígida]
# * Si (Edad = Joven) y (Astigmatismo = +) y (Lagrima = Normal) Entonces [Lente = Rígida]
# * Si (Astigmatismo = -) y (Lagrima = Normal) y (Diagnóstico = Hipermétrope) Entonces [Lente = Blanda]
# * Si (Astigmatismo = -) y (Lagrima = Normal) y (Edad = Joven) Entonces [Lente = Blanda]
# * Si (Edad = Prepresbicia) y (Astigmatismo = -) y (Lagrima = Normal) Entonces [Lente = Blanda]
# * En caso contrario, [Lente = Ninguna]

# Con estas reglas de decisión, si queremos clasificar el ejemplo 
#   ["Joven","Hipermétrope","-","Normal"]
# lo clasificaríamos como "Blanda", ya que la primera regla que cubre al
# ejemplo es la tercera. 
# Si queremos clasificar el ejemplo 
# ["Joven","Hipermétrope","-","Reducida"]
# entonces lo calificaríamos como "Ninguna", ya que no lo cubre ninguna de las
# reglas, excepto la última.
# ---------

# En python, los conjuntos de reglas de decisión se pueden representar de la
# siguiente manera (no es obligatorio representarlo así, es sólo una posible
# manera):

# [[Clase_1,[R11,R12, ...]],
#  [Clase_2,[R21,R22,....]] 
#  .....
#  [Clase_n,[[]]]

# Donde [Ri1,Ri2,...] a su vez son la lista de reglas (en realidad, sólo sus
# condiciones) de la clase i. 

# Ejemplo:
# --------

# Por ejemplo, lo que sigue es la representación en python del conjunto de
# reglas de decisión anterior:
 
# [['Rígida',
#  [[(2, '+'), (3, 'Normal'), (1, 'Miope')],
#   [(0, 'Joven'), (2, '+'), (3, 'Normal')]]],
# ['Blanda',
#  [[(2, '-'), (3, 'Normal'), (1, 'Hipermétrope')],
#   [(2, '-'), (3, 'Normal'), (0, 'Joven')],
#   [(0, 'Prepresbicia'), (2, '-'), (3, 'Normal')]]],
# ('Ninguna', [[]])]

# Un conjunto de reglas de decisión para el problema de jugar al tenis: 

# [['no', [[(0, 'Soleado'), (2, 'Alta')], 
#          [(0, 'Lluvia'), (3, 'Fuerte')]]],
#  ['si', [[]]]]
# ---------

# Funciones que se piden:
# -----------------------

# - Una función "reglas_decision_cobertura(entr,atributos,clases)", que
#   recibiendo como entrada un conjunto de entrenamiento (en forma de lista de
#   ejemplos), la lista de los atributos del problema (tal y como se representa
#   en los archivos ded datos) y la lista de valores de clasificación del
#   problema, aprende un conjunto de reglas de decisión mediante el algoritmo de
#   cobertura. En concreto, esta función debe ordenar las clases de menor a
#   mayor frencuencia en el conjunto de entrenamiento, y en ese orden, para cada
#   clase aprender el correspondiente conjunto de reglas (llamando a la función
#   "cobertura" anteriormente implementada). Para la última clase (la más
#   frecuente en el conjunto de entrenamiento), no se aprenden reglas, sino que
#   se coloca una única regla sin condiciones.

# - Una función "imprime_RD(reglas_decision,atributos,atributo_clasificacion)"
#   que recibe un conjunto de reglas de clasificación, la lista de los atributos
#   del problema (tal y como se representa en los archivos de datos) y el nombre
#   del atributo de clasificación, e imprime las reglas de una manera más
#   legible, tal y como por ejemplo se muestra arriba. 

# - Una función "clasifica_RD(ej,reglas_decision)" que recibe un ejemplo ej y
#   un conjunto de reglas de decisión, y devuelve la clasificación que el
#   conjunto de reglas de decisión da para ese ejemplo.

# - Una función "rendimiento_RD(reglas_decision,ejemplos)" que devuelve el
#   rendimiento del conjunto de reglas de decisión sobre un conjunto de
#   ejemplos de los que ya se conoce su valor de clasificación. El rendimiento se
#   define como la proporción de ejemplos que se clasifican correctamente. 


# Ejemplos:
# ---------

# Jugar al tenis:
# ______________

# >>> jt_rd=reglas_decision_cobertura(jugar_tenis.entr,jugar_tenis.atributos,jugar_tenis.clases)
# >>> imprime_RD(jt_rd,jugar_tenis.atributos,jugar_tenis.atributo_clasificación)

# * Si (Cielo = Soleado) y (Humedad = Alta) Entonces [Jugar Tenis = no]
# * Si (Cielo = Lluvia) y (Viento = Fuerte) Entonces [Jugar Tenis = no]
# * En caso contrario, [Jugar Tenis = si]

# >>> clasifica_RD(['Soleado' ,'Suave','Alta','Fuerte'],jt_rd)
# 'no'
# >>> rendimiento_RD(jt_rd,jugar_tenis.entr)
# 1.0


# Lentes de contacto:
# ___________________

# >>> lentes_rd=reglas_decision_cobertura(lentes.entr,lentes.atributos,lentes.clases)
# >>> imprime_RD(lentes_rd,lentes.atributos,lentes.atributo_clasificación)

# * Si (Astigmatismo = +) y (Lagrima = Normal) y (Diagnóstico = Miope) Entonces [Lente = Rígida]
# * Si (Edad = Joven) y (Astigmatismo = +) y (Lagrima = Normal) Entonces [Lente = Rígida]
# * Si (Astigmatismo = -) y (Lagrima = Normal) y (Diagnóstico = Hipermétrope) Entonces [Lente = Blanda]
# * Si (Astigmatismo = -) y (Lagrima = Normal) y (Edad = Joven) Entonces [Lente = Blanda]
# * Si (Edad = Prepresbicia) y (Astigmatismo = -) y (Lagrima = Normal) Entonces [Lente = Blanda]
# * En caso contrario, [Lente = Ninguna]

# >>> clasifica_RD(["Joven","Hipermétrope","-","Normal"],lentes_rd)
# 'Blanda'
# >>> clasifica_RD(["Joven","Hipermétrope","-","Reducida"],lentes_rd)
# 'Ninguna'
# >>> rendimiento_RD(lentes_rd,lentes.entr)
# 1.0

# Votos:
# ______


# >>> votos_rd=reglas_decision_cobertura(votos.entr,votos.atributos,votos.clases)
# >>> imprime_RD(votos_rd,votos.atributos,votos.atributo_clasificación)

# * Si (voto4 = s) y (voto7 = s) Entonces [Partido = republicano]
# * Si (voto4 = s) y (voto2 = ?) Entonces [Partido = republicano]
# * Si (voto4 = s) y (voto13 = n) Entonces [Partido = republicano]
# * Si (voto4 = s) y (voto6 = n) Entonces [Partido = republicano]
# * Si (voto4 = s) y (voto8 = ?) Entonces [Partido = republicano]
# * Si (voto4 = s) y (voto14 = ?) Entonces [Partido = republicano]
# * Si (voto4 = s) y (voto11 = ?) Entonces [Partido = republicano]
# * Si (voto4 = s) y (voto15 = ?) Entonces [Partido = republicano]
# * Si (voto4 = s) y (voto7 = ?) Entonces [Partido = republicano]
# * Si (voto4 = s) y (voto14 = n) Entonces [Partido = republicano]
# * Si (voto4 = s) y (voto3 = n) y (voto13 = s) Entonces [Partido = republicano]
# * Si (voto4 = ?) y (voto9 = ?) Entonces [Partido = republicano]
# * Si (voto3 = n) y (voto12 = ?) Entonces [Partido = republicano]
# * Si (voto3 = n) y (voto6 = n) y (voto15 = n) Entonces [Partido = republicano]
# * En caso contrario, [Partido = demócrata]

# >>> clasifica_RD(votos.test[23],votos_rd)
# 'demócrata'
# >>> rendimiento_RD(votos_rd,votos.entr)
# 1.0
# >>> rendimiento_RD(votos_rd,votos.valid)
# 0.9565217391304348
# >>> rendimiento_RD(votos_rd,votos.test)
# 0.9195402298850575


# Concesión de crédito:
# _____________________

# >>> credito_rd=reglas_decision_cobertura(credito.entr,credito.atributos,credito.clases)
# >>> imprime_RD(credito_rd,credito.atributos,credito.atributo_clasificación)

# * Si (Empleo = funcionario) y (Ingresos = altos) Entonces [Crédito = conceder]
# * Si (Propiedades = dos o más) y (Ingresos = medios) Entonces [Crédito = conceder]
# * Si (Empleo = laboral) y (Ingresos = altos) y (Productos = ninguno) Entonces [Crédito = conceder]
# * Si (Propiedades = dos o más) y (Empleo = funcionario) y (Estado civil = soltero) Entonces [Crédito = conceder]
# * Si (Propiedades = dos o más) y (Empleo = funcionario) y (Productos = uno) Entonces [Crédito = conceder]
# * Si (Empleo = laboral) y (Ingresos = altos) y (Propiedades = dos o más) Entonces [Crédito = conceder]
# * Si (Empleo = laboral) y (Ingresos = altos) y (Hijos = dos o más) Entonces [Crédito = conceder]
# * Si (Propiedades = dos o más) y (Empleo = funcionario) y (Hijos = uno) Entonces [Crédito = conceder]
# * Si (Empleo = laboral) y (Ingresos = altos) y (Estado civil = viudo) Entonces [Crédito = conceder]
# * Si (Propiedades = dos o más) y (Empleo = funcionario) y (Estado civil = divorciado) Entonces [Crédito = conceder]
# * Si (Propiedades = dos o más) y (Empleo = funcionario) y (Productos = dos o más) y (Hijos = dos o más) Entonces [Crédito = conceder]
# * Si (Ingresos = altos) y (Empleo = laboral) y (Estado civil = casado) Entonces [Crédito = conceder]
# * Si (Propiedades = dos o más) y (Empleo = parado) y (Hijos = dos o más) y (Estado civil = divorciado) Entonces [Crédito = conceder]
# * Si (Empleo = laboral) y (Ingresos = altos) y (Propiedades = una) y (Hijos = uno) Entonces [Crédito = conceder]
# * Si (Hijos = ninguno) y (Propiedades = dos o más) y (Estado civil = casado) y (Productos = uno) y (Ingresos = bajos) Entonces [Crédito = conceder]
# * Si (Hijos = ninguno) y (Empleo = parado) y (Estado civil = viudo) y (Productos = ninguno) Entonces [Crédito = conceder]
# * Si (Propiedades = dos o más) y (Empleo = parado) y (Productos = dos o más) y (Hijos = ninguno) Entonces [Crédito = conceder]
# * Si (Hijos = ninguno) y (Propiedades = ninguna) y (Estado civil = viudo) y (Empleo = parado) Entonces [Crédito = conceder]
# * Si (Productos = uno) y (Propiedades = dos o más) y (Hijos = dos o más) y (Empleo = parado) y (Estado civil = soltero) Entonces [Crédito = conceder]
# * Si (Empleo = laboral) y (Estado civil = divorciado) y (Propiedades = ninguna) y (Hijos = ninguno) Entonces [Crédito = conceder]
# * Si (Ingresos = bajos) y (Empleo = parado) y (Propiedades = una) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) y (Propiedades = ninguna) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Propiedades = ninguna) y (Empleo = funcionario) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = parado) y (Productos = ninguno) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) y (Productos = dos o más) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = parado) y (Hijos = ninguno) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = laboral) y (Productos = uno) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = parado) y (Estado civil = viudo) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) y (Propiedades = una) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Propiedades = ninguna) y (Productos = ninguno) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = parado) y (Productos = uno) y (Propiedades = ninguna) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Propiedades = ninguna) y (Empleo = jubilado) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) y (Hijos = uno) Entonces [Crédito = no conceder]
# * Si (Empleo = parado) y (Ingresos = medios) y (Propiedades = ninguna) y (Productos = dos o más) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Estado civil = divorciado) y (Propiedades = ninguna) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Estado civil = divorciado) y (Empleo = laboral) y (Productos = ninguno) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Empleo = parado) y (Propiedades = ninguna) y (Productos = uno) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) y (Estado civil = soltero) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Productos = ninguno) y (Propiedades = una) y (Estado civil = soltero) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) y (Estado civil = divorciado) y (Productos = ninguno) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = laboral) y (Productos = ninguno) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Empleo = parado) y (Propiedades = ninguna) y (Hijos = uno) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Hijos = dos o más) y (Propiedades = una) y (Productos = dos o más) Entonces [Crédito = no conceder]
# * Si (Empleo = parado) y (Ingresos = bajos) y (Productos = uno) y (Hijos = uno) Entonces [Crédito = no conceder]
# * Si (Empleo = parado) y (Ingresos = medios) y (Productos = ninguno) y (Hijos = uno) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Empleo = parado) y (Productos = ninguno) y (Estado civil = soltero) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Hijos = dos o más) y (Propiedades = una) y (Empleo = parado) Entonces [Crédito = no conceder]
# * Si (Empleo = jubilado) y (Ingresos = bajos) y (Estado civil = divorciado) y (Hijos = ninguno) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Propiedades = ninguna) y (Empleo = parado) y (Estado civil = divorciado) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Empleo = jubilado) y (Productos = dos o más) y (Propiedades = una) Entonces [Crédito = no conceder]
# * Si (Empleo = laboral) y (Hijos = dos o más) y (Propiedades = ninguna) y (Ingresos = medios) y (Productos = uno) Entonces [Crédito = no conceder]
# * En caso contrario, [Crédito = estudiar]

# >>> clasifica_RD(credito.test[44],credito_rd)
# 'estudiar'
# >>> clasifica_RD(credito.test[11],credito_rd)
# 'conceder'

# >>> rendimiento_RD(credito_rd,credito.entr)
# 1.0
# >>> rendimiento_RD(credito_rd,credito.valid)
# 0.8950617283950617
# >>> rendimiento_RD(credito_rd,credito.test)
# 0.8895705521472392

def apariciones_clase(entr, clase):
    count = 0
    for muestra in entr:
        if muestra[-1] == clase:
            count += 1
    return count

def reglas_decision_cobertura(entr,atributos,clases):
    reglas = []
    for clase in clases:
        reglas.append([clase, cobertura(entr, atributos, clase)])
    #Soluciona que un mismo valor sea cubierto por varias reglas
    reglas.sort(key = lambda x: apariciones_clase(entr, x[0]))
    #Soluciona que ninguna regla cubra el ejemplo
    reglas[-1][1] = []
    return reglas

#reglas_decision_cobertura(jugar_tenis.entr, jugar_tenis.atributos, jugar_tenis.clases)






# -----------------------------------
# PARTE 3: Poda para reducir el error
# -----------------------------------

# Uno de los principales problema en el aprendizaje de conjuntos de reglas de
# decisión es el sobreajuste. Es decir, que el conjunto de reglas aprendido se
# ajuste tanto al conjunto de entrenamiento que aprenda también el "ruido", o
# características que son específicas del conjunto de entrenamiento, pero que
# no ocurren en general.

# Para combatir el sobreajuste, una técnica muy extendida es aplicar un
# proceso de "podado" de la reglas que se han aprendido. Por podado de reglas
# entendemos quitar algunas condiciones a las reglas, o incluso eliminar
# alguna regla completamente (más abajo se describen las posibles podas con
# detalle). Para medir si el realizar una determinada poda es beneficioso,
# medimos el rendimiento en un conjunto de ejemplos distinto al de
# entrenamiento (que llamaremos conjunto de validación). El rendimiento del
# conjunto final de reglas de decisión, resultante de las podas, se comprueba
# sobre un tercer conjuto de ejemplos (llamado de "test"), distinto de los dos
# anteriores. 

# En nuestro caso, vamos a aplicar una técnica de podado muy simple, de manera
# que sólo permitimos dos tipos de podas:
# - Elegir una regla con más de una condición, y eliminar LA ÚLTIMA condición.
# - Elegir una clase que tenga más de una regla y eliminar completamente LA
#   ÚLTIMA regla de esa clase 

# El algoritmo que se pide implementar es muy similar al que se ha visto en el
# tema 7 para árboles de decisión excepto que las podas que se pueden realizar
# se hacen sobre las reglas y tienen que ser de uno de los dos tipos anteriores.

# En concreto, a partir de un conjunto RD de reglas de decisión que se recibe
# como entrada (que será el que se ha aprendido mediante cobertura sobre el
# conjunto de entrenamiento) y de un conjunto de ejemplos de validación, el
# algoritmo de poda de reglas (o de POSPODA) debe realizar lo siguiente:

# 1. Medir el rendimiento de RD sobre el conjunto de validación.
# 2. Para cada posible manera de realizar una poda de uno de los dos tipos
#    anteriores, se mide el rendimiento, sobre el conjunto de validación, del 
#    conjunto de reglas resultante de realizar esa poda. 
#    Sea RD* el resultado de la poda con el MEJOR rendimiento.
# 3. Si RD tiene un rendimiento menor o igual que el de RD*, entonces hacer RD
#    igual a RD*, e ir de nuevo al punto 1. Si RD tiene un rendimiento mayor
#    que RD*, entonces terminar y devolver RD.         


# Función que se pide:
# -------------------


# - Definir una función "poda_RD(reglas_de_decision,ejemplos)", que recibiendo
#   como entrada un conjunto de reglas de decisión y un conjunto de ejemplos de
#   validación, devuelve un nuevo conjunto de reglas de decisión que resulta de
#   aplicar el algoritmo de poda que se acaba de describir.

  

# Ejemplos:
# ---------


# Votos:
# ______

# >>> votos_rd_pd=poda_RD(votos_rd,votos.valid)
# >>> imprime_RD(votos_rd_pd,votos.atributos,votos.atributo_clasificación)

# * Si (voto4 = s) Entonces [Partido = republicano]
# * En caso contrario, [Partido = demócrata]

# >>> rendimiento_RD(votos_rd_pd,votos.entr)
# 0.96415770609319
# >>> rendimiento_RD(votos_rd_pd,votos.valid)
# 0.9855072463768116
# >>> rendimiento_RD(votos_rd_pd,votos.test)
# 0.9080459770114943


# Concesión de crédito:
# _____________________


# >>> credito_rd_pd=poda_RD(credito_rd,credito.valid)
# >>> imprime_RD(credito_rd_pd,credito.atributos,credito.atributo_clasificación)

# * Si (Empleo = funcionario) y (Ingresos = altos) Entonces [Crédito = conceder]
# * Si (Propiedades = dos o más) y (Ingresos = medios) Entonces [Crédito = conceder]
# * Si (Empleo = laboral) y (Ingresos = altos) Entonces [Crédito = conceder]
# * Si (Propiedades = dos o más) y (Empleo = funcionario) Entonces [Crédito = conceder]
# * Si (Ingresos = bajos) y (Empleo = parado) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Propiedades = ninguna) y (Empleo = funcionario) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = parado) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = parado) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = laboral) y (Productos = uno) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = parado) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Propiedades = ninguna) y (Productos = ninguno) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = parado) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Propiedades = ninguna) y (Empleo = jubilado) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) Entonces [Crédito = no conceder]
# * Si (Empleo = parado) y (Ingresos = medios) y (Propiedades = ninguna) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Estado civil = divorciado) y (Propiedades = ninguna) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Estado civil = divorciado) y (Empleo = laboral) y (Productos = ninguno) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Empleo = parado) y (Propiedades = ninguna) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Productos = ninguno) y (Propiedades = una) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = jubilado) Entonces [Crédito = no conceder]
# * Si (Ingresos = bajos) y (Empleo = laboral) y (Productos = ninguno) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Empleo = parado) y (Propiedades = ninguna) Entonces [Crédito = no conceder]
# * Si (Ingresos = medios) y (Hijos = dos o más) y (Propiedades = una) y (Productos = dos o más) Entonces [Crédito = no conceder]
# * En caso contrario, [Crédito = estudiar]

# >>> rendimiento_RD(credito_rd_pd,credito.entr)
# 0.9353846153846154
# >>> rendimiento_RD(credito_rd_pd,credito.valid)
# 1.0
# >>> rendimiento_RD(credito_rd_pd,credito.test)
# 0.9877300613496932


# Comentario:
# -----------

# Como se observa, en el caso del ejemplo del crédito, el rendimiento sobre el
# conjunto de test mejora considerablemente una vez se realiza la poda (aunque
# empeora sobre el conjunto de entrenamiento, lo cual es previsible). En el caso
# de los votos, el conjunto podado no mejora al conjunto sin podar. Decir que
# aunque la técnica de podar que aquí se pide es simple y bastante aceptable,
# existen técnicas de poda más sofisticadas, que obtienen mejores resultados.



# -----------------------
# PARTE 4: Clasificadores
# -----------------------

# En ese apartado NO SE PIDE IMPLEMENTAR NINGÚN ALGORITMO, tan solo nos va
# servir para tratar los dos clasificadores vistos (cobertura y cobertura con
# pospoda) bajo un marco común

# En este trabajo, por clasificador, entendemos una clase que incluye métodos
# para el entrenamiento y la clasificación, junto con otros métodos, como la
# impresión del clasificador. En concreto, un clasificador será una subclase
# de la siguiente clase general:

class MetodoClasificacion:
    """
    Clase base para métodos de clasificación
    """

    def __init__(self, atributo_clasificacion,clases,atributos):

        """
        Argumentos de entrada al constructor (ver jugar_tenis.py, por ejemplo)
         
        * atributo_clasificacion: nombre del atributo de clasificación 
        * clases: lista de posibles valores del atributo de clasificación.  
        * atributos: lista con pares en los que están los atributos (o
                     características)  y su lista de valores posibles.
        """

        self.atributo_clasificacion=atributo_clasificacion
        self.clases = clases
        self.atributos=atributos


    def entrena(self,entr,valid=None):
        """
        Método genérico para entrenamiento y ajuste del
        clasificador. Deberá ser definido para cada clasificador en
        particular. 
        
        Argumentos de entrada:

        * entr: ejemplos del conjunto de entrenamiento 
        * valid: ejemplos del conjunto de validación. 
                 Algunos clasificadores simples no usan conjunto de
                 validación, por lo que en esos casos se 
                 omitiría este argumento. 
        """
        pass

    def clasifica(self, ejemplo):
        """
        Método genérico para clasificación de un ejemplo, una vez entrenado el
        clasificador. Deberá ser definido para cada clasificador en
        particular.

        Si se llama a este método sin haber entrenado previamente el
        clasificador, debe devolver un excepción ClasificadorNoEntrenado
        (introducida más abajo) 
        """
        pass

    def imprime_clasificador(self):
        """
        Método genérico para imprimir por pantalla el clasificador
        obtenido. Deberá ser definido para cada clasificador en 
        particular. 

        Si se llama a este método sin haber entrenado previamente el
        clasificador, debe devolver un excepción ClasificadorNoEntrenado
        (introducida más abajo) 
        """
        pass



# Excepción que ha de devolverse se llama al método de clasificación (o al de
# impresión) antes de ser entrenado:  
        
class ClasificadorNoEntrenado(Exception): pass


# Nótese que para cualquier objeto que sea instancia de una subclase de la
# clase anterior, podemos calcular su rendimiento como clasificador, sobre un
# conjunto dado de ejemplos. Es lo que hace la siguiente función:

# Función general de rendimiento:

def rendimiento(clasificador,ejemplos):
    return sum([(clasificador.clasifica(ejemplo[:-1])==ejemplo[-1]) 
                for ejemplo in ejemplos])/len(ejemplos)

# En este marco de clasificadores que se ha presentado, encajan muchos de los
# métodos usados en el aprendizaje automático de clasificadores, definiendo de
# manera concreta el aprendizaje y la clasificación. Se pide definir en este
# marco general los dos clasificadores vistos en los apartados anteriores.
 

# Clases que se piden:
# ====================

# * Implementar la clase ClasificadorCobertura, como subclase de la clase
#   MetodoClasificacion anterior. En esta clase, los métodos son:
#   - Entrenamiento: algoritmo de aprendizaje de reglas de decisión por
#     cobertura.  
#   - Clasificación: clasificar con el conjunto de reglas de decisión
#     anterior. 
#   - Imprimir clasificador: imprimir el conjunto de reglas de decisión.
#   Además de los atributos de la clase genérica, se pueden incluir otros si
#   fuera necesario (por ejemplo, será necesario un atributo de la clase para
#   guardar el conjunto de reglas de decisión).  

# * Implementar la clase ClasificadorCoberturaPospoda, de manera análoga a la
#   anterior, pero en el que el entrenamiento consiste en aplicar cobertura,
#   seguido de una aplicación del algoritmo de pospoda. Cobertura se aplica
#   con el conjunto de entrenamiento y la poda con el conjunto de validación.



# Ejemplos:
# ---------

# Votos:
# ______


# >>> clasificador_cob_votos=ClasificadorCobertura(votos.atributo_clasificación,
#                                     votos.clases,
#                                     votos.atributos)
#
# >>> clasificador_cob_votos.entrena(votos.entr)
#
# >>> clasificador_cob_votos.clasifica(['n','s','n','s','s','s','n','n','n','s','?','s','s','s','n','s'])
# 'republicano'
#
#
# >>> rendimiento(clasificador_cob_votos,votos.valid)
# 0.9565217391304348
#
# >>> rendimiento(clasificador_cob_votos,votos.test)
# 0.9195402298850575
#
# >>> clasificador_cobpos_votos=ClasificadorCoberturaPospoda(votos.atributo_clasificación,
#                                     votos.clases,
#                                     votos.atributos)
#
# >>> clasificador_cobpos_votos.entrena(votos.entr,votos.valid)
#
# >>> rendimiento(clasificador_cobpos_votos,votos.test)
# 0.9080459770114943



# Concesión de crédito:
# _____________________


# >>> clasificador_cob_credito=ClasificadorCobertura(credito.atributo_clasificación,
#                                     credito.clases,
#                                     credito.atributos)
#
# >>> clasificador_cob_credito.entrena(credito.entr)
#
# >>> clasificador_cob_credito.clasifica(['funcionario','uno','dos o más','dos o más','soltero','altos','conceder'])
# 'conceder'
#
# >>> rendimiento(clasificador_cob_credito,credito.test)
# 0.8895705521472392
#
#
# >>> clasificador_cobpos_credito=ClasificadorCoberturaPospoda(credito.atributo_clasificación,
#                                     credito.clases,
#                                     credito.atributos)
#           
# >>> clasificador_cobpos_credito.entrena(credito.entr,credito.valid)
#
# >>> rendimiento(clasificador_cobpos_credito,credito.test)
# 0.9877300613496932



# ---------------------------------------------------------------------------
# PARTE 5: Entendiendo la supervivencia en el hundimiento del Titanic
# ---------------------------------------------------------------------------

# En este apartado, se pide usar los dos clasificadores anteriores para,
# a partir de los datos sobre pasajeros del Titanic (a descargar desde la
# página del trabajo), tratar de obtener un árbol de decisión para explicar la
# supervivencia o no de un pasajero del Titanic.

# Para ello, realizar los siguientes pasos:

# - Preprocesado de los datos: los datos están "en bruto", así que hay que
#   preparar los datos para que los puedan usar los clasificadores.
# - Aprendizaje y ajuste del modelo: aplicando a los datos los entrenamientos
#   de alguno de los clasificadores del apartado anterior.
# - Evaluacion del rendimiento del clasificador. 


# Damos a continuación algunos comentarios sobre la etapa del preprocesado de
# los datos:

# - En el conjunto de datos que se proporcionan hay una serie de atributos que
#   obviamente no influyen en la supervivencia (por ejemplo, el nombre del
#   pasajero). Esto hace que haya que seleccionar como atributos las
#   características que se crean realmente relevantes. Esto se suele
#   realizar con algunas técnicas estadísticas, pero en este trabajo sólo
#   vamos a pedir elegir (eligiendo razonablemente, o probando varias
#   alternativas) TRES ATRIBUTOS que se consideren son los que mejor
#   determinan la supervivencia o no.
# - El atributo "Edad" es numérico, y nuestra implementación no trata bien los
#   atributos con valores numéricos. Existen técnicas para tratar los
#   atributos numéricos, que básicamente dividen los posibles valores a tomar
#   en intervalos, de la mejor manera posible. En nuestro caso, por
#   simplificar, lo vamos a hacer directamente con el siguiente criterio:
#   transformar el valor EDAD en un valor binario, en el que sólo anotamos si
#   el pasajero tiene 13 AÑOS O MENOS, o si tiene MÁS DE 13 AÑOS.
# - En los datos, hay algunos valores de algunos ejemplos, que aparecen como
#   NA (desconocidos). Dos técnicas muy simples para tratar valores
#   desconocidos pueden ser: sustituir NA por el valor más frecuente de entre 
#   los ejemplos de la clase, o por la media aritmética de ese valor en los
#   ejemplos de la misma clase (esta última opción sólo tiene sentido con los
#   atributos numéricos).
# - Para realizar el entrenamiento, la poda y la medida del rendimiento, se
#   necesita dividir el conjunto de datos en tres partes: entrenamiento,
#   validación y test. Hay que decidir la proporción adecuada de datos que van
#   a cada parte. También hay que procurar además que la partición sea
#   estratificada: la proporción de los ejemplos según los distintos valores
#   de los atributos debe de ser en cada parte, similar a la proporción en el
#   total de ejemplos.   


# El resultado final de esta parte debe ser:

# * Un archivo titanic.py, con un formato análogo a los archivos de datos que
#   se han proporcionado (votos.py o credito.py, por ejemplo), en el que se
#   incluye el resultado del preprocesado de los datos en bruto.  

# * Un conjunto de reglas de decisión (el que mejor rendimiento obtenga
#   finalmente), en el que se explique la supervivencia o no de un pasajero en
#   el Titanic. Se pide explicar (mediante comentarios) todo el proceso
#   realizado hasta llegar a esas reglas de decisoón. Incluir este conjuto de
#   reglas decisión (como comentario al código) en el fichero titanic.py






