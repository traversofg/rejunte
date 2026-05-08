-- Ejercicio 1: Fibonacci
{-# LANGUAGE TemplateHaskell #-}
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}

import Data.Fixed (mod')

{-# HLINT ignore "Redundant bracket" #-}
fib :: Integer -> Integer
fib n
  | n == 0 || n == 1 = n
  | otherwise = fib (n - 1) + fib (n - 2)

-- Ejercicio 2: Parte Entera
parteEntera :: Float -> Integer
parteEntera x
  | (x >= 0) && (x < 1) = 0
  | otherwise = 1 + parteEntera (x - 1)

-- Ejercicio 3: esDivisible

{-- Especificacion del problema:

problema esDivisible ( x:N, y:N) : Bool {
    requiere: {True}
    asegura: { res = True if x 'mod' y == 0 else res = False }
}

--}

esDivisible :: Integer -> Integer -> Bool
esDivisible x y
  | x < y = False
  | x == y = True
  | otherwise = esDivisible (x - y) y

-- Ejercicio 4: sumaImpares

{-- Especificacion del problema:

problema sumaImpares (n:N) : N {
    requiere: { n >= 0 }
    asegura: { res = n^2 }
}

--}

sumaImpares :: Integer -> Integer
sumaImpares n
  | n == 1 = 1
  | otherwise = (2 * n - 1) + sumaImpares (n - 1)

-- Ejercicio 5: medioFact
medioFact :: Integer -> Integer
medioFact n
  | n == 0 || n == 1 = 1
  | otherwise = n * medioFact (n - 2)

-- Ejercicio 6: digitosIguales

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

{--
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n
    | n < 10 = True
    | otherwise =
        todosDigitosIguales ( div n 10 ) == uD
    where uD = ultimoDigito n
--}

-- Definimos la función todosDigitosIguales ESTO LO HIZO CHATGPT PORQUE TENGO SUEÑO MAÑANA LO MIRO
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n
  | n < 10 = True -- Si el número tiene un solo dígito, todos los dígitos son iguales
  | otherwise = (ultimoDigito n == ultimoDigito (n `div` 10)) && todosDigitosIguales (n `div` 10)
  where
    -- Función auxiliar para obtener el último dígito de un número
    ultimoDigito x = x `mod` 10

-- uD :: Integer -> Integer
-- uD n = mod n 10

tI :: Integer -> Bool
tI n
  | n < 10 = True
  | otherwise = uD (div n 10) == uD n && tI (div n 10)
  where
    uD n = mod n 10

-- Ejercicio 7 NO ME SALE

cantDigitos :: Integer -> Integer
cantDigitos n
  | n < 10 = 1
  | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i
  | n < 10 = n
  | otherwise = mod (div n (10 ^ ((cantDigitos n) - i))) 10

-- Ejercicio 8

sumaDigitos :: Integer -> Integer
sumaDigitos n
  | n < 10 = n
  | otherwise = ultimoDigito n + sumaDigitos (div n 10)

-- Ejercicio 9 !!!!!

sacarPrimero :: Integer -> Integer -- AUX
sacarPrimero n
  | n < 10 = n -- chanta pero sino se me rompe la otra
  | otherwise = mod n (10 ^ (cantDigitos n - 1))

esCapicua :: Integer -> Bool
esCapicua n
  | n < 10 = True
  | otherwise =
      ultimoDigito n == iesimoDigito n 1 -- comparo extremos
        && esCapicua
          ( sacarPrimero (div n 10) ) -- llamado recursivo sin los extremos


-- Ejercicio 12

raiz2aprox :: Integer -> Float
raiz2aprox n = sucesion (n) - 1
  where
    sucesion n
      | n == 1 = 2
      | otherwise =
          2 + 1 / sucesion (n - 1)

-- Ejercicio 13

{-- Especificación:

Problema dobleSuma ( n:Z, m:Z) : Z
    requiere = { n,m >= 0 }
    asegura = { res = \Sum_{i=1}^{n} \Sum_{j=1}^{m} i^{j} }

no se si hay una mejor forma de especificarlo que escribirlo cual si fuera LaTex

--}

sumatoria :: Integer -> Integer -> Integer
sumatoria n m
  | m == 1 = n
  | otherwise =
      n ^ m + sumatoria n (m - 1)

dobleSuma :: Integer -> Integer -> Integer
dobleSuma 1 1 = 1
dobleSuma n 1 = 12345623465

-- ES MUY TARDE NO PUEDO HACER ESTO AHORA, ME VOY A DORMIR

-- Ejercicio 14

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m =
  (sumatoria q n) * (sumatoria q m)