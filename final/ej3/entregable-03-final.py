# ==========================================================
# Inteligencia Artificial. Tercer curso. 
# Grado en Ingeniería Informática - Tecnologías Informáticas
# Curso 2016-17
# Entregable grupo 3. 
# Tercera entrega (evaluación final)
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




# ==========
# Enunciado:
# ==========

# Se pide definir en python una función
# inferencia_enumeracion(var,observado,red), que implementa el algoritmo de
# inferencia por enumeración que se describe en las diapositivas 62 y 63 del
# tema 6.

# Esta función recibe como argumentos de entrada un variable var de consulta,
# un diccionario con las observaciones, y una red bayesiana.

# Las redes se representan mediante una estructura python que se explica más
# abajo, junto con algunas redes de ejemplos (son la misma estructura y
# ejemplos que se usaron en la práctica 4 que se hizo durante el curso).


# Estos son algunos ejemplos de resultados obtenidos con la función que se
# pide:

# >>> inferencia_enumeracion("robo",{"juanllama":True,"mariallama":True},red_alarma)
# {False: 0.7158281646356071, True: 0.2841718353643929}
# >>> inferencia_enumeracion("robo",{"juanllama":False,"mariallama":True},red_alarma)
# {False: 0.993123753926579, True: 0.006876246073421025}
# >>> inferencia_enumeracion("terremoto",{"juanllama":True,"mariallama":False},red_alarma)
# {False: 0.9954613599992471, True: 0.0045386400007529125}
# >>> inferencia_enumeracion("fumador",{"infarto":False,"deportista":True},red_infarto)
# {False: 0.7217365088935784, True: 0.2782634911064215}
# >>> inferencia_enumeracion("fumador",{"infarto":True,"deportista":True},red_infarto)
# {False: 0.46232526423457204, True: 0.537674735765428}
# >>> inferencia_enumeracion("hierba mojada",{"nublado":True},red_aspersor)
# {False: 0.2548, True: 0.7452000000000001}
# >>> inferencia_enumeracion("Sistema Combustible OK",
#                                     {"Antigüedad Batería":"vieja",
#                                      "Alternador OK":True, 
#                                      "Filtro de Aire Limpio":False,
#                                      "Coche Arranca":False},
#                                     red_arranque_coche)
# ... 
# {False: 0.13227454785058085, True: 0.8677254521494192}
# >>> inferencia_enumeracion("Sistema Combustible OK",
#                                     {"Antigüedad Batería":"muy_vieja",
#                                      "Alternador OK":True, 
#                                      "Filtro de Aire Limpio":True,
#                                      "Coche Arranca":False},
#                                     red_arranque_coche)
# ... 
# {False: 0.21034735344677868, True: 0.7896526465532213}
# >>> inferencia_enumeracion("Motor de Arranque OK",
#                                     {"Antigüedad Batería":"muy_vieja",
#                                      "Alternador OK":True, 
#                                      "Filtro de Aire Limpio":True,
#                                      "Coche Arranca":False},
#                                     red_arranque_coche)
# ... 
# {False: 0.016827788275742293, True: 0.9831722117242577}


# =========== Solución

def inferencia_enumeracion(var,observado,red):
    #Variables
    distribucion = {}
    
    #Funciones auxiliares
    def normaliza(distribucion):
        suma = sum(distribucion.values())
        for valor, probabilidad in distribucion.items():
            distribucion[valor] = probabilidad / suma
        return distribucion

    def variables(red):
        #Devuelve los nodos en orden de arriba a abajo
        lista = []
        red = red[1]
        nodos = list(red.keys())
        lista = list(nodo for nodo in nodos if len(red[nodo]) == 0)
        for nodo in lista:
            nodos.remove(nodo)
        while len(nodos) > 0:
            for nodo in nodos:
                padres = red[nodo]
                if set(padres) <= set(lista) and (nodo not in lista):
                    lista.append(nodo)
                    nodos.remove(nodo)
        lista.reverse()
        return lista

    def p(variable, valor, observado):
        posicion = red[0][variable].index(valor)
        padres = red[1][variable]
        valores_padres = [observado[padre] for padre in padres]
        valores_padres = tuple(valores_padres)
        probabilidad = red[2][variable][valores_padres][posicion]
        return probabilidad

    def enum_aux(variables, observado, red):
        if len(variables) == 0:
            return 1
        variables = list(variables)
        y = variables.pop()
        if y in observado:
            return p(y, observado[y], observado) * enum_aux(variables, observado, red)
        else:
            suma = 0
            for v_y in red[0][y]:
                nuevo_observado = dict(observado)
                nuevo_observado[y] = v_y
                suma += p(y, v_y, observado) * enum_aux(variables, nuevo_observado, red)
            return suma

    #Algoritmo
    for valor in red[0][var]:
        observado[var] = valor
        distribucion[valor] = enum_aux(variables(red), observado, red)
    return normaliza(distribucion)

