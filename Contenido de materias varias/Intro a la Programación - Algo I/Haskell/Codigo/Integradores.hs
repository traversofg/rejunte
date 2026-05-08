module Integradores where

{- ---------------------------
-- EJERCICIOS INTEGRADORES --
--------------------------- -}

-- module integradores where

----- SISTEMA DE STOCK -----


-- Ejercicio 1

generarStock :: [String] -> [(String, Int)]
generarStock [] = []
generarStock (producto:resto) =
    contarProducto producto (producto:resto) : generarStock (sacarProducto producto resto)

contarProducto :: String -> [String] -> (String, Int)
contarProducto nombreProducto [] = (nombreProducto, 0)
contarProducto nombreProducto (primerElemento:restoDeLista)
    | nombreProducto == primerElemento =
        (nombreProducto, snd (contarProducto nombreProducto restoDeLista) + 1)
        -- En esta ultima linea estoy agarrando el segundo elemento de la tupla
        -- y sumandolo al resultado del llamado recursivo.

        -- Si no son iguales, no hago nada y sigo buscando:
    | otherwise = contarProducto nombreProducto restoDeLista

sacarProducto :: String -> [String] -> [String]
sacarProducto _ [] = []
sacarProducto prodASacar (primerElemento:restoDeLista)
    | prodASacar == primerElemento = -- Acá viene llamado recursivo con la lista\1er elem
        sacarProducto prodASacar restoDeLista
    | otherwise = -- Idem pero conservando el primer elemento
        primerElemento : sacarProducto prodASacar restoDeLista


-- Ejercicio 2

stockDeProducto :: String -> [(String, Int)] -> Int
stockDeProducto _ [] = 0
stockDeProducto producto ((prod, stock):xs)
    | producto == prod = stock
    | otherwise = stockDeProducto producto xs


-- Ejercicio 3

dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock [] _ = 0
dineroEnStock ((producto, stock):restoStock) ((productoComparacion, precio):restoPrecios)
    | producto == productoComparacion =
        fromIntegral (stock) * precio + dineroEnStock restoStock restoPrecios
    | otherwise = dineroEnStock listaStock restoPrecios
        where listaStock = (producto, stock):restoStock


testDinero :: Float
testDinero = dineroEnStock listaStock listaPrecios
    where
        listaStock = [("Nike",13),("Adidas",2),("Puma",3),("Under Armour",11),("Levi's",2),("Gucci",2),("Zara",10),("H&M",1)]
        listaPrecios = [("Nike", 89.99), ("Adidas", 79.99),("Puma", 69.99), ("Under Armour", 95.50), ("Levi's", 59.99), ("Gucci", 299.99), ("Zara", 45.00), ("H&M", 29.99)]


-- Ejercicio 4

aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
-- |res| = |listaPrecios|
-- Aplica 20% dto. a todo producto con stock mayor a 10
aplicarOferta _ [] = []
aplicarOferta stock ((producto, precio):restoPrecios) =
    (producto, precioFinal) : (aplicarOferta stock restoPrecios)
    where
        precioFinal = getPrecioFinal precio stockProd
        stockProd = stockDeProducto producto stock

getPrecioFinal :: Float -> Int -> Float
getPrecioFinal precioOriginal stock
    | stock > 10 = precioOriginal * 0.80
    | otherwise = precioOriginal

testOferta :: [(String, Float)]
testOferta = aplicarOferta listaStock listaPrecios
    where
        listaStock = [("Nike",13),("Adidas",2),("Puma",3),("Under Armour",11),("Levi's",2),("Gucci",2),("Zara",10),("H&M",1)]
        listaPrecios = [("Nike", 89.99), ("Adidas", 79.99),("Puma", 69.99), ("Under Armour", 95.50), ("Levi's", 59.99), ("Gucci", 299.99), ("Zara", 45.00), ("H&M", 29.99)]


-- -- -- -- -- -- -- -- -- -- 
----- SOPA DE NUMEROS -----
-- -- -- -- -- -- -- -- -- -- 

type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int, Int)
type Camino = [Posicion]

tab :: Tablero
tab = [
    [13, 12, 06, 04],
    [01, 01, 32, 25],
    [09, 02, 14, 07],
    [07, 03, 05, 16],
    [27, 02, 08, 18]
    ]

camino :: Camino
camino = [(1,0), (1,1), (2,1), (3,1), (3,2)]


-- Ejercicio 5

maximo :: Tablero -> Int
maximo [unicaFila] = maximoEnFila unicaFila
maximo (filaActual:restoFilas)
    | maximoEnFila filaActual > maximo restoFilas =
        maximoEnFila filaActual
    | otherwise = maximo restoFilas

maximoEnFila :: Fila -> Int
maximoEnFila [ultimoElemento] = ultimoElemento
maximoEnFila (elemActual:restoElem)
    | elemActual > maximoEnFila restoElem = elemActual
    | otherwise = maximoEnFila restoElem


-- Ejercicio 6

masRepetido :: Tablero -> Int
masRepetido tablero =
    fst ( masOcurrente (
            aparicionesTotal (
                achatarTablero tablero
            )
        )
    )

