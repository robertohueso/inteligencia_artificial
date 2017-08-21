# ==========================================================
# Inteligencia Artificial. Tercer curso. 
# Grado en Ingeniería Informática - Tecnologías Informáticas
# Curso 2016-17
# Segundo entrega (evaluación final)
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




# *****************************************************************************
# Este ejercicio está inspirado en uno de los "The Pac-Man Projects"; en
# concreto el primero de esos proyectos, dedicado a búsqueda en espacio de
# estados. Estos proyectos han sido desarrollados en la UC Berkely para su
# curso CS188 de Introducción a la Inteligencia Artificial
# (http://inst.eecs.berkeley.edu/~cs188/pacman/)
# *****************************************************************************



# ========================
# DESCRIPCIÓN DEL PROBLEMA
# ========================

# Se pide resolver, mediante técnicas de búsqueda en espacio de estados, el
# llamado problema de "cuatro esquinas en el laberinto". En este problema
# recibimos como entrada un laberinto rectangular, formado por una rejilla de
# casillas, algunas de ellas ocupadas por un obstáculo. Inicialmente, en una
# de las casillas libres hay situado un robot (que llamaremos PacMan) que
# puede moverse de casilla en casilla, con cuatro posibles tipos de
# movimientos: arriba, abajo, izquierda y derecha; por supuesto, sólo puede
# moverse a casillas sin obstáculos. El objetivo es encontrar una secuencia de
# movimientos para PacMan de manera que en su recorrido visite las casillas
# correspondientes a las cuatro esqunas del laberinto (que supondremos
# libres).

# Por ejemplo, un laberinto podría ser algo así, siendo "P" la posición de
# PacMan y "*" las casillas con obstáculo: 

# ********
# *      *
# *   P  *
# * **** *
# * *    *
# * * ****
# * *    *
# ********

# Una posible solución sería:

# Izquierda -> Izquierda -> Izquierda -> Abajo -> Abajo -> Abajo -> Abajo 
# -> Arriba -> Arriba -> Arriba -> Arriba -> Arriba -> Derecha -> Derecha 
# -> Derecha -> Derecha -> Derecha -> Abajo -> Abajo -> Abajo -> Izquierda 
# -> Izquierda -> Izquierda -> Abajo -> Abajo -> Derecha -> Derecha -> Derecha']


# =================================
# LECTURA DE LABERINTOS EN FICHEROS
# =================================


# Los ficheros laberintox.txt, con x=1,...,5, contienen una representación
# gráfica de cinco laberintos de ejemplo. Estos ficheros de texto contienen
# una primera línea con las dimensiones del laberinto (en la dimensión no
# contamos los bordes del laberinto) y en las siguientes líneas se incluye la
# representación gráfica.

# La siguiente función auxiliar se puede usar para leer un laberinto de un
# fichero y cargar toda la información en una estructura de datos:


def lee_laberinto(fichero):
    """Lee de un fichero de texto en el que está representado
       el laberinto y devuelve una tupla (dim,mat,pos) donde:
       - dim es una tupla (n,m) donde n es el número de filas del laberinto 
         y m el número de columnas (sin contar los bordes). 
       - mat es una matriz nxm (en forma de lista de listas) en la que su
         componente mat[i][j] es 0 si en la casilla (i,j) no hay obstáculo 
         y 1 si hay obstáculo.
       - pos es una tupla (x,y) con las coordenadas de la posición inicial de
         PacMan (las coordenadas empiezan a contar en el 0)"""    
   
    with open(fichero) as entrada:
        cabecera=entrada.readline().split()
        nfils,ncols=int(cabecera[0]),int(cabecera[1])
        next(entrada)
        laberinto=[[0 for _ in range(ncols)]  for _ in range(nfils)]
        for f in range(nfils):
            linea=entrada.readline()[1:]
            for c in range(ncols):
                if linea[c]=="*":
                    laberinto[f][c]=1
                elif linea[c]=="P":
                    pos_pacman=(f,c)
    return ((nfils,ncols),laberinto,pos_pacman)

# Ejemplo de uso (en laberinto1.txt está el laberinto del ejemplo anterior):

# >>> lab1=lee_laberinto("laberinto1.txt")
# >>> lab1
# ((6, 6), 
#  [[0, 0, 0, 0, 0, 0], 
#   [0, 0, 0, 0, 0, 0], 
#   [0, 1, 1, 1, 1, 0], 
#   [0, 1, 0, 0, 0, 0], 
#   [0, 1, 0, 1, 1, 1], 
#   [0, 1, 0, 0, 0, 0]], 
#  (1, 3))

# Nótese que la estructura de datos que usamos para almacenar un laberinto es
# una tupla (una terna) con: la dimensión, la matriz que representa los huecos
# y obstáculos, y la posición inicial de PacMan. 


# =================================
# PROBLEMAS DE ESPACIOS DE ESTADOS
# =================================


# La siguiente clase es una descripción general de un problema de espacio de
# estados, tal y como se ha visto en la Práctica 2:

