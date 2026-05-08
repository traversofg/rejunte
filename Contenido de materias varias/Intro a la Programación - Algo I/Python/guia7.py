def pertenece1(s: list[int], e: int) -> bool:
    res = False
    for elem in s:
        if elem == e:
            res = True
    return res



def pertenece2(s: list[int], e: int) -> bool:

    for elem in s:
        if elem == e:
            return True
    
    return False


def pertenece3(s: list[int], e: int) -> bool:
    apariciones = 0
    for elem in s:
        if elem == e:
            apariciones += 1
    return apariciones >= 1

#print(pertenece1([1,2,3], 3))
#print(pertenece2([1,2,3], 3))
#print(pertenece3([1,2,3], 3))


# --------------------------- #

def divide_a_todos(s: list[int], e: int) -> bool:
    i = 0
    for elem in s:
        if elem % e != 0:
            i += 1
    return i == 0

# print(divide_a_todos([6,9,12,15], 3))

# --------------------------- #

def suma_total(s: list[int]) -> int:
    suma = 0
    for elem in s:
        suma += elem
    return suma

# print(suma_total([1,2,3]))

# --------------------------- #

def maximo(s: list[int]) -> int:
    maximo = s[0]
    for i in range(len(s)):
        if s[i] > maximo:
            maximo = s[i]
    return maximo

# print(maximo([1,2,3,4,5,6,77,76,75,88]))

# --------------------------- #

def minimo(s: list[int]) -> int:
    minimo = s[0]
    for i in range(len(s)):
        if s[i] < minimo:
            minimo = s[i]
    return minimo

# print(minimo([1,2,3,4,5,6,77,76,75,88]))

# --------------------------- #

def ordenados(s:list[int]) -> bool :
    count = 0
    for i in range(len(s)-1):
        if s[i+1] < s[i]:
            count += 1
    return count == 0

# print(ordenados([1,2,2,3,4]))

# --------------------------- #

