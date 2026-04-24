# Guion de Presentacion — Relaciones de Equivalencia

> **Nota:** Entre corchetes `[Avanzar]` se indica cuando avanzar la presentacion. Las instrucciones en *cursiva* describen lo que se ve en pantalla. El texto normal es lo que hay que decir (parafrasear, no leer textualmente).

---

## Slide 1 — Titulo

*Se ve: "Relaciones de Equivalencia" con subtitulo "Clases de equivalencia y Particiones".*

> Buenas. En esta presentacion vamos a hablar sobre las relaciones de equivalencia. Primero repasamos las propiedades que las definen, despues vemos que son las clases de equivalencia, el conjunto cociente y las particiones. Y al final resolvemos dos ejercicios del Trabajo Practico 4 — uno sencillo para fijar los conceptos y otro que nos va a permitir construir formalmente los numeros racionales.

**[Avanzar]**

---

## Slide 2 — Repaso: Propiedades de Relaciones

*Se ve: el titulo "Repaso: Propiedades de Relaciones" y un texto introductorio.*

> Antes de definir que es una relacion de equivalencia, repasemos rapidamente las tres propiedades que la componen. Seguro ya las vimos, pero conviene tenerlas frescas.

**[Avanzar]** *(aparece "Reflexividad")*

> La primera es la **reflexividad**. Una relacion es reflexiva cuando todo elemento del conjunto se relaciona consigo mismo. En simbolos: para todo x en A, se cumple que x R x.

**[Avanzar]** *(aparece "Simetria")*

> La segunda es la **simetria**. Una relacion es simetrica cuando si x se relaciona con y, entonces y tambien se relaciona con x. No hay direccion privilegiada.

**[Avanzar]** *(aparece "Transitividad")*

> Y la tercera es la **transitividad**. Si x se relaciona con y, e y se relaciona con z, entonces x se tiene que relacionar directamente con z. Es como encadenar relaciones.

**[Avanzar]**

---

## Slide 3 — Definicion de Relacion de Equivalencia

*Se ve: pantalla de seccion "Relacion de Equivalencia — Definicion formal".*

> Ahora si, con las tres propiedades frescas, vamos a la definicion.

**[Avanzar]** *(aparece el titulo y la definicion en texto)*

> Una relacion R definida sobre un conjunto A es una **relacion de equivalencia** si y solo si cumple las tres propiedades al mismo tiempo: tiene que ser reflexiva, simetrica y transitiva. Si alguna de las tres falla, no es de equivalencia.

**[Avanzar]** *(aparece la formula con las 3 propiedades entre llaves)*

> Aca la tienen expresada formalmente. R es de equivalencia en A si y solo si se cumplen las tres condiciones juntas. Reflexiva para todo x. Simetrica para todo par. Transitiva para toda cadena.

**[Avanzar]** *(aparece la nota de notacion)*

> Una observacion de notacion: cuando R es de equivalencia, en vez de escribir R se suele usar un simbolo como la **tilde** (∼), el **doble tilde** (≈) o la **triple barra** (≡). Es pura convencion para resaltar que es una equivalencia y no una relacion cualquiera.

**[Avanzar]**

---

## Slide 4 — Ejemplos

*Se ve: pantalla de seccion "Ejemplos — Relaciones de equivalencia".*

> Veamos dos ejemplos clasicos para entender mejor el concepto.

**[Avanzar]** *(aparece "Ejemplo 1: La igualdad")*

> El primer ejemplo es la **igualdad matematica**. El simbolo igual, el mas basico de todos. En cualquier conjunto, la igualdad es trivialmente una relacion de equivalencia.

**[Avanzar]** *(aparecen los 3 checks: reflexiva, simetrica, transitiva)*

> ¿Por que? Porque cumple las tres propiedades sin esfuerzo: *a* es igual a *a* — reflexiva. Si *a* es igual a *b*, entonces *b* es igual a *a* — simetrica. Y si *a* es igual a *b* y *b* es igual a *c*, entonces *a* es igual a *c* — transitiva. Las tres de manera casi obvia.

