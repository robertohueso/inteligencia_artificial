# ==========================================================
# Inteligencia Artificial. Tercer curso. 
# Grado en Ingeniería Informática - Tecnologías Informáticas
# Curso 2016-17
# Entregable grupo 2. 
# Segunda entrega 
# ===========================================================


# Escribir el código Python de las funciones que se piden en el
# espacio que se indica en cada ejercicio.

# IMPORTANTE: NO CAMBIAR EL NOMBRE NI A ESTE ARCHIVO NI A LAS FUNCIONES QUE SE
# PIDEN (aquellas funciones con un nombre distinto al que se pide en el
# ejercicio NO se corregirán).

# ESTE ENTREGABLE SUPONE 0.4 PUNTOS DE LA NOTA TOTAL 

# *****************************************************************************
# HONESTIDAD ACADÉMICA Y COPIAS: la realización de los ejercicios es un
# trabajo personal, por lo que deben completarse por cada estudiante de manera
# individual.  La discusión con los compañeros y el intercambio de información 
# DE CARÁCTER GENERAL con los compañeros se permite, pero NO AL NIVEL DE
# CÓDIGO. Igualmente el remitir código de terceros, obtenido a través
# de la red o cualquier otro medio, se considerará plagio. 

# Cualquier plagio o compartición de código que se detecte significará
# automáticamente la calificación de CERO EN LA ASIGNATURA para TODOS los
# alumnos involucrados, independientemente de otras medidas de carácter 
# DISCIPLINARIO que se pudieran tomar. Por tanto a estos alumnos NO se les 
# conservará, para futuras convocatorias, ninguna nota que hubiesen obtenido
# hasta el momento. 
# *****************************************************************************


# ============================================================================
# En este entregable se pide completar la práctica 3 vista en
# clase. Concretamente los ejercicios 7, 8, 9 y 10, en los que 
# se pide terminar de implementar el algoritmo genético y definir el
# problema de la mochila representándolo para que pueda ser abordado por el
# algoritmo genético implementado. 
# ============================================================================  


# A continuación incluimos el código del algoritmo genético implementado en la
# práctica 3 (nótese que aún queda por implementar la función 
# nueva_generacion_t)



# ==========================================================================

import random

class Problema_Genetico(object):
    """ Clase para representar un problema para que sea abordado mediante un
    algoritmo genético general. Consta de los siguientes atributos:
    - genes: lista de posibles genes en un cromosoma
    - longitud_individuos: la longitud de los cromosomas
    - decodifica: método que recibe el fenotipo (cromosoma) y devuelve el
      fenotipo (elemento del problema original que el cromosoma representa) 
    - fitness: método de valoración de los cromosomas (actúa sobre el
      genotipo)
    - muta: función que realiza una mutación de un cromosoma
    - cruza: función que realiza un cruce entre dos cromosomas"""

    def __init__(self,genes,longitud_individuos,decodifica,fitness):
        self.genes= genes
        self.longitud_individuos= longitud_individuos
        self.decodifica= decodifica
        self.fitness= fitness

    def muta(self, c, prob):
        return [random.choice(self.genes) if random.random() < prob else g for g in c]
        

    def cruza(self,c1,c2):
        pos=random.randrange(1,self.longitud_individuos-1)
        cr1= c1[:pos] + c2[pos:] 
        cr2= c2[:pos] + c1[pos:] 
        return [cr1,cr2]

def poblacion_inicial(problema_genetico,tamaño):
    return [[random.choice(problema_genetico.genes) 
             for _ in range(problema_genetico.longitud_individuos)] 
             for _ in range(tamaño)]

def cruza_padres(problema_genetico,padres):
    hijos=[]
    for j in range(0,len(padres),2):
        hijos.extend(problema_genetico.cruza(*padres[j:j+2])) 
    return hijos

def muta_individuos(problema_genetico, poblacion, prob):
    return list(map(lambda x: problema_genetico.muta(x,prob),poblacion))

def selecciona_uno_por_torneo(problema_genetico, poblacion,k,opt):
    participantes=random.sample(poblacion,k)
    return opt(participantes, key=problema_genetico.fitness)

def seleccion_por_torneo(problema_genetico,poblacion,n,k,opt):
    return [selecciona_uno_por_torneo(problema_genetico,poblacion,k,opt) for _ in range(n)]




def algoritmo_genetico_t(problema_genetico,k,opt,ngen,tamaño,prop_cruces,prob_mutar):
    poblacion= poblacion_inicial(problema_genetico,tamaño)
    n_padres=round(tamaño*prop_cruces)
    n_padres= (n_padres if n_padres%2==0 else n_padres-1)
    n_directos= tamaño-n_padres

    for _ in range(ngen):
        poblacion= nueva_generacion_t(problema_genetico,k,opt,poblacion,n_padres,n_directos,prob_mutar)

    mejor_cr= opt(poblacion, key=problema_genetico.fitness)
    mejor=problema_genetico.decodifica(mejor_cr)
    return (mejor,problema_genetico.fitness(mejor_cr)) 

    
