# ==========================================================
# Inteligencia Artificial. Tercer curso. 
# Grado en Ingeniería Informática - Tecnologías Informáticas
# Curso 2016-17
# Entregable grupo 2. 
# Primera entrega (evaluación final)
# ===========================================================


# Escribir el código Python de las funciones que se piden en el
# espacio que se indica en cada ejercicio.

# IMPORTANTE: NO CAMBIAR EL NOMBRE NI A ESTE ARCHIVO NI A LAS FUNCIONES QUE SE
# PIDEN (aquellas funciones con un nombre distinto al que se pide en el
# ejercicio NO se corregirán).

# ESTE ENTREGABLE SUPONE 0.5 PUNTOS DE LA NOTA TOTAL 

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



# ---------------------------------------------------------------------------
# EJERCICIO 1)
# Supongamos una mesa redonda en la que hay sentadas n personas, numeradas del
# 0 al n-1, en el sentido de las agujas del reloj. Dado un número entero
# positivo q, diremos que una persona está "q-conectada" con otra, si
# desde uno se puede llegar al otro contando de q en q. Por ejemplo, si en la
# mesa hay 9 personas, el 1 está 3-conectado con el 7, ya que 1--> 4 --> 7
# Sin embargo, el 2 no está 3-conectado con el 1, pero sí que está
# 4-conectado, ya que 2 --> 6 --> 1. 

# Definir una función conectados_n_q(n,q) que devuelve las listas de
# q-conectados entre sí, en una mesa redonda con n personas.
#
# Ejemplos:
#
# >>> conectados_n_q(9,3)
# [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
# >>> conectados_n_q(9,4)
# [[0, 4, 8, 3, 7, 2, 6, 1, 5]]
# >>> conectados_n_q(8,2)
# [[0, 2, 4, 6], [1, 3, 5, 7]]
# >>> conectados_n_q(12,8)
# [[0, 8, 4], [1, 9, 5], [2, 10, 6], [3, 11, 7]]
# -----------------------------------------------------------------------------


def conectados_n_q(n, q):
    listas = list()
    personas = list(range(n))
    it = 0
    while any(personas):
        nueva_lista = [personas[it]]
        personas[it] = False
        while True:
            nueva_persona = (nueva_lista[-1] + q) % n
            if nueva_lista[0] == nueva_persona:
                break
            nueva_lista.append(personas[nueva_persona])
            personas[nueva_persona] = False
        listas.append(nueva_lista)
        it += 1
    return listas


# -----------------------------------------------------------------------------
# EJERCICIO 2)

# Decimos que el elemento a_ij de una matriz numérica cuadrada a, es un punto
# de silla si es el máximo de los elementos de la fila i y el mínimo de los
# elementos de la columna j.  Es posible probar que una matriz cuyos elementos
# son todos distintos tiene a lo sumo un único punto de silla.  Definir una
# función silla(a) que recibiendo como entrada una matriz a con números
# distintos (representada mediante la lista de sus filas, y cada fila también
# como una lista), devuelva la tupla (i, j) tal que el elemento a_ij es un
# punto de silla de a. Devolver False si la matriz no tiene puntos de silla.

# Ejemplos:

# >>> punto_de_silla([[1,2,3],[4,5,6],[7,8,9]])
# (0, 2)
# >>> punto_de_silla([[11,12],[14,9]])
# False
# >>> punto_de_silla([[1,4,3,2],[9,8,7,6],[5,10,11,13],[12,14,15,16]])
# (0, 1)
# -------------------------------------------------------------------------










# ---------------------------------------------------------------------------
# EJERCICIO 3)

# Definir una función ciclo(g), que dado un grafo dirigido g, devuelva un camino
# cíclico en ese grafo, si hay tal. Si no existen ciclos en el grafo, debe
# devolver False. Entendemos por "camino cíclico", un camino en el grafo
# que empieza y acaba en el mismo nodo. Si existen varios caminos cíclicos,
# la función sólo debe devolver uno de ellos.  
# El grafo que recibe como entrada vendrá dado mediante un diccionario que
# asigna a cada nodo la lista de nodos con los que está conectado. 

# Ejemplos:
# >>> grafo1={"a":["b"],"b":["c","e"],"c":["f"],"d":["a"],"e":["c","f","g"],"f":["d","g"],"g":[]}
# >>> ciclo(grafo1)
# ['f', 'd', 'a', 'b', 'c', 'f']
# >>> grafo2={"a":["b","d"],"b":["c","e"],"c":["f"],"d":[],"e":["c","f","g"],"f":["d","g"],"g":[]}
# >>> ciclo(grafo2)
# False
# >>> grafo3={"a":["b","d"],"b":["c","e"],"c":["f"],"d":[],"e":["c","f"],"f":["d","g"],"g":["e"]}
# >>> ciclo(grafo3)
# ['g', 'e', 'c', 'f', 'g']
# ----------------------------------------------------------------------------