achatarTablero :: Tablero -> Fila
achatarTablero [] = []
achatarTablero (filaActual:restoDeFilas) =
    filaActual ++ achatarTablero restoDeFilas

cantApariciones :: Int -> Fila -> Int
cantApariciones _ [] = 0
cantApariciones n (elemActual:restoElem)
    | n == elemActual = 1 + cantApariciones n restoElem
    | otherwise = cantApariciones n restoElem

aparicionesPorElemento :: Int -> Fila -> (Int, Int)
aparicionesPorElemento n fila = (n, cantApariciones n fila)

quitarTodos :: Int -> [Int] -> [Int]
quitarTodos _ [] = []
quitarTodos n (x:xs)
    | n == x = quitarTodos n xs
    | otherwise = x : quitarTodos n xs

aparicionesTotal :: Fila -> [(Int, Int)]
aparicionesTotal [] = []
aparicionesTotal (x:xs) =
    aparicionesPorElemento x xs : aparicionesTotal (quitarTodos x xs)

masOcurrente :: [(Int, Int)] -> (Int, Int)
masOcurrente [unicaAparicion] = unicaAparicion
masOcurrente ((elem, aparicionesElemento) : (elem2, aparicionesElemento2) : restoApariciones)
    | aparicionesElemento > aparicionesElemento2 = masOcurrente (actual : restoApariciones)
    | otherwise = masOcurrente (actual2 : restoApariciones)
    where
        actual = (elem, aparicionesElemento)
        actual2 = (elem2, aparicionesElemento2)


-- Ejercicio 7

valoresDeCamino:: Tablero -> Camino -> [Int]
valoresDeCamino _ [] = []
valoresDeCamino tab (posicionActual:restoPosiciones) =
    valorPos tab posicionActual : valoresDeCamino tab restoPosiciones

valorFila :: Tablero -> Posicion -> Fila
valorFila tab (0, _) = head tab
valorFila tab (f, c) = valorFila (tail tab) (f-1, c)

valorCol :: Fila -> Posicion -> Int
valorCol fila (_, 0) = head fila
valorCol fila (f, col) = valorCol (tail fila) (f, col-1)

valorPos :: Tablero -> Posicion -> Int
valorPos tablero posicion = valorCol (valorFila tablero posicion) posicion


-- Ejercicio 8

esCaminoFibo :: [Int] -> Int -> Bool
--  El input [Int] es la salida de valoresDeCamino para
-- algun determinado camino arbitrario. 
--  El entero es un numero a partir del cual iniciar 
-- la sucesion de Fibonacci.
esCaminoFibo [x] n =
    x == fib n

esCaminoFibo (x:xs) n =
    x == fib n
    &&
    esCaminoFibo xs (n+1)

fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)


-- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- - PERFECTOS AMIGOS - -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- --

-- Ejercicio 9: Divisores propios
divisoresPropios :: Int -> [Int]
divisoresPropios 1 = [1]
divisoresPropios n = 1 : obtenerDivisores n 2

obtenerDivisores :: Int -> Int -> [Int]
obtenerDivisores a b
    | a == b = []
    | (mod a b == 0) = b : pasoRecursivo
    | otherwise = pasoRecursivo
    where pasoRecursivo = obtenerDivisores a (b+1)

-- Ejercicio 10: numeros 'amigos'
sonAmigos :: Int -> Int -> Bool
sonAmigos n m =
    sumaDivisores (divisoresPropios n) == m
    &&
    sumaDivisores (divisoresPropios m) == n

sumaDivisores :: [Int] -> Int
sumaDivisores [] = 0
sumaDivisores (x:xs) = x + sumaDivisores xs

--Ejercicio 11
losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos n = primerosPerfectosAux n 0 1

esPerfecto :: Int -> Bool
esPerfecto 1 = False
esPerfecto n = 
    sumaDivisores (divisoresPropios n) == n

primerosPerfectosAux :: Int -> Int -> Int -> [Int]
primerosPerfectosAux cantidad contador _ | cantidad == contador = []
primerosPerfectosAux cantidad contador num
    | esPerfecto num = num : primerosPerfectosAux cantidad (contador+1) (num+1)
    | otherwise = primerosPerfectosAux cantidad contador (num+1)


--Ejercicio 12:
listaDeAmigos :: [Int] -> [(Int, Int)]
listaDeAmigos [ultimoElem] = []
listaDeAmigos (x1:xs) = 
    amigosAux x1 xs ++ listaDeAmigos xs

amigosAux :: Int -> [Int] -> [(Int, Int)]
amigosAux _ [] = []
amigosAux n (x:xs)
    | sonAmigos n x = (n, x) : pasoRecursivo
    | otherwise = pasoRecursivo
    where pasoRecursivo = amigosAux n xs

listaNros :: [Int] -- Para test
listaNros = [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 496, 8128, 945, 36, 48]
{- 
Esta lista tiene 5 pares de nros amigos:

1ro : (220, 284)
2do : (1184, 1210)
3ro : (2620, 2924)
4to : (5020, 5564)
5to : (6232, 6368)

Y ademas contiene los numeros 
[496, 8128, 945, 36, 48],
que no estan relacionados con nada.

-}