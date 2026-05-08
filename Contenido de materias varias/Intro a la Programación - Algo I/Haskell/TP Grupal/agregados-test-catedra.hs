import Test.HUnit
import Data.List
import Solucion
-- No está permitido agregar nuevos imports.

-- AL FINAL DE TODO ESTAN LAS LISTAS Y BOLUDECES QUE VAYA
-- AGREGANDO PARA HACER NUEVOS CASOS DE TEST


runCatedraTests = runTestTT allTests

allTests = test [
    "vuelosValidos" ~: testsEjvuelosValidos,
    "ciudadesConectadas" ~: testsEjciudadesConectadas,
    -- "modernizarFlota" ~: testsEjmodernizarFlota,
    "ciudadMasConectada" ~: testsEjciudadMasConectada,
    "sePuedeLlegar" ~: testsEjsePuedeLlegar,
    "duracionDelCaminoMasRapido" ~: testsEjduracionDelCaminoMasRapido,
    "puedoVolverAOrigen" ~: testsEjpuedoVolverAOrigen
    ]

-- corregir los tests si es necesario con las funciones extras que se encuentran al final del archivo

-- Tests Ejercio 1

testsEjvuelosValidos = test [
    "vuelos válido con un elemento" ~: vuelosValidos [("BsAs", "Rosario", 5.0)] ~?= True,
    "vuelos validos con varios elementos" ~: vuelosValidos ejemploVuelosValidos ~?= True,
    "vuelos validos con vuelos inversos" ~: vuelosValidos vuelosValidosInversos ~?= True,
    "vuelos invalidos con varios elementos" ~: vuelosValidos vuelosInvalidosPorCiudades ~?= False,
    "vuelos invalidos por ciudades iguales" ~: vuelosValidos vuelosInvalidosPorCiudades ~?= False,
    "vuelos invalidos por vuelo repetido" ~: vuelosValidos vuelosInvalidosPorRepeticion ~?= False,
    "vuelos invalidos por duracion negativa" ~: vuelosValidos vuelosInvalidoDuracionNeg ~?= False
    ]

-- Tests Ejercicio 2
{-
testsEjciudadesConectadas = test [
    "ciudad conectada con un elemento" ~: ciudadesConectadas  [("BsAs", "Rosario", 5.0)] "Rosario" ~?= ["BsAs"],
    "ciudad conectada con varios elementos" ~: expectPermutacion (ciudadesConectadas ejemploVuelosValidos "Buenos Aires") ["Berlin", "Madrid"],
    "ciudad conectada solo x llegada" ~: expectPermutacion (ciudadesConectadas ejemploVuelosValidos "Roma") ["Paris", "Berlin"],
    "ciudad conectada solo x salida" ~: expectPermutacion (ciudadesConectadas ejemploVuelosValidos "Paris") ["Madrid", "Roma"]
    ]
-}

testsEjciudadesConectadas = test [
    "Ciudad conectada con un vuelo hacia ella" ~: ciudadesConectadas [("BsAs", "Rosario", 5.0)] "Rosario" ~?= ["BsAs"],
    "Ciudad conectada con vuelos múltiples desde ella" ~: expectPermutacion (ciudadesConectadas ejemploVuelosValidosLarga "Buenos Aires") ["Madrid", "Berlin", "Nueva York", "Sídney"],
    "Ciudad conectada con vuelos múltiples hacia ella" ~: expectPermutacion (ciudadesConectadas ejemploVuelosValidosLarga "Madrid") ["Buenos Aires", "Paris", "Londres"],
    "Ciudad con vuelo de ida y vuelta" ~: expectPermutacion (ciudadesConectadas ejemploVuelosValidosLarga "Tokio") ["Los Angeles", "Seúl"],
    "Ciudad conectada sin vuelos directos" ~: expectPermutacion (ciudadesConectadas ejemploVuelosValidosLarga "Roma") ["Paris", "Berlin", "Londres"],
    "Ciudad sin vuelos hacia ni desde ella" ~: ciudadesConectadas ejemploVuelosValidosLarga "Lisboa" ~?= []
    ]

-- Tests Ejercicio 3
testsEjmodernizarFlota = test [
    "flota modernizada con un elemento" ~: modernizarFlota [("BsAs", "Rosario", 10.0)] ~?= [("BsAs", "Rosario", 9.0)],

    -- Flota modernizada con varios elementos, faltaría tener en cuenta el margen de error
    "flota modernizada con varios elementos" ~: expectlistProximity
                                                (duracionesAgencia (modernizarFlota ejemploVuelosValidos))
                                                (multiplicarLista 0.9 (duracionesAgencia ejemploVuelosValidos))                             
    ]

-- Tests Ejercicio 4
testsEjciudadMasConectada = test [
    "ciudad Mas conectada que aparece dos veces" ~: ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Rosario", "Córdoba", 7.0)] ~?= "Rosario",

    "ciudad mas conectada con varios elementos" ~: expectAny
                                                    (ciudadMasConectada ejemploVuelosValidos)
                                                    (ciudadesEnLaAgencia ejemploVuelosValidos),

    "ciudad mas conectada con MAS elementos" ~: expectAny
                                                    (ciudadMasConectada ejemploVuelosValidosLarga)
                                                    ["Buenos Aires", "Londres"]
    ]

