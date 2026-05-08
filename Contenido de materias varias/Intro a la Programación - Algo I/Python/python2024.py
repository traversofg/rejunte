from random import randint
from math import floor

"""                       ¡¡     RESUELTO DE CHARLY      !!   


          Primeros pasos:
          1. Hacemos nuestro archivo con las funciones (python2024.py )
          2. Abrimos el compilador interactivo ( python o python3 , ver
          version)
          3. Importamos el archivo con nuestras funciones (import python2024)
          4. Las usamos interactivamente (python2024.<nombre funcion>)
          5. Para recargar el archivo hay que cerrar el intérprete (exit())
          y volver a empezar

            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣬⠷⣶⡖⠲⡄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠸⣿⡀⠀⡁⠈⠙⠢⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠉⠣⠬⢧⠀⠀⠀⠀⠈⠻⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⢀⡴⠃⠀⠀⢠⣴⣿⡿⠀⠀⠀⠐⠋⠀⠀⠀⠀⠀⠀⠘⠿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⢀⡴⠋⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠒⠓⠛⠓⠶⠶⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⢠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀
            ⡞⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢷⡄⠀⠀⠀⠀⠀⠀
            ⢻⣇⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀
            ⠀⠻⣟⠋⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀
            ⠀⠀⠀⠉⠓⠒⠊⠉⠉⢸⡙⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠘⣆⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⠀⠀⢻⡄⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⣧⡀⠀⠀⢀⡄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠇⠀⠀⠀⠀⠀⠀⢣⠀

                    """ 
print("            -----------------------------------------------------------------      ")        
print("           |              1 : Recorrido y busqueda en secuencias             |     ")          
print("            -----------------------------------------------------------------      ")         

# Ejercicio 1. Codificar en Python las siguientes funciones sobre secuencias:

# 1   -----------------------------------------------------------------------------
# Entrada (in): al salir de la funcion o procedimiento, la variable
# pasada como parametro continuara teniendo su valor original.
# nota: no utilizar la funcion sum() nativa

def pertenece(ls: list[int], e: int) -> bool:
    # True <-> 0 ≤ i < |s| ∧ s[i] = e
    # verdadero si lo que esta en la posision i de esa lista coincide con e 
    for x in ls:
        if x == e:
            return True
    return False

print ( "test-ejercicio1 valor verdadero: True", pertenece([1,3,4],1))
print ( "test-ejercicio1 valor verdadero: True", pertenece([1],1))
print ( "test-ejercicio1 valor verdadero: True", pertenece([7,3,1],1))

def pertenece_2(ls: [int], e: int) -> bool:
    #cuando usas el while es muy probable que necesites de un contador para incrementar en este caso i 

    indice_actual: int = 0
    longitud: int = len(ls)
    pertenece: bool = False
    # arranca en 0 , si arrancara en 1 seria <= len (s) , si arranca en 1 hay que tener cuidado en la posicion
    # si el tamaño es 3 -> la secuencia es 0 1 2 y corta
    # lo que va comparando el elemento con lo que esta en el indice ls[0], ls[1], ls[2]
    while (indice_actual < longitud):
        if (e == ls[indice_actual]): # solo entra al if si es la condicion verdadera
            pertenece = True # en el caso que nunca entre al if porque no encuentra una igualdad 
                            # retorna el valor inicial que era false
        indice_actual = indice_actual + 1
    return pertenece

print ( "test-ejercicio1 valor : False | valor calculado: ",pertenece_2([7,3,4],1))
print ( "test-ejercicio1 valor : True | valor calculado", pertenece_2([7,3,1],1))

print ( "--------------------------------------------------------------------")
# 2 -----------------------------------------------------------------------------

def divide_a_todos(ls: list[int], e: int) -> bool:
    # e nunca es cero (osea que puede ser negativo o positivo)
    # no dice nada de la lista asi que puede ser vacia, en ese caso es True
    # True <-> para todo i ∈ Z si 0 ≤ i < |s|→ s[i] mod e = 0
    # verdadero si lo que esta en la posision i de esa lista es divisor de e 
    for n in ls: 
        if n % e != 0: # este seria el mod en python (recordar que es par si mod n 2 == 0 en este casa n % 2 ==0)
            print (n) # lo puse para ver en la terminal cuando corta y printea el n donde freno la ejecucion
            return False
    return True

print ( "test-ejercicio2 valor : True | valor calculado: ",divide_a_todos([7,3,4],-1))
print ( "test-ejercicio2 valor : True | valor calculado: ", divide_a_todos([8,4,4],2))
print ( "test-ejercicio2 valor : False | valor calculado: ", divide_a_todos([4,2,9,6],2))
print ( "test-ejercicio2 valor : False | valor calculado: ", divide_a_todos([2,11,4,6],2))
print ( "test-ejercicio2 valor : True | valor calculado: ", divide_a_todos([],2))

# la diferencia entre las dos propuestas es que el for corta cuando cumple la condicion del if 
# en cambio el while recorre toda la lista hasta completar el tamaño de ls 

def divide_a_todos_2(s: [int], e: int) -> bool: 
    indice_actual: int = 0
    longitud: int = len(s)
    divide_a_todos: bool = True
    # es importante que indice_actual arranque en cero porque esta relacionado su incremento con
    # la posicion en una lista y no es lo mismo ls[0] que ls[1]
    # el incremento seria ls[0], ls[1], ls[2] y corta cuando es igual al tamaño
    while (indice_actual < longitud):
        if (s[indice_actual] % e != 0):
            divide_a_todos = False # cambio de estado
        indice_actual = indice_actual + 1

    return divide_a_todos

print ( "test-ejercicio2 valor : True | valor calculado: ",divide_a_todos_2([7,3,4],-1))
print ( "test-ejercicio2 valor : True | valor calculado: ", divide_a_todos_2([7,3,1],1))
print ( "test-ejercicio2 valor : False | valor calculado: ", divide_a_todos_2([7,3,1],8))
print ( "test-ejercicio2 valor : False | valor calculado: ", divide_a_todos_2([7,3,1],2))
print ( "test-ejercicio2 valor : True | valor calculado: ", divide_a_todos_2([],2))

print ( "--------------------------------------------------------------------")
# 3 -----------------------------------------------------------------------------

def suma_total(ls: list[int]) -> int:
    #requiere dice true, asi que puede ser una lista vacia, tambien le podemos pasar numeros positivos y negativos
    suma_total: int = 0
    # el for pasa por toda la lista y a cada elemento lo va sumando a la variable suma_total
    for i in ls:
        suma_total += i # aca no hay un if o algo que me frene el proceso por lo que recorre todo ls

    return suma_total
print ( "test-ejercicio3 valor : 11 | valor calculado: ", suma_total([7,3,1]))
print ( "test-ejercicio3 valor : 0 | valor calculado: ", suma_total([]))
print ( "test-ejercicio3 valor : 5 | valor calculado: ", suma_total([7,-3,1]))

print ( "--------------------------------------------------------------------")

def suma_total_2 (s: [int]) -> int:
    total: int = 0
    indice_actual: int = 0
    longitud: int = len(s)
    #arranca el while con indice_actual=0 y total =0 
    #valor_actual = s[0]
    # total = 0 + valor_actual
    # indice_actual cambia a +1
    #valor_actual = s[1]
    # total = total + valor_actual
    # indice_actual cambia a +1 y asi sucesivamente
    while (indice_actual < longitud):
        valor_actual: int = s[indice_actual] # a cada valor que agarre de la lista lo guarda en la variable
        total = total + valor_actual #suma el valor que agarra a lo que vale total en ese momento
        indice_actual += 1
    
    return total
print ( "test-ejercicio3 valor : 11 | valor calculado: ", suma_total_2([7,3,1]))
print ( "test-ejercicio3 valor : 0 | valor calculado: ", suma_total_2([]))
print ( "test-ejercicio3 valor : 5 | valor calculado: ", suma_total_2([7,-3,1]))

print ( "--------------------------------------------------------------------")
# 4 -----------------------------------------------------------------------------
def maximo(ls: list[int]) -> int:
    # el requiere te dice que no te van a pasar una lista de tamaño 0 
    # no dice nada sobre si los elementos son positivos o negativo asi que pueden pertenecer a la lista
    # Supone que el primer elemento es el máximo
    max_val = ls[0]
    
    # Recorrer la lista desde el segundo elemento
    #for i in range(1,n) -> [1,2,n]
    for i in range(1, len(ls)):
        if ls[i] > max_val:
            max_val = ls[i] #no hay return asi que termina todo el for
    
    return max_val # max_val va cambiando durante toda la iteracion
print ( "test-ejercicio4 valor : 3 | valor calculado: ", maximo([-7,3,1]))
print ( "test-ejercicio4 valor : 2 | valor calculado: ", maximo([2]))
print ( "test-ejercicio4 valor : 7 | valor calculado: ", maximo([7,-3,1]))

print ( "--------------------------------------------------------------------")
# 5 -----------------------------------------------------------------------------
def minimo (ls: list[int]) -> int:
    min_val = ls[0]
    for i in range(1, len(ls)):
        if ls[i] < min_val:
            min_val = ls[i]
    
    return min_val

print ( "test-ejercicio5 valor : -7 | valor calculado: ", minimo([-7,3,1]))
print ( "test-ejercicio5 valor : 2 | valor calculado: ", minimo([2]))
print ( "test-ejercicio5 valor : -3 | valor calculado: ", minimo([7,-3,1]))

print ( "--------------------------------------------------------------------")
# 6 -----------------------------------------------------------------------------
def ordenados(ls: list[int]) -> bool:
    # True <-> para todo i ∈ Zs i 0 ≤ i < (|s|−1) → s[i] < s[i+1]
    # arranca en s[0] hasta s[n-1]
    # verdadero <-> [1,3,9]
    # solo devuelve falso si cumple que no esta ordenado
    # ordenado aca significa que no necesariamente tiene que ser consecutivo 
    for i in range(len(ls) - 1):
        if ls[i] > ls[i+1]:
            return False
    return True

