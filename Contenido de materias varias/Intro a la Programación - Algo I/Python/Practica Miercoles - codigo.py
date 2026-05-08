############################## Ej1.1 ##############################

def imprimir_hola_mundo():
    print("Hola mundo")
    
def imprimir_hola_mundo_alternativo(): # Cumple la especificación? Sí :)
    print("Hola mundo")
    while True:
        pass
    
############################## Ej1.5 ##############################

def perimetro():
    return 2 * 3.14159265358979323846

import math
def perimetro_alternativo(): # Mejor esta versión en un trabajo real
    return 2 * math.pi

############################## Ej2 ##############################

def es_multiplo_de(n: int, m: int) -> bool:
    return n % m == 0

############################## Ej3 ##############################

def es_nombre_largo(nombre: str) -> bool:
    # return 3 <= len(nombre) and len(nombre) <= 8
    return 3 <= len(nombre) <= 8 # Alternativa más compacta

############################## Ej5 ##############################

def devolver_el_doble_si_es_par(un_numero: int) -> int: 
    if un_numero % 2 == 0:
        return un_numero * 2
    return un_numero

def devolver_el_doble_si_es_par_alternativo(un_numero: int) -> int:
    if un_numero % 2 == 0:
        un_numero = un_numero * 2
    return un_numero 

# Ambas alternativas son válidas. Es muy 'de juguete' el ejemplo preferir una. 
# No tiene nada de malo a priori usar más de un return, hay casos donde es más claro y casos que no.

############################## Ej6.2 ##############################

def ej_6_2():
    actual: int = 10
    while actual <= 40:
        print(actual)
        actual += 2 # también se puede ir sumando 1 y preguntando con un if si imprimir o no, está es más corta
        
def ej_6_2_alternativa_con_for():
    for i in range(10, 40+1, 2): # notar que el 'hasta' es no inclusivo!
        print(i)
        
############################## Ej6.3 ##############################

def ej_6_4(numero: int):
    while numero >= 1:
        print(numero)
        numero -= 1
    print('Despegue')
    
def ej_6_4_alternativa_con_for(numero: int):
    for i in range(numero, 0, -1): # Vamos 'incrementando -1' hasta llegar al 0
        print(i)
    print('Despegue')
    
############################## Ej7 ##############################

# Ya lo metimos en el anterior

############################## Ej8 ##############################

def ejemploReturn(xArgumento: int) -> int:
    print("En ejemploReturn: ", xArgumento)
    xArgumento = xArgumento + 40
    return xArgumento

def ejemploVarGlobal():
    global xGlobal
    print("En ejemploVarGlobal: ", xGlobal)
    xGlobal = xGlobal + 30
    
"""
xGlobal: int = 1
xGlobal = ejemploReturn(xGlobal)
print("En codigo libre: ", xGlobal)
ejemploVarGlobal()
print("En codigo libre: ", xGlobal)
xGlobal = ejemploReturn(xGlobal)
print("En codigo libre: ", xGlobal)
ejemploVarGlobal()
print("En codigo libre: ", xGlobal)
"""