**[Avanzar]**

*Ahora se ve: "Ejemplo 2: La relacion Identidad".*

> El segundo ejemplo es la **relacion identidad**, que se denota con un delta subindice A.

**[Avanzar]** *(aparece la definicion formal de Δ_A)*

> Formalmente, la identidad en un conjunto A es el conjunto de todos los pares (x, x) donde x pertenece a A. Es decir, solo relacionamos cada elemento consigo mismo y con ningun otro.

> Esto la hace reflexiva, simetrica, antisimetrica y transitiva al mismo tiempo. Por eso es, simultaneamente, una relacion de equivalencia Y una relacion de orden. Es la relacion mas "minima" posible que cumple ambas definiciones.

**[Avanzar]**

---

## Slide 5 — Clases de Equivalencia

*Se ve: pantalla de seccion "Clases de Equivalencia — Agrupando elementos relacionados".*

> Ahora vamos con un concepto fundamental: las **clases de equivalencia**. Esto es donde las relaciones de equivalencia empiezan a cobrar sentido practico.

**[Avanzar]** *(aparece la definicion formal)*

> Dada una relacion de equivalencia R sobre A, y tomando un elemento *a* del conjunto, definimos la **clase de equivalencia de a** — que escribimos con una barrita arriba, *a* barra — como el conjunto de todos los elementos de A que estan relacionados con *a*.

> En otras palabras: la clase de *a* agrupa a todos los elementos que, segun la relacion, son "equivalentes" a *a*.

**[Avanzar]** *(aparece la visualizacion del conjunto A con las 3 burbujas coloreadas)*

> Para verlo graficamente: imaginemos un conjunto A con nueve elementos. La relacion los agrupa naturalmente en tres clases distintas, que aca representamos con tres burbujas de colores.

**[Avanzar]** *(aparece la burbuja roja con su etiqueta)*

> La primera clase — la roja — contiene los elementos 1, 4 y 7. Todos ellos estan relacionados entre si.

**[Avanzar]** *(aparece la burbuja verde)*

> La segunda clase agrupa al 2, 5 y 8.

**[Avanzar]** *(aparece la burbuja violeta)*

> Y la tercera agrupa al 3, 6 y 9. Fijense que cada elemento cae en una sola clase — y cada clase contiene a todos los elementos que se relacionan con cualquiera de sus miembros.

**[Avanzar]** *(aparece la propiedad clave)*

> Y aca viene una propiedad fundamental: **dos clases son iguales si y solo si sus representantes estan relacionados**. Si tomo el 1 y el 4, ambos estan en la misma burbuja, entonces *1 barra* es igual a *4 barra*. Son literalmente el mismo conjunto. Esto va a ser importante en los ejercicios.

**[Avanzar]**

---

## Slide 6 — Conjunto Cociente

*Se ve: titulo "Conjunto Cociente" y su definicion formal.*

> Ahora bien, si tomamos TODAS las clases de equivalencia y las juntamos, formamos un nuevo conjunto al que llamamos **conjunto cociente**, que se escribe A barra R, o A sobre R.

**[Avanzar]** *(aparece la definicion: A/R = {ā : a ∈ A})*

> Formalmente: el cociente de A por R es el conjunto de todas las clases de equivalencia. Es importante notar que **es un conjunto de conjuntos**: cada elemento del cociente no es un elemento de A, sino una CLASE — es decir, un subconjunto de A.

**[Avanzar]** *(aparece la animacion del colapso)*

> Para visualizarlo: a la izquierda tenemos el conjunto A con sus tres clases marcadas por burbujas. Lo que hace el cociente es **colapsar cada burbuja en un solo punto**. Cada clase entera se convierte en un unico elemento del nuevo conjunto.

