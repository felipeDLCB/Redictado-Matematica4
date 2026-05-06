# Guion — Núcleo e Imagen de un Morfismo

Tono: coloquial-formal, voseo rioplatense. Pensado para acompañar la presentación
`presentacion.py` (clase `NucleoImagenSlides`). Cada bloque corresponde a una
slide o sub-slide.

---

## Slide 1 — Título

> Bien, vamos a hablar de **núcleo e imagen** de un morfismo de grupos. Son dos
> conjuntos que aparecen siempre que tenemos un homomorfismo entre dos grupos, y
> son **la herramienta clave** para entender qué tan "informativa" es una función
> que respeta la estructura algebraica. Después vamos a resolver los ejercicios
> 19 y 22 del TP5, que justamente prueban las dos propiedades fundamentales de
> estos conjuntos.

---

## Slide 2 — Repaso: ¿qué es un morfismo de grupos?

> Antes de meternos con núcleo e imagen, repasemos rápido qué es un morfismo. Si
> tenemos dos grupos —`(G, ∗)` y `(H, ∘)`— una función `f : G → H` es un
> **homomorfismo** cuando respeta la operación. ¿Qué significa eso? Que da lo
> mismo operar primero en `G` y después aplicar `f`, que aplicar `f` primero a
> cada elemento y operar en `H`. Esa es la fórmula clave:
>
> `f(a ∗ b) = f(a) ∘ f(b)`.
>
> De esta única propiedad se desprenden dos consecuencias que vamos a usar todo
> el tiempo: **el neutro va al neutro** —`f(e_G) = e_H`— y **el inverso va al
> inverso** —`f(a⁻¹) = f(a)⁻¹`. Guardense estas dos, porque son las que hacen
> funcionar todas las demostraciones que siguen.

---

## Slide 3 — Definición de Núcleo

### 3a) Definición formal

> Acá viene la primera definición. El **núcleo** de `f`, que escribimos `Nu(f)`,
> es el conjunto de los elementos de `G` que `f` manda al neutro de `H`:
>
> `Nu(f) = { x ∈ G : f(x) = e_H }`.
>
> Importante: el núcleo **vive en `G`**, en el dominio. Son los elementos que
> "mueren", que se aplastan contra el neutro cuando los pasás por la función.

### 3b) Diagrama

> Mirá el diagrama. A la izquierda tenés a `G`, a la derecha a `H`. Adentro de
> `H` marqué con verde el neutro `e_H`. Todos los elementos rojos que ves
> agrupados en `G` son los que terminan ahí, en `e_H` —esos son el núcleo—.
> Los puntos blancos en `G` representan a los elementos que `f` manda a otros
> lugares de `H`, no al neutro.
>
> Pensá al núcleo como **el conjunto de cosas que la función "no distingue"
> del neutro**. Si el núcleo es chiquito, la función está discriminando bien.
> Si el núcleo es grande, está "aplastando" mucha información.

---

## Slide 4 — Definición de Imagen

### 4a) Definición formal

> Ahora la otra mitad: la **imagen** de `f`, `Im(f)`, son los elementos de `H`
> que están "alcanzados" por la función:
>
> `Im(f) = { y ∈ H : ∃ x ∈ G con f(x) = y } = f(G)`.
>
> Acá la diferencia importante: la imagen **vive en `H`**, en el codominio. Es
> el rango efectivo de la función.

### 4b) Diagrama

> En el diagrama, los puntos verdes adentro de `H` son los que efectivamente
> aparecen como `f(x)` para algún `x` en `G`. El punto gris suelto representa
> un elemento de `H` que **nadie** alcanzó —no está en la imagen—.
>
> Si la imagen coincide con todo `H`, la función es **suryectiva**. Si la
> imagen es más chica, la función no llega a cubrir todo el codominio.

---

## Slide 5 — Ejercicio 19

### 5a) Enunciado

