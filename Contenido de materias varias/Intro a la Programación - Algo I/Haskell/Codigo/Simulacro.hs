module Simulacro where

{- ----------------------
SIMULACRO PARCIAL HASKELL
---------------------- -}
type Persona = String
type Relacion = (Persona, Persona)

relacionesValidas :: [Relacion] -> Bool
relacionesValidas [] = True
relacionesValidas (relacionActual:restoDeRelaciones) =
    not (mismaPersona relacionActual) &&
    not (relacionRepetida relacionActual restoDeRelaciones) &&
    pasoRecursivo
    where pasoRecursivo = relacionesValidas restoDeRelaciones


mismaPersona :: Relacion -> Bool
mismaPersona (a,b) = a == b


relacionRepetida :: Relacion -> [Relacion] -> Bool
relacionRepetida _ [] = False
relacionRepetida a (b:resto) =
    mismaRelacion a b || relacionRepetida a resto
    where mismaRelacion (a,b) (c,d) =
            ( a == c && b == d ) || ( a == d && b == c )


-- Pequeños casos de test --

testRelacionesValidasUno :: Bool -- Esperado: False
testRelacionesValidasUno = relacionesValidas relacionesUno

relacionesUno :: [Relacion]
relacionesUno = [("Gabriela", "Jose"),
                 ("Maria", "Maria"),
                 ("Maria", "Jose"),
                 ("Gabriela", "Carlos"),
                 ("Gabriela", "Carlos"),
                 ("Carlos", "Carlos"),
                 ("Gabriela", "Gabriela"),
                 ("Jose", "Maria"),
                 ("Maria", "Gabriela"),
                 ("Maria", "Carlos")]


testRelacionesValidasDos :: Bool -- Esperado: True
testRelacionesValidasDos = relacionesValidas relacionesDos

relacionesDos :: [Relacion]
relacionesDos = [("Gabriela", "Jose"),
                 ("Gabriela", "Maria"),
                 ("Gabriela", "Carlos"),
                 ("Maria", "Jose"),
                 ("Maria", "Carlos"),
                 ("Jose", "Carlos")]

-- -- -- -- -- -- -- -- -- -- -- -- -- --
{- Problema Personas: la idea es generar una lista con todos los nombres
que aparecen en una lista de relaciones (la cual se asume que ya pasó el filtro
de relacionesValidas), pero sin repetir nombres, es decir que cada nombre aparece
una sola vez.

    Estrategia para atacarlo: me armo primero una lista a lo bruto con todos los
nombres, sin fijarme si estan o no repetidos, para despues con una funcion (o mas)
auxiliar, eliminar los repetidos.
-}

personas :: [Relacion] -> [Persona]
personas relaciones = quitarRepetidos ( personasRepe relaciones )

personasRepe :: [Relacion] -> [Persona]
personasRepe [] = []
personasRepe (rs:restoRs) = fst rs : snd rs : personasRepe restoRs

quitarRepetidos :: [Persona] -> [Persona]
quitarRepetidos [] = []
quitarRepetidos (x:xs) = x: quitarRepetidos (quitarTodos x xs)

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos elem (x:xs)
    | elem == x = quitarTodos elem xs
    | otherwise = x:quitarTodos elem xs

-- -- -- -- -- -- -- -- -- -- -- -- -- --
{- Problema amigosDe: armar una lista de personas que son "amigos de"
una cierta persona. Esto sería, dado un nombre, dar una lista con los
nombres de todos aquellos que aparezcan en una tupla con esta persona,
dentro de una lista que se asume pasó por relacionesValidas.

    Estrategia: con la misma idea que el ej anterior, puedo armar una
lista que contenga todos los nombres, incluyendo repeticiones, que
acompañan a "persona" en la lista de relaciones, para luego ocuparme
de limpiarla y que quede una aparicion de cada nombre.
    Esta lista con nombres repetidos la puedo armar recorriendo de
forma recursiva la lista "relaciones" y cada vez que una de las compo-
nentes coincida con "persona", me guardo la otra componente.

    A ver si sale con esto che.
    ----------------------------
    Update: fue muchisimo mas facil de lo que pensaba que iba a ser.
No hacía falta limpiar los repetidos pq la lista ya pasó por relVal.
-}

amigosDe :: Persona -> [Relacion] -> [Persona]
amigosDe _ [] = []
amigosDe persona ((p1, p2):otrasAmistades)
    | p1 == persona = p2 : pasoRecursivo
    | p2 == persona = p1 : pasoRecursivo
    | otherwise = pasoRecursivo
    where pasoRecursivo = amigosDe persona otrasAmistades

-- -- -- -- -- -- -- -- -- -- -- -- -- --
{- Problema  personaConMasAmigos: devuelvo el string (nombre / persona)
que más veces aparece en las tuplas de "relaciones". En caso de empate,
devuelve cualquiera de los que estan empatados.

    Estrategia: ni la mas putisima idea.

    Quizas primero una funcion que usando la funcion "personas", agarre
cada uno de esos nombres y lo pase por amigosDe, deolviendo una tupla
con el nombre y un Int representando la longitud de la lista amigosDe
-}


personaConMasAmigos :: [Relacion] -> Persona
personaConMasAmigos relaciones =
    maxAmistades ( cantidadAmigos ( personas relaciones ) relaciones )

cantidadAmigos :: [Persona] -> [Relacion] -> [(Persona, Int)]
cantidadAmigos [] _ = []
cantidadAmigos (p1:ps) relaciones =
    (p1, longitud (amigosDe p1 relaciones)) : pasoRecursivo
    where pasoRecursivo = cantidadAmigos ps relaciones

maxAmistades :: [(Persona, Int)] -> Persona
maxAmistades [(ultimaPersona, _)] = ultimaPersona
maxAmistades ((p1, c1):(p2,c2):otrasPersonas)
    | c1 > c2 = maxAmistades ((p1, c1):otrasPersonas)
    | otherwise = maxAmistades ((p2, c2):otrasPersonas)

longitud :: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs