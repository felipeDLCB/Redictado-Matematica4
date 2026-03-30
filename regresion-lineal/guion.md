# Guion de Presentación — Regresión Lineal Simple (Ejercicio 3)

> **Nota para los integrantes:** Entre corchetes `[Slide X]` se indica cuándo avanzar la presentación. Las instrucciones en *cursiva* describen lo que se ve en pantalla. El texto normal es lo que hay que decir (parafrasear, no leer textualmente).

---

## INTEGRANTE 1 — Introducción + Inciso a)

### Slide 1 — Título

*Se ve: "Regresión Lineal Simple" con subtítulo "Ejercicio 3 — Transmisión en Redes"*

> Buenas, vamos a presentar el Ejercicio 3 del Trabajo Práctico, que trata sobre regresión lineal simple. Lo vamos a resolver paso a paso y explicar cada concepto en el camino.

**[Avanzar]**

---

### Slide 2 — ¿Qué es la Regresión Lineal?

*Se ve: definición de regresión lineal, luego aparece un mini scatter plot con una recta ajustada.*

> Empecemos por lo básico. La regresión lineal es un método estadístico que nos permite modelar la relación entre dos variables. La idea es simple: si tenemos una variable independiente *x* y una variable dependiente *Y*, queremos encontrar una recta que describa cómo se relacionan.

**[Avanzar]** *(aparece el gráfico con la recta)*

> Como ven en el gráfico, tenemos puntos dispersos y una recta que intenta pasar lo más cerca posible de todos ellos. Esa recta es lo que buscamos construir.

**[Avanzar]**

---

### Slide 3 — El Modelo de Regresión Lineal Simple

*Se ve: la ecuación Y = β₀ + β₁x + ε, con etiquetas que aparecen una a una.*

> El modelo de regresión lineal simple se expresa así: Y es igual a β₀ más β₁ por x más ε.

**[Avanzar]** *(aparecen las etiquetas de cada componente)*

> Veamos qué significa cada parte:
> - **Y** es la variable dependiente, lo que queremos predecir.
> - **β₀** es la ordenada al origen, el valor de Y cuando x vale cero.
> - **β₁** es la pendiente, nos dice cuánto cambia Y por cada unidad que aumenta x.
> - **x** es la variable independiente, lo que conocemos.
> - **ε** es el error aleatorio. En la realidad, los datos no caen exactamente sobre una recta; siempre hay una variación aleatoria. El error captura esa diferencia entre el valor real y el que predice el modelo.
>
> Un punto importante: sin el error ε, todos los puntos caerían exactamente sobre la recta. Pero en la práctica eso no pasa, por eso necesitamos este término.

**[Avanzar]**

---

### Slide 4 — Método de Mínimos Cuadrados

*Se ve: un scatter plot, aparece una recta, luego líneas verticales (residuos) desde los puntos hasta la recta, y cuadrados rojos semitransparentes.*

> Ahora, ¿cómo encontramos la "mejor" recta? Usamos el método de mínimos cuadrados.
>
> La idea es la siguiente: para cada punto, medimos la distancia vertical entre el punto observado y la recta. Esa distancia se llama **residuo**.

**[Avanzar]** *(aparecen los residuos como líneas punteadas)*

> Si elevamos al cuadrado cada residuo — para que no se cancelen los positivos con los negativos — y sumamos todos, obtenemos una medida de qué tan lejos está la recta de los datos.

**[Avanzar]** *(aparecen los cuadrados y la fórmula f(β₀, β₁) = Σ(yᵢ - β₀ - β₁xᵢ)²)*

> Nuestro objetivo es encontrar los valores de β₀ y β₁ que hagan que esa suma sea la menor posible. Es decir, minimizamos f(β₀, β₁). Los valores que lo logran se llaman **estimaciones de mínimos cuadrados** y se notan con "gorrito": β̂₀ y β̂₁.

**[Avanzar]**

---

### Slide 5 — Contexto del Ejercicio

*Se ve: enunciado resumido del problema, luego la tabla de datos.*

> Vamos al ejercicio. En un departamento de informática, un grupo de investigación quiere estudiar la relación entre la longitud de un paquete de red — medida en bytes — y el tiempo que tarda en transmitirse — medido en milisegundos. Hicieron 10 experimentos con distintas longitudes y midieron los tiempos.

**[Avanzar]** *(aparece la tabla con los 10 datos)*

> Acá tienen la tabla con los datos. Las longitudes van desde 100 hasta 300 bytes, y los tiempos van desde 52 hasta 135 milisegundos. A simple vista, parece que a mayor longitud, mayor tiempo.