**[Avanzar]** *(aparecen las etiquetas {1,2}, {3}, {4,5} al lado de cada punto)*

> Asi, una clase que contenia los elementos 1 y 2 se transforma en un unico elemento del cociente: la clase *{1,2}*. La clase del 3, que solo tenia al 3, se convierte en la clase *{3}*. Y la que tenia 4 y 5, en la clase *{4,5}*.

**[Avanzar]** *(aparece A/R = {{1,2}, {3}, {4,5}})*

> Entonces el cociente A sobre R termina siendo un conjunto con tres elementos: las tres clases. Cada clase, UN punto del cociente. Este concepto es clave porque nos permite "simplificar" el conjunto original agrupando elementos equivalentes.

**[Avanzar]**

---

## Slide 7 — Particiones

*Se ve: pantalla de seccion "Particiones — Dividiendo un conjunto en partes".*

> El ultimo concepto teorico, antes de los ejercicios, es el de **particion**. Y vamos a ver que esta muy relacionado con todo lo que venimos hablando.

**[Avanzar]** *(aparece la visualizacion del conjunto A y la definicion)*

> Una **particion** de un conjunto A es una familia de subconjuntos no vacios de A que cumple tres condiciones.

**[Avanzar]** *(aparecen las 4 regiones A1, A2, A3, A4 dentro del rectangulo)*

> Graficamente, pensemos a A como un rectangulo dividido en cuatro regiones: A1, A2, A3, A4. Para que sea una particion, tienen que cumplirse tres condiciones.

**[Avanzar]** *(aparecen las 3 condiciones con checks)*

> Condicion 1: **cada parte tiene que ser no vacia**. No pueden haber regiones vacias, siempre tiene que haber al menos un elemento dentro.

> Condicion 2: **las partes tienen que ser disjuntas dos a dos**. Es decir, ningun elemento puede pertenecer a dos regiones al mismo tiempo. No hay superposicion.

> Condicion 3: **la union de todas las partes tiene que cubrir todo A**. No puede quedar ningun elemento afuera de alguna region.

> Si se cumplen las tres, tenemos una particion.

**[Avanzar]** *(aparece el titulo "Teorema Fundamental")*

> Y aca viene el resultado mas potente del tema: el **Teorema Fundamental**.

**[Avanzar]** *(aparece el diagrama con las dos representaciones y la doble implicacion)*

> El teorema dice lo siguiente: si R es una relacion de equivalencia en A, entonces el conjunto cociente A sobre R es una particion de A. Y **tambien vale el reciproco**: toda particion de A induce una relacion de equivalencia, donde dos elementos estan relacionados si pertenecen al mismo subconjunto de la particion.

**[Avanzar]** *(aparece la nota "Equivalencias y particiones son dos caras de la misma moneda")*

> Esta es la frase clave para entender el tema: **relaciones de equivalencia y particiones son dos caras de la misma moneda**. Hablar de una es hablar de la otra. Esto es lo que hace tan utiles a las relaciones de equivalencia — nos permiten particionar conjuntos de manera natural.

**[Avanzar]**

---

## Slide 8 — Ejercicio 29 del TP4

*Se ve: pantalla de seccion "Ejercicio 29 — Trabajo Practico 4".*

> Con toda la teoria repasada, vamos al primer ejercicio resuelto: el **ejercicio 29 del Trabajo Practico 4**. Es un caso sencillo que nos sirve para aplicar todos los conceptos de forma concreta.

**[Avanzar]** *(aparece el enunciado con A y R)*

> El enunciado nos da un conjunto A = {1, 2, 3, 4}, y una relacion R definida por estos ocho pares ordenados. Nos pide **mostrar que R es de equivalencia**, hallar las clases y determinar la particion que induce.

> Para probar que es de equivalencia, tenemos que verificar las tres propiedades.

**[Avanzar]**

### Reflexividad

*Se ve: "Ej. 29 — Reflexividad".*