print ( "test-ejercicio6 valor : True | valor calculado: ", ordenados([-7,1,11]))
print ( "test-ejercicio6 valor : True | valor calculado: ", ordenados([2]))
print ( "test-ejercicio6 valor : False | valor calculado: ", ordenados([7,-3,1]))


def ordenados_2(s:[int]) -> bool:
    ordenados: bool = True
    indice: int = 0
    longitud: int = len(s)

    while (indice + 1 < longitud):
        for numero in s:
            if (s[indice] > s[indice + 1]):
                ordenados = False
        indice = indice + 1
    
    return ordenados

print ( "test-ejercicio6 valor : True | valor calculado: ", ordenados_2([-7,1,11]))
print ( "test-ejercicio6 valor : True | valor calculado: ", ordenados_2([2]))
print ( "test-ejercicio6 valor : False | valor calculado: ", ordenados_2([7,-3,1]))

print ( "--------------------------------------------------------------------")
# 7 -----------------------------------------------------------------------------
def pos_maximo (ls: list[int]) -> int:
    # como es true el require, puede ser vacio, con positivos y negativos
    # (Si |s|= 0, entonces res = −1; si no, res = al ́ındice de la posicion 
    # donde aparece el mayor elemento de s
    # si hay varios es la primera aparicion
    # tener en cuenta que arranca a contar en pos 0 1 2 3 ....
    tamaño: int=len(ls) 
    pos_max_val = 0
    if tamaño==0 : #si no tiene elementos entra aca
        return -1 
    else: # si hay minimo un elemento entra
        max_val = ls[0]
        for i in range(1, len(ls)):
            if ls[i] > max_val:
                max_val = ls[i] #no hay return asi que termina todo el for
                pos_max_val=i
        return pos_max_val
    
print ( "test-ejercicio 7 valor : 2 | valor calculado: ", pos_maximo([-7,1,11,8]))
print ( "test-ejercicio 7 valor : 0 | valor calculado: ", pos_maximo([2]))
print ( "test-ejercicio 7 valor : -1 | valor calculado: ", pos_maximo([]))
print ( "test-ejercicio 7 valor : 4 | valor calculado: ", pos_maximo([7,-3,1,2,10]))
print ( "test-ejercicio 7 valor : 0 | valor calculado: ", pos_maximo([7,-3,1,2]))

print ( "--------------------------------------------------------------------")
# 8-----------------------------------------------------------------------------

def pos_minimo(ls: list[int]) -> int:
    pos_min_val = 0

    if not ls:  # truco: Manejo de lista vacía, si es vacia ls es false , not false es true
        return -1
    else:
        min_val = ls[0]
        for i in range(1, len(ls)):
            if ls[i] < min_val:
                min_val = ls[i]
                pos_min_val=i
        
        return pos_min_val
print ( "test-ejercicio 8 valor : 2 | valor calculado: ", pos_minimo([1,11,-7]))
print ( "test-ejercicio 8 valor : 0 | valor calculado: ", pos_minimo([2]))
print ( "test-ejercicio 8 valor : -1 | valor calculado: ", pos_minimo([]))
print ( "test-ejercicio 8 valor : 1 | valor calculado: ", pos_minimo([7,-3,1]))

print ( "--------------------------------------------------------------------")

# 9 -----------------------------------------------------------------------------
def tiene_palabra_larga(palabras: list[str]) -> bool:
    # devolver verdadero si alguna palabra tiene longitud mayor a 7
    for palabra in palabras:
        if len(palabra) > 7:
            return True # si encuentra una que sea mayor a 7 corta el programa y retorna true
    return False # sino corta antes, llega a finalizar el ciclo for y devuelve false

print ( "test-ejercicio 9 valor : True | valor calculado: ", tiene_palabra_larga(["hola","jujuy y salta", "sol"]))
print ( "test-ejercicio 9 valor : False | valor calculado: ", tiene_palabra_larga([]))
print ( "test-ejercicio 9 valor : False | valor calculado: ", tiene_palabra_larga(["",""]))
print ( "test-ejercicio 9 valor : False | valor calculado: ", tiene_palabra_larga(["s","tengoTt"]))

# 10 -----------------------------------------------------------------------------
def palindromo(texto: str) -> bool:
    # se lee igual en ambos sentidos
    # las cadenas de texto vacıas o con 1 solo elemento son palındromo
    # no creo que se pueda usar texto[-1] para acceder al ultimo elemento
    i = 0
    j = len(texto) - 1  # Índice del último carácter   

    if len(texto) <= 1:
        return True

    while i < j:
        if texto[i] != texto[j]:
            return False
        i += 1
        j -= 1  # Decrementar j para moverse hacia el principio
    return True

print ( "test-ejercicio 10 valor : False | valor calculado: ", palindromo(" tengo sueño"))
print ( "test-ejercicio 10 valor : True | valor calculado: ", palindromo(""))
print ( "test-ejercicio 10 valor : True | valor calculado: ", palindromo("    "))
print ( "test-ejercicio 10 valor : False | valor calculado: ", palindromo("charly"))
print ( "test-ejercicio 10 valor : True | valor calculado: ", palindromo("holaaloh"))
print ( "test-ejercicio 10 valor : True | valor calculado: ", palindromo("oso"))

def palindromo_3(palabra: str) -> bool:
    palindromo: bool = True
    
    for i in range(0,len(palabra),1):
        if palabra[i] != palabra[len(palabra)-1-i]:
            palindromo = False
    return palindromo

def palindromo_4(texto: str) -> bool:
    i: int = 0

    while i < floor(len(texto) / 2):
        if texto[i] != texto[-i-1]:
            return False
        i += 1
    return True

print ( "--------------------------------------------------------------------")
# 11 -----------------------------------------------------------------------------

def tres_consecutivos_iguales(lista: list[int]) -> bool:
    # True <-> si hay 3 numeros iguales consecutivos
    # Recorrer la lista, pero sin llegar a los últimos dos elementos
    for i in range(len(lista) - 2):
        if lista[i] == lista[i + 1] == lista[i + 2]:
            return True
    return False

print ( "test-ejercicio 11 valor : False | valor calculado: ", tres_consecutivos_iguales([2,5,3,8]))
print ( "test-ejercicio 11 valor : True | valor calculado: ", tres_consecutivos_iguales([2,5,6,7,11,11,11]))
print ( "test-ejercicio 11 valor : True | valor calculado: ", tres_consecutivos_iguales([1,1,2,2,3,4,4,4,5,5,5]))
print ( "test-ejercicio 11 valor : True | valor calculado: ", tres_consecutivos_iguales([1,3,5,5,5,5,7,1]))
print ( "test-ejercicio 11 valor : False | valor calculado: ", tres_consecutivos_iguales([8,7,5,9,1]))
print ( "test-ejercicio 11 valor : False | valor calculado: ", tres_consecutivos_iguales([]))

print ( "--------------------------------------------------------------------")
# 12 -----------------------------------------------------------------------------
def tres_vocales_distintas(palabra: str) -> bool:
    #tiene al menos 3 vocales, osea 3, 4 y 5
    vocales: list[str] = ["a","e","i","o","u","A","E","I","O","U"]
    cant_vocales: int=0
    for c in palabra:
        if  pertenece(c,vocales):
            cant_vocales += 1
            vocales = eliminar_elemento(c,vocales)
    return cant_vocales >= 3

def pertenece(elem: str, lista: list[str]) -> bool:
    res: bool = False
    for x in lista:
        if x == elem:
            res = True
    return res

def eliminar_elemento (elem: str, lista: list[str])-> list[str]:
    lista_nueva: list[str]=[]
    for x in lista:
        if x != elem:
            lista_nueva.append(x)
    return lista_nueva


print ( "test-ejercicio 12 valor : True | valor calculado: ", tres_vocales_distintas("aeiou"))
print ( "test-ejercicio 12 valor : False | valor calculado: ", tres_vocales_distintas("aaa"))
print ( "test-ejercicio 12 valor : False | valor calculado: ", tres_vocales_distintas("afagee"))
print ( "test-ejercicio 12 valor : True | valor calculado: ", tres_vocales_distintas("charlie"))
print ( "test-ejercicio 12 valor : False | valor calculado: ", tres_vocales_distintas(""))
print ( "test-ejercicio 12 valor : True | valor calculado: ", tres_vocales_distintas("osoagemo"))