# ==================    

# Lo que sigue son los ejercicios que se piden en este entregable. Mantenemos
# la numeración como ejercicios dentro de la práctica 3.



# =======================

# ================================================
# Parte I: Implementación de un algoritmo genético 
# ================================================

# -----------
# Ejercicio 7
# -----------

# Se pide definir la única función auxiliar que queda por definir en el
# algoritmo anterior; es decir, la función
# nueva_generacion_t(problema_genetico,k,opt,poblacion,n_padres,n_directos,prob_mutar)
# que a partir de una población dada, calcula la siguiente generación.

# Una vez definida, ejecutar el algoritmo genético anterior, para resolver el
# problema cuad_gen (tanto en minimización como en maximización).

# Por ejemplo:

# >>> algoritmo_genetico_t(cuad_gen,3,min,20,10,0.7,0.1)
# (0, 0)
# >>> algoritmo_genetico_t(cuad_gen,3,max,20,10,0.7,0.1)
# (1023, 1046529)

# NOTA: téngase en cuenta que el algoritmo genético devuelve un par con el
# mejor fenotipo encontrado, y su valoración.

# ========== Solución:
def nueva_generacion_t(problema_genetico,k,opt,poblacion,n_padres,n_directos,prob_mutar):
    padres = seleccion_por_torneo(problema_genetico, poblacion, n_padres, k, opt)
    hijos = cruza_padres(problema_genetico, padres)
    mutacion = muta_individuos(problema_genetico, hijos, prob_mutar)
    return mutacion

#Funciones extra para el problema cuad_gen
def decod_cuad(x):
    string = ''
    for i in x:
        string += str(i)
    return int(string, 2)

def fit_cuad(x):
    return decod_cuad(x)**2

#Solucion
cuad_gen = Problema_Genetico([0,1], 10, decod_cuad, fit_cuad)
sol_cuad_max = algoritmo_genetico_t(cuad_gen,3,max,20,10,0.7,0.1)
sol_cuad_min = algoritmo_genetico_t(cuad_gen,3,min,20,10,0.7,0.1)
print("Cuad Max: " + str(sol_cuad_max))
print("Cuad Min: " + str(sol_cuad_min))

# ===================================================
# Parte II: Representación del problema de la mochila
# ===================================================


# Problema de la mochila: dados n objetos de pesos p_i y valor v_i
# (i=1,...,n), seleccionar cuáles se meten en una mochila que soporta un
# peso P máximo, de manera que se máximice el valor de los objetos
# introducidos. 

# En las dispositivas 46 y 47 del tema 5, se explica cómo se puede representar
# este problema para ser abordado por un algoritmo genético. En esta parte se
# pide implementar esa representación.


# -----------
# Ejercicio 8
# -----------

# Definir una función 
# decodifica_mochila(cromosoma, n_objetos, pesos, capacidad)
# que recibe como entrada:

# - un cromosoma (en este caso, una lista de 0s y 1s, de longitud igual a
#   n_objetos) 
# - n_objetos: número total de objetos de la mochila
# - pesos: una lista con los pesos de los objetos
# - capacidad: peso máximo de la mochila.

# Tal y como se explica en las mencionadas diapositivas del tema 6, esta
# función debe devolver una lista de 0s y 1s que indique qué objetos están en
# la mochila y cuáles no (el objeto i está en la mochila si y sólo si en la
# posición i-ésima de la lista hay un 1). Esta lista se obtendrá a partir del
# cromosoma, pero teniendo en cuenta que a partir del primer objeto que no
# quepa, éste y los siguientes se consideran fuera de la mochila,
# independientemente del valor que haya en su correspondiente posición de
# cromosoma.  


# ========== Solución:

def decodifica_mochila(cromosoma, n_objetos, pesos, capacidad):
    peso_acumulado = 0
    lista_valores = []
    for i in range(len(cromosoma)):
        if cromosoma[i] == 1 and peso_acumulado + pesos[i] <= capacidad:
            lista_valores.append(1)
            peso_acumulado += pesos[i]
        else:
            lista_valores.append(0)
    return lista_valores

# ==============================================


# -----------
# Ejercicio 9
# -----------

# Definir una función 

# fitness_mochila(cromosoma, n_objetos, pesos, capacidad, valores)

# que devuelva el valor total de los objetos que están dentro de la mochila
# que representa el cromosma, según la codificación explicada en el ejercicio
# anterior. Aquí valores es la lista de los valores de cada objeto y el resto
# de argumentos son los mismos que en el ejercicio anterior.

# ============== Solución:

def fitness_mochila(cromosoma, n_objetos, pesos, capacidad, valores):
    valor_actual = 0
    lista = decodifica_mochila(cromosoma, n_objetos, pesos, capacidad)
    for i in range(len(lista)):
        if lista[i] == 1:
            valor_actual += valores[i]
    return valor_actual


