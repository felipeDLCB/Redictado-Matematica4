# Guion — Independencia Lineal

## Slide 1 — Título

Buenas. Hoy vemos **Independencia Lineal**, dentro de espacios vectoriales. Es uno de los conceptos centrales del álgebra lineal: lo necesitamos para hablar de bases, dimensión, y para entender cuándo un conjunto de vectores describe un espacio sin redundancia.

→ siguiente

---

## Slide 2 — Motivación

Antes de la definición formal, la idea.

Cuando trabajamos con un espacio vectorial V, buscamos describirlo con la **menor cantidad posible de vectores**. La pregunta natural es: ¿cuándo un vector del conjunto está "de más"?

Veamos un ejemplo concreto. Tomemos el conjunto S formado por (2,1), (1,-2) y (1,3) en R².

Si miramos con atención, notamos que (2,1) es exactamente la suma de los otros dos: (1,-2) + (1,3) = (2,1).

Entonces (2,1) **no aporta información nueva**. Cualquier cosa que pudiéramos generar con los tres vectores, la generamos solo con dos. Es redundante.

Esta noción de "redundancia" es lo que vamos a formalizar.

→ siguiente

---

## Slide 3 — Definición de Dependencia Lineal

Decimos que los vectores v₁, v₂, …, vᵣ son **linealmente dependientes** si existen escalares c₁, c₂, …, cᵣ **no todos nulos** tales que:

c₁v₁ + c₂v₂ + … + cᵣvᵣ = 0

La clave está en "no todos nulos". Existe una combinación lineal **no trivial** que da el vector nulo. Es decir, podemos llegar al cero usando coeficientes que no sean todos cero.

Volviendo al ejemplo anterior: (2,1) - (1,-2) - (1,3) = 0. Coeficientes 1, -1, -1 — no todos nulos. Por lo tanto, el conjunto es linealmente dependiente.

→ siguiente

---

## Slide 4 — Definición de Independencia Lineal

La definición opuesta. Los vectores son **linealmente independientes** si la única forma de obtener el vector nulo como combinación lineal es con **todos los coeficientes iguales a cero**.

Es decir: c₁v₁ + … + cᵣvᵣ = 0 implica c₁ = c₂ = … = cᵣ = 0.

La clave: la **única** combinación que da nulo es la trivial. No hay forma de "cancelar" entre sí los vectores con coeficientes no nulos.

Esta es la propiedad que queremos: ningún vector es redundante, todos aportan algo.

→ siguiente

---

## Slide 5 — Teorema 1: el vector nulo siempre da Dependencia Lineal

Primer teorema. Si el vector nulo está en el conjunto, el conjunto es automáticamente linealmente dependiente.

¿Por qué? Si S = {0, v₁, v₂, …, vᵣ}, podemos armar la combinación:

5·0 + 0·v₁ + 0·v₂ + … + 0·vᵣ = 0

El 5 lo elegí arbitrariamente, podría ser cualquier número no nulo. El punto es: el coeficiente que acompaña al vector nulo puede ser cualquier cosa, porque cualquier número por cero da cero. Entonces siempre tenemos una combinación nula no trivial.

Consecuencia: **el vector nulo nunca puede formar parte de una base**.

→ siguiente

---

## Slide 6 — Teorema 2: Unicidad de la combinación lineal

Si S es linealmente independiente, entonces todo vector en gen(S) se escribe de **una sola manera** como combinación lineal de los vectores de S.

Demostración rápida. Supongamos que un vector v tiene dos representaciones:
- v = a₁v₁ + … + aᵣvᵣ
- v = b₁v₁ + … + bᵣvᵣ

Restando ambas:

0 = (a₁ - b₁)v₁ + … + (aᵣ - bᵣ)vᵣ

Como S es linealmente independiente, la única forma de obtener cero es que todos los coeficientes sean cero: aᵢ - bᵢ = 0 para todo i. Por lo tanto aᵢ = bᵢ. Las representaciones son iguales. ∎

Esto es **fundamental**: la independencia lineal garantiza que las coordenadas de un vector respecto de una base son únicas.

→ siguiente

---

## Slide 7 — Teorema 3: más vectores que la dimensión

Sea V un espacio vectorial con una base de n vectores. Entonces **todo conjunto de m vectores con m > n es linealmente dependiente**.

Intuitivamente: si la dimensión es n, no podemos tener más de n vectores independientes "metidos" en V. Siempre habrá redundancia.

Miremos el dibujo: en R² (dimensión 2), tomemos tres vectores cualesquiera — v₁, v₂, v₃. Por más que los elijamos, **uno de ellos va a poder escribirse como combinación de los otros dos**. Es inevitable.

Este teorema es una herramienta potentísima: contás vectores, contás dimensión, y si hay más vectores que dimensión, **listo, son dependientes**. No hace falta hacer ninguna cuenta.

→ siguiente

---

## Slide 8 — Teorema 4: n vectores Linealmente Independientes en dimensión n

Si dim(V) = n, entonces:
- n vectores linealmente independientes **generan V** (forman base).
- n vectores que generan V son **linealmente independientes** (forman base).

Lo útil: cuando tenés **la cantidad justa** de vectores (igual a la dimensión), basta probar **una sola condición** — independencia o generación — y la otra viene de regalo.

Es decir, ahorra trabajo: en vez de demostrar que es base (las dos cosas), demostrás una y la otra sale por este teorema.

→ siguiente

---

## Slide 9 — Ejercicio 6(b): conjunto Linealmente Independiente

Veámoslo en acción. S = {(1,0,0), (0,1,0), (0,0,1)} en R³.

Planteamos la combinación lineal nula:

c₁(1,0,0) + c₂(0,1,0) + c₃(0,0,1) = (0,0,0)

Sumando componente a componente: (c₁, c₂, c₃) = (0,0,0).

Por igualdad de vectores: c₁ = 0, c₂ = 0, c₃ = 0.

La **única** solución es la trivial. Por lo tanto, S es **linealmente independiente**.

Bonus: como tenemos 3 vectores linealmente independientes en R³ (dimensión 3), por el Teorema 4, S es **base canónica** de R³.

→ siguiente

---

## Slide 10 — Ejercicio 6(a): conjunto Linealmente Dependiente

Ahora S = {(1,0,0), (0,1,0), (0,0,1), (1,2,3)} en R³.

Primera observación, sin hacer cuentas: tenemos **4 vectores en R³** (dimensión 3). Por el Teorema 3, m > n, así que **automáticamente** es linealmente dependiente. Listo.

Pero verifiquémoslo explícitamente. Notemos que:

(1,2,3) = 1·(1,0,0) + 2·(0,1,0) + 3·(0,0,1)

Pasando todo a un lado:

1·(1,0,0) + 2·(0,1,0) + 3·(0,0,1) + (-1)·(1,2,3) = 0

Coeficientes 1, 2, 3, -1 — **no todos nulos**. Entonces S es linealmente dependiente.

→ siguiente

---

## Slide 11 — Cierre

Eso fue todo. Para repasar mentalmente: dependencia lineal = redundancia; independencia lineal = unicidad. Los teoremas nos dan atajos para decidir sin hacer cuentas cuando podemos.

¿Preguntas?