> Dale, vamos al primer ejercicio. El 19 dice: dado un homomorfismo
> `f : G → H`, probar que **el núcleo es subgrupo de `G`** y **la imagen es
> subgrupo de `H`**. Esto es importante porque te dice que núcleo e imagen no
> son conjuntos cualquiera —tienen ellos mismos estructura de grupo, heredada
> del grupo original—.

### 5b) Estrategia

> ¿Cómo se prueba que algo es subgrupo? Usamos el **criterio de subgrupo**:
> alcanza con verificar dos cosas. Primero, que el conjunto **no sea vacío**.
> Segundo, que esté **cerrado bajo `a ∗ b⁻¹`** —es decir, que si tomás dos
> elementos del subconjunto y operás uno con el inverso del otro, seguís
> adentro—. Si se cumplen estas dos, ya es subgrupo. Vamos a aplicar esto a
> `Nu(f)` y a `Im(f)`.

### 5c) Parte (a) — Paso 1: Nu(f) no es vacío

> Empezamos con el núcleo. ¿Cómo mostramos que no es vacío? Encontramos al menos
> un elemento adentro. Y tenemos uno gratis: el neutro `e_G`. ¿Por qué? Porque
> por la propiedad de morfismo sabemos que `f(e_G) = e_H` —el neutro va al
> neutro—. O sea que `e_G` cumple la condición de núcleo, y por lo tanto está
> en `Nu(f)`. Entonces el núcleo nunca está vacío, **siempre tiene al menos al
> neutro**.

### 5d) Parte (a) — Paso 2: cierre

> Segundo paso. Tomamos dos elementos cualquiera del núcleo, `a` y `b`. Por
> definición, `f(a) = e_H` y `f(b) = e_H`. Queremos ver que `a ∗ b⁻¹` también
> está en el núcleo, o sea, que `f(a ∗ b⁻¹) = e_H`.
>
> Aplicamos morfismo: `f(a ∗ b⁻¹) = f(a) ∘ f(b⁻¹) = f(a) ∘ f(b)⁻¹`. Reemplazamos
> los valores: `e_H ∘ e_H⁻¹`. Y como el inverso del neutro es el neutro, queda
> `e_H ∘ e_H = e_H`. Listo. Eso prueba que `a ∗ b⁻¹` está en el núcleo.

### 5e) Parte (a) — Conclusión

> Tenemos las dos condiciones del criterio: el núcleo es no vacío y está cerrado
> bajo `a ∗ b⁻¹`. Por lo tanto, `Nu(f)` es subgrupo de `G`. Listo, primera parte
> demostrada.

### 5f) Parte (b) — Paso 1: Im(f) no es vacío

> Vamos por la imagen. Otra vez el mismo truco para mostrar que no es vacía:
> `f(e_G) = e_H`, así que `e_H` está en la imagen. Por lo tanto `Im(f)` no es
> vacío.

### 5g) Parte (b) — Paso 2: cierre

> Tomamos dos elementos `y₁`, `y₂` en la imagen. Por definición de imagen,
> existen `x₁` y `x₂` en `G` tales que `f(x₁) = y₁` y `f(x₂) = y₂`.
>
> Calculamos `y₁ ∘ y₂⁻¹`. Usando que `f` es morfismo: esto es igual a
> `f(x₁) ∘ f(x₂)⁻¹`, que es `f(x₁) ∘ f(x₂⁻¹)`, y juntando todo,
> `f(x₁ ∗ x₂⁻¹)`.
>
> Acá viene el detalle clave: como `G` **es un grupo**, `x₁ ∗ x₂⁻¹` también
> pertenece a `G`. Y entonces `f(x₁ ∗ x₂⁻¹)` es la imagen de un elemento de
> `G` —es decir, está en `Im(f)`—. Listo el cierre.

### 5h) Parte (b) — Conclusión

> No vacío más cerrado bajo la operación: `Im(f)` es subgrupo de `H`. Quedó
> demostrado el ejercicio 19 completo.