# ===============================================



# ============================================================
# Parte III: Resolviendo instancias del problema de la mochila
# ============================================================


# Damos aquí tres instancias concretas del problema de la mochila. Damos
# también sus soluciones optimas, para que se puedan comparar con los
# resultados obtenidos por el algoritmo genético:

# _______________________________________________________
# Problema de la mochila 1:
# 10 objetos, peso máximo 165
pesos1 = [23,31,29,44,53,38,63,85,89,82]
valores1 = [92,57,49,68,60,43,67,84,87,72]

# Solución óptima= [1,1,1,1,0,1,0,0,0,0], con valor 309
# _______________________________________________________

# _______________________________________________________
# Problema de la mochila 2:
# 15 objetos, peso máximo 750

pesos2 = [70,73,77,80,82,87,90,94,98,106,110,113,115,118,120]
valores2 = [135,139,149,150,156,163,173,184,192,201,210,214,221,229,240]

# Solución óptima= [1,0,1,0,1,0,1,1,1,0,0,0,0,1,1] con valor 1458
# _______________________________________________________


# _______________________________________________________
# Problema de la mochila 3:
# 24 objetos, peso máximo 6404180
pesos3 = [382745,799601,909247,729069,467902, 44328,
       34610,698150,823460,903959,853665,551830,610856,
       670702,488960,951111,323046,446298,931161, 31385,496951,264724,224916,169684]
valores3 = [825594,1677009,1676628,1523970, 943972,  97426,
       69666,1296457,1679693,1902996,
       1844992,1049289,1252836,1319836, 953277,2067538, 675367,
       853655,1826027, 65731, 901489, 577243, 466257, 369261]

# Solución óptima= [1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1] con valoración 13549094

# _______________________________________________________


# ------------
# Ejercicio 10
# ------------

# Definir variables m1g, m2g y m3g, referenciando a instancias de
# Problema_Genetico que correspondan, respectivamente, a los problemas de la
# mochila anteriores.

# Usar el algoritmo genético anterior para resolver estos problemas.

# Por ejemplo:

# >>> algoritmo_genetico_t(m1g,3,max,100,50,0.8,0.05)
# ([1, 1, 1, 1, 0, 1, 0, 0, 0, 0], 309)

# >>> algoritmo_genetico_t(m2g,3,max,100,50,0.8,0.05)
# ([1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0], 1444)
# >>> algoritmo_genetico_t(m2g,3,max,200,100,0.8,0.05)
# ([0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0], 1439)
# >>> algoritmo_genetico_t(m2g,3,max,200,100,0.8,0.05)
# ([1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1], 1458)

# >>> algoritmo_genetico_t(m3g,5,max,400,200,0.75,0.1)
# ([1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 13518963)
# >>> algoritmo_genetico_t(m3g,4,max,600,200,0.75,0.1)
# ([1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], 13524340)
# >>> algoritmo_genetico_t(m3g,4,max,1000,200,0.75,0.1)
# ([1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 13449995)
# >>> algoritmo_genetico_t(m3g,3,max,1000,100,0.75,0.1)
# ([1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 13412953)
# >>> algoritmo_genetico_t(m3g,3,max,2000,100,0.75,0.1)
# ([0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 13366296)
# >>> algoritmo_genetico_t(m3g,6,max,2000,100,0.75,0.1)
# ([1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1], 13549094)



# =========== Solución:

#Fitness casos particulares
def fit1(cromosoma):
    return fitness_mochila(cromosoma, 10, pesos1, 165, valores1)

def fit2(cromosoma):
    return fitness_mochila(cromosoma, 15, pesos2, 750, valores2)

def fit3(cromosoma):
    return fitness_mochila(cromosoma, 24, pesos3, 6404180, valores3)

#Decodificar casos particulares
def decod1(cromosoma):
    return decodifica_mochila(cromosoma, 10, pesos1, 165)

def decod2(cromosoma):
    return decodifica_mochila(cromosoma, 15, pesos2, 750)

def decod3(cromosoma):
    return decodifica_mochila(cromosoma, 24, pesos3, 6404180)

#Resolucion del problema
m1g = Problema_Genetico([0,1], len(pesos1), decod1, fit1)
m2g = Problema_Genetico([0,1], len(pesos2), decod2, fit2)
m3g = Problema_Genetico([0,1], len(pesos3), decod3, fit3)

sol_mochila1 = algoritmo_genetico_t(m1g, 3, max, 100, 50, 0.8, 0.05)
sol_mochila2 = algoritmo_genetico_t(m2g, 3, max, 200, 100, 0.8, 0.05)
sol_mochila3 = algoritmo_genetico_t(m3g, 3, max, 400, 150, 0.75, 0.1)

print("Solucion mochila 1: " + str(sol_mochila1))
print("Solucion mochila 2: " + str(sol_mochila2))
print("Solucion mochila 3: " + str(sol_mochila3))

#Por Roberto Hueso Gomez.

# ===================================

