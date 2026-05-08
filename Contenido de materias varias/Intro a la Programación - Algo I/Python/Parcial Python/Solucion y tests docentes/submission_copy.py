from queue import Queue as Cola
from queue import LifoQueue as Pila

# Ejercicio 1
def multiplos_de_primos(v: list[int]) -> dict[int,int]:
    res: dict[int, int] = dict()

    if not v: return {}

    for valor in v:
        for num in range(2,valor+1):
            if valor % num == 0 and es_primo(num):
                    actualizar(res, num)

    return res

def pertenece(secuencia, elem) -> bool:
    for e in secuencia:
        if elem == e: return True
    return False

def actualizar(diccionario: dict[int, int], valor: int) -> None:
    if pertenece(diccionario.keys(), valor):
        diccionario[valor] += 1
    else:
        diccionario[valor] = 1

def es_primo(num: int) -> bool:
    for nro in range(2, num):
        if num % nro == 0:
            return False
    return True

# Ejercicio 2
def longitud_mas_grande(A: list[list[int]]) -> int:
    largos: list[int] = []
    cant_columnas: int = len(A[0])

    for fila_actual in A:
        largo_actual: int = 0
        for i in range(len(fila_actual)):
            if fila_actual[i] == 1:
                largo_actual += 1
            else:
                largos.append(largo_actual)
                largo_actual = 0
        
        # Agrego la ultima secuencia
        ultimo = fila_actual[len(fila_actual)-1]
        if ultimo == 1: largos.append(largo_actual)
    
    return maximo(largos)

def maximo(secuencia: list[int]) -> int:
    res: int = secuencia[0]
    for num in secuencia:
        if num > res: res = num
    return res

# Ejercicio 3
def resolver_cuentas(A: Pila[str]) -> list[int]:
    
    if not A: return []

    res: list[int] = []
    
    pila_aux: Pila[str] = Pila()
    while not A.empty():
        cuenta: str = A.get()
        pila_aux.put(cuenta)
        res.append(calcular(cuenta))
    
    while not pila_aux.empty():
        A.put(pila_aux.get())

    return res


# Practicamente calcao del resuelto, una pena
def calcular(cuenta: str) -> int:
    res: int = 0

    # Necesito un valor que se vaya actualizando

    nro_actual: int = 0

    # Y aparte algo que me indique el signo a utilizar

    signo: int = 1      # {+/- 1}
    
    for digito in cuenta:
        
        #   Si el digito es un signo, entonces actualizo
        # el valor de res con el nro actual y el signo actual,
        # que serian los valores a la izq de este signo.
      
        if digito == '+':
            
            res += signo * nro_actual
            # Luego actualizo el signo para el sig nro
            # y reseteo el nro_actual.
            signo = 1
            nro_actual = 0
        elif digito == '-':
            
            res += signo * nro_actual

            # Luego actualizo el signo para el sig nro
            # y reseteo el nro_actual.
            signo = -1
            nro_actual = 0
        else:
            # Si tengo dos nros seguidos, deberia contar
            # al anterior como el de las decenas y a este
            # como el de las unidades, y asi para la cant que tenga
            nro_actual = nro_actual * 10 + int(digito)

    # Como solo actualizo res cuando me encuentro un signo,
    # ahora tengo que agregar el valor del ultimo nro acumulado.

    res += signo * nro_actual

    return res


# Ejercicio 4
from math import sqrt
def dame_el_que_falta(s: list[tuple[int,int]]) -> tuple[int,int]:
    max_: int = int(sqrt((len(s))+1))
    for i in range(1, max_ + 1):
        for j in range(1, max_ + 1):
            if not pertenece(s, (i,j)):
                return (i,j)
    return (-1, -1)