print ( "--------------------------------------------------------------------")
# 13 -----------------------------------------------------------------------------
def secuencia_mas_larga(s: [int]) -> int:
    # devolver la posicion donde empieza la primera secuencia mas larga ordenada crecientemente 

    """                               Variables Iniciales
    ● pos: Guarda la posición inicial de la subsecuencia más larga encontrada. Inicialmente se asigna 0.
    ● conteo: Cuenta la longitud de la subsecuencia creciente actual. Empieza en 1, porque cada elemento individual 
    cuenta como una subsecuencia de longitud 1.
    ● mas_larga: Almacena la longitud de la subsecuencia creciente más larga encontrada hasta el momento.Inicialmente se asigna 0.
    ● i: Índice actual dentro de la lista.
    Comienza en 0 y se incrementa dentro del bucle.
    ● tamaño: Almacena el tamaño de la lista s para evitar recalcularlo. Se calcula al inicio con len(s).

    """

    pos: int = 0
    conteo: int = 1
    mas_larga: int = 0
    i: int = 0
    tamaño: int = len(s)
    # arranca en 0 hasta len-1
    while i < (tamaño - 1):
        """El bucle recorre la lista desde el primer elemento (i = 0) hasta el penúltimo (i < tamaño - 1).
            Condición: if s[i] < s[i + 1]
                Verifica si el elemento actual s[i] es menor que el siguiente s[i + 1].
                    Acciones:
                    Incrementa el contador conteo en 1, porque la secuencia sigue siendo creciente."""
        if s[i] < s[i + 1]:
            conteo += 1
            """Condición: else (cuando s[i] >= s[i + 1])
               Significa que la secuencia creciente actual ha terminado.
                    Acciones:
                    Verifica si la longitud de la subsecuencia actual (conteo) es mayor que la longitud de la subsecuencia más larga encontrada (mas_larga):
                        Si es mayor:
                        Actualiza mas_larga con el valor de conteo.
                        Calcula la posición inicial de la subsecuencia como i - conteo + 1 y la asigna a pos.
                    Reinicia el contador conteo a 1 para la próxima subsecuencia.
                Incrementa i en 1 para continuar con el siguiente elemento."""
        else:
            if conteo > mas_larga:
                mas_larga = conteo
                pos = i - conteo + 1
            conteo = 1
        i += 1
    """Comprobación Final
    Después de salir del bucle, es posible que la subsecuencia creciente más larga termine justo al final de la lista. Esta última subsecuencia no se compara dentro del bucle, así que se hace una verificación final:
    Condición: if conteo > mas_larga
        Si la longitud de la última subsecuencia (conteo) es mayor que mas_larga:
        Actualiza la posición inicial pos con el índice de inicio de esta subsecuencia: tamaño - conteo."""
    if conteo > mas_larga:
        pos = tamaño - conteo

    return pos

print ( "test-ejercicio 13 valor : 2 | valor calculado: ", secuencia_mas_larga([2,5,3,4,8,11,10,9,8,7,6,5,4,3,2]))
print ( "test-ejercicio 13 valor : 1 | valor calculado: ", secuencia_mas_larga([8,3,5,2]))
print ( "test-ejercicio 13 valor : 6 | valor calculado: ", secuencia_mas_larga([2,5,6,7,5,3,2,11,12,13,14]))
print ( "test-ejercicio 13 valor : 6 | valor calculado: ", secuencia_mas_larga([2,5,6,7,5,3,2,11,12,13,14,15]))
print ( "test-ejercicio 13 valor : 0 | valor calculado: ", secuencia_mas_larga([1]))
print ( "test-ejercicio 13 valor : -1 | valor calculado: ", secuencia_mas_larga([]))

print ( "--------------------------------------------------------------------")
# 14 -----------------------------------------------------------------------------
def cantidad_digitos_impares(ls: list[int]) -> int:
    # requieree dice que los numerosson mayores o iguales a 0
    cant_impar = 0

    # Recorrer cada número en la lista
    for numero in ls:
        # Revisar cada dígito del número
        while numero > 0:
            digito = numero % 10 #me voy quedando con el resto que es el ultimo digito de numero
            # Verificar si el dígito es impar
            if digito % 2 != 0:
                cant_impar += 1
            # Eliminar el último dígito
            numero //= 10 # ahora numero no tiene su ultimo digito

    return cant_impar

print ( "test-ejercicio 14 valor : 5 | valor calculado: ", cantidad_digitos_impares([57, 2383, 812, 246]))
print ( "test-ejercicio 14 valor : 0 | valor calculado: ", cantidad_digitos_impares([]))
print ( "test-ejercicio 14 valor : 10 | valor calculado: ", cantidad_digitos_impares([2,5,6,7,5,3,2,11,12,13,14]))
print ( "test-ejercicio 14 valor : 0 | valor calculado: ", cantidad_digitos_impares([242,248,240]))
print ( "test-ejercicio 14 valor : 1 | valor calculado: ", cantidad_digitos_impares([1]))
print ( "test-ejercicio 14 valor : 15 | valor calculado: ", cantidad_digitos_impares([13579,13579,13579]))

print ("          ----------------------------------------------------------------------------   ")
print ("         |      2:  Recorrido: filtrando, modificando y procesando secuencias         |  ")
print ("          ----------------------------------------------------------------------------   ")
"""
NOTA:    ● Entrada y salida (inout): al salir de la funcion o procedimiento, la
variable pasada como parametro tendra un nuevo valor asignado
dentro de dicha funcion o procedimiento. Su valor inicial SI importa
dentro de la funcion o procedimiento en cuestion
         ● Entrada (in): al salir de la funcion o procedimiento, la variable
        pasada como parametro continuara teniendo su valor original.

# Ejercicio 2. Implementar las siguientes funciones sobre secuencias pasadas por parametro:
"""
# 1 -----------------------------------------------------------------------------

def CerosEnPosicionesPares(ls: list[int]) -> list[int]:
    # requiere: True (la lista puede ser vacía, contener números negativos o positivos)
    # entrada: inout (modifica la lista original)
    # asegura: |s| = |s@pre| y, para todo i: si i es impar, s[i] = s@pre[i]; si i es par, s[i] = 0
    
    for i in range(len(ls)):  # Iterar sobre todos los índices
        if i % 2 != 0:  # Si el índice es par
            ls[i] = 0  # Sustituir por 0
    return ls

print ( "test-ejercicio 2.1 valor : [-4, 0, 812, 0] | valor calculado: ", CerosEnPosicionesPares([-4, 2383, 812, 246]))
print ( "test-ejercicio 2.1 valor : [] | valor calculado: ", CerosEnPosicionesPares([]))
print ( "test-ejercicio 2.1 valor : [2,0,6,0,5,0,2,0,12,0,14] | valor calculado: ", CerosEnPosicionesPares([2,5,6,7,5,3,2,11,12,13,14]))
print ( "test-ejercicio 2.1 valor : [242,0,240] | valor calculado: ", CerosEnPosicionesPares([242,248,240]))

print ( "--------------------------------------------------------------------")
# 2 -----------------------------------------------------------------------------
def CerosEnPosicionesPares2 (ls: list[int]) -> list[int]:
    #entrada in
    new_list: list[int] = ls.copy()
    CerosEnPosicionesPares(new_list)
    return new_list

print ( "test-ejercicio 2.2 valor : [-4, 0, 812, 0] | valor calculado: ", CerosEnPosicionesPares([-4, 2383, 812, 246]))
print ( "test-ejercicio 2.2 valor : [] | valor calculado: ", CerosEnPosicionesPares([]))
print ( "test-ejercicio 2.2 valor : [2,0,6,0,5,0,2,0,12,0,14] | valor calculado: ", CerosEnPosicionesPares([2,5,6,7,5,3,2,11,12,13,14]))
print ( "test-ejercicio 2.2 valor : [242,0,240] | valor calculado: ", CerosEnPosicionesPares([242,248,240]))

print ( "--------------------------------------------------------------------")
#3 -----------------------------------------------------------------------------
def eliminar_vocales(texto: str) -> str:
    texto_sin_vocales: str = ""
    vocales: list[chr] = ['a', 'e', 'i', 'o', 'u']

    for c in texto:
        if not c in vocales:
            texto_sin_vocales += c
    
    return texto_sin_vocales

print ( "test-ejercicio 2.3 valor : hl | valor calculado: ", eliminar_vocales("hola"))
print ( "test-ejercicio 2.3 valor :  t | valor calculado: ", eliminar_vocales(" t"))
print ( "test-ejercicio 2.3 valor : jklñsf | valor calculado: ", eliminar_vocales("jklñsf"))
print ( "test-ejercicio 2.3 valor :  | valor calculado: ", eliminar_vocales("aaeeio"))

print ( "--------------------------------------------------------------------")
# 4 -----------------------------------------------------------------------------
def reemplaza_vocales(texto: str) -> str:
    texto_sin_vocales: str = ""
    vocales: list[chr] = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(texto)):
        if pertenece (texto[i], vocales):
            texto_sin_vocales += '_'
        else:
            texto_sin_vocales += texto[i]
    
    return texto_sin_vocales

def pertenece(elem: str, lista: list[str]) -> bool:
    res: bool = False
    for x in lista:
        if x == elem:
            res = True
    return res

print ( "test-ejercicio 2.4 valor : h l | valor calculado: ", reemplaza_vocales("hola"))
print ( "test-ejercicio 2.4 valor :  t | valor calculado: ", reemplaza_vocales(" t"))
print ( "test-ejercicio 2.4 valor : jklñsf | valor calculado: ", reemplaza_vocales("jklñsf"))
print ( "test-ejercicio 2.4 valor :  | valor calculado: ", reemplaza_vocales("aaeeio"))

print ( "--------------------------------------------------------------------")
# 5 -----------------------------------------------------------------------------
def da_vuelta_str(string: str) -> str:
    # Para todo i ∈Z si 0 ≤i < |res|→ res[i] = s[|s|−i −1]
    # abc
    # res[0]= s[3-0-1]=s[2]
    # res[1]= s[3-1-1]=s[1]
    # res[2]= s[3-2-1]=s[0]
    str_al_reves: str = ""
    for i in range(len(string)- 1, -1, -1):
        str_al_reves += string[i]
    
    return str_al_reves

print ( "test-ejercicio 2.5 valor : aloh | valor calculado: ", da_vuelta_str("hola"))
print ( "test-ejercicio 2.5 valor :   | valor calculado: ", da_vuelta_str(""))
print ( "test-ejercicio 2.5 valor : fsñlkj | valor calculado: ", da_vuelta_str("jklñsf"))
print ( "test-ejercicio 2.5 valor : oieeaa | valor calculado: ", da_vuelta_str("aaeeio"))

def da_vuelta_str2(string: str) -> str:
    str_al_reves: str = ""
    longitud: int = len(string)

    for i in range(longitud):
        str_al_reves += string[longitud - 1 - i]
    
    return str_al_reves

