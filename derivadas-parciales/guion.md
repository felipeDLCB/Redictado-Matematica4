Hasta ahora vimos cómo resolver derivadas parciales usando las reglas de derivación, pero, ¿de dónde salen estas reglas? Para entenderlo, tenemos que ir a la base fundamental de todo esto.

En esta diapositiva, vemos la definición formal de la derivada parcial, la cual utiliza el concepto de límite para capturar un cambio infinitesimal en la función. Al igual que en las funciones de una sola variable, analizamos qué sucede cuando le damos un incremento muy, muy pequeño a una de las variables.

- **Si derivamos respecto a** x: Evaluamos la función sumándole un pequeño cambio "h" únicamente a la variable x, mientras que la variable y se queda exactamente igual. Al restarle la función original y dividir todo por "h" cuando este tiende a cero, el límite nos muestra cómo cambia la función en ese instante.
- **Si derivamos respecto a** y: Hacemos exactamente lo mismo, pero esta vez el cambio infinitesimal, al que llamamos "k", se lo sumamos solamente a la variable y, dejando constante a la variable x.

Esta definición es la que matemáticamente justifica por qué podemos tratar a la otra variable como si fuera un número fijo.

8

Para que esto no quede solo en la teoría, veamos un ejemplo muy sencillo de cómo se aplica esta definición. Analicemos la función f(x,y)=xy.

Primero, vamos a calcular la **derivada respecto a** x:

1. Aplicamos la fórmula del límite cuando "h" tiende a cero. En el numerador, reemplazamos la x por (x+h) y lo multiplicamos por y. A eso le restamos la función original, que es xy.
2. Si hacemos la distributiva en el primer término, nos queda xy+hy. A esto le restamos el xy original.
3. Como tenemos un xy positivo y un xy negativo, se cancelan, y solo nos queda hy sobre h. Al simplificar la h de arriba con la de abajo, el resultado de la derivada es simplemente y.

Ahora hacemos lo mismo para la **derivada respecto a** y:

1. Planteamos el límite cuando "k" tiende a cero. Esta vez dejamos la x quieta y reemplazamos la y por (y+k).
2. Al distribuir, obtenemos xy+xk, y a eso le restamos la función original xy.
3. Nuevamente, los términos xy se cancelan. Nos queda xk dividido k. Simplificamos las "k" y el resultado final nos da x.

Como pueden ver, la matemática detrás del límite nos demuestra exactamente lo que decíamos al principio: cuando derivamos respecto a una variable, la otra actúa literalmente como una constante que acompaña."