**[Avanzar]** *(la tabla se achica y aparece el gráfico de dispersión)*

> Si graficamos estos puntos, confirmamos que existe una tendencia lineal creciente. No es perfecta — los puntos no están todos alineados — pero la tendencia es clara. Esto justifica usar un modelo de regresión lineal.

**[Avanzar]**

---

### Slide 6 — ¿Qué buscamos?

*Se ve: sobre el scatter plot, una recta que rota probando distintas posiciones hasta "encajar".*

> Ahora, entre todas las rectas posibles, tenemos que encontrar la que mejor se ajusta a estos datos. Vean cómo la recta va probando distintas posiciones...

*(la recta se estabiliza en la posición correcta)*

> ...hasta que encuentra la que minimiza la suma de los cuadrados de los residuos. Esa es nuestra recta de mínimos cuadrados.

**[Avanzar]**

---

### Slide 7 — Fórmulas de los Estimadores

*Se ve: las fórmulas β̂₁ = Sxy/Sxx y β̂₀ = ȳ - β̂₁x̄*

> Para calcular la recta, usamos estas fórmulas. La pendiente β̂₁ se obtiene dividiendo Sxy entre Sxx. Y la ordenada al origen β̂₀ se calcula con las medias de x e y.
>
> Sxx mide la variabilidad de los datos en x, y Sxy mide cómo varían x e y juntas. Son las sumatorias que vemos abajo.

**[Avanzar]**

---

### Slide 8 — Cálculo de las medias

*Se ve: x̄ = 1940/10 = 194, ȳ = 871/10 = 87,1*

> Primer paso: calculamos las medias. La media de x es 1940 dividido 10, que da 194 bytes. La media de y es 871 dividido 10, que da 87,1 milisegundos.

**[Avanzar]** *(aparecen líneas punteadas en el gráfico en x̄ e ȳ, con el punto medio resaltado)*

> En el gráfico pueden ver las líneas punteadas marcando las medias, y el punto donde se cruzan: (194, 87.1). Este punto siempre pertenece a la recta de regresión, es una propiedad del método.

**[Avanzar]**

---

### Slide 9 — Cálculo de Sxx y Sxy

*Se ve: fondo negro con las fórmulas de Sxx y Sxy con los valores sustituidos.*

> Ahora calculamos Sxx y Sxy. Usamos las fórmulas computacionales que son más prácticas:
>
> Sxx = la suma de los xᵢ al cuadrado, menos el cuadrado de la suma de los xᵢ dividido n. Eso nos da 424.350 menos 376.360, igual a **47.990**.
>
> Sxy = la suma de xᵢ por yᵢ, menos el producto de las sumas dividido n. Da 183.760 menos 168.974, igual a **14.786**.

**[Avanzar]**

---

### Slide 10 — Cálculo de β̂₁

*Se ve: la fórmula β̂₁ = Sxy/Sxx que se transforma paso a paso.*

> Ahora sí, calculamos la pendiente. β̂₁ es igual a Sxy sobre Sxx.

**[Avanzar]** *(se sustituyen los valores: 14786/47990)*

> Reemplazamos: 14.786 dividido 47.990...

**[Avanzar]** *(aparece el resultado: 0,3081)*

> ...que nos da **0,3081**. Este número tiene un significado muy concreto que ya vamos a ver.

**[Avanzar]**

---

### Slide 11 — Cálculo de β̂₀ y recta final

*Se ve: β̂₀ = ȳ - β̂₁x̄ con transformaciones paso a paso.*

> Para β̂₀ usamos la fórmula: ȳ menos β̂₁ por x̄.

**[Avanzar]** *(se sustituyen valores y aparece el resultado: 27,3275)*

> Eso es 87,1 menos 0,3081 por 194, que da **27,3275**.

**[Avanzar]** *(aparece la recta final ŷ = 0,3081x + 27,3275 enmarcada)*

> Entonces nuestra recta de regresión estimada es: **ŷ = 0,3081x + 27,3275**. Esta es la respuesta al inciso a).

**[Avanzar]** *(la recta se dibuja sobre el gráfico de dispersión)*

> Y acá la ven dibujada sobre los datos. Se ajusta bastante bien a la tendencia de los puntos.

**[Avanzar]**

---

## INTEGRANTE 2 — Incisos b) y c)


### Slide 12-13 — Predicción para x = 170

*Se ve: sobre el gráfico, aparece una línea vertical punteada en x=170 que sube hasta tocar la recta.*

> Gracias. Ahora que ya tenemos la recta, la podemos usar para hacer predicciones. El inciso b) nos pide: ¿cuánto tardaría la transmisión si la longitud del paquete es de 170 bytes?
>
> Lo primero que tenemos que verificar es que 170 está dentro del rango de nuestros datos, que va de 100 a 300. Como 170 sí está dentro, podemos usar la recta con confianza. Esto se llama **interpolación**.

