module Solucion where

type Ciudad = String
type Duracion = Float
type Vuelo = (Ciudad, Ciudad, Duracion)

type AgenciaDeViajes = [Vuelo]

-- Funciones auxiliares generales

ciudadOrigen :: Vuelo -> Ciudad
ciudadOrigen (origen, _, _) = origen

ciudadDestino :: Vuelo -> Ciudad
ciudadDestino (_, destino, _) = destino

duracionVuelo :: Vuelo -> Duracion
duracionVuelo (_, _, duracion) = duracion

duracionesAgencia :: AgenciaDeViajes -> [Duracion]
duracionesAgencia [] = [0]
duracionesAgencia (d:ds) =
    duracionVuelo d : duracionesAgencia ds

vueloValido :: Vuelo -> Bool
vueloValido (origen, destino, duracion) = 
    origen /= destino && 
    duracion > 0

quitarVuelo :: Vuelo -> AgenciaDeViajes -> AgenciaDeViajes
quitarVuelo _ [] = []
quitarVuelo vuelo (v1:restoVuelos)
    | vuelo == v1 = pasoRecursivo
    | otherwise = v1 : pasoRecursivo
    where
        pasoRecursivo = quitarVuelo vuelo restoVuelos

limpiarRepetidos :: AgenciaDeViajes -> AgenciaDeViajes
limpiarRepetidos [] = []
limpiarRepetidos (v:vs)
    | vueloRepetido v vs = pasoRecursivo
    | otherwise = v : pasoRecursivo
    where
        pasoRecursivo = limpiarRepetidos vs

limpiarRepetidosCiudad :: [Ciudad] -> [Ciudad]
limpiarRepetidosCiudad [] = []
limpiarRepetidosCiudad (c:cs)
    | ciudadRepetida c cs = pasoRecursivo
    | otherwise = c : pasoRecursivo
    where pasoRecursivo = limpiarRepetidosCiudad cs

ciudadRepetida :: Ciudad -> [Ciudad] -> Bool
ciudadRepetida _ [] = False
ciudadRepetida ciudad (c:cs)
    | ciudad == c = True
    | otherwise = ciudadRepetida ciudad cs

longitud :: [t] -> Integer
longitud [] = 0
longitud (_:ts) = 1 + longitud ts


-- EJERCICIO 1
vuelosValidos :: AgenciaDeViajes -> Bool
vuelosValidos [] = True
vuelosValidos (v1:restoVuelos) = 
    not (vueloRepetido v1 restoVuelos) &&
    not (ciudadesRepetidas v1 restoVuelos) &&
    vueloValido v1 &&
    vuelosValidos restoVuelos 

vueloRepetido :: Vuelo -> AgenciaDeViajes -> Bool
vueloRepetido _ [] = False
vueloRepetido vuelo (v1:restoVuelos)
    | vuelo == v1 = True
    | otherwise = vueloRepetido vuelo restoVuelos

ciudadesRepetidas :: Vuelo -> AgenciaDeViajes -> Bool -- feo nombre pero qcy
ciudadesRepetidas _ [] = False
ciudadesRepetidas vuelo (v1:restoVuelos)
    | (ciudadOrigen vuelo == ciudadOrigen v1) &&
      (ciudadDestino vuelo == ciudadDestino v1) &&
      (duracionVuelo vuelo /= duracionVuelo v1) = True
    | otherwise = ciudadesRepetidas vuelo restoVuelos


-- EJERCICIO 2 -- FALTAN CASOS DE TEST
ciudadesConectadas :: AgenciaDeViajes -> Ciudad -> [Ciudad]
ciudadesConectadas vuelos ciudad = 
    limpiarRepetidosCiudad ( conexionesDesde ++ conexionesHacia )
    where
        conexionesDesde = ciudadesConectadasDesde vuelos ciudad
        conexionesHacia = ciudadesConectadasHacia vuelos ciudad


ciudadesConectadasHacia :: AgenciaDeViajes -> Ciudad -> [Ciudad] -- destino vuelo == ciudad
ciudadesConectadasHacia [] _ = []
ciudadesConectadasHacia (vuelo:restoVuelos) ciudad
    | ciudadDestino vuelo == ciudad = ciudadOrigen vuelo : pasoRecursivo
    | otherwise = pasoRecursivo
    where
        pasoRecursivo = ciudadesConectadasHacia restoVuelos ciudad


ciudadesConectadasDesde :: AgenciaDeViajes -> Ciudad -> [Ciudad] -- origen vuelo == ciudad
ciudadesConectadasDesde [] _ = []
ciudadesConectadasDesde (vuelo:restoVuelos) ciudad
    | ciudadOrigen vuelo == ciudad = ciudadDestino vuelo : pasoRecursivo
    | otherwise = pasoRecursivo
    where
        pasoRecursivo = ciudadesConectadasDesde restoVuelos ciudad



-- EJERCICIO 3
modernizarFlota :: AgenciaDeViajes -> AgenciaDeViajes
modernizarFlota [] = []
modernizarFlota (v:vs) =
    (origen v, destino v, 0.9 * duracion v) : modernizarFlota vs -- Borrar y escribir el código correcto
    where
        origen = ciudadOrigen 
        destino = ciudadDestino 
        duracion  = duracionVuelo


-- EJERCICIO 4
ciudadMasConectada :: AgenciaDeViajes -> Ciudad
ciudadMasConectada agencia = 
    maxConexiones (
        conexionesPorCiudad (ciudades agencia) agencia
    ) 
    where ciudades = ciudadesEnLaAgencia

maxConexiones :: [(Ciudad, Integer)] ->  Ciudad
maxConexiones [(ciudad, _)] = ciudad
maxConexiones (t1:t2:ts) -- t por tupla jejo
    | snd t1 > snd t2 = maxConexiones (t1:ts)
    | otherwise = maxConexiones (t2:ts)

ciudadesEnLaAgencia :: AgenciaDeViajes -> [Ciudad]
ciudadesEnLaAgencia [] = []
ciudadesEnLaAgencia (v:vs) = limpiarRepetidosCiudad (
    ( origen v : [destino v] ) ++ ciudadesEnLaAgencia vs
    )
    where
        origen = ciudadOrigen 
        destino = ciudadDestino 

conexionesPorCiudad :: [Ciudad] -> AgenciaDeViajes -> [(Ciudad, Integer)]
conexionesPorCiudad [] _ = []
conexionesPorCiudad (ciudad:cs) agencia =
    ( ciudad, cant_conexiones agencia ciudad ) : conexionesPorCiudad cs agencia
    where
        cant_conexiones a c = longitud ( ciudadesConectadas a c )

-- EJERCICIO 5
sePuedeLlegar :: AgenciaDeViajes -> Ciudad -> Ciudad -> Bool
sePuedeLlegar vuelos origen destino = True -- Borrar y escribir el código correcto


-- EJERCICIO 6
duracionDelCaminoMasRapido :: AgenciaDeViajes -> Ciudad -> Ciudad -> Duracion
duracionDelCaminoMasRapido _ _ _ = 10.0 -- Borrar y escribir el código correcto



-- EJERCICIO 7
puedoVolverAOrigen :: AgenciaDeViajes -> Ciudad ->  Bool
puedoVolverAOrigen vuelos origen = True -- Borrar y escribir el código correcto