---

## Slide 6 — Ejercicio 22

### 6a) Enunciado

> Pasamos al ejercicio 22, que es **el resultado más útil** de esta parte. Dice
> así: `f` es **monomorfismo** —o sea, morfismo inyectivo— **si y sólo si** su
> núcleo es trivial, es decir, está formado únicamente por el neutro.
>
> ¿Por qué es tan útil? Porque chequear inyectividad a mano puede ser un
> quilombo, pero **calcular el núcleo es directo**: resolvés `f(x) = e₂` y
> mirás qué soluciones hay.
>
> Como es un "si y sólo si", hay que probar las dos implicaciones.

### 6b) Ida (⟹): inyectiva ⟹ núcleo trivial

> Empecemos por la ida. Asumimos que `f` es inyectiva, queremos llegar a que el
> núcleo es `{e₁}`.
>
> Tomamos un `x` cualquiera en el núcleo. Por definición, `f(x) = e₂`. Pero
> también sabemos —por morfismo— que `f(e₁) = e₂`. Entonces tenemos
> `f(x) = f(e₁)`. Y acá entra la hipótesis: como `f` es inyectiva, dos
> elementos con la misma imagen tienen que ser iguales. Por lo tanto `x = e₁`.
>
> Esto vale para cualquier `x` en el núcleo, así que el único elemento posible
> es el neutro. `Nu(f) = {e₁}`.

### 6c) Vuelta (⟸): núcleo trivial ⟹ inyectiva

> La vuelta es la más interesante. Asumimos que el núcleo es solo el neutro y
> queremos probar inyectividad.
>
> Tomamos `a, b` en `G₁` con `f(a) = f(b)`. Queremos ver que `a = b`. Operamos
> a la derecha por `f(b)⁻¹`: nos queda `f(a) ∘ f(b)⁻¹ = e₂`. Por morfismo,
> esto es `f(a ∗ b⁻¹) = e₂`.
>
> ¿Qué nos dice esto? Que `a ∗ b⁻¹` está en el núcleo. Y por hipótesis, el
> núcleo solamente tiene al neutro. Entonces `a ∗ b⁻¹ = e₁`, y despejando,
> `a = b`.
>
> Entonces `f` es inyectiva.

### 6d) Conclusión del 22

> Las dos implicaciones probadas: queda equivalente.
>
> `f` es monomorfismo si y sólo si `Nu(f) = {e₁}`.
>
> Quedate con esta idea: **el núcleo mide cuán inyectiva es la función**. Si es
> trivial, la función inyecta perfecto. Cuanto más grande el núcleo, menos
> inyectiva es la función.

---

## Slide 7 — Resumen

> Para cerrar, recapitulamos los cuatro puntos centrales:
>
> 1. **Núcleo**: elementos del dominio que van al neutro.
> 2. **Imagen**: elementos del codominio que son alcanzados.
> 3. **Ejercicio 19**: ambos heredan estructura — núcleo es subgrupo del
>    dominio, imagen es subgrupo del codominio.
> 4. **Ejercicio 22**: el núcleo es el test de inyectividad — núcleo trivial
>    equivale a morfismo inyectivo.
>
> Con esto tenés casi toda la maquinaria que se usa después para los teoremas
> de isomorfismo —pero eso ya es para otra clase—.

---

## Slide 8 — Cierre

> Eso fue todo: **núcleo e imagen** de un morfismo. Si entendiste estos dos
> conjuntos y la equivalencia del ejercicio 22, tenés la base para todo lo que
> sigue en teoría de grupos. ¡Gracias!

---

## Notas de presentación

- Velocidad de animaciones: 1.5× (ya configurada en `play()`).
- En cada `next_slide()` hay pausa natural para respirar y mirar al público.
- Los pasos de los ejercicios 19 y 22 están separados slide-por-slide para
  poder detenerte y preguntar "¿se entiende?" después de cada paso.
