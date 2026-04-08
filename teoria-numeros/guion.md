# Guion de Presentacion — Numeros Racionales (Teoria de Numeros)

> **Nota para los integrantes:** Entre corchetes `[Slide X]` se indica cuando avanzar la presentacion. Las instrucciones en *cursiva* describen lo que se ve en pantalla. El texto normal es lo que hay que decir (parafrasear, no leer textualmente).

---

## INTEGRANTE 1 — Introduccion + Racionales

### Slide 1 — Titulo

*Se ve: "Numeros Racionales" con subtitulo "Propiedades y Demostraciones", linea decorativa, y "Matematica 4 — Teoria de Numeros — 2025".*

> Buenas, vamos a presentar dos ejercicios del Trabajo Practico de Teoria de Numeros. Ambos tienen que ver con propiedades fundamentales de los numeros racionales: la clausura de operaciones y la densidad. Los vamos a resolver paso a paso.

**[Avanzar]**

---

### Slide 2 — Definicion de numero racional

*Se ve: la definicion formal Q = {a/b : a ∈ Z, b ∈ Z, b ≠ 0}.*

> Antes de meternos en las demostraciones, repasemos que es un numero racional. Formalmente, el conjunto Q esta formado por todos los numeros que se pueden expresar como el cociente de dos enteros, con la condicion de que el denominador sea distinto de cero.

**[Avanzar]** *(aparece la explicacion en texto)*

> Es decir: si puedo escribir un numero como a sobre b, con a y b enteros y b distinto de cero, entonces ese numero es racional.

**[Avanzar]** *(aparecen los ejemplos: 3/4, -7/2, 0/5 = 0, 8/1 = 8)*

> Aca tenemos algunos ejemplos. Fijense que el 0 es racional porque se puede escribir como 0 sobre 5, y el 8 tambien es racional porque es 8 sobre 1. Cualquier entero es racional.

**[Avanzar]**

---

### Slide 3 — Z ⊂ Q

*Se ve: la inclusion Z ⊂ Q, luego la justificacion.*

> Justamente eso nos lleva a una propiedad importante: los enteros estan contenidos dentro de los racionales. ¿Por que? Porque todo entero n se puede escribir como n sobre 1, que es un cociente de enteros con denominador distinto de cero.

**[Avanzar]** *(aparecen las conversiones: 5 = 5/1, -3 = -3/1, 0 = 0/1)*

> Aca lo ven con ejemplos concretos: el 5 es 5/1, el -3 es -3/1, el 0 es 0/1. Todos son racionales.

**[Avanzar]** *(aparece el diagrama de Venn con Z dentro de Q)*

> El diagrama de Venn lo muestra claramente: Z es un subconjunto de Q. Todo entero es racional, pero no todo racional es entero — por ejemplo, 3/4 no es entero.

**[Avanzar]**

---

### Slide 4 — Operaciones entre racionales

*Se ve: las 4 operaciones (suma, resta, producto, inverso) en una grilla 2x2.*

> Ahora repasemos como se operan los racionales. Tenemos las cuatro operaciones fundamentales:
>
> La **suma** de a/b mas c/d se hace con denominador comun: es (ad + bc) sobre bd.
> La **resta** es lo mismo pero con un menos: (ad - bc) sobre bd.
> El **producto** es directo: se multiplican numeradores y denominadores, ac sobre bd.
> Y el **inverso** de a/b es simplemente b sobre a, siempre que a no sea cero.

**[Avanzar]** *(aparece el texto clave sobre clausura)*

> Lo importante aca — y esto es lo que vamos a demostrar formalmente despues — es que el resultado de cada una de estas operaciones sigue siendo un cociente de enteros. Es decir, las operaciones son **cerradas** en Q: si empezas con racionales, terminas con racionales.

**[Avanzar]**

---

## INTEGRANTE 2 — Ejercicio 10 (Densidad de Q)

### Slide 5 — Seccion: Ejercicio 10

*Se ve: titulo "Ejercicio 10" con subtitulo "Densidad de los numeros racionales".*

> Gracias. Ahora vamos a ver el Ejercicio 10, que trata sobre una propiedad muy interesante de los racionales: la **densidad**.

**[Avanzar]**

---

### Slide 6 — ¿Que es la densidad de Q?

*Se ve: explicacion de la densidad, luego contraste con los enteros y una recta numerica.*

> ¿Que significa que Q sea denso? Significa que entre cualquier par de numeros racionales, siempre podemos encontrar otro numero racional. No importa cuan cerca esten los dos numeros: siempre hay uno en el medio.

**[Avanzar]** *(aparece el contraste con los enteros y la recta numerica)*