> Primero, **reflexividad**. ¿Todos los elementos estan relacionados consigo mismos? Verificamos que (1,1), (2,2), (3,3) y (4,4) pertenezcan a R.

**[Avanzar]** *(aparece "R es reflexiva ✓")*

> Los cuatro estan. Entonces R es reflexiva.

**[Avanzar]**

### Simetria

*Se ve: "Ej. 29 — Simetria".*

> Ahora, **simetria**. Para cada par (x, y) en R, ¿esta tambien el par (y, x)? Los pares no triviales son (1,2) y (3,4). Vemos que tanto (2,1) como (4,3) tambien pertenecen a R. Los pares de la forma (x, x) son trivialmente simetricos.

**[Avanzar]** *(aparece "R es simetrica ✓")*

> Por lo tanto, R es simetrica.

**[Avanzar]**

### Transitividad

*Se ve: "Ej. 29 — Transitividad".*

> Y por ultimo, **transitividad**. Tomamos todos los pares componibles — es decir, los que tienen un elemento en comun — y verificamos que el par compuesto tambien este en R.

> Por ejemplo: (1,2) y (2,1) componen en (1,1), que esta. (3,4) y (4,3) componen en (3,3), que esta. (4,3) y (3,4) componen en (4,4), que tambien esta.

**[Avanzar]** *(aparece "R es transitiva ✓")*

> Todos los pares compuestos estan en R. Entonces R es transitiva.

**[Avanzar]**

### Conclusion: es de equivalencia

*Se ve: "Ej. 29 — R es de equivalencia" con el recuadro de conclusion.*

> Las tres propiedades se cumplen — reflexiva, simetrica, transitiva. Por lo tanto, **R es una relacion de equivalencia en A**.

**[Avanzar]**

### Clases de equivalencia

*Se ve: "Ej. 29 — Clases de equivalencia".*

> Ahora calculamos las clases. La clase del 1 es el conjunto de todos los elementos relacionados con 1. Segun R, eso nos da {1, 2}. Si hacemos lo mismo para el 2, tambien obtenemos {1, 2}.

**[Avanzar]** *(aparece la conclusion de que clase 1 = clase 2)*

> Entonces las clases del 1 y del 2 son **iguales**. Recuerden la propiedad que vimos antes: dos clases son iguales si sus representantes se relacionan. Como (1,2) esta en R, las clases coinciden.

> Lo mismo pasa con el 3 y el 4: ambos caen en la clase {3, 4}.

**[Avanzar]**

### Particion inducida

*Se ve: "Ej. 29 — Particion inducida" con A/R = {{1,2}, {3,4}}.*

> Entonces el conjunto cociente A sobre R es la coleccion de estas dos clases: **{1,2} y {3,4}**.

**[Avanzar]** *(aparecen los 3 checks de la particion)*

> Y podemos verificar que es efectivamente una particion: **ninguna de las dos partes es vacia**, **son disjuntas** porque no comparten elementos, y **su union es todo A**. Se cumplen las tres condiciones.

> Listo el ejercicio 29. Ahora vamos a uno mas interesante.

**[Avanzar]**

---

## Slide 9 — Ejercicio 32 del TP4

*Se ve: pantalla de seccion "Ejercicio 32 — Trabajo Practico 4".*

> El **ejercicio 32** es, desde mi punto de vista, uno de los ejercicios mas interesantes del practico. Porque lo que parece una relacion abstracta en realidad nos va a permitir **construir formalmente los numeros racionales** a partir de los enteros.

**[Avanzar]** *(aparece el enunciado)*

### Enunciado

> El enunciado nos dice: tenemos una relacion ∼ definida en Z por Z cero (los enteros con los enteros no nulos), dada por la siguiente condicion: (x, y) esta relacionado con (z, w) si y solo si x por w es igual a y por z.

> Nos pide tres cosas: probar que es de equivalencia, hallar la clase del elemento (-1, 4), y mostrar que cada clase se puede identificar con un numero racional.

**[Avanzar]**

### Intuicion

*Se ve: "Ej. 32 — Intuicion" y la explicacion de xw = yz como fracciones.*

> Antes de ir a la prueba formal, quedemonos un minuto con la intuicion. ¿Que significa que xw sea igual a yz?

> Si pensamos al par (x, y) como la **fraccion x sobre y**, entonces la condicion xw = yz es exactamente lo que obtenemos al hacer **productos cruzados**: x sobre y es igual a z sobre w.

**[Avanzar]** *(aparece la equivalencia con x/y = z/w)*

> Es decir, dos pares estan relacionados si **representan la misma fraccion**. Por ejemplo, (1,2), (2,4), (3,6) y (4,8) estan todos relacionados entre si — porque todos representan a un medio.

> Con esta intuicion en mente, las demostraciones se vuelven mucho mas faciles de seguir.

**[Avanzar]**

### Reflexividad

*Se ve: "Ej. 32 — Reflexividad" con la demostracion.*

> Empecemos con **reflexividad**. Para todo par (x, y), ¿vale que (x, y) esta relacionado consigo mismo?

> Aplicamos la definicion: (x, y) ∼ (x, y) si y solo si x por y es igual a y por x. Y eso se cumple siempre — es simplemente la **conmutatividad del producto de enteros**.

**[Avanzar]** *(aparece "∼ es reflexiva ✓")*

> Por lo tanto, la relacion es reflexiva.

**[Avanzar]**

### Simetria

*Se ve: "Ej. 32 — Simetria".*

> Ahora **simetria**. Tomamos dos pares cualquiera (x, y) y (z, w), y queremos probar que si (x, y) ∼ (z, w), entonces (z, w) ∼ (x, y).

> Paso 1: asumimos (x, y) ∼ (z, w), lo que por definicion significa x por w igual a y por z.

> Paso 2: usamos la conmutatividad del producto: y por z es igual a z por y, y x por w es igual a w por x.

> Paso 3: reemplazando, llegamos a z por y igual a w por x, que es exactamente la condicion para que (z, w) ∼ (x, y).

**[Avanzar]** *(aparece "∼ es simetrica ✓")*

> Por lo tanto, la relacion es simetrica.

**[Avanzar]**

### Transitividad (parte 1)

*Se ve: "Ej. 32 — Transitividad" con la hipotesis.*

> Y ahora la mas larga: **transitividad**. Tomamos tres pares: (x, y), (z, w), (k, h). La hipotesis es que (x, y) ∼ (z, w) y que (z, w) ∼ (k, h). Queremos probar que (x, y) ∼ (k, h).

> Paso 1: asumimos las dos hipotesis.

> Paso 2: por definicion, sabemos que **x por w = y por z**, y que **z por h = w por k**.

**[Avanzar]**

### Transitividad (parte 2 — demostracion)

*Se ve: los pasos 3, 4, 5 de la demostracion.*

> Ahora el truco algebraico que nos lleva a la conclusion.

> Paso 3: multiplicamos ambos lados de la primera igualdad por h. Obtenemos **x por w por h es igual a y por z por h**.

> Paso 4: usamos la segunda igualdad, que nos dice que z por h es igual a w por k. Reemplazamos en el lado derecho: **x por w por h es igual a y por w por k**.

> Paso 5: aca es crucial notar que **w es distinto de cero** — porque estamos en Z por Z cero, el segundo factor nunca es cero. Entonces podemos **simplificar w** de ambos lados, y nos queda **x por h igual a y por k**. Eso es exactamente la condicion para (x, y) ∼ (k, h).

**[Avanzar]** *(aparece "∼ es transitiva ✓")*

> Por lo tanto, la relacion es transitiva.

**[Avanzar]**

### Conclusion: es de equivalencia

*Se ve: "Ej. 32 — ∼ es de equivalencia" con el recuadro final.*