# ==========================

# ------------------------------------------------------------------------------------


# Representación de redes bayesianas para el entregable 3 (y ejemplos)
# ====================================================================


# Usaremos una estructura de datos prefijada, para representar redes
# bayesianas. Por ejemplo, la siguiente variable red_alarma contiene la
# representación de la red bayesiana del ejemplo de la alarma visto en clase:

red_alarma=[{"robo":[True,False],
             "terremoto":[True,False],
             "alarma":[True,False],
             "juanllama":[True,False],
             "mariallama":[True,False]},
             
             {"robo":[],
              "terremoto":[],
              "alarma":["robo","terremoto"],
              "juanllama":["alarma"],
              "mariallama":["alarma"]},
              
             {"robo":{():[0.001,0.999]},
              "terremoto":{():[0.002,0.998]},
              "alarma":{(True,True):[0.95,0.05],
                        (True,False):[0.94,0.06],
                        (False,True):[0.29,0.71],
                        (False,False):[0.001,0.999]},
              "juanllama":{(True,):[0.9,0.1],
                           (False,):[0.05,0.95]},
              "mariallama":{(True,):[0.7,0.3],
                            (False,):[0.01,0.99]}}]


# En general, una red bayesiana se representará mediante una lista de tres
# elementos. Cada uno de estos elementos representará:

# 1. Las variables aleatorias y sus posibles valores: un diccionario que asocia
#    que asocia cada nombre de variable con una lista de sus posible valores. 
# 2. Los padres de cada variable en la red: un diccionario que asocia a cada
#    nombre de variable con una lista de sus padres. 
# 3. Las tablas de probabilidad de cada nodo: un diccionario que asocia a cada
#    nombre de variable su tabla de probabilidad. A su vez, la tabla asociada
#    a cada variable X es un diccionario que asocia a cada combinación de
#    valores de los padres, la distribución de probabilidad de X dada esa
#    combinación de valores. 
#
#    Por ejemplo, si en la tabla de "alarma" hay una correspondencia  
#    (True,False):[0.94,0.06], 
#    quiere decir que:
#    P(alarma=True|Robo=True,Terremoto=False)=0.94, y que     
#    P(alarma=False|Robo=True,Terremoto=False)=0.06.
#
#    Nótese que el orden implícito de los valores de una variable, y de
#    sus padres, es el que está definido en los correspondientes
#    diccionarios. 

# Lo que sigue son otras dos redes que también se han mostrado en clase de
# teoría: 

red_infarto=[{"deportista":[True,False],
              "alimentación_equilibrada":[True,False],
              "hipertenso":[True,False],
              "fumador":[True,False],
              "infarto":[True,False]},
              
              {"deportista":[],
               "alimentación_equilibrada":[],
               "hipertenso":["deportista","alimentación_equilibrada"],
               "fumador":[],
               "infarto":["hipertenso","fumador"]},
               
               {"deportista":{():[0.1,0.9]},
                "alimentación_equilibrada":{():[0.4,0.6]},
                "hipertenso":{(True,True):[0.01,0.99],
                              (True,False):[0.25,0.75],
                              (False,True):[0.2,0.8],
                              (False,False):[0.7,0.3]},
                "fumador":{():[0.4,0.6]},
                "infarto":{(True,True):[0.8,0.2],
                           (True,False):[0.7,0.3],
                           (False,True):[0.6,0.4],
                           (False,False):[0.3,0.7]}}]

red_aspersor=[{"hierba mojada":[True,False],
               "lluvia":[True,False],
               "nublado":[True,False],
               "aspersor":[True,False]},

               {"nublado":[],
               "aspersor":["nublado"],
               "lluvia":["nublado"],
               "hierba mojada":["aspersor","lluvia"]},

               {"nublado":{():[0.5,0.5]},
                "aspersor":{(True,):[0.1,0.9],
                            (False,):[0.5,0.5]},
                "lluvia":{(True,):[0.8,0.2],
                          (False,):[0.2,0.8]},
                "hierba mojada":{(True,True):[0.99,0.01],
                                 (True,False):[0.9,0.1],
                                 (False,True):[0.9,0.1],
                                 (False,False):[0.0,1.0]}}]