**[Avanzar]** *(aparece el cálculo: ŷ = 0,3081 × 170 + 27,3275)*

> Reemplazamos en la ecuación: 0,3081 por 170 más 27,3275...

*(aparece el resultado: 79,7055 ms y la nota de interpolación válida)*

> ...y obtenemos **79,7055 milisegundos**. Esa es nuestra estimación del tiempo de transmisión para un paquete de 170 bytes.

**[Avanzar]**

---

### Slide 14-15 — ¿Y si x = 500?

*Se ve: el gráfico se extiende hacia la derecha, la recta se prolonga con línea punteada, aparece una X roja en x=500.*

> Ahora viene una pregunta muy importante: el inciso c) nos pregunta si podemos usar nuestra recta para predecir el tiempo cuando la longitud es 500 bytes.
>
> Veamos qué pasa si extendemos el gráfico. Nuestros datos llegan hasta x=300, pero 500 está mucho más allá. La recta se puede prolongar, sí — matemáticamente no hay problema — pero eso no significa que la predicción sea confiable.

**[Avanzar]** *(aparecen las zonas verde y roja)*

*Se ve: zona verde "Interpolación" entre 100-300, zona roja "Extrapolación" más allá de 300, "500 ∉ (100, 300)".*

> Acá está la clave. Cuando predecimos dentro del rango de datos observados — de 100 a 300 bytes — estamos haciendo **interpolación**, que es confiable. Pero cuando predecimos fuera de ese rango, estamos haciendo **extrapolación**, y eso es peligroso.
>
> ¿Por qué? Porque nuestro modelo solo "conoce" lo que pasa entre 100 y 300 bytes. No sabemos si la relación lineal se mantiene más allá. Podría ser que a partir de cierta longitud, el tiempo crezca de forma exponencial, o que se estabilice, o que cambie por completo. No tenemos datos para saberlo.
>
> Entonces la respuesta al inciso c) es **no**: no es recomendable usar la recta para predecir con x=500, porque 500 no pertenece al intervalo (100, 300) y estaríamos extrapolando.

**[Avanzar]** *(aparece explicación en texto)*

**[Avanzar]**

---

## INTEGRANTE 3 — Inciso d) + Conclusión

### Slide 16 — Significado de β̂₁

*Se ve: se reconstruye el scatter plot con la recta de regresión, aparece un "escalón" sobre la recta que muestra Δx y Δy.*

> Gracias. Ahora pasemos al inciso d), que nos pregunta cuánto aumenta el tiempo de transmisión por cada byte adicional. La respuesta está justamente en la pendiente β̂₁.
>
> Fíjense en el gráfico: el triángulo que se forma sobre la recta muestra que cuando x aumenta — ese es el segmento horizontal — y sube un poco — ese es el segmento vertical. La relación entre esos dos cambios es la pendiente.

**[Avanzar]**

---

### Slide 17 — Interpretación física

*Se ve: β̂₁ = 0,3081 ms/byte con texto explicativo.*

> β̂₁ = 0,3081 milisegundos por byte. Esto significa que **por cada byte adicional en la longitud del paquete, el tiempo de transmisión aumenta en promedio 0,3081 milisegundos**.
>
> Ojo: esto es una estimación, no un valor exacto. Es el cambio promedio estimado a partir de nuestros datos.

**[Avanzar]**

---

### Slide 18 — Conclusión

*Se ve: bullets con los puntos clave de la presentación.*

> Para cerrar, repasemos lo que vimos:
>
> 1. La **regresión lineal** es una herramienta que nos permite modelar relaciones lineales entre dos variables.
> 2. Los estimadores β̂₀ y β̂₁ se obtienen **minimizando la suma de los cuadrados de los residuos** — el método de mínimos cuadrados.
> 3. Para nuestro ejercicio, obtuvimos la recta **ŷ = 0,3081x + 27,3275**.
> 4. Es fundamental respetar el **rango de los datos** — solo podemos predecir de forma confiable entre 100 y 300 bytes.
> 5. La pendiente nos dice que el tiempo aumenta **0,3081 ms por cada byte adicional**.
>
> En resumen, la regresión lineal es una herramienta poderosa y muy usada en informática — desde análisis de redes como en este caso, hasta machine learning y ciencia de datos. Pero siempre hay que ser cuidadosos con los límites del modelo.

**[Avanzar]**

*Se ve: "¡Gracias!"*

> Eso es todo. ¿Alguna pregunta?