class Problema(object):
    """Clase abstracta para un problema de espacio de estados. Los problemas
    concretos habría que definirlos como subclases de Problema, implementando
    acciones, aplica y eventualmente __init__, es_estado_final y
    coste_de_aplicar_accion. Una vez hecho esto, se han de crear instancias de
    dicha subclase, que serán la entrada a los distintos algoritmos de
    resolución mediante búsqueda."""  


    def __init__(self, estado_inicial, estado_final=None):
        """El constructor de la clase especifica el estado inicial y
        puede que un estado_final, si es que es único. Las subclases podrían
        añadir otros argumentos"""
        
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final

    def acciones(self, estado):
        """Devuelve las acciones aplicables a un estado dado. Lo normal es
        que aquí se devuelva una lista, pero si hay muchas se podría devolver
        un iterador, ya que sería más eficiente."""
        abstract

    def aplica(self, estado, accion):
        """ Devuelve el estado resultante de aplicar accion a estado. Se
        supone que accion es aplicable a estado (es decir, debe ser una de las
        acciones de self.acciones(estado)."""
        abstract

    def es_estado_final(self, estado):
        """Devuelve True cuando estado es final. Por defecto, compara con el
        estado final, si éste se hubiera especificado al constructor. Si se da
        el caso de que no hubiera un único estado final, o se definiera
        mediante otro tipo de comprobación, habría que redefinir este método
        en la subclase.""" 
        return estado == self.estado_final

    def coste_de_aplicar_accion(self, estado, accion):
        """Devuelve el coste de aplicar accion a estado. Por defecto, este
        coste es 1. Reimplementar si el problema define otro coste """ 
        return 1

# ========
# SE PIDE:
# ========

# -----------------------------------------------------------------------------
# (1)

# Implementar una clase Laberinto_Cuatro_Esquinas (¡ojo, con ese nombre!), que
# represente el problema de "cuatro esquinas en el laberinto"
# Esta clase DEBE SER SUBCLASE de la clase Problema y  su constructor recibe
# como argumento una estructura de las que se obtienen al leer el laberinto de
# un fichero (por ejemplo, como la variable lab1 del ejemplo anterior).    
# --------------------------------------------------------------------------

class Laberinto_Cuatro_Esquinas(Problema):
    
    class Movimientos():
        ARRIBA = (-1, 0)
        ABAJO = (1, 0)
        IZQUIERDA = (0, -1)
        DERECHA = (0, 1)

    def tupla(self, estado):
        nuevo_estado = (tuple(estado[0]),
                        tuple(tuple(x) for x in estado[1]),
                        tuple(estado[2]))
        return nuevo_estado

    def lista(self, estado):
        nuevo_estado = [list(estado[0]),
                        list(list(x) for x in estado[1]),
                        list(estado[2])]
        return nuevo_estado
        
    def __init__(self, laberinto):
        estado_inicial = self.tupla(laberinto)
        self.tamano = estado_inicial[0]
        tam_ajust = (self.tamano[0] - 1, self.tamano[1] - 1)
        super().__init__(estado_inicial)
        e_final_gen = self.lista(estado_inicial)
        e_final_gen[1][0][0] = 2
        e_final_gen[1][0][tam_ajust[1]] = 2
        e_final_gen[1][tam_ajust[0]][0] = 2
        e_final_gen[1][tam_ajust[0]][tam_ajust[1]] = 2
        self.estado_final = [list(e_final_gen) for i in range(4)]
        self.estado_final[0][2] = [0, 0]
        self.estado_final[1][2] = [0, tam_ajust[1]]
        self.estado_final[2][2] = [tam_ajust[0], tam_ajust[1]]
        self.estado_final[3][2] = [tam_ajust[0], 0]
        self.estado_final = set(self.tupla(estado) for estado in self.estado_final)

    def acciones(self, estado):
        acciones = []
        tam = estado[0]
        lab = estado[1]
        pos = estado[2]
        #Comprueba que no haya muro
        def comprobar_uno(accion):
            nueva_pos = tuple(sum(x) for x in zip(pos, accion))
            return lab[nueva_pos[0]][nueva_pos[1]] == 1
        #Aniade acciones
        acciones.append(self.Movimientos.ARRIBA)
        acciones.append(self.Movimientos.ABAJO)
        acciones.append(self.Movimientos.IZQUIERDA)
        acciones.append(self.Movimientos.DERECHA)
        #Comprobamos bordes y entornos
        if pos[0] == 0 or comprobar_uno(self.Movimientos.ARRIBA):
            acciones.remove(self.Movimientos.ARRIBA)
        if pos[0] == self.tamano[0] - 1 or comprobar_uno(self.Movimientos.ABAJO):
            acciones.remove(self.Movimientos.ABAJO)
        if pos[1] == 0 or comprobar_uno(self.Movimientos.IZQUIERDA):
            acciones.remove(self.Movimientos.IZQUIERDA)
        if pos[1] == self.tamano[1] - 1 or comprobar_uno(self.Movimientos.DERECHA):
            acciones.remove(self.Movimientos.DERECHA)
        return tuple(acciones)

    def aplica(self, estado, accion):
        n_estado = self.lista(estado)
        pos = [sum(x) for x in zip(n_estado[2], accion)]
        n_estado[2] = pos
        if pos == [0, 0]:
            n_estado[1][0][0] = 2
        elif pos == [0, self.tamano[1] - 1]:
            n_estado[1][0][self.tamano[1] - 1] = 2
        elif pos == [self.tamano[0] - 1, 0]:
            n_estado[1][self.tamano[0] - 1][0] = 2
        elif pos == [self.tamano[0] - 1, self.tamano[1] - 1]:
            n_estado[1][self.tamano[0] - 1][self.tamano[1] - 1] = 2
        return self.tupla(n_estado)
    
    def es_estado_final(self, estado):
        if estado in self.estado_final:
            return True
        else:
            return False

