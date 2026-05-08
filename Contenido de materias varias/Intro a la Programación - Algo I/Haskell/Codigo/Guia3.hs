{-- Introducción a Haskell --}

-- Ejercicio 1
f :: Int -> Int
f 1 = 4
f 4 = 131
f 16 = 16

g :: Int -> Int
g 8 = 16
g 16 = 4
g 131 = 1

h :: Int -> Int -- h = f(g(x))
h n = f (g n)

k :: Int -> Int
k n = g (f n)

-- Ejercicio 2

absoluto :: Int -> Int
absoluto x | x>=0 = x
           | otherwise = -x

maxAbs :: Int -> Int -> Int
maxAbs x y  | absoluto x > absoluto y = absoluto x
            | absoluto x < absoluto y = absoluto y
            | otherwise = absoluto x

maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z   | x > y && x > z = x
                | y > x && y > z = y
                | z > x && z > y = z
                |otherwise = maxAbs otromax z
                where otromax = maxAbs x y
-- debe haber una mejor forma de hacer esto pero no quiero pensar

algunoEsCero :: Float -> Float -> Bool
algunoEsCero x y  | x == 0 || y == 0 = True
                  | otherwise = False

algunoEsCeroPM :: Float -> Float -> Bool
algunoEsCeroPM x 0 = True
algunoEsCeroPM 0 y = True
algunoEsCeroPM x y = False

ambosCero :: Float -> Float -> Bool
ambosCero x y | x == 0 && y == 0 = True
              | otherwise = False

ambosCeroPM :: Float -> Float -> Bool
ambosCeroPM 0 0 = True
ambosCeroPM x y = False

-- Ejercicio 4

prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt (a, b) (c, d) = a*c + b*d

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (a, b) (c, d) | a < c && b < d = True
                        | otherwise = False



distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (a, b) (c, d) = sqrt ( (a+c)^2 + (b+d)^2 )

sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (x, y, z) = x + y + z

sumaSiMultiplo :: Int -> Int -> Int
sumaSiMultiplo x n | mod x n == 0 = x
                   | otherwise = 0

sumaSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumaSoloMultiplos (x, y, z) n = sumaSiMultiplo x n +
                                sumaSiMultiplo y n +
                                sumaSiMultiplo z n

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x, y, z) | mod x 2 == 0 = 1
                       | mod y 2 == 0 = 2
                       | mod z 2 == 0 = 3
                       | otherwise    = 4

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)