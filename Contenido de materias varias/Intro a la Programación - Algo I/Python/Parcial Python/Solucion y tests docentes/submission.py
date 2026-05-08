from queue import Queue as Cola
from queue import LifoQueue as Pila

# Ejercicio 1
def multiplos_de_primos(v: list[int]) -> dict[int,int]:
    res: dict[int, int] = dict()
    divisores_primos: list[int] = list()

    for value in v:
        for n in range(1,value):
            if (value%n == 0 and
                es_primo(n) and
                not pertenece(n, divisores_primos)):

                divisores_primos.append(n)
    
    res = {p: 0 for p in divisores_primos}
    
    for p in divisores_primos:
        count: int = 0
        for value in v:
            if value%p == 0: count+=1
        res[p] = count
    res.pop(1)

    return res

def pertenece(value:any, lista:list[any]) -> bool:
    for elem in lista:
        if elem == value:
            return True
    return False

def es_primo(num: int) -> bool:
    divisores: list[int] = []
    for n in range(1,num+1):
        if num%n == 0:
            divisores.append(n)
    return len(divisores)<=2


# Ejercicio 2
def longitud_mas_grande(A: list[list[int]]) -> int:
    
    sqs: list[list[int]] = list()

    for sec in A:
        sec_temp: list[int] = list()
        for num in sec:
            if num == 1: 
                sec_temp.append(num)
            else:
                if sec_temp: sqs.append(sec_temp)
                sec_temp = []
                
    res: int = len(sqs[0])
    for sec in sqs:
        if len(sec)>res:
            res = len(sec)

    return res

# Ejercicio 3
def resolver_cuentas(A: Pila[str]) -> list[int]:
    
    cuentas: list[str] = list()
    while not A.empty():
        cuenta: str = A.get()
        cuentas.append(cuenta)
    
    for i in range(len(cuentas)-1, 0, -1):
        A.put(i)
    
    res: list[int] = list()
    for cuenta in cuentas:
        
        suma_temp: int = 0
        if not pertenece(cuenta[0], '+-'):
            suma_temp = int(cuenta[0])
        elif pertenece(cuenta[0], '+-'):
            suma_temp = int(cuenta[1])
        
        for i in range(1,len(cuenta)-1):
            if cuenta[i]=='+':
                suma_temp += int(cuenta[i+1])
            elif cuenta[i]=='-':
                suma_temp -= int(cuenta[i+1])
        
        res.append(suma_temp)
            
    return res

def esta_bien_formado(s: str) -> bool:
    char_permitidos: str = '+-0123456789'
    
    aux: list[str] = [char for char in s]
    ultimo = aux.pop()
    aux.append(ultimo)
    
    if pertenece(ultimo, '+-'):
        return False

    for i in range(1,len(aux)):
        if not pertenece(aux[0], char_permitidos):
            return False
        elif not pertenece(aux[i], char_permitidos):
            return False
        elif pertenece(aux[i], '+-') and pertenece(aux[i-1], '+-'):
            return False

    return True
    
# Ejercicio 4
def dame_el_que_falta(s: list[tuple[int,int]]) -> tuple[int,int]:
    
    n: int = s[0][0]
    for t in s:
        for num in t:
            if num>n: n = num
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if not pertenece((i,j),s): 
                return (i,j)