# Finalmente, la siguiente red es un traducción al castellano de la red "Car
# Starting Problem" del "applet" de redes bayesianas de AISpace:

red_arranque_coche=[{"Alternador OK":[True,False],
                     "Sistema de Carga OK":[True,False],	
                     "Antigüedad Batería":["nueva", "vieja", "muy_vieja"],	
                     "Voltaje Batería":["fuerte", "débil", "nada"],	
                     "Fusible OK":[True,False],
                     "Distribuidor OK":[True,False],
                     "Voltaje en Conexión":["fuerte", "débil", "nada"],
                     "Motor de Arranque OK":[True,False],
                     "Sistema de Arranque OK":[True,False],
                     "Faros":["brillante", "dim", "apagado"],
                     "Bujías":["okay", "holgada", "anulada"],
                     "Coche Maniobra":[True,False],
                     "Tiempo de Encendido":["bien", "mal", "muy_mal"],
                     "Sistema Combustible OK":[True,False],
                     "Filtro de Aire Limpio":[True,False],
                     "Sistema de Aire OK":[True,False],
                     "Coche Arranca":[True,False],
                     "Calidad Bujías":["bien", "mal", "muy_mal"],
                     "Bujías Adecuadas":[True,False]},
                     
			   {"Alternador OK":[],
			   "Sistema de Carga OK":["Alternador OK"],	
             		   "Antigüedad Batería":[],	
             		   "Voltaje Batería":["Sistema de Carga OK", "Antigüedad Batería"],	
             		   "Fusible OK":[],
             		   "Distribuidor OK":[],
             		   "Voltaje en Conexión":["Voltaje Batería", "Fusible OK", "Distribuidor OK"],
             		   "Motor de Arranque OK":[],
             		   "Sistema de Arranque OK":["Voltaje Batería", "Fusible OK", "Motor de Arranque OK"],
             		   "Faros":["Voltaje en Conexión"],
             		   "Bujías":[],
             		   "Coche Maniobra":["Sistema de Arranque OK"],
             		   "Tiempo de Encendido":["Distribuidor OK"],
             		   "Sistema Combustible OK":[],
             		   "Filtro de Aire Limpio":[],
             		   "Sistema de Aire OK":["Filtro de Aire Limpio"],
             		   "Coche Arranca":["Coche Maniobra", "Sistema Combustible OK", 
                                        "Sistema de Aire OK", "Bujías Adecuadas"],
             		   "Calidad Bujías":["Voltaje en Conexión", "Bujías"],
             		   "Bujías Adecuadas":["Tiempo de Encendido", "Calidad Bujías"]},


			   {"Alternador OK":{():[0.9997,0.0003]},
			   "Sistema de Carga OK":{(True,):[0.995, 0.005],
                                      (False,):[0.0, 1.0]},	
             		   "Antigüedad Batería":{():[0.4, 0.4, 0.2]},	
             		   "Voltaje Batería":{(True,"nueva"):[0.999, 0.0008, 0.0002],
                                          (True,"vieja"):[0.99, 0.008, 0.002],
                                          (True,"muy_vieja"):[0.6, 0.3, 0.1],		      
                                          (False,"nueva"):[0.8, 0.15, 0.05],
                                          (False,"vieja"):[0.05, 0.3, 0.65],
                                          (False,"muy_vieja"):[0.002, 0.1, 0.898]},	
             		   "Fusible OK":{():[0.999, 0.001]}, 
             		   "Distribuidor OK":{():[0.99, 0.01]},
             		   "Voltaje en Conexión":{("fuerte", True, True):[0.98, 0.015, 0.005],
                                              ("fuerte", True, False):[0.0, 0.0, 1.0],
                                              ("fuerte", False, True):[0.0, 0.0, 1.0],
                                              ("fuerte", False, False):[0.0, 0.0, 1.0],
                                              ("débil", True, True):[0.1, 0.8, 0.1],
                                              ("débil", True, False):[0.0, 0.0, 1.0],
                                              ("débil", False, True):[0.0, 0.0, 1.0],
                                              ("débil", False, False):[0.0, 0.0, 1.0],
                                              ("nada", True, True):[0.0, 0.0, 1.0],
                                              ("nada", True, False):[0.0, 0.0, 1.0],
                                              ("nada", False, True):[0.0, 0.0, 1.0],
                                              ("nada", False, False):[0.0, 0.0, 1.0]},
             		   "Motor de Arranque OK":{():[0.992, 0.008]},
             		   "Sistema de Arranque OK":{("fuerte", True, True):[ 0.998, 0.002],
                                                 ("fuerte", True, False):[ 0.0, 1.0],
                                                 ("fuerte", False, True):[ 0.0, 1.0],
                                                 ("fuerte", False, False):[ 0.0, 1.0],
                                                 ("débil", True, True):[ 0.72, 0.28],
                                                 ("débil", True, False):[ 0.0, 1.0],
                                                 ("débil", False, True):[ 0.0, 1.0],
                                                 ("débil", False, False):[ 0.0, 1.0],
                                                 ("nada", True, True):[ 0.0, 1.0],
                                                 ("nada", True, False):[ 0.0, 1.0],
                                                 ("nada", False, True):[ 0.0, 1.0],
                                                 ("nada", False, False):[ 0.0, 1.0]},
             		   "Faros":{("fuerte",):[0.98, 0.015, 0.005],
                                ("débil",):[0.05, 0.9, 0.05],
                                ("nada",):[0.0, 0.0, 1.0]},
             		   "Bujías":{():[0.99, 0.003, 0.007]},
             		   "Coche Maniobra":{(True,):[0.98, 0.02],
                                         (False,):[0.0, 1.0]},
             		   "Tiempo de Encendido":{(True,):[0.97, 0.02, 0.01],
                                              (False,):[0.2, 0.3, 0.5]},
             		   "Sistema Combustible OK":{():[0.9, 0.1]},
             		   "Filtro de Aire Limpio":{():[0.9, 0.1]},
             		   "Sistema de Aire OK":{(True,):[0.9, 0.1],
                                             (False,):[0.3, 0.7]},
             		   "Coche Arranca":{  (True, True, True, True):[ 1.0, 0.0],
                                          (True, True, True, False):[ 0.0, 1.0],
                                          (True, True, False, True):[ 0.0, 1.0],
                                          (True, True, False, False):[ 0.0, 1.0],
                                          (True, False, True, True):[ 0.0, 1.0],
                                          (True, False, True, False):[ 0.0, 1.0],
                                          (True, False, False, True):[ 0.0, 1.0],
                                          (True, False, False, False):[ 0.0, 1.0],
                                          (False, True, True, True):[ 0.0, 1.0],
                                          (False, True, True, False):[ 0.0, 1.0],
                                          (False, True, False, True):[ 0.0, 1.0],
                                          (False, True, False, False):[ 0.0, 1.0],
                                          (False, False, True, True):[ 0.0, 1.0],
                                          (False, False, True, False):[ 0.0, 1.0],
                                          (False, False, False, True):[ 0.0, 1.0],
                                          (False, False, False, False):[ 0.0, 1.0]},
             		   "Calidad Bujías":{("fuerte", "okay"):[ 1.0, 0.0, 0.0],
                                         ("fuerte", "holgada"):[ 0.0, 1.0, 0.0],
                                         ("fuerte", "anulada"):[ 0.0, 0.0, 1.0],
                                         ("débil", "okay"):[ 0.0, 1.0, 0.0],
                                         ("débil", "holgada"):[ 0.0, 0.5, 0.5],
                                         ("débil", "anulada"):[ 0.0, 0.2, 0.8],
                                         ("nada", "okay"):[ 0.0, 0.0, 1.0],
                                         ("nada", "holgada"):[ 0.0, 0.0, 1.0],
                                         ("nada", "anulada"):[ 0.0, 0.0, 1.0]},
             		   "Bujías Adecuadas":{("bien", "bien"):[ 0.99, 0.01],
                                           ("bien", "mal"):[ 0.5, 0.5],
                                           ("bien", "muy_mal"):[ 0.1, 0.9],
                                           ("mal", "bien"):[ 0.5, 0.5],
                                           ("mal", "mal"):[ 0.05, 0.95],
                                           ("mal", "muy_mal"):[ 0.01, 0.99],
                                           ("muy_mal", "bien"):[ 0.1, 0.9],
                                           ("muy_mal", "mal"):[ 0.01, 0.99],
                                           ("muy_mal", "muy_mal"):[ 0.0, 1.0]}}]
