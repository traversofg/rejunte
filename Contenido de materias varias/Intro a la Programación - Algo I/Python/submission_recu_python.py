from queue import Queue as Cola

# Ej 1
def minimos(s: list[list[int]]) -> dict[int, int]:
    
    """
    Recibe una lista de sublistas de enteros;
        Claves de res: minimos de las sublistas
        Valores de res: cantidad de sublistas cuyo minimo es n
    """
    
    res: dict[int, int] = {}
    
    for seq in s:
        if seq:
            min: int = buscar_minimo(seq)
            actualizar_dict(min, res)
    
    return res

def buscar_minimo(seq: list[int]) -> int:
    if not seq: return None
    min: int = seq[0]
    for num in seq:
        if num<min: min = num
    return min

def actualizar_dict(valor: any, diccionario: dict[any, int]) -> None:
    # Lo dejo con 'any' porque me sirve para el Ej4
    if pertenece(valor, diccionario.keys()):
        diccionario[valor] += 1
    else:
        diccionario[valor] = 1

def pertenece(item: any, seq: any) -> bool:
    for s in seq:
        if item == s: return True
    return False


# Ej 2
def es_matriz_espejada(A: list[list[int]]) -> bool:
    
    """
    Recibe una matriz y devuelve True si y solo si:
        Todas las filas de A son 'capicua'
    """
    for fila in A:
        if not es_espejada(fila): return False
    return True

def es_espejada(seq: list[int])-> bool:
    for i in range(len(seq)):
        espejo: int = len(seq)-1-i
        if seq[i] != seq[espejo]:
            return False
    return True

# Ej 3
def solo_tuplas_consistentes(c: Cola[tuple[int, bool]]) -> None:
    
    cumple_A: list[tuple[int, bool]] = []
    cumple_B: list[tuple[int, bool]] = []

    while not c.empty():
        t: tuple[int, bool] = c.get()
        if cumple_condicion_A(t):
            cumple_A.append(t)
        elif cumple_condicion_B(t):
            cumple_B.append(t)

    tuplas_consistentes: list[tuple[int, bool]] = cumple_A + cumple_B

    for t in tuplas_consistentes:
        c.put(t)
    
    return

def cumple_condicion_A(t: tuple[int,bool]) -> bool:
    c1 = t[0]>0
    c2 = t[1]
    return c1 and c2

def cumple_condicion_B(t: tuple[int,bool]) -> bool:
    c1 = t[0]<0
    c2 = not t[1]
    return c1 and c2

# Ej 4 
def segunda_cantidad_max_apariciones(texto: str) -> str:
    
    """
        Dado un texto con al menos dos caracteres distintos,
        en el cual no hay ningun par de caracteres con la misma
        cantidad de apariciones, devuelve el caracter que tenga
        la segunda maxima cantidad de apariciones.

        Podria armar un diccionario con las apariciones por caracter,
        buscar el maximo de los valores de este diccionario, eliminar
        esa entrada, y volver a hacer lo mismo. 
        Necesitaría un par de funcs aux:
            eliminar(int,seq)->seq
            buscar_maximo(seq)->int
        No se si me fascina esta forma de hacerlo pero bueno, si
        funciona anda me dijeron una vez, que se yo. La verdad que no
        se me estaría ocurriendo otra forma más eficiente de resolverlo.
    """
    res: str = ''

    apariciones: dict[str, int] = {}
    for char in texto:
        actualizar_dict(char, apariciones)

    # No me convence, aunque parece funcionar
    max_apariciones: int = buscar_maximo(apariciones.values())
    aps_sin_max: list[int] = eliminar_num(max_apariciones, apariciones.values())
    segundo_max: int = buscar_maximo(aps_sin_max)

    for char, count in apariciones.items():
        if count == segundo_max:
            return char

def eliminar_num(n:int, seq:list[int]) -> list[int]:
    res: list[int] = []
    for num in seq:
        if num != n:
            res.append(num)
    return res

def buscar_maximo(s:list[int]) -> int:
    if not s: return None
    seq = list(s)
    max: int = seq[0]
    for num in seq:
        if num>max: max = num
    return max