> Fijense que esta propiedad NO la tienen los enteros. Si tomo el 3 y el 4, ¿hay algun entero entre medio? No, no hay ninguno. Pero en los racionales si: entre 3 y 4 tengo el 3.5, entre 3 y 3.5 tengo el 3.25, y asi infinitamente. Eso es la densidad.

**[Avanzar]**

---

### Slide 7 — Enunciado formal

*Se ve: "Dados a, b ∈ Q con a < b, demostrar que existe x ∈ Q tal que a < x < b", luego la idea clave.*

> El enunciado formal es este: dados dos racionales a y b con a menor que b, hay que demostrar que existe un racional x que esta estrictamente entre ambos.

**[Avanzar]** *(aparece x = (a+b)/2 y la explicacion)*

> La idea clave de la demostracion es usar el **promedio**. Si tomamos x igual a (a + b) sobre 2, tenemos un candidato natural. ¿Por que? Porque el promedio de dos numeros siempre cae entre ambos, y ademas — como vamos a ver — el promedio de dos racionales es racional.

**[Avanzar]**

---

### Slide 8 — Demostracion paso a paso

*Se ve: los 4 pasos de la demostracion apareciendo uno a uno.*

> Vamos con la demostracion formal.
>
> **Paso 1**: Partimos de la hipotesis. Tenemos a y b racionales, con a menor que b.

**[Avanzar]**

> **Paso 2**: Definimos nuestro candidato: x = (a + b) / 2.

**[Avanzar]**

> **Paso 3**: Tenemos que verificar que x es racional. Aca es donde usamos lo que se demuestra en el Ejercicio 9. Como a y b son racionales, su suma a + b tambien es racional — eso es la clausura de la suma. Y luego, multiplicar (a+b) por 1/2 da un racional — eso es la clausura del producto. Entonces x pertenece a Q.

**[Avanzar]**

> **Paso 4**: Falta probar que a < x < b. Veamos:
>
> Como a es menor que b, si sumo a de ambos lados tengo 2a < a + b, y dividiendo por 2 queda a < (a+b)/2 = x.
>
> De la misma forma, como a < b, sumo b de ambos lados: a + b < 2b, divido por 2, y queda x = (a+b)/2 < b.
>
> Combinando ambas: a < x < b, con x racional. Queda demostrado.

**[Avanzar]** *(aparece el Q.E.D.)*

**[Avanzar]**

---

### Slide 9 — Visualizacion en recta numerica

*Se ve: recta numerica con puntos a y b, luego aparecen puntos medios sucesivos.*

> Para que se vea de forma mas intuitiva, veamos la densidad en una recta numerica. Aca tenemos a y b.

**[Avanzar]** *(aparece x1, el primer punto medio)*

> El punto medio x1 cae justo en la mitad.

**[Avanzar]** *(aparecen x2 y x3)*

> Pero ahora entre a y x1 hay otro punto medio x2, y entre x1 y b hay otro, x3. Y esto no termina nunca.

**[Avanzar]** *(aparecen muchos mas puntos llenando el intervalo)*

> Si seguimos, el intervalo se va llenando de puntos racionales. Siempre podemos encontrar otro mas. El proceso es infinito: no existe un par de racionales que sean "vecinos" sin nada entre medio.

**[Avanzar]**

---

## INTEGRANTE 3 — Ejercicio 9 (Clausura) + Cierre

### Slide 10 — Seccion: Ejercicio 9

*Se ve: titulo "Ejercicio 9 — Adicionales" con subtitulo "Clausura de operaciones en Q".*

> Gracias. Ahora vamos a demostrar formalmente lo que ya se uso en el ejercicio anterior: que los numeros racionales son cerrados bajo las operaciones basicas. Este es el Ejercicio 9.

**[Avanzar]**

---

### Slide 11 — Enunciado del Ejercicio 9

*Se ve: "Sean u y v numeros racionales. Probar que: (a) u+v ∈ Q y u-v ∈ Q, (b) u·v ∈ Q, (c) Si u ≠ 0, u⁻¹ ∈ Q".*

> El enunciado nos pide probar tres cosas: primero, que la suma y la resta de dos racionales es racional. Segundo, que el producto de dos racionales es racional. Y tercero, que el inverso multiplicativo de un racional no nulo tambien es racional.
>
> La estrategia es la misma en los tres casos: expresamos los racionales como cocientes de enteros, operamos, y verificamos que el resultado sigue siendo un cociente de enteros con denominador distinto de cero.

**[Avanzar]**

---

### Slide 12 — Ejercicio 9 (a): u + v ∈ Q y u - v ∈ Q

*Se ve: hipotesis, luego el calculo de la suma paso a paso.*