> Las tres propiedades se cumplen. Por lo tanto, **∼ es una relacion de equivalencia en Z por Z cero**.

**[Avanzar]**

### Clase de (-1, 4)

*Se ve: "Ej. 32 — Clase de (-1, 4)" con los calculos.*

> Ahora calculamos la clase del elemento **(-1, 4)**. Por definicion, es el conjunto de todos los pares (x, y) tales que **-1 por y = 4 por x**.

> Despejando, obtenemos **y = -4x**.

**[Avanzar]** *(aparece la expresion de la clase)*

> Entonces la clase de (-1, 4) es el conjunto de todos los pares de la forma **(x, -4x)** con x distinto de cero. Esto incluye, por ejemplo, los pares (-2, 8), (-1, 4), (1, -4), (2, -8), y asi.

> Y aca lo interesante: **todos estos pares representan la misma fraccion, menos un cuarto**. Si ustedes toman cualquiera de esos pares como una fraccion, todos simplifican a -1/4. Esa es la intuicion que teniamos al principio, hecha explicita.

**[Avanzar]**

### Los racionales como cociente

*Se ve: "Ej. 32 — Los racionales como cociente".*

> Ahora vamos al tercer punto del ejercicio: mostrar que **cada clase se identifica con un numero racional**.

> Como vimos, si (x, y) ∼ (z, w), entonces xw = yz, lo que es lo mismo que decir que **x sobre y es igual a z sobre w**. Es decir, dos pares estan en la misma clase si y solo si representan la misma fraccion.

**[Avanzar]** *(aparece la correspondencia entre clase y fraccion)*

> Entonces podemos identificar cada clase de equivalencia con **un unico numero racional**. La clase de (x, y) se corresponde naturalmente con el racional x sobre y.

**[Avanzar]**

### Conclusion final: Q como cociente

*Se ve: la identidad Z × Z₀ / ∼ = Q con el recuadro final.*

> Y aca llegamos al resultado mas importante de todo el ejercicio: **el conjunto cociente de Z por Z cero bajo esta relacion es exactamente Q** — el conjunto de los numeros racionales.

> Esto es lo que hace al ejercicio tan importante: **no es solo un ejercicio de verificacion, es la construccion formal de los numeros racionales**. Cuando definimos Q de esta forma, estamos diciendo que un numero racional ES una clase de equivalencia de pares de enteros — todos los pares que representan la misma fraccion.

> Esta construccion es fundamental en matematica. Es la misma idea que se usa para construir muchas otras estructuras: tomar un conjunto "grande" y cocientarlo por una relacion de equivalencia para obtener algo nuevo.

**[Avanzar]**

---

## Slide 10 — Resumen

*Se ve: titulo "Resumen" y los conceptos principales en una grilla.*

> Para cerrar, recordemos rapidamente los conceptos clave que vimos.

> Una **relacion de equivalencia** es aquella que cumple las tres propiedades: reflexiva, simetrica y transitiva.

> La **clase de equivalencia** de un elemento *a* es el conjunto de todos los elementos relacionados con *a*.

> El **conjunto cociente** es la coleccion de todas las clases — agrupamos el conjunto original en sus "grupos equivalentes".

> Una **particion** es una familia de subconjuntos no vacios, disjuntos, cuya union cubre todo el conjunto.

> Y el **teorema clave** conecta ambos conceptos: el cociente A sobre R es particion de A si y solo si R es una relacion de equivalencia. Son dos maneras de ver lo mismo.

**[Avanzar]**

---

## Slide 11 — Cierre

*Se ve: "Relaciones de Equivalencia" y "¡Gracias!".*

> Con esto cerramos. Vimos la teoria completa, la aplicamos en un ejercicio sencillo, y terminamos construyendo los racionales desde los enteros — que es una de las construcciones mas elegantes de la matematica.

> Gracias.

**[Fin]**