print ( "--------------------------------------------------------------------")
# 6 -----------------------------------------------------------------------------
# (|res| ≤ |s|) ∧ (para todo i ∈ Zsi 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j∈Z si
# (0 ≤ i, j < |res| ∧ i ̸= j) → res[i] ̸= res[j])}

def eliminar_repetidos(string: str) -> str:

    str_sin_repetidos: str = ""
    for i in range(len(string)): #Este bucle recorre cada carácter en la cadena.
                                #Variable i: Indica la posición actual del carácter que se está evaluando.

        esta_repetida: bool = False #arranca con que no esta repetida

        for j in range(i+1, len(string)): #Bucle interno: Compara el carácter en la posición i con todos los 
                                        #caracteres que aparecen después de él en la cadena (j).
                                        #Si string[i] es igual a string[j], significa que el carácter está repetido.
                                        #esta_repetida se marca como True, y el bucle se interrumpe con break.
            if string[i] == string [j]:
                esta_repetida = True
                break

        if not esta_repetida:#Si esta_repetida es False, significa que el carácter en la 
                            #posición i no aparece nuevamente en la cadena.
                            #En este caso, se agrega el carácter a la cadena str_sin_repetidos.
            str_sin_repetidos += string[i]

    return str_sin_repetidos


print ( "test-ejercicio 2.6 valor : hola | valor calculado: ", eliminar_repetidos("hooolaao"))
print ( "test-ejercicio 2.6 valor :  so | valor calculado: ", eliminar_repetidos("oso"))
print ( "test-ejercicio 2.6 valor : jklñsf | valor calculado: ", eliminar_repetidos("jklñsff"))
print ( "test-ejercicio 2.6 valor : aeiou | valor calculado: ", eliminar_repetidos("aaeeioou"))

print ( "--------------------------------------------------------------------")
# Ejercicio 3-----------------------------------------------------------------------------
def resultadoMateria(notas: list[int]) -> int:
    # el tamaño de la lista de notas tiene que se mayor y estricto que cero > 0
    # el valor de nota es 0 ≤ notas[i] ≤ 10
    todas_aprobadas = todas_materias_aprobadas(notas)
    promedio_notas = promedio(notas)

    if not todas_aprobadas or promedio_notas < 4:
        return 3
    
    if promedio_notas < 7:
        return 2
    
    return 1

def todas_materias_aprobadas(notas: list[int]) -> bool:
    for nota in notas:
        if nota < 4:
            return False
    
    return True

def promedio(notas: list[int]) -> float:
    return suma_total(notas) / len(notas)

print ( "test-ejercicio 3 valor : 3 | valor calculado: ", resultadoMateria([0]))
print ( "test-ejercicio 3 valor : 3 | valor calculado: ", resultadoMateria([2,4,1,3,0]))
print ( "test-ejercicio 3 valor : 1 | valor calculado: ", resultadoMateria([7,8,9,7,8]))
print ( "test-ejercicio 3 valor : 2 | valor calculado: ", resultadoMateria([4,6,7,6,7]))

print ( "--------------------------------------------------------------------")
# Ejercicio 4 -----------------------------------------------------------------------------

def calcular_saldo(movimientos: list[tuple[str,float]]) -> float:
    saldo: float = 0 #saldo inicial es cero

    for operacion, monto in movimientos:
        if operacion == 'I':
            saldo += monto
        elif operacion == 'R':
            saldo -= monto
    return saldo

print ( "test-ejercicio 4 valor : 1280 | valor calculado: ", calcular_saldo([("I",2000), ("R", 20),("R", 1000),("I", 300)]))



print("          ----------------------------------------------------------------------------   ")       
print("         |                                3:  Matrices                                |  ")    
print("          ----------------------------------------------------------------------------   ")          

# Ejercicio 5 Analizando parametros in y out vs. resultado
# Entrada (in): al salir de la funcion o procedimiento, la variable
#       pasada como parametro continuara teniendo su valor original.

# Entrada (out) al salir de la funcion o procedimiento, la variable
# pasada como parametro tendra un nuevo valor asignado dentro de
# dicha funcion o procedimiento. Su valor inicial no importa ni deberıa
# ser leıdo dentro de la funcion o procedimiento en cuestion
# 1 -----------------------------------------------------------------------------
def pertenece_a_cada_uno_version_1(s: list[list[int]], e: int, res: list[bool]):
    #                            in s:seq⟨seq⟨Z⟩⟩,     in e:Z, out res: seq⟨Bool⟩)
    
    #Nota: Reutilizar la funcion pertenece() implementada previamente para listas 
    for i in range(len(s)):
        res.append(pertenece_a_la_lista(e,s[i]))

    #return res solo para testear ya que es una variable out

def pertenece_a_la_lista(elem: int, lista: list[int]) -> bool:
    res: bool = False
    for x in lista:
        if x == elem:
            res = True
    return res


print ( "test-ejercicio 5.1 valor : [True, False ,False, False] | valor calculado: ", pertenece_a_cada_uno_version_1([[1,2],[5,6]], 8, [True,False]))
print ( "test-ejercicio 5.1 valor : [True, True, True, True] | valor calculado: ", pertenece_a_cada_uno_version_1([[8,2],[5,8]], 8, [True]))

print ( "--------------------------------------------------------------------")
# 2-----------------------------------------------------------------------------
def pertenece_a_cada_uno_version_2(s: list[list[int]], e: int, res: list[bool]):
    #                            in s:seq⟨seq⟨Z⟩⟩,     in e:Z, out res: seq⟨Bool⟩)
    res.clear()

    for i in range(len(s)):
        res.append(pertenece_a_la_lista(e,s[i]))
    
    #return res solo para testear ya que es una variable out

print ( "test-ejercicio 5.1 valor : [False, False] | valor calculado: ", pertenece_a_cada_uno_version_2([[1,2],[5,6]], 8, [True,False]))
print ( "test-ejercicio 5.1 valor : [True, True] | valor calculado: ", pertenece_a_cada_uno_version_2([[8,2],[5,8]], 8, [True]))

print ( "--------------------------------------------------------------------")
# 3-----------------------------------------------------------------------------

def pertenece_a_cada_uno_version_3(s: list[list[int]], e: int) -> list[bool]:
    #                              in s:seq⟨seq⟨Z⟩⟩,   in e:Z) : seq⟨Bool⟩
    res: list[bool]=[]
    for i in range(len(s)):
        res.append(pertenece_a_la_lista(e,s[i]))

    return res
print ( "test-ejercicio 5.1 valor : [False, False] | valor calculado: ", pertenece_a_cada_uno_version_3([[1,2],[5,6]], 8))
print ( "test-ejercicio 5.1 valor : [True, True] | valor calculado: ", pertenece_a_cada_uno_version_3([[8,2],[5,8]], 8))

print ( "--------------------------------------------------------------------")

# 4 -----------------------------------------------------------------------------
# Pensar: ¿Como cambia este problema respecto de la version 1? Pensar en relacion de fuerza entre: 
# implementacion en Python y las especificaciones. 
# ¿Se puede usar la implementacion del ejercicio 2 para la especificacion del 1? 
# ¿Se puede usar la implementacion del ejercicio 1 para la especificacion del 2? Justificar su respuesta

""" 
# ejercicio 6 Implementar las siguientes funciones sobre matrices (secuencias de secuencias)
""" 
# 1-----------------------------------------------------------------------------
def es_matriz(s: list[list[int]]) -> bool:
    # es = true ↔(|s|> 0) ∧(|s[0]|> 0) ∧(Para todo i∈Z si 0 ≤ i < |s|→|s[i]|= |s[0]|)
    len_filas = len(s[0])

    if len(s) == 0 or len_filas == 0:
        return False

    for fila in s:
        if len(fila) != len_filas:
            return False
    
    return True

print ( "test-ejercicio 6.1 valor : False | valor calculado: ", es_matriz([[],[5,6]]))
print ( "test-ejercicio 6.1 valor : False | valor calculado: ", es_matriz([[8,2],[5,8,5]]))
print ( "test-ejercicio 6.1 valor : False | valor calculado: ", es_matriz([[8,2,4,5],[5,8,5]]))
print ( "test-ejercicio 6.1 valor : True | valor calculado: ", es_matriz([[8,2],[5,8],[7,8]]))
print ( "test-ejercicio 6.1 valor : True | valor calculado: ", es_matriz([[8,9,10,11],[5,6,2,4],[7,6,6,7]]))

print ( "--------------------------------------------------------------------")
# 2-----------------------------------------------------------------------------
def filas_ordenadas(m: list[list[int]], res: list[bool]):#-> list[bool]:
    #               in m:seq⟨seq⟨Z⟩⟩,   out res: seq⟨Bool⟩
    # Nota: Reutilizar la funcion ordenados() implementada previamente para lista
    # el requiere dice que tiene que cumplir que sea matriz osea es_matriz==true
    # Para todo i ∈Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])
    res.clear()

    for fila in m:
        res.append(ordenados(fila))

    #return res solo para testear ya que es una variable out (en la terminal seve como NONE)

def ordenados(ls: list[int]) -> bool:
    # True <-> para todo i ∈ Zs i 0 ≤ i < (|s|−1) → s[i] < s[i+1]
    # arranca en s[0] hasta s[n-1]
    # verdadero <-> [1,3,9]
    # solo devuelve falso si cumple que no esta ordenado
    # ordenado aca significa que no necesariamente tiene que ser consecutivo 
    for i in range(len(ls) - 1):
        if ls[i] > ls[i+1]:
            return False
    return True