# -----------------------------------------------------------------------------
# (2)

# Definir dos heurísticas, al menos una de ellas admisible para este
# problema. Las dos funciones heurísticas deben de llamarse, respectivamente
# h1_cuatro_esquinas y h2_cuatro_esquinas  (¡ojo, con esos nombres!)
# --------------------------------------------------------------------------

def h1_cuatro_esquinas(estado):
    
    def distancia(posicion, esquina):
        return sum(abs(a - b) for a, b in zip(posicion, esquina))
    
    pos = estado[2]
    esquinas = [[0, 0],
                [0, estado[0][1] - 1],
                [estado[0][0] - 1, 0],
                [estado[0][0] - 1, estado[0][1] - 1]]
    return min(distancia(pos, esq) for esq in esquinas)



# -----------------------------------------------------------------------------
# (3)


# Probar la implementación buscando soluciones a los distintos laberintos de
# los ejemplos, usando para ello las implementaciones de los distintos
# algoritmos de búsqueda que se han proporcionado como fichero auxiliar en la
# práctica 2.

# IMPORTANTE:
# * Se valorará que las soluciones obtenidas sean de longitud mínima y
#   que se encuentren analizando cuantos menos nodos mejor. 
# * No incluir las soluciones encontradas en el archivo que se entregue, ya
#   que éstas serán obtenidas ejecutando la implementación que se entregue. 



# ================
# Ejemplos de uso:
# ================

# >>> busqueda_en_profundidad(p1).solucion() 
# ['Derecha', 'Derecha', 'Abajo',
# 'Abajo', 'Izquierda', 'Izquierda', 'Izquierda', 'Abajo', 'Abajo', 'Derecha',
# 'Derecha', 'Derecha', 'Izquierda', 'Izquierda', 'Izquierda', 'Arriba',
# 'Arriba', 'Derecha', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Izquierda',
# 'Izquierda', 'Izquierda', 'Izquierda', 'Izquierda', 'Abajo', 'Abajo', 'Abajo',
# 'Abajo', 'Arriba', 'Arriba', 'Arriba', 'Arriba', 'Derecha', 'Derecha',
# 'Derecha', 'Derecha', 'Derecha', 'Arriba', 'Izquierda', 'Izquierda',
# 'Izquierda', 'Izquierda', 'Izquierda']

# >>> busqueda_a_estrella(p1,h1_cuatro_esquinas).solucion()
# ['Izquierda', 'Izquierda', 'Izquierda', 'Abajo', 'Abajo', 'Abajo', 'Abajo',
# 'Arriba', 'Arriba', 'Arriba', 'Arriba', 'Arriba', 'Derecha', 'Derecha',
# 'Derecha', 'Derecha', 'Derecha', 'Abajo', 'Abajo', 'Abajo', 'Izquierda',
# 'Izquierda', 'Izquierda', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Derecha']

# Para calcular longitud de la solcuión encontrada y número de nodos analizados:

# >>> len(busqueda_en_profundidad(p1e).solucion())
# 46
# >>> p1e.analizados
# 57
# >>> p1e=Problema_con_Analizados(p1)
# >>> len(busqueda_a_estrella(p1e,h1_cuatro_esquinas).solucion())
# 28
# >>> p1e.analizados
# 195
def pp_resultado(resultado):
    for accion in resultado:
        if accion == (-1, 0):
            print('Arriba')
        elif accion == (1, 0):
            print('Abajo')
        elif accion == (0, -1):
            print('Izquierda')
        elif accion == (0, 1):
            print('Derecha')

from algoritmos_de_busqueda import búsqueda_en_profundidad
from algoritmos_de_busqueda import búsqueda_a_estrella

lab1 = lee_laberinto('laberinto1.txt')

p1 = Laberinto_Cuatro_Esquinas(lab1)
busqueda = búsqueda_a_estrella(p1, h1_cuatro_esquinas)
pp_resultado(busqueda.solucion())
print(len(busqueda.solucion()))