-- Tests Ejercicio 5
testsEjsePuedeLlegar = test [
    "Se puede llegar caso verdadero con una escala" ~: sePuedeLlegar [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" "Córdoba" ~?= True
    ]

testsEjduracionDelCaminoMasRapido = test [
    "duración del camino más rápido con una escala" ~: duracionDelCaminoMasRapido [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" "Córdoba" ~?= 10.0
    ]

testsEjpuedoVolverAOrigen = test [
        "puedo volver a origen caso verdadero con una escala" ~: puedoVolverAOrigen [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" ~?= True
    ]



-- Funciones extras

-- margetFloat(): Float
-- asegura: res es igual a 0.00001
margenFloat = 0.00001

-- expectAny (actual: a, expected: [a]): Test
-- asegura: res es un Test Verdadero si y sólo si actual pertenece a la lista expected
expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- expectlistProximity (actual: [Float], expected: [Float]): Test
-- asegura: res es un Test Verdadero si y sólo si:
--                  |actual| = |expected|
--                  para todo i entero tal que 0<=i<|actual|, |actual[i] - expected[i]| < margenFloat()
expectlistProximity:: [Float] -> [Float] -> Test
expectlistProximity actual expected = esParecidoLista actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esParecidoLista :: [Float] -> [Float] -> Bool
esParecidoLista actual expected = (length actual) == (length expected) && (esParecidoUnaAUno actual expected)

esParecidoUnaAUno :: [Float] -> [Float] -> Bool
esParecidoUnaAUno [] [] = True
esParecidoUnaAUno (x:xs) (y:ys) = (aproximado x y) && (esParecidoUnaAUno xs ys)

aproximado :: Float -> Float -> Bool
aproximado x y = abs (x - y) < margenFloat


-- expectAnyTuplaAprox (actual: CharxFloat, expected: [CharxFloat]): Test
-- asegura: res un Test Verdadero si y sólo si:
--                  para algun i entero tal que 0<=i<|expected|,
--                         (fst expected[i]) == (fst actual) && |(snd expected[i]) - (snd actual)| < margenFloat()

expectAnyTuplaAprox :: (Char, Float) -> [(Char, Float)] -> Test
expectAnyTuplaAprox actual expected = elemAproxTupla actual expected ~? ("expected any of: " ++ show expected ++ "\nbut got: " ++ show actual)

elemAproxTupla :: (Char, Float) -> [(Char, Float)] -> Bool
elemAproxTupla _ [] = False
elemAproxTupla (ac,af) ((bc,bf):bs) = sonAprox || (elemAproxTupla (ac,af) bs)
    where sonAprox = (ac == bc) && (aproximado af bf)



-- expectPermutacion (actual: [T], expected[T]) : Test
-- asegura: res es un Test Verdadero si y sólo si:
--            para todo elemento e de tipo T, #Apariciones(actual, e) = #Apariciones(expected, e)

expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)

multiplicarLista :: Float -> [Float] -> [Float]
multiplicarLista _ [] = []
multiplicarLista n (x:xs) = n*x : multiplicarLista n xs



-- Casos de test agregados (no de catedra)

ejemploVuelosValidos :: AgenciaDeViajes
ejemploVuelosValidos = 
    [ ("Buenos Aires", "Madrid", 12.0)
    , ("Paris", "Madrid", 2.5)
    , ("Paris", "Roma", 3.0)
    , ("Berlin", "Roma", 2.8)
    , ("Berlin", "Buenos Aires", 15.0)
    ]

ejemploVuelosValidosLarga :: AgenciaDeViajes
ejemploVuelosValidosLarga = 
    [ ("Buenos Aires", "Madrid", 12.0)
    , ("Paris", "Madrid", 2.5)
    , ("Paris", "Roma", 3.0)
    , ("Berlin", "Roma", 2.8)
    , ("Berlin", "Buenos Aires", 15.0)
    , ("Buenos Aires", "Nueva York", 10.0)
    , ("Nueva York", "Los Angeles", 6)
    , ("Los Angeles", "Tokio", 11.5)
    , ("Tokio", "Seúl", 2)
    , ("Seúl", "Sídney", 9.5)
    , ("Sídney", "Buenos Aires", 13)
    , ("Londres", "Berlin", 1.5)
    , ("Londres", "Paris", 2.0)
    , ("Roma", "Londres", 2.3)
    , ("Madrid", "Londres", 1.7)
    ]

    
vuelosInvalidosPorCiudades :: AgenciaDeViajes
vuelosInvalidosPorCiudades = 
    [ ("Buenos Aires", "Madrid", 12.0)
    , ("Paris", "Roma", 2.0)  -- Válido pero con diferente duración, lo que lo invalida
    , ("Paris", "Roma", 3.0)
    , ("Madrid", "Paris", 2.5)
    , ("Roma", "Berlin", 2.8)
    , ("Berlin", "Buenos Aires", 15.0)
    ]

vuelosInvalidosPorRepeticion :: AgenciaDeViajes
vuelosInvalidosPorRepeticion = 
    [ ("Buenos Aires", "Madrid", 12.0)
    , ("Madrid", "Paris", 2.5)
    , ("Paris", "Roma", 3.0)
    , ("Roma", "Berlin", 2.8)
    , ("Berlin", "Buenos Aires", 15.0)
    , ("Madrid", "Paris", 2.5)  -- Vuelo repetido (mismo origen, destino y duración)
    ]

vuelosInvalidoDuracionNeg :: AgenciaDeViajes
vuelosInvalidoDuracionNeg =
    [ ("Buenos Aires", "Madrid", 12.0)
    , ("Madrid", "Paris", 2.5)
    , ("Paris", "Roma", -3.0)  -- Vuelo inválido por duración negativa
    , ("Roma", "Berlin", 2.8)
    , ("Berlin", "Buenos Aires", 15.0)
    ]

vuelosValidosInversos :: AgenciaDeViajes
vuelosValidosInversos = 
    [ ("Buenos Aires", "Madrid", 12.0)
    , ("Madrid", "Buenos Aires", 12.0)  -- Inverso al primer vuelo, pero debería ser válido
    ]