print ( "test-ejercicio 6.2 valor : [False,True] | valor calculado: ", filas_ordenadas([[7,6],[5,6]],[]))
print ( "test-ejercicio 6.2 valor : [False,True] | valor calculado: ", filas_ordenadas([[8,2],[5,8]],[False]))
print ( "test-ejercicio 6.2 valor : [True, True, True]| valor calculado: ", filas_ordenadas([[8,9,10],[1,2,6],[7,9,15]],[True,False]))
print ( "test-ejercicio 6.2 valor : [True, False] | valor calculado: ", filas_ordenadas([[8,9],[5,6],[7,6]], [True]))

print ( "--------------------------------------------------------------------")
# 3 -----------------------------------------------------------------------------
def columna(m: list[list[int]], c: int) -> list[int]:
    # Devolver los elementos de la columna c en cada fila de la matriz
    # 0 <= c < |m[0]|
    res: list[int]=[]
    for fila in m:
        res.append(fila[c]) 
    return res

print ( "test-ejercicio 6.3 valor : [6,6,7] | valor calculado: ", columna([[7,6],[5,6],[8,7]], 1))
print ( "test-ejercicio 6.3 valor : [8,5] | valor calculado: ", columna([[8,2],[5,8]],0))
print ( "test-ejercicio 6.3 valor : [8,1,7]| valor calculado: ", columna([[8,9,10],[1,2,6],[7,9,15]],0))
print ( "test-ejercicio 6.3 valor : [11,4,7] | valor calculado: ", columna([[8,9,10,11],[5,6,2,4],[7,6,6,7]],3 ))

print ( "--------------------------------------------------------------------")
# 4 -----------------------------------------------------------------------------
def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    # Verificar cada columna si está ordenada
    res: list[bool]=[]
    for c in range(len(m[0])):
       res.append(ordenados(columna(m, c))) 
    return res

def columna(m: list[list[int]], c: int) -> list[int]:
    res: list[int]=[]
    for fila in m:
        res.append(fila[c]) 
    return res

def ordenados(ls: list[int]) -> bool: 
    for i in range(len(ls) - 1):
        if ls[i] > ls[i+1]:
            return False
    return True
        
print ( "test-ejercicio 6.4 valor : [False,True] | valor calculado: ", columnas_ordenadas([[7,6],[5,6],[8,7]]))
print ( "test-ejercicio 6.4 valor : [False,True] | valor calculado: ", columnas_ordenadas([[8,2],[5,8]]))
print ( "test-ejercicio 6.4 valor : [False,False,False] | valor calculado: ", columnas_ordenadas([[8,9,10],[1,2,6],[7,9,15]]))
print ( "test-ejercicio 6.4 valor : [False,False,False,True] | valor calculado: ", columnas_ordenadas([[8,9,10,1],[5,6,2,4],[7,6,6,7]]))

print ( "--------------------------------------------------------------------")
# 5 -----------------------------------------------------------------------------
def transponer(m: list[list[int]]) -> list[list[int]]:
    # Generar la matriz transpuesta usando la función columna()
    res: list[list[int]]=[]
    for c in range(len(m[0])):
            res.append(columna(m, c))
    return res

def columna(m: list[list[int]], c: int) -> list[int]:
    res: list[int]=[]
    for fila in m:
        res.append(fila[c]) 
    return res
print ( "test-ejercicio 6.5 valor : [[7,5,8],[6,6,7]] | valor calculado: ", transponer([[7,6],[5,6],[8,7]]))
print ( "test-ejercicio 6.5 valor : [[8,5],[2,8]] | valor calculado: ", transponer([[8,2],[5,8]]))

print ( "--------------------------------------------------------------------")
# 6 -----------------------------------------------------------------------------
def quien_gana_tateti(matriz: list[list[str]]) -> int:
    # Verificar filas y columnas
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != " ":
            return 1 if matriz[i][0] == "X" else 0
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != " ":
            return 1 if matriz[0][i] == "X" else 0

    # Verificar diagonales
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != " ":
        return 1 if matriz[0][0] == "X" else 0
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != " ":
        return 1 if matriz[0][2] == "X" else 0

    # Si no hay ganador
    return 2

# 7  OPCIONAL-----------------------------------------------------------------------------
# Para poder importar la biblioteca numpy es necesario instalarla primero

# import numpy as np
def matriz_random_elevada(d: int, p: int) -> list[list[int]]:
    matriz = np.random.random((d, d))

    for i in range(d):
        for j in range(d):
            matriz[i][j] = calcular_valor_de_producto_de_matriz(matriz, i, j)
    
    return matriz

""" 
       ------------------------------------------------------------------
      |          4: Programas interactivos usando secuencias             |
       ------------------------------------------------------------------

Ejercicio 7. Vamos a elaborar programas interactivos (usando la funcion input()3) que nos permita solicitar al usuario
informacion cuando usamos las funciones.
""" 
# 1 -----------------------------------------------------------------------------
def lista_estudiantes() -> list[str]:
    estudiantes: list[str] = []

    nombre: str = ""

    while nombre != "listo":
        if nombre != "":
            estudiantes.append(nombre)
        
        nombre = input("Ingrese el nombre de un estudiante: ")
    
    return estudiantes

def lista_estudiantes() -> [str]:
    lista:[str] = []
    nombre = input("introduzca los nombres de los estudiantes \n")

    while nombre != "listo":
        nombre = input()
        lista.append(nombre)
    
    return lista


# 2 -----------------------------------------------------------------------------
def imprimir_menu(creditos: float):
    print(f"Operaciones\t\tCreditos: {creditos}\n")
    print("C - Cargar créditos")
    print("D - Descontar créditos")
    print("X - Finalizar la simualción")


def obtener_opcion_ej2() -> chr:
    opc: chr = ''
    opc_validas: list[chr] = ['C', 'D', 'X']

    while not opc in opc_validas:
        opc = input("\nIngrese una opción: ").upper()
    
    return opc

def obtener_historial() -> list[tuple[chr, float]]:
    opc: chr = ''
    historial: list[tuple[chr, float]] = []
    creditos: float = 0

    print("Bienvenido a su monedero electrónico\n")
    
    while opc != 'X':
        imprimir_menu(creditos)
        opc = obtener_opcion_ej2()

        if opc == 'C':
            monto: float = float(input("\nMonto a cargar: "))
            creditos += monto
            historial.append(('C', monto))

            print("\n-- Operación realizada con éxito --\n")
        elif opc == 'D': 
            monto: float = float(input("\nMonto a descontar: "))

            if (monto > creditos):
                print("\nCreditos insuficientes\n")
                continue

            creditos -= monto
            historial.append(('D', monto))

            print("\n-- Operación realizada con éxito --\n")
    
    return historial

def obtener_historial_2() -> ([(str, int)]):
    carga_inicial:int = 0
    lista:[(str,int)] = []

    instruccion = input("introduzca C para cargar creditos, D para descontarlos o X para finalizar.\n")


    while not pertenece_str(instruccion,["X","x"]):
         if instruccion == "C" or instruccion == "c":
            carga = input("introduzca el monto a cargar:\n")
            carga_inicial += int(carga)
            tupla = (instruccion, int(carga))
            lista.append(tupla)
            instruccion = input("introduzca C para cargar creditos, D para descontarlos o X para finalizar.\n")

         elif instruccion == "D" or instruccion == "d":
            carga = input("introduzca el monto a descontar:\n")
            carga_inicial -= int(carga)
            tupla = (instruccion, int(carga))
            lista.append(tupla)
            instruccion = input("introduzca C para cargar creditos, D para descontarlos o X para finalizar.\n")

                   
    print("\nadios.\n")
    return lista

# 3 -----------------------------------------------------------------------------
def siete_y_medio():
    cartas: list[int] = []
    suma: float = 0
    opc: chr = ''

    print("Siete y medio")

    while suma <= 7 and opc != 'P':
        carta = repartir_carta()
        cartas.append(carta)
        suma += calcular_valor(carta)

        if suma <= 7:
            opc = obtener_opcion_ej3()
            
    
    imprimir_resultado(suma)

    return cartas

        
def obtener_opcion_ej3() -> chr:
    opc: chr = ''
    opc_validas = ['S', 'P']

    print("S - Sacar una carta")
    print("P - Plantarse")

    while not opc in opc_validas:
        opc = input("\nIngrese una opción: ").upper()
    
    return opc


def repartir_carta() -> int:
    carta: int = randint(1, 12)

    while carta == 8 or carta == 9:
        carta: int = randint(1, 12)
    
    print(f"\n--- Obtuviste un {carta} ---\n")
    return carta

def calcular_valor(carta: int) -> float:
    figuras: list[int] = [10,11,12]

    if carta in figuras:
        return 0.5
    
    return carta

def imprimir_resultado(suma: float):
    if suma <= 7.5:
        print(f"\nGanaste!\tResultado: {suma}")
        return
    
    print(f"\nPerdiste!\tResultado: {suma}")

#4 -----------------------------------------------------------------------------
def fortaleza_de_contraseña(contraseña: str) -> str:
    if len(contraseña) < 5:
        return "ROJA"
    
    if len(contraseña) <= 8:
        return "AMARILLA"
    
    tiene_mayuscula: bool = False
    tiene_minuscula: bool = False
    tiene_digito_numerico: bool = False

    for c in contraseña:
        if c >= 'a' and c <= 'z':
            tiene_minuscula = True
            continue

        if c >= 'A' and c <= 'Z':
            tiene_mayuscula = True
            continue

        if c >= '0' and c <= '9':
            tiene_digito_numerico = True
            continue
    
    if tiene_minuscula and tiene_mayuscula and tiene_digito_numerico:
        return "VERDE"
    
    return "AMARILLA"


def fortaleza_contraseña_2(c: str) -> str:
    longitud: int = len(c)
    
    if (longitud < 5):
        return "ROJO"
    
    if ((tiene_numero(c)) and (tiene_mayuscula(c)) and (tiene_minuscula(c)) and (len(c) > 8)):
        return "VERDE"
    
    return "AMARILLO"
def tiene_minuscula(c: str) -> bool:
    indice_actual: int = 0
    longitud: int = len(c)
    tiene_minuscula: bool = False

    while (indice_actual < longitud):
        if ((c[indice_actual] <= "z") and (c[indice_actual]>= "a")):
            tiene_minuscula = True
        indice_actual = indice_actual + 1
    
    return tiene_minuscula
        
def tiene_mayuscula(c: str) -> bool:
    indice_actual: int = 0
    longitud: int = len(c)
    tiene_mayuscula: bool = False

    while (indice_actual < longitud):
        if ((c[indice_actual] <= "Z")  and (c[indice_actual]>= "A")):
            tiene_mayuscula = True
        indice_actual = indice_actual + 1
    
    return tiene_mayuscula

def tiene_numero(c: str) -> bool:
    indice_actual: int = 0
    longitud: int = len(c)
    tiene_numero: bool = False

    while (indice_actual < longitud):
        if ((c[indice_actual] <= "9") and (c[indice_actual]>= "0")):
            tiene_numero = True
        indice_actual = indice_actual + 1
    
    return tiene_numero

# ejemplo extras-----------------------------------------------------------------------------
def calcular_valor_de_producto_de_matriz(matriz: list[list[int]], i: int, j: int) -> int:
    suma: int = 0

    for k in range(len(matriz)):
        suma += matriz[i][k] * matriz[k][j]
    
    return suma

def cuentabancaria(s:[(str, int)]) -> int:
    res: int = 0

    for tupla in s:
        if(tupla[0] == "I"):
            res = res + tupla[1]
        else:
            res = res - tupla[1]

    return res

def cuantas_vocales(palabra: str) -> int:
    vocales = 0
    if palabra.count("a") >= 1:
        vocales += 1
    if palabra.count("e") >= 1:
        vocales += 1
    if palabra.count("i") >= 1:
        vocales += 1   
    if palabra.count("o") >= 1:
        vocales += 1
    if palabra.count("u") >= 1:
        vocales += 1
    return vocales 

def pares_ceros_in(lista:[int]) -> [int]:
    nueva:[int] = []
    
    for i in lista:
        if (i % 2 == 0):
            nueva.append(0)
        else: nueva.append(i)
        
    return nueva
        