def pos_max(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        return s.index(maximo(s))
    
def pos_max2(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        for i in range(len(s)):
            if s[i] == maximo(s):
                return i
                break

# print(pos_max([99,1,2,3])) # expected : 0
# print(pos_max2([99,1,2,3])) # expected : 0

# print(pos_max([1,2,3,99])) # expected : 3
# print(pos_max2([1,2,3,99])) # expected : 3

# print(pos_max([1,99,2,3])) # expected : 1
# print(pos_max2([1,99,2,3])) # expected : 1

# pos_minimo es igual pero se aplica la funcion minimo en vez de maximo

# --------------------------- #

def problema9(s: list[list[chr]]) -> bool:
    res = False
    for elem in s:
        if len(elem) > 7:
            res = True
    return res

# print(problema9(["termo", "gato", "tener", "jirafas"]))
# print(problema9(["termo", "gato", "tener", "jirafas", "elefante"]))

# --------------------------- #

def palindromo(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]
    
# print(palindromo("Radar")) 

# --------------------------- #

def tres_vocales(s: str) -> bool :
    apariciones = []
    vocales = ["a", "e", "i", "o", "u"]
    for char in s:
        if pertenece1(vocales, char) and not pertenece1(apariciones, char):
            apariciones.append(char)
    return len(apariciones) >= 3

# print(
    # tres_vocales("hola"),
    # tres_vocales("aaa"),
    # tres_vocales("murcielago")
# )

# --------------------------- #

"""

Problema encontrar secuencia:

Dado una lista de enteros, quiero poder encontrar una secuencia de numeros ordenados dentro de la misma.

Me armo una lista vacia, 

"""
s = []

secuencias = []
index_seq = -1
nros_seq = []
for i in range(len(s)-1):
    
    if s[i+1] > s[i]:
        nros_seq.append(s[i+1])
    secuencias.append(nros_seq)

# continua_secuencia

# list[j+1] > list[j]
def coso(s: list[int]) -> int:
    sqs = []
    res = -1
    for i in range(len(s)):
        seq = [s[i]]
        j = i+1
        while j<len(s) and s[j] == s[j - 1] + 1:
            seq.append(s[j])
            j += 1
        sqs.append(len(seq))
        if len(seq) == maximo(sqs):
            res = i
    return res

# print('\n',
    # coso([1,2,3,4,5]), '\n', # expected : 0
    # coso([1,2,3,5,6,10,11]), '\n', # expected : 0
    # coso([1,2,3,5,6,10,11,12]), '\n', # expected : 5
    # coso([1,2,3,5,6,10,11,12,13]), '\n' # expected : 5
# )

"""
# Respuesta de ChatGPT:
def coso(s: list[int]) -> int:
    if not s:
        return -1  # Si la lista está vacía, devolvemos -1

    max_len = 0  # Longitud máxima de la secuencia más larga
    current_len = 1  # Longitud de la secuencia actual
    res = 0  # Índice de inicio de la secuencia más larga
    start = 0  # Índice de inicio de la secuencia actual

    for i in range(1, len(s)):
        if s[i] == s[i - 1] + 1:  # Si el número es consecutivo
            current_len += 1
        else:
            # Si encontramos una secuencia más larga, actualizamos max_len y res
            if current_len > max_len:
                max_len = current_len
                res = start
            # Reiniciamos la longitud de la secuencia actual y el índice de inicio
            current_len = 1
            start = i

    # Al finalizar el bucle, verificamos si la última secuencia fue la más larga
    if current_len > max_len:
        res = start

    return res
"""

# print('\n',
    # coso([1,2,3,4,5]), '\n', # expected : 0
    # coso([1,2,3,5,6,10,11]), '\n', # expected : 0
    # coso([1,2,3,5,6,10,11,12]), '\n', # expected : 5
    # coso([1,2,3,5,6,10,11,12,13]), '\n' # expected : 5
# )

# print(coso([1, 2, 3, 5, 6, 7, 8, 10]))  # Output: 3 (inicia en el índice 3, con la secuencia más larga [5, 6, 7, 8])
# print(coso([10, 11, 5, 6, 7, 2, 3, 4]))  # Output: 2 (inicia en el índice 2, con la secuencia más larga [5, 6, 7])

# --------------------------- #

def cant_digitos_impares(seq : list[int]) -> int:
    count: int = 0
    for elem in seq:
        for num in str(elem):
            if int(num) % 2 != 0:
                count += 1
    return count

# print(
    # cant_digitos_impares([57, 2383, 812, 246])
# )

# --------------------------- #

# ------- EJERCICIO 2 ------- #

# --------------------------- #

def ceros_pos_pares(seq : list[int]):
    for i in range(len(seq)):
        if i % 2 == 0:
            seq[i] = 0
    print(seq)

# ceros_pos_pares([0,1,2,3,4,5,6])

def ceros_pos_pares2(seq : list[int]) -> list[int]:
    res: list[int] = []
    for i in range(len(seq)):
        if i%2 != 0:
            res.append(seq[i])
        else:
            res.append(0)
    return res

# print(
    # ceros_pos_pares2([0,1,2,3,4,5,6])
# )

# --------------------------- #
vocales: str = "AaEeIiOoUu"
"""
def mod_string(string : str) -> str:
    string = list(string)
    for letter in string:
        if letter in vocales:
            string.remove(letter)
    return str(string)
"""
# print(mod_string("aeiouKJJJJ"))

def mod_string2(string: str) -> str:
    res: str = ""
    for letter in string:
        if letter not in vocales:
            res += letter
    return res

# print(mod_string2("aeiouKJJJJ"))
def mod_string3(string: str) -> str:
    res: str = ''.join( # En esta materia no vale usar .join()
        letter for letter in string 
        if letter not in vocales
    )
    return res

# print(mod_string3("aeiouKJJJJ"))

def reemplaza_vocales(string: list[chr]) -> str:
    res: str = ''
    for char in string:
        if char in vocales:
            res += '_'
        else:
            res += char
    return res

# print(
    # reemplaza_vocales(
        # 'HOLA COMO ESTAMOS'
    # )
# )

# --------------------------- #

def da_vuelta_str(string : str) -> str: # type: ignore
    ref: int = len(string) - 1
    res: str = ''
    for i in range(len(string)):
        res += string[ref - i]
    return res

# print(da_vuelta_str("Radar"))

# --------------------------- #

def eliminar_repetidos(string: str) -> str:
    seq: str = string.lower()
    res: str = ''
    for char in seq:
        if char not in res:
            res += char
    return res

# print(
    # eliminar_repetidos("HOLAa CoOMOo eESTAS")
# )

# --------------------------- #