> Arrancamos con el inciso a). Sean u = a/b y v = c/d, con a, c enteros y b, d enteros distintos de cero. Esas son nuestras hipotesis.

**[Avanzar]** *(aparece el calculo de la suma)*

> Calculamos u + v: es a/b mas c/d, que con denominador comun da (ad + bc) sobre bd.

**[Avanzar]** *(aparece la verificacion)*

> Ahora verificamos que el resultado es racional:
> - El numerador ad + bc es entero, porque es suma y producto de enteros.
> - El denominador bd es entero, porque es producto de enteros.
> - Y bd es distinto de cero, porque b y d son ambos distintos de cero.
>
> Entonces u + v es un cociente de enteros con denominador no nulo. Es racional.

**[Avanzar]** *(aparece el check de la suma)*

**[Avanzar]** *(se limpia y aparece la resta)*

> Para la resta es analogo. u - v = (ad - bc) sobre bd. El numerador ad - bc es entero por la misma razon, y el denominador bd sigue siendo distinto de cero.

**[Avanzar]** *(aparece la verificacion y la conclusion de la resta)*

> Queda demostrado: tanto u + v como u - v pertenecen a Q.

**[Avanzar]** *(aparece el Q.E.D.)*

**[Avanzar]**

---

### Slide 13 — Ejercicio 9 (b): u · v ∈ Q

*Se ve: hipotesis compacta, luego el calculo del producto.*

> Inciso b). Mismas hipotesis: u = a/b, v = c/d.

**[Avanzar]** *(aparece el calculo del producto)*

> El producto es directo: u por v es (a/b) por (c/d), que da ac sobre bd.

**[Avanzar]** *(aparece la verificacion)*

> Verificamos:
> - ac es entero, porque el producto de enteros es cerrado en Z.
> - bd es entero, por la misma razon.
> - bd es distinto de cero, porque b y d son distintos de cero.
>
> Entonces u · v es racional.

**[Avanzar]** *(aparece Q.E.D.)*

**[Avanzar]**

---

### Slide 14 — Ejercicio 9 (c): Si u ≠ 0, u⁻¹ ∈ Q

*Se ve: hipotesis con la condicion u ≠ 0 implicando a ≠ 0.*

> Inciso c). Aca tenemos una hipotesis adicional: u tiene que ser distinto de cero. ¿Por que? Porque si u = a/b y u es distinto de cero, entonces a tiene que ser distinto de cero. Si a fuera cero, tendriamos u = 0/b = 0, contradiccion.

**[Avanzar]** *(aparece el calculo del inverso)*

> El inverso multiplicativo de u = a/b es simplemente b/a. Le damos vuelta la fraccion.

**[Avanzar]** *(aparece la verificacion)*

> Verificamos que b/a es racional:
> - b es entero — era el denominador original.
> - a es entero — era el numerador original.
> - a es distinto de cero — por la hipotesis de que u no es cero.
>
> Entonces u⁻¹ = b/a pertenece a Q.

**[Avanzar]** *(aparece la comprobacion: u · u⁻¹ = (a/b)(b/a) = ab/ba = 1)*

> Y como comprobacion, verificamos que u por su inverso da 1: (a/b) por (b/a) es ab sobre ba, que es 1. Perfecto.

**[Avanzar]** *(aparece Q.E.D.)*

**[Avanzar]**

---

### Slide 15 — Resumen Ejercicio 9

*Se ve: las 4 propiedades con checks animados, y la conclusion sobre estructura de cuerpo.*

> Resumiendo el Ejercicio 9: demostramos que Q es cerrado bajo las cuatro operaciones fundamentales. La suma, la resta, el producto, y el inverso de racionales siempre dan racionales.

**[Avanzar]** *(aparecen los checks y la conclusion)*

> Esto es lo que en algebra se llama tener **estructura de cuerpo**. Q no es solamente un conjunto de numeros: es un cuerpo, donde podemos operar libremente sin salirnos del conjunto.

**[Avanzar]**

---

### Slide 16 — Conclusiones

*Se ve: bullets con los puntos clave.*

> Para cerrar, repasemos lo que vimos:
>
> Primero, Q es cerrado bajo suma, resta, multiplicacion e inverso — eso fue el Ejercicio 9, y nos dice que Q tiene estructura de cuerpo.
>
> Segundo, Q es denso: entre dos racionales cualesquiera siempre existe otro racional — eso fue el Ejercicio 10.
>
> Estas dos propiedades son fundamentales en la teoria de numeros y son la base para entender despues la construccion de los numeros reales.

**[Avanzar]**

*Se ve: "¡Gracias!"*

> Eso es todo. ¿Alguna pregunta?