def sacar_vocales(cadena:str) -> str:
    nuevo:str = ""

    for letra in cadena:
        if not (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
            nuevo += letra

    return nuevo
def pertenece_str(caracter:str, cadena:str) -> bool:
    pertenece_str:bool = False

    for letra in cadena: 
        if letra == caracter:
            pertenece_str = True

    return pertenece_str

def todas_mayores_a(minimo, notas:[int]) -> bool:
    todas_mayores_a = True

    for nota in notas:
        if nota < minimo:
            todas_mayores_a = False
    
    return todas_mayores_a

def aprobado(notas:[int]) -> int :
    nota:int = 0
    promedio:int = suma_total(notas) // len(notas)

    if not todas_mayores_a(4,notas):
        nota = 0

    elif promedio >= 7:
        nota = 1

    elif  7 > promedio:
        nota = 2

    return nota

print("                      ------------------------------------------------------------------   ")         
print("                     |                            1. Pilas                              |  ")         
print("                      ------------------------------------------------------------------   ")         
              
"""
Ejercicio 1. Implementar una funcion generar nros al azar
(in cantidad : int, in desde : int, in hasta : int) → Pila[int]
que genere una pila de cantidad de numeros enteros al azar en el rango [desde, hasta].
Pueden usar la funcion random.randint(< desde >, < hasta >) y la
clase LifoQueue() que es un ejemplo de una implementacion basica:
    from queue import LifoQueue as Pila
    p = Pila()
    p.put(1) # apilar
    elemento = p.get() # desapilar
    p.empty () # vacia?

""" 
from queue import LifoQueue as Pila
import random

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    # que genere una pila de cantidad de numeros enteros al azar en el rango [desde, hasta]
    pila: Pila = Pila()

    while cantidad > 0:
        pila.put(random.randint(desde, hasta)) #apilar
        cantidad -= 1
    
    return pila

print ( "test-ejercicio 1.1  valor calculado: ", generar_nros_al_azar(5,2,8).queue)
print ( "test-ejercicio 1.1  valor calculado: ", generar_nros_al_azar(1,8,19).queue)

print ( "--------------------------------------------------------------------")
# Ejericio 2 -----------------------------------------------------------------------------
def cantidad_elementos(pila: Pila) -> int:
    #                  in p : Pila) →int 
    # Si se usa get() para recorrer la pila, esto
    # modifica el parametro de entrada. Y como la especificacion
    # dice que es de tipo in hay que restaurarla.
    pila_res: Pila = Pila()
    cantidad: int = 0

    
    while not pila.empty():
        pila_res.put(pila.get())
        cantidad += 1
    
    mover_pila(pila_res, pila)
    return cantidad

def mover_pila(pila_origen: Pila, pila_destino: Pila)-> Pila:
    while not pila_origen.empty():
        pila_destino.put(pila_origen.get()) # apilo en destino lo desapilado en origen ,

pila_2=  Pila()
lista =[("luis",3),("charly",3),("otis",4)]
for x in lista:
    pila_2.put(x)

print ( "test-ejercicio 1.2 valor : 3 | valor calculado: ", cantidad_elementos(pila_2))

print ( "--------------------------------------------------------------------")
# Ejericio 3 -----------------------------------------------------------------------------
def buscar_el_maximo(pila: Pila[int]) -> int:
    pila_res: Pila = Pila()
    max: int = pila.get() #Tomo el ultimo elemento de la pila
    pila_res.put(max) #pila_res arranca con un elemento 

    while not pila.empty():
        elem = pila.get() #tomo el ultimo pero aca el ultimo seria el penultimo de la pila original

        if elem > max:
            max = elem
        
        pila_res.put(elem)
    
    mover_pila(pila_res, pila)

    return max

pila_3=  Pila()
lista =[3,2,4,5,3]
for x in lista:
    pila_3.put(x)

print ( "test-ejercicio 1.3 valor : 5 | valor calculado: ", buscar_el_maximo(pila_3))

print ( "--------------------------------------------------------------------")
# Ejericio 4 -----------------------------------------------------------------------------
def buscar_nota_maxima(p: Pila[tuple[str, int]]) -> tuple[str, int]:
    # La pila no es vacía, garantizado por la precondición
    pila_res: Pila[tuple[str, int]] = Pila()
    max_elem = p.get()  # Tomar el primer elemento como máximo inicial
    pila_res.put(max_elem)  # Agregar el elemento a la pila auxiliar

    # Iterar mientras haya elementos en la pila original
    while not p.empty():
        elem = p.get()  # Tomar el último elemento de la pila original
        if elem[1] > max_elem[1]:  # Comparar las notas (segunda posición del elemento)
            max_elem = elem  # Actualizar el máximo
        pila_res.put(elem)  # Restaurar el elemento en la pila auxiliar

    # Restaurar la pila original o mover_pila(pila_res, p)
    while not pila_res.empty():
        p.put(pila_res.get())

    return max_elem

pila_4=  Pila()
lista =[("pablo",3),("charly",10),("marcos",4)]
for x in lista:
    pila_4.put(x)

print ("test-ejercicio 1.4 valor : (charly,10) | valor calculado: ", buscar_nota_maxima(pila_4))

print ( "--------------------------------------------------------------------")
# Ejericio 5 -----------------------------------------------------------------------------

def esta_bien_balanceada(operacion: str) -> bool:
    res: bool = True
    parentesis: Pila = Pila()

    for i in range(len(operacion)):
        if operacion[i] == '(':
            parentesis.put(0) # No importa el contenido de la pila sino la cantidad de elementos
        elif operacion[i] == ')':
            if parentesis.empty():
                res = False
            else:
                parentesis.get()
    
    if res:
        res = parentesis.empty()
    
    return res

print ("test-ejercicio 1.5 valor : True | valor calculado: ", esta_bien_balanceada("1+(2x3-(20/5))"))
print ("test-ejercicio 1.5 valor : False | valor calculado: ", esta_bien_balanceada("1+)2x3(()"))

print ( "--------------------------------------------------------------------")
# Ejericio 6 -----------------------------------------------------------------------------

def evaluar_expresion(s: str) -> float:
    operandos: Pila = Pila()

    for op in split_string(s):
        if op == '+':
            b = operandos.get()
            a = operandos.get()

            operandos.put(a + b)
        elif op == '-':
            b = operandos.get()
            a = operandos.get()

            operandos.put(a - b)
        elif op == '*':
            b = operandos.get()
            a = operandos.get()

            operandos.put(a * b)
        elif op == '/':
            b = operandos.get()
            a = operandos.get()

            operandos.put(a / b)
        else:
            operandos.put(int(op))
        
    return operandos.get()

def split_string (expresion:str)-> list[str]:
    res: list[str]=[]
    for s in expresion:
        if s!=" ":
            res.append(s)
    return res

print ("test-ejercicio 1.6 valor : 33 | valor calculado: ", evaluar_expresion("3 4 + 5 * 2 -"))

print ( "--------------------------------------------------------------------")
# Ejericio 7 -----------------------------------------------------------------------------
def intercalar_pilas(p1:Pila,p2:Pila)-> Pila:
    pila_aux1: Pila= Pila()
    pila_aux2: Pila= Pila()
    pila_res: Pila = Pila()

    #Invertimos la pila p1 y la pila p2
    while not p1.empty():
        pila_aux1.put(p1.get())
        pila_aux2.put(p2.get())

    # Para cada elemento dentro de las pilas, los obtenemos y lo retornamos en la pila resultado
    while not pila_aux1.empty():
        pila_res.put(pila_aux1.get())
        pila_res.put(pila_aux2.get())
    return pila_res

pila_p1=  Pila()
lista =[3,5,4]
for x in lista:
    pila_p1.put(x)

pila_p2=  Pila()
lista =[55,44,66]
for x in lista:
    pila_p2.put(x)

print ("test-ejercicio 1.6 valor : [3,55,5,44,4,66] | valor calculado: ", intercalar_pilas(pila_p1, pila_p2).queue)
#def intercalar(p1:Pila, p2:Pila) -> Pila:
#    x:int = 0
#    ser:Pila = Pila()
#    res:Pila = Pila() 
#    while not p2.empty():
#        if x % 2 == 0 and not p1.empty():
#            ser.put(p1.get())
#            p2.get()
#        elif not p2.empty():
#            p1.get()
#            ser.put(p2.get())
#        x+=1
#    while not ser.empty():
#        res.put(ser.get())
#    return res
#
#    return pila_res
print("                      ------------------------------------------------------------------   ")         
print("                     |                            2. Colas                              |  ")         
print("                      ------------------------------------------------------------------   ")         

from queue import Queue as Cola

# Ejericio 8 -----------------------------------------------------------------------------
"""
c = Cola()
c.put(1) # encolar
elemento = c.get() # desencolar () la primera de la Cola
c.empty () # vacia?
"""
def generar_nros_al_azar_cola(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    cola: Cola = Cola()

    while cantidad > 0:
        cola.put(random.randint(desde, hasta))
        cantidad -= 1
    
    return cola

print ("test-ejercicio 8 valor :  valor calculado: ", generar_nros_al_azar_cola(2,4,8).queue)

print ( "--------------------------------------------------------------------")
# Ejericio 9 -----------------------------------------------------------------------------

def cantidad_elementos_cola(cola: Cola) -> int:
    cola_aux: Cola = Cola()
    cantidad: int = 0

    while not cola.empty():
        cola_aux.put(cola.get())
        cantidad += 1
    
    mover_cola(cola_aux, cola)
    
    return cantidad

def mover_cola(cola_origen: Cola, cola_destino: Cola):
    while not cola_origen.empty():
        cola_destino.put(cola_origen.get())
    return max

cola=  Cola()
lista =[55,44,66]
for x in lista:
    cola.put(x)

print ("test-ejercicio 9 valor : 3  valor calculado: ", cantidad_elementos_cola(cola))

def mover_cola(cola_origen: Cola, cola_destino: Cola):
    while not cola_origen.empty():
        cola_destino.put(cola_origen.get())

print ( "--------------------------------------------------------------------")
# Ejericio 10 -----------------------------------------------------------------------------

def buscar_el_maximo_cola(cola: Cola[int]) -> int:
    cola_aux: Cola = Cola()
    max = cola.get()
    cola_aux.put(max)

    while not cola.empty():
        elem = cola.get()

        if elem > max:
            max = elem

        cola_aux.put(elem)
     
    mover_cola(cola_aux, cola)
    return max

def mover_cola(cola_origen: Cola, cola_destino: Cola):
    while not cola_origen.empty():
        cola_destino.put(cola_origen.get())
    

cola10=  Cola()
lista =[55,44,66]
for x in lista:
    cola10.put(x)

print ("test-ejercicio 10 valor : 66 valor calculado: ", buscar_el_maximo_cola(cola10))

print ( "--------------------------------------------------------------------")
# Ejericio 11 -----------------------------------------------------------------------------
def buscar_nota_minima(c: Cola[tuple[str, int]])-> int:
    #  min_elem es la tupla donde aparece la minima nota
    cola_res: Cola[tuple[str, int]] = Pila()
    min_elem = c.get() 
    cola_res.put(min_elem) 

    while not c.empty():
        elem = c.get() 
        if elem[1] < min_elem[1]: 
            min_elem = elem  
        cola_res.put(elem) 

    while not cola_res.empty():
        c.put(cola_res.get())

    return min_elem

cola_11=  Cola()
lista =[("charly",10),("pablo",3),("marcos",4)]
for x in lista:
    cola_11.put(x)

print ("test-ejercicio 11 valor : (pablo,3) valor calculado: ", buscar_nota_minima(cola_11))

print ( "--------------------------------------------------------------------")
# Ejericio 12 -----------------------------------------------------------------------------
def intercalar_colas(c1:Cola,c2:Cola)-> Cola:
    cola_aux1: Cola= Cola()
    cola_aux2: Cola= Cola()
    cola_res: Cola = Cola()

    while not c1.empty():
        cola_aux1.put(c1.get())
        cola_aux2.put(c2.get())

    while not cola_aux1.empty():
        cola_res.put(cola_aux1.get())
        cola_res.put(cola_aux2.get())
    return cola_res

cola_p1=  Cola()
lista =[3,5,4]
for x in lista:
    cola_p1.put(x)

cola_p2=  Cola()
lista =[55,44,66]
for x in lista:
    cola_p2.put(x)

print ("test-ejercicio 12 valor : [3,55,5,44,4,66] | valor calculado: ", intercalar_pilas(cola_p1, cola_p2).queue)

print ( "--------------------------------------------------------------------")
# Ejericio 13 -----------------------------------------------------------------------------
from typing import TypeVar #, Tuple
T = TypeVar('T')
 
def armar_secuencia_de_bingo() -> Cola[int]:
    numeros: list[int] = []
    cola: Cola[int] = Cola()
 
    while len (numeros) < 100:
        n = random.randint(0,99)
        if not pertenece_seq(n,numeros): 
            cola.put(n)
            numeros.append(n)
 
    return cola

def jugar_carton_de_bingo(carton:list,bolillero:Cola[int])->int:
 
    jugadas:int=0
    numeros_marcados:int=0
    bolillero_aux:Cola[int]=Cola()
 
    #Sigo sacando bolillas hasta que marque todos los numeros
    while numeros_marcados < 12:
        bolilla_sacada=bolillero.get()
        bolillero_aux.put(bolilla_sacada)
        if pertenece_seq (bolilla_sacada,carton):
            numeros_marcados+=1
        jugadas+=1
 
    #Una vez que marque todos, paso todas las bolillas restantes al bolillero auxiliar
    while not bolillero.empty():
        bolilla_sacada:int = bolillero.get()
        bolillero_aux.put(bolilla_sacada)
 
    #Luego las devuelvo del bolillero auxiliar al original, para que quede igual que al principio        
    while not bolillero_aux.empty():
        bolilla_sacada:int  = bolillero_aux.get()
        bolillero.put(bolilla_sacada)
 
    return jugadas
 
def pertenece_seq ( elem:T,cadena: list[T]) -> bool:
    for i in cadena:
        if i == elem: 
            return True
    return False
 
"""
Extrae un número de la cola bolillero con get.
Verifica si el número extraído pertenece al cartón del jugador con pertenece.
Si sí, incrementa cantidad_aciertos.
Incrementa cantidad_jugadas y almacena el número en bolillero_aux.
Una vez alcanzados 12 aciertos, los números restantes de bolillero_aux se devuelven a bolillero usando mover_cola.
Devuelve cantidad_jugadas.
"""
bolillero = armar_secuencia_de_bingo()
carton = [10, 2, 30, 40, 5, 60, 7, 80, 90, 0, 15, 25]
print ("test-ejercicio 13 valor : | valor calculado: ", jugar_carton_de_bingo(carton, bolillero))

print ( "--------------------------------------------------------------------")
# Ejericio 14 -----------------------------------------------------------------------------

def n_pacientes_urgentes(pedidos_atencion: Cola[tuple[int, str, str]]) -> int:
    pedidos_atencion_aux: Cola[tuple[int, str, str]] = Cola()
    cantidad_pacientes_urgentes: int = 0

    while not pedidos_atencion.empty():
        pedido: tuple[int, str, str] = pedidos_atencion.get()

        if pedido[0] <= 3:
            cantidad_pacientes_urgentes += 1
        
        pedidos_atencion_aux.put(pedido)
    
    mover_cola(pedidos_atencion_aux, pedidos_atencion)
    
    return cantidad_pacientes_urgentes

print ( "--------------------------------------------------------------------")
# Ejericio 15 -----------------------------------------------------------------------------

def atencion_a_clientes(cola_clientes: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    cola_clientes_aux: Cola[tuple[str, int, bool, bool]] = Cola()

    subgrupos_colas: list[Cola[tuple[str, int, bool, bool]]] = [Cola(), Cola(), Cola()] # lista con subgrupos
    con_prioridad, con_cuenta_preferencial, resto = 0, 1, 2 # enum de cada subgrupo

    cola_ordenada: Cola[tuple[str, int, bool, bool]] = Cola()

    while not cola_clientes.empty():
        cliente = cola_clientes.get()

        tiene_prioridad: bool = cliente[3]
        tiene_cuenta_preferencial: bool = cliente[2]

        if tiene_prioridad:
            subgrupos_colas[con_prioridad].put(cliente)
        elif tiene_cuenta_preferencial:
            subgrupos_colas[con_cuenta_preferencial].put(cliente)
        else:
            subgrupos_colas[resto].put(cliente)
        
        cola_clientes_aux.put(cliente)

    
    for cola in subgrupos_colas:
        while not cola.empty():
            cola_ordenada.put(cola.get())
    
    mover_cola(cola_clientes_aux, cola_clientes)
    
    return cola_ordenada

print("                      ------------------------------------------------------------------   ")         
print("                     |                          3.Diccionarios                          |  ")         
print("                      ------------------------------------------------------------------   ")         
    

# Ejericio 16 -----------------------------------------------------------------------------

def agrupar_por_longitud(nombre_archivo: str) -> dict[int, int]:
    file = open(nombre_archivo, 'r', encoding="utf-8")
    contenido: str = file.read()
    file.close()

    grupo_por_longitud: dict[int, int] = {}

    for palabra in obtener_palabras(contenido):
        longitud: int = len(palabra)

        if grupo_por_longitud.get(longitud) == None:
            grupo_por_longitud[longitud] = 1
        else:
            grupo_por_longitud[longitud] += 1
    
    return grupo_por_longitud

# Ejericio 17 -----------------------------------------------------------------------------

def calcular_promedio_por_estudiante_dict(nombre_archivo: str) -> dict[str, float]:
    file = open(nombre_archivo, "r", encoding="utf-8")
    lineas: list[str] = file.readlines()
    file.close()

    lista_lu: list[str] = obtener_lista_lu(lineas)

    promedios: dict[str, int] = {}

    for lu in lista_lu:
        promedios[lu] = promedio_estudiante(nombre_archivo, lu)
    
    return promedios

# Ejericio 18 -----------------------------------------------------------------------------

def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    file = open(nombre_archivo, "r", encoding="utf-8")
    contenido: str = file.read()
    file.close()

    palabras: list[str] = obtener_palabras(contenido)

    apariciones_palabras: dict[str, int] = {}

    for palabra in palabras:
        if apariciones_palabras.get(palabra) == None:
            apariciones_palabras[palabra] = 1
        else:
            apariciones_palabras[palabra] += 1
    
    palabra_mas_frecuente: tuple[str, int] = (palabras[0], apariciones_palabras[palabras[0]])

    for palabra, apariciones in apariciones_palabras.items():
        if apariciones > palabra_mas_frecuente[1]:
            palabra_mas_frecuente = (palabra, apariciones)
    
    return palabra_mas_frecuente[0]

# Ejericio 19 -----------------------------------------------------------------------------

historiales: dict[str, Pila[str]] = {}

def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str):
    if historiales.get(usuario) == None:
        historial_nuevo: Pila = Pila()
        historial_nuevo.put(sitio)
        historiales[usuario] = historial_nuevo
    else:
        historiales[usuario].put(sitio)

def navegar_atras(historiales: dict[str, Pila[str]], usuario: str):
    if historiales[usuario] != None and not historiales[usuario].empty():
        historiales[usuario].get()

# Ejericio 20 -----------------------------------------------------------------------------

inventario: dict[str, dict[str, float]] = {}
# inventario = {}
# agregar_producto(inventario, "Camisa", 20.0, 50)
# agregar_producto(inventario, "Pantal ́on", 30.0, 30)
# actualizar_existencias(inventario, "Camisa", 10)
# valor_total = calcular_valor_inventario(inventario)
# print("Valor total del inventario:", valor_total) # Deber ́ıa imprimir 1300.00

def agregar_producto(inventario: dict[str, dict[str, float]], nombre: str, precio: float, cantidad: int):
    inventario[nombre] = {"Precio": precio, "Cantidad": cantidad}

def actualizar_stock(inventario: dict[str, dict[str, float]], nombre: str, cantidad: int):
    if inventario[nombre] != None:
        inventario[nombre]["Cantidad"] = cantidad

def actualizar_precios(inventario: dict[str, dict[str, float]], nombre: str, precio: float):
    if inventario[nombre] != None:
        inventario[nombre]["Precio"] = precio

def calcular_valor_inventario(inventario: dict[str, dict[str, float]]) -> float:
    valor: float = 0

    for producto in inventario.values():
        valor += producto["Precio"] * producto["Cantidad"]
    
    return valor


def get_full_path(nombre_archivo: str):
    return base_path + nombre_archivo


print("                      ------------------------------------------------------------------   ")         
print("                     |                            4. Archivos                           |  ")         
print("                      ------------------------------------------------------------------   ")       
# Ejericio 21 -----------------------------------------------------------------------------
#1
def contar_lineas(nombre_archivo: str) -> int:
    file = open(nombre_archivo, "r")
    lineas = file.readlines()
    cantidad_lineas: int = len(lineas)
    file.close()
    return cantidad_lineas

# 2
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    file = open(nombre_archivo, 'r', encoding="utf-8")
    contenido: str = file.read()
    file.close()
    res: bool = pertenece(palabra, obtener_palabras(contenido))

    return res

def pertenece(elem, list: list) -> bool:
    res: bool = False

    for x in list:
        if x == elem:
            res = True
    
    return res

def obtener_palabras(texto: str) -> list[str]:
    palabras: list[str] = []
    chars: list[str] = list(texto)
    palabra_actual: str = ""

    for i in range(len(chars)):
        if chars[i] == ' ' or chars[i] == '\n' or i == len(chars) - 1:
            if palabra_actual != "":
                palabras.append(palabra_actual)
            palabra_actual = ""
        else:
            palabra_actual += chars[i]
    
    return palabras

# 3
def cantidad_apariciones(nombre_archivo: str, palabra: str) -> int:
    file = open(nombre_archivo, 'r', encoding="utf-8")
    contenido: str = file.read()
    file.close()
    
    cantidad: int = 0

    for palabra_actual in obtener_palabras(contenido):
        if palabra == palabra_actual:
            cantidad += 1
    
    return cantidad

# Ejericio 22 -----------------------------------------------------------------------------
def clonar_sin_comentarios(nombre_archivo: str):
    in_file = open(nombre_archivo, 'r', encoding="utf-8")
    lineas: list[str] = in_file.readlines()
    in_file.close()

    lineas_sin_comentarios: list[str] = []

    for linea in lineas:
        if not es_comentario(linea):
            lineas_sin_comentarios.append(linea)
    
    out_file = open("sin_comentarios.txt", 'w', encoding="utf-8")
    out_file.writelines(lineas_sin_comentarios)
    out_file.close()
    

def es_comentario(linea: str) -> bool:
    res: bool = False
    chars: list[str] = list(linea)
    es_el_primero = True

    for i in range(len(chars)):
        if chars[i] == "#" and es_el_primero:
            res = True
        elif chars[i] != " ":
            es_el_primero = False

    return res

# Ejericio 23 -----------------------------------------------------------------------------

def invertir_lineas(nombre_archivo: str):
    in_file = open(nombre_archivo, 'r', encoding="utf-8")
    lineas: list[str] = in_file.readlines()
    in_file.close()

    lineas_invertidas: list[str] = []

    for linea in lineas:
        lineas_invertidas.insert(0, linea)
    
    out_file = open("reverso.txt", 'w', encoding="utf-8")
    out_file.writelines(lineas_invertidas)
    out_file.close()

# Ejericio 24 -----------------------------------------------------------------------------
def agregar_frase_al_final(nombre_archivo: str, frase: str):
    file = open(nombre_archivo, 'a', encoding="utf-8")
    file.write('\n' + frase)
    file.close()

# Ejericio 25 -----------------------------------------------------------------------------
def agregar_frase_al_principio(nombre_archivo: str, frase: str):
    file = open(nombre_archivo, 'r+', encoding="utf-8")
    lineas = file.readlines()
    lineas.insert(0, frase + '\n')
    file.seek(0)
    file.writelines(lineas)
    file.close()

# Ejericio 26 -----------------------------------------------------------------------------
def listar_palabras_de_archivo(nombre_archivo: str) -> list[str]:
    file = open(nombre_archivo, 'rb')
    bytes: list[int] = file.read()
    file.close()

    palabras: list[str] = []
    palabra_actual: str = ""

    for byte in bytes:
        char: str = chr(byte)

        if es_caracter_valido(char):
            palabra_actual += char
        else:
            if len(palabra_actual) >= 5:
                palabras.append(palabra_actual)
            
            palabra_actual = ""
    
    return palabras


def es_caracter_valido(char: str) -> bool:
    return (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '1' and char <= '9') or char == ' ' or char == '_'

# Ejericio 27 -----------------------------------------------------------------------------

def calcular_promedio_por_estudiante(nombre_archivo_notas: str, nombre_archivo_promedios: str):
    in_file = open(nombre_archivo_notas, 'r', encoding="utf-8")
    filas: list[str] = in_file.readlines()
    in_file.close()

    lista_lu = obtener_lista_lu(filas)

    out_file = open(nombre_archivo_promedios + '.csv', 'w', encoding="utf-8")
    out_file.write("nro de LU,promedio\n")

    for lu in lista_lu:
        promedio: float = promedio_estudiante(nombre_archivo_notas, lu)

        out_file.write(f"{lu},{promedio}\n")
    
    out_file.close()


def obtener_lista_lu(filas: list[str]) -> list[str]:
    lista_lu: list[str] = []

    for i in range(1,len(filas)):
        lu = separar_por(filas[i], ",")[0]

        if not pertenece(lu, lista_lu):
            lista_lu.append(lu)
    
    return lista_lu

def promedio_estudiante(nombre_archivo: str, lu: str) -> float:
    file = open(nombre_archivo, 'r', encoding="utf-8")
    filas: list[str] = file.readlines()
    file.close()

    suma_notas: float = 0
    cant_materias: int = 0

    for i in range(1, len(filas)):
        [lu_actual, _, _, nota] = separar_por(filas[i], ",")

        if lu_actual == lu:
            suma_notas += float(nota)
            cant_materias += 1
    
    promedio: float = round(suma_notas / cant_materias, 2)

    return promedio

def separar_por(string: str, separador: str) -> list[str]:
    lista_str: list[str] = []
    substr: str = ""

    for c in string:
        if c == separador:
            lista_str.append(substr)
            substr = ""
        else:
            substr += c
    
    lista_str.append(substr)

    return lista_str
