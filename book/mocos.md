# Mocos
Los ordenadores, son rápidos y tienen una memoria enorme: son máquinas capaces de ejecutar millones de instrucciones por segundo y de gestionar cantidades inimaginables de datos. Pero eso no significa que sean listos. De hecho no saben hacer nada por sí solos. Para que un ordenador, o una tablet, un móvil,
hagan algo concreto, deben ejecutar un programa. Y un programa es un conjunto de órdenes escritas por los programadores.

Lo interesante de la programación es que podemos tomar el control de la máquina para que esta haga lo que nosotros queramos: desde una instrucción simple, hasta programás muy complejos como navegadores o juegos. La programación engancha porque puedes crear lo que quieras, sin más límite que tu imaginación y tus habilidades.

Pero ¿en qué lenguaje nos podemos comunicar con los ordenadores? Existen infinidad de ellos. Internamente, el ordenador utiliza el lenguaje binario, es decir, una secuencia de unos y ceros
que es capaz de interpretar para hacer algo. Sin embargo, para facilitar la tarea de programación, hay lenguajes más simples, que se parecen mucho al lenguaje de las personas.

Python es uno de esos lenguajes, y tiene muchas virtudes: es sencillo, muy fácil de aprender, permite hacer cualquier cosa, dispone de infinidad de librerías y encima se utiliza de manera profesional. En este libro aprenderás a programar utilizando Python. De forma progresiva, irás conociendo nuevas herramientas que te ofrece el lenguaje para aprender a crear programas más complejos.

¿Qué necesitas para empezar ya mismo? Un navegador. Desde el primer capítulo nos dedicaremos a programar. La mejor forma de apreder a programar es... ¡programando! No hay que tener ningún miedo, y además, es lo más divertido. Así que basta de cháchara. ¡Pasa al siguiente capítulo para escribir tu primer programa!

Nota:
Quizá hayas oido que los ordenadores pueden tener inteligencia artificial o puede que te hayas
enfrentado a juegos en los que los enemigos parecen ser muy listos. En realidad, lo que hace el ordenador es ejecutar programas.

Nota2:
Si quieres instalarte un entorno de programación convencional, ve al apéndice X.

# Hola mundo
```Python
print("Hola mundo!")
```
Si pruebas esto deberías ver por la pantalla algo así:

```console
Hola mundo!
```

## Comentarios

En un programa, se pueden poner comentarios. Se trata de texto que no se ejecuta y que el ordenador ignora completamente. ¿para qué se utiliza? Generalmente los comentarios se utilizan para explicar determinadas partes del programa.

```Python
# Este programa dice Hola
print("Hola")
```
Python ignora el comentario y mostrará `Hola` por pantalla.
También se pueden hacer comentarios de varias líneas:

```Python
"""
Este es un programa python
creado por Ada
y revisado por Neko
"""
```
A veces, los comentarios se utilizan de manera temporal para "desactivar" una parte del código que no queremos que se ejecute.

Nota: en general tienes que evitar los comentarios. Un buen programador tiene que intentar escribir programas tan fáciles de entender que no necesiten comentario alguno.

# Variables
Las variables sirven para guardar datos. Los programas de ordenador se dedican, básicamente, a manejar datos para solucionar un problema y ofrecer un resultado. En todo ese proceso es necesario guardar datos, y para eso se utilizan las variables. Las variables son como contenedores de datos. En cierto modo es como los vasos, platos, fuentes que se utilizan para cocinar: contienen algo, se trabajo con ello, se mezcla, se procesa y se consigue un resultado. Con un poco de suerte algo rico.
Para definir una variable en python basta con indicar su nombre y darla algún valor. Por ejemplo:
```Python
nombre = "Ada"
```

Acabamos de crear una variable que contiene el valor "Ada". "Ada" es un dato, de tipo texto. Ahora podemos mostrar el valor de esa variable por la pantalla:

```Python
print(nombre)
```
Que por pantalla sería

```console
Ada
```
En cualquier momento, podríamos cambiar el valor de esa variable:
```Python
nombre = "Ada"
print(nombre)
nombre = "Neko"
print(nombre)
```
Y por pantalla veríamos:
```console
Ada
Neko
```

Nota:
También se puede mostrar el contenido de una variable como parte del mensaje.
Existen varias opciones para ello:
## Separar por comas
Basta con intercalar las variables y el texto con comas:
```Python
nombre = "Bug"
edad = 10
print("Hola, me llamo", nombre)
print("Soy", nombre, "tengo", edad, "años")
```
Que por pantalla sería

```console
Hola, me llamo Bug
Soy Bug tengo 10 años
```

## String de formato
Un mensaje que precedido de la letra `f` y las variables entre llaves:
```Python
nombre = "Bug"
edad = 10
print(f"Hola, me llamo {nombre}")
print(f"Soy {nombre} tengo {edad} años")
```
Que por pantalla sería

```console
Hola, me llamo Bug
Soy Bug tengo 10 años
```

## Sustitución de porcentaje
Se crea un mensaje donde los elementos %s son sustituidos por variables.
```Python
print("Hola, me llamo %s" % nombre)
```
Que por pantalla sería

```console
Hola, me llamo Ada
```

Puedes hacer lo mismo con varias variables
```Python
nombre = "Neko"
edad = 5

print("Hola, me llamo %s y tengo %d años" % (nombre, edad))
```
Que por pantalla sería:

```console
Hola, me llamo Neko y tengo 5 años
```
# Tipos de datos
¡Datos! Es la materia prima con la que trabajan los programas. Son el elemento que transforman. Un programa recibe datos, los transforma y los devuelve como un resultado.
Los datos pueden ser de distinto tipo, según lo que nuestro programa tenga que hacer. Pueden ser números, puedes ser palabras o textos, pueden incluso ser nulos o vacíos.
Para guardar los datos, generalmente usamos variables.
Si comparamos la programación con la cocina, el azúcar, la harina y los huevos serían datos, los recipientes serían variables: la tarta sería otro dato, el resultado y la receta sería el programa.
¿Cómo sabe Python que tipo de dato maneja? No hace falta indicarselo como en otros lenguajes. Por eso es un lenguaje más simple y flexible. Aunque tampoco podremos hacer lo que nos de la gana con los datos.

A continuación, vamos a ver los tipos básicos de datos

## Números
Se trata de todos los tipos de números:
- Enteros:
1, 2, 3, 4,...

```python
contador = 10
edad = 12
```

- Con decimales:
Los números con decimales se expresan utilizando un `.` para separar la parte entera de la decimal, como 4.5 o 3.1415. Es probable que en clase de mates utilices una coma para separar las decimales, pero en programación se usa el formato inglés y debemos usar un `.`.

```python
peso = 34.67
precio = 242.9943
```

- Negativos:
Los números menores que 0 se expresan con un guión por delante: -4, -5, -3.1415,...

```python
nota = -5
temperaturaEnMarte = -50.676
```

## Texto
El texto, también llamados cadenas o *strings* son cualquier conjunto de palabras entre comillas dobles o simples.

```python
nombre = "Ada"
frase = ""
palabras = 'Voy a trabajar'
novia = 'Solo quiero que seamos "amigos"'
```
En el caso del texto, podemos meter una serie de caracteres especiales que nos permiten efectos interesantes. Esos caracteres se escriben con una contrabarra o backslash por delante: `\`

- Salto de linea
Esto añade un salto de línea al texto si este se muestra por pantalla:

```python
frase = "Hola,\n qué tal"
```
se mostrará así:
```shell
Hola,
qué tal
```

- Tabulaciones
Esto añade una tabulación (varios espacios) al texto si este se muestra por pantalla:

```python
frase = "Nombre\tApellido\tEdad"
```
se mostrará así:
```shell
Nombre	Apellido	Edad
```
Otros caracteres especiales:

- \\ Para mostrar la contrabarra en un texto.
- \" Para mostrar una comilla doble en un texto.
- \' Para mostrar una comilla simple en un texto.
- \a Para hacer sonar un pitido.

## Booleanos
El tipo booleano solo puede tener dos valores posibles:
`True` o `False`, es decir verdadero o false. Se trata de un tipo de dato fundamental en programación ya que se utiliza para tomar decisiones.

```python
terminado = False
esMayor = True
pythonMola = True
```

## Listas
Las listas son conjuntos de datos, que se definen de la siguiente manera:

```python
amigas = ["Ada", "Miranda", "Ruby"]
```
Pueden ser de cualquier tipo, pero lo normal es que todos los elementos de una lista sean del mismo tipo:

```python
enemigas = []
edades = [12, 16, 30, 0, 22, 1, 1, 12]
verdades = [True, False, False, True]
```
Para poder referirnos a un valor concreto de la lista, tenemos que indicar la posición del elemento de la lista que nos interesa, empezando desde 0:

```python
nombres = ["Ada", "Neko", "Bug"]
print(nombres[0])  # "Ada"
```
En el caso de la lista `nombres`, las posiciones posibles serán 0, 1 y 2.
¡Pero ojo! si pasas una posición demasiado grande, el programa terminará con error:
```python
nombres = ["Ada", "Neko", "Bug"]
print(nombres[4])  # ¡ERROR!
```
Volveremos sobre las listas y otras estructuras más adelante. 

## None
Aunque suene un poco raro, en los programas a veces hay que tratar con algo que representa el vacío, la nada. 
Existe una palabra que nos permite representar la nada en Python, y esa es: `None`

```python
valorInicial = None
dato = None
```
En realidad no se suele utilizar para crear variables. None representa un valor en situaciones especiales. Por ejemplo, si se trata de sacar información de un sitio en el que no hay nada como un fichero, o un dato que el usuario no nos da.

# Leyendo datos
Para que un programa pueda hacer algo, muchas veces necesita que el usuario introduzca un dato. Por ejemplo, si queremos que un programa nos diga cuantas letras tiene nuestro nombre, o cuanto falta para nuestro cumpleaños, lo primero que tendrá que hacer el programa es pedir un dato.

Los programas básicos como los que estamos viendo de momento, utilizan la consola para ejecutarse. Son esas pantallas negras donde se ponen órdenes escritas ;)

Para poder pedirle al usuario un dato y guardarlo en una variable, se utiliza la función `input`:

```python
nombre = input("Dime tu nombre: ")
print("Hola ", nombre)
```

En la pantalla verías lo siguiente:

```code
Dime tu nombre: 
```
La función input hace que el mensaje `Dime tu nombre: ` aparezca en pantalla. También hace que el programa se pare a la espera de que el usuario escriba algo.
Si el usuario escribe `Rosa` en la consola, se vería:

```code
Dime tu nombre: Rosa
Hola Rosa
```

## Cuidado con los datos
Cada vez que uses la funcion `input` para que el usuario escriba algo, sea lo que sea **se guardará como texto**. Aunque se escriba un número:


```python
valor = input("Dame un número: ")
doble = valor + valor
print(doble)
```

Si el usuario introduce un número como `4` este sería el resultado:

```console
Dame un número: 4
44
```
En lugar de sumar `4 + 4` y mostrar `8`, lo que ha hecho es unir `4` y `4`, porque en realidad, cuando se ha leido a través de `input` ese `4` es texto: `"4"`

Para evitarlo, tenemos que usar otra función para convertir ese dato en número entero: `int()`

```python
valor = input("Dame un número: ")
doble = int(valor) + int(valor)
print(doble)
```

O incluso lo podemos convertir antes:

```python
valor = input("Dame un número: ")
valor = int(valor)
doble = valor + valor
print(doble)
```

O incluso aplicarlo a `input`: 


```python
valor = int(input("Dame un número: "))
doble = valor + valor
print(doble)
```

Ahora sí:
```console
Dame un número: 4
8
```

# Operadores
Los programas necesitan hacer cálculos con números, procesar datos, tomar decisiones según los valores. Para ello necesitamos los operadores.

## Operadores aritméticos
Son todos aquellos que te permitirán hacer sumas, restas y todas los cálculos básicos con valores y con aquello que se guarde en variables, como por ejemplo, la suma:

```python
chicles = 4
chicles = chicles + 2
```
El programa calcula que de tener 4 chicles, has pasado a tener 6.
Las operaciones básicas en programación son:
- suma: `+`
- resta: `-`
- multiplicación: `*`
- división: `/`

Por ejemplo para calcular el total de segundos que tiene un día:
```python
minutos = 60
segundos = 60
horas = 24

totalSegundos = segundos * minutos * horas
```

Puedes hacer operaciones tan complejas como hagan falta. Para que estas sean más fáciles de leer se pueden utillizar paréntesis como se hace en mates:

```python
ada = 14
bug = 10
neko = 2
media = (ada + bug + neko) / 3
```

### Módulo y exponencial
Hay una operación muy importante en programación, que quizá no sea tan frecuente en las mates: se trata del **módulo**. Es una división que devuelve el residuo en lugar del resultado de la división:

```python
valor = 8
resultado = valor % 3
```
El valor de resultado será: `2`.

El exponencial es el resultado de multiplicar un número por sí mismo varias veces. En Python se puede hacer esta operación con el operador `**`:

```python
valor = 2
resultado = valor ** 3 # equivale a: 2 * 2 * 2
```

El resultado sería `8`.

## Operadores de comparación
Se trata de operadores que nos permiten comparar un valor con otro. Generalmente se usa con números y el resultado de estas operaciones es `True`o `False`.

Por ejemplo, para comprobar si un valor es igual a otro usamos el operador: `==`

```python
valor = 5
resultado = valor == 5
```

El resultado sería `True`.

Los operadores de comparación serían:

- Igual: `==`
- Distinto: `!=`
- Mayor que: `>`
- Menor que: `<`
- Mayor o igual: `>=`
- Menor o igual: `<=`

También puede utilizarse este operador con texto, tanto para comprobar igualdad:

```python
nombre = "Ada"
resultado = nombre == "Bug"
```
El resultado sería `False`.
También nos permite comparar si un texto es mayor o menor en orden alfabético:

```python
nombre = "Ada"
resultado = "Ada" < "Bug"
```

El resultado sería `True`.

## Operadores booleanos
Los operadores booleanos nos permiten hacer operaciones con valores booleanos `True`o `False`. 

### and
Este operador solo devuelve `True` si los dos operandos también son `True`:

```python
valor = 5
resultado = (valor == 5) and True;
```

El resultado sería `True`.
Para resumir todas las posibles opciones, esta sería lo que se denomina tabla de la verdad del operador `and`.

|a | | b| resultado |
|--|--|--|--|
|`False` | `and` |`False` |`False` |
|`False` | `and` |`True` |`False` |
|`True` | `and` |`False` |`False` |
|`True` | `and` |`True` |`True` |

### or
Este operador solo devuelve `True` si cualquiera de los dos operandos también son `True`:

```python
valor = 5
resultado = (valor == 5) or True;
```

El resultado sería `True`.
Para resumir todas las posibles opciones, esta sería lo que se denomina tabla de la verdad del operador `or`.

|a | | b| resultado |
|--|--|--|--|
|`False` | `or` |`False` |`False` |
|`False` | `or` |`True` |`True` |
|`True` | `or` |`False` |`True` |
|`True` | `or` |`True` |`True` |

### not
Este operador solo devuelve `True` si los dos operandos también son `True`:

```python
valor = True
resultado = not valor;
```

El resultado sería `False`.
Para resumir todas las posibles opciones, esta sería lo que se denomina tabla de la verdad del operador `not`.

| | a| resultado |
|--|--|--|
| `not` |`False` |`False` |
| `not` |`True` |`False` |

### Combinando operadores
Podemos combinar los operadores tanto como necesitemos:

```python
jubilado = 65
if edad > 17 and edad < (jubilado + 1):
	print("Ya puedes trabajar")
```

Generalmente, los operadores condicionales se utilizan dentro de las condiciones de los bloques condicionales, bucles, etc.

# Condiciones
En algún momento, los programas necesitan hacer una cosa u otra dependiendo de una condición. Por ejemplo, si un usuario introduce un dato incorrecto, el programa se acaba.
Si un dato tiene determinado valor, se procesa de una forma y si no, de otra. ¿Cómo se consigue ese comportamiento? Mediante condiciones.

Las condiciones son estructuras de programación que nos permiten que un código se ejecute solo cuando se cumplan unas condiciones.

## if
La estructura más simple para hacer una condición es el `if`, el cual tiene este aspecto:

```python
if *condicion*:
	*instrucciones*
	*instrucciones*
	*...*
```

Como puedes observar, `if` comienza con una condición. La condición puede ser cualquier expresión que devuelva un booleano, es decir, será True o False, verdadero o falso.
Si es True, las instrucciones dentro del `if` se ejecutarán, y si no se saltarán.
Por ejemplo

```python
valor = -2
if valor < 0:
	print("El valor es menor que 0")
print("Fin del programa")
```

Resultaría en:

```console
El valor es menor que 0
Fin del programa
```
En cambio:

```python
valor = 5
if valor < 0:
	print("El valor es menor que 0")
print("Fin del programa")
```

Resultaría en:

```console
Fin del programa
```

Nota:
También debes observar algo muy importante: las instrucciones dentro del `if` van detrás de unos espacios o una tabulación. Esa es una peculiaridad del lenguaje de programación Python: en cualquier bloque como una condicón, un bucle, una función, su contenido debe ir tabulado. Esa es una forma que facilita la lectura y permite reconocer fácilmente la estructura de un programa para otros programadores. Incluso para ti mismo si lo has creado.

## if else
Con el if podemos crear un bloque que solo se ejecute si se cumple una condición. Pero ¿Qué pasa si queremos que el programa haga una cosa u otra según una condición?
Para poder meter "la otra" opción, utilizamos una estructura if-else:

```python
if *condicion*:
	*instrucciones*
else:
	*instrucciones*
```

Por ejemplo:

```python
nombre = input("Dime tu nombre: ")
if nombre != "":
	print("Hola ", nombre)
else:
	print("¡No has metido nada!")
```

Podría verse algo así, según lo que meta el usuario:

```console
Dime tu nombre: Ada
Hola Ada
```

Pero si el usuario simplemente pulsa enter sin escribir nada:

```console
Dime tu nombre:
¡No has metido nada!
```

## if elif else
Existe otra variante cuando necesitamos comprobar varias condiciones. Para eso existe la estructura if-elif-else:

```python
if *condicion1*:
	*instrucciones*
elif: *condicion2*:
	*instrucciones*
elif *condicion3*
	*instrucciones*
else:
	*instrucciones*
```

Supongamos que queremos un programa que sea capaz de saludar en distintos idiomas. Podriamos crear un programa como el siguiente:

```python
idioma = input("¿Qué idioma hablas?")

if idioma == "Español":
	print("Hola"):
elif idioma == "Inglés":
	print("Hello"):
elif idioma == "Francés":
	print("Salut")
else:
	print("No conozco ese idioma")
```

Podemos tener tantos `elif` como hagan falta.

# Bucles
Como decíamos al principio, los ordenadores son muy muy tontos. Solo hacen lo que se les diga. Pero por contra, tienen enormes capacidades y una paciencia infinita. No les importará lo más mínimo hacer lo que sea tantas veces como sea necesario.

Una de las tareas más típicas para un ordenador es repetir una instrucción. Esto es algo que se puede conseguir mediante estructuras de bucle. Un bucle es una acción que se repite. Generalmente un bucle tiene una condición para ejecutarse. Si esas condiciones se cumplen, entonces se ejecutarán las órdenes que contenga ese bucle.
Puedes ver un bucle como una montaña rusa en la que das varias vueltas. 
A continuación veremos distintos tipos de bucle.

## Bucle while
Un bucle while se ejecuta mientras una condición se cumpla. Su estructura es muy simple:

```python
while *condicion*:
	*instrucciones*
```
Por ejemplo, vamos a ejecutar un bucle mientras el valor de una variable sea mayor que 0.

```python
contador = 10
while contador > 0:
	print("Estoy dentro del bucle")
	contador = contador - 1
```

Nota: ¡Ojo! ¿Te has fijado en que dentro del bucle estamos restando un valor a `contador`? Si no tenemos cuidado y nos olvidamos de hacer eso, el valor de contador nunca cambiaría y crearíamos un bucle infinito. ¡El programa nunca terminaría y se quedaría atascado para siempre!

Veamos otro ejemplo. El siguiente programa solicita un dato al usuario en un bucle. El programa no saldrá del bucle mientras el usuario no meta un dato distinto de vacío `""`:

```python
nombre = ""
while nombre == "":
	nombre = input("¿Cómo te llamas?")

print("Hola", nombre)
```

## Bucle For
El bucle for lo utilizamos para repetir una acción un número concreto de veces. Más que una condición, utiliza una especie de contador:

```python
for *variable* in *rango*:
	*instrucciones*
```

Por ejemplo, el siguiente bucle mostrará el mensaje `hola` 5 veces:

```python:
for i in range(4):
	print("Hola")
```
El resultado sería:
```code
Hola
Hola
Hola
Hola
```

Algo muy interesante en los bucles for es que la variable `i`, la cual podría tener el nombre que queramos, tendrá el valor correspondiente a cada vuelta del bucle. Para verlo mejor, basta con cambiar un poco el programa anterior:

```python:
for i in range(4):
	print("Hola", i)
```

Y comprobar el resultado:

```code
Hola 0
Hola 1
Hola 2
Hola 3
```

### Cambiar el rango
Por defecto, `range(4)` está devolviendo una lista de 0 a 3, es decir: 0, 1, 2, 3. Son un total de cuatro elementos y por tanto el bucle dará cuatro vueltas.

Obviamente, se puede crear cualquier tipo de rango. Si no se indica nada, el rango comienza en 0. Pero se puede indicar un rango entre dos números:
range(0, 4) # 0, 1, 2, 3
range(2, 6) # 2, 3, 4, 5

Por ejemplo:

```python:
for i in range(5, 9):
	print("Hola", i)
```
El resultado sería:
```code
Hola 5
Hola 6
Hola 7
Hola 8
```

También se puede indicar un tercer parámetro para indicar cómo se salta de un valor a otro. Por ejemplo de 2 en 2:
```python
range(1, 11, 2) # 1, 3,
```

En el siguiente ejemplo, el bucle se haría con números pares.
```python:
for i in range(0, 6, 2):
	print("Hola", i)
```
El resultado sería:
```code
Hola 0
Hola 2
Hola 4
```

### Hacia atrás
También se podría recorrer el bucle hacia atrás, utilizando un salto negativo

```python:
print("Iniciando cuenta atrás: ")
for i in range(5, 0, -1):
	print(i)
```

El resultado sería:

```code
5
4 
3
2
1
```

### Bucles sobre listas
Los bucles `for` son especialmente útiles cuando queremos recorrer todos los elementos de una lista, para mostrarlos, procesarlos o lo que sea. La forma es muy sencilla:

```python
objetos = ["estrella", "seta", "flor"]
for objeto in objetos:
	print(objetos)
```
En cada vuelta del bucle la varialbe `objeto` tomara un valor de la lista `objetos`, así que el resultado sería el siguiente:

```console
estrella
seta
flor
```

### Saliendo del bucle
En ocasiones puede que nos interese salir de un bucle y no seguir procesando nada más. Supongamos que tenemos un programa para buscar un nombre dentro de una lista:

```python
nombres = ["Mia", "Jon", "Arya", "Ane", "Bug", "Ada", "Lisp"]
for nombre in nombres:
	if nombre == "Ane":
		print("Ane está en la lista")
```
El problema de ese programa es que aunque encuentre a `Ane`, el bucle seguirá hasta el final de la lista. Si esa lista es muy grande, nuestro programa será ineficiente! Como decíamos al principio, los ordenadores son muy tontos. Si no les decimos que paren, seguirán adelante.

Por suerte, en los bucles podemos usar la instrucción `break`, la cual conseguirá que el bucle termine de golpe:

```python
nombres = ["Mia", "Jon", "Arya", "Ane", "Bug", "Ada", "Lisp"]
for nombre in nombres:
	if nombre == "Ane":
		print("Ane está en la lista")
		break
```

## ¿Cuándo usar while o for?
Aunque con los dos podrías hacer lo mismo, realmente cada uno tiene un uso más lógico.

El bucle for se utiliza claramente cuando se quiere ejecutar algo un número concreto de veces, ni más ni menos. O bien, como veremos más adelante, cuando se quieren recorrer estructuras de datos como listas de principio a fin.

El bucle while se puede utilizar cuando las condiciones no son muy concretas. Por ejemplo, si queremos que el usuario introduzca un dato, lo podemos hacer en un bucle. El bucle no terminará hasta que el usuario no introduzca un dato bueno (esa sería la condición).

# Estructuras de datos

## Listas

## Diccionarios

## Listas de diccionarios

## Bucle sobre estructuras

# Funciones

## Retorno

## Parámetros

# Librerías

## Python {#python}

For a developer is not enough to know one programming language, it is often said that is good to know many of them. After all the language is but a mere tool to build programs. Python has been around for many years and one of my pending task was to take a look at it. Some friends (<a href="http://twitter.com/Eugenia4v">@Eugenia4v</a>,<a href="http://twitter.com/Claw_Shadow">@Claw_Shadow</a>,<a href="http://twitter.com/@D00m3dr4v3n">@D00m3dr4v3n</a>) are always telling me about the benefits of Python not to mention plenty of papers where Python is even recommended as the language of choice to get into programming. I guess that when Google itself has been using Python from the beginning, and when this language is a requirement for many job offers there is something about it. Despite the title of this post, I spent more than 21 minutes coding around and trying the basics so don't expect a deep dive into Python. This is just a quick guide


![python logo](http://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/320px-Python_logo_and_wordmark.svg.png)

### Python language
Python is: interpreted, weakly typed, (could be compilated), case sensitive, supports oop, functional, imperative programming,...
apart from the classic definition, if you come from c style languages at first glance you'll notice the lack of semicolons. But the real change in Python is the use of indentation to create code blocks. So instead using  brackets for if-else-loops-functions you have to use indents or tabs properly. This at least, somehow leads to mandatory code convention (<a href="https://www.python.org/dev/peps/pep-0008">they exists too</a>), here there is no room for discussion about the most clear way to write an if-else structure; there is only "one style" so follow it or your code will not run at all. But to sum up, and above all, python was designed to be easy to read

### Environments
Name | Type | Free?
--- | --- | ---
Pycharm | Desktop | Free
PyDev | Desktop | Free
[Repl.it](https://repl.it/languages/python) | Web | Free


### Writing and running hello world
So you have just installed python in you windows box or you are running a linux machine, which means that python is most likely in da house. Open any text editor, write this and save it with .py extension:

```python
print('Hello World desde España y olé' # testing utf-8 :P
print("Welcome to python \'resume\'"
print("New Line \n and ring the bell \a"
```

To run this we can just execute <code>python filename.py</code>, or give it execution perms and run it directly

If you want to test some python code directly in the interpreter, just run python and the python prompt will show up awaiting for your commands.

### Comments

We have single line comments and multiline comments. The first line gives support for utf-8 characters.


```python
# -*- coding: utf-8 -*-
# This is a single line comment
"""
some python in a few lines, by Pello Altadill
This is a multiple line comment
more suitable for long texts like this
greetz to any
"""

```

### Variables

There are no types in python. Variable declaration is the simplest possible.


```python
# variable definitions ###########
number = 666
negativeNumber = -42
decimals = 3.1415
name = "Legion"
anotherName = "Legion of Doom"
letterA = 'a'
letterB = "b"
godExists = True
itsMe = False
# multiline string,
prayer = """Gods of war I call you,
my sword is by my side,
I seek a life of honor,
free from all false pride"""

# multiple assignment, c-style
a = b = c = 0

# but not strongly typed...
a = True
c = 'Hello'

a = 10
b = -a
c = 42
```


### Operators

Comparing with other languages we have some extra operators here. Bit operators are omitted, but you've them all.


```python
# expressions ##########
# arithmethyc
a = b + c
b = a - c
c = a * b
a = b / c # returns floating point
a = b // c # integer division
modulus = a % c
thePower = a ** 3

# of course this are available:
a += b
b -= c
c *= a
a /= b
b %= 42

# booleans, as always
theTruth = godExists and itsMe
theTruth = godExists or false
theTruth = not godExists

# comparison operators
areEqual = a == b
areNotEqual = a!= b   # a &lt;&gt; b works, but obsolete
isBigger = a &gt; b
isLess = a &lt; b
biggerOrEqual = a &gt;= b
lessOrEqual = a &lt;= b

# combination of all of them
superTrue = ( (a-1) &gt; b) or (not(c == (b*4)))

# concatenation use , in general. + for strings
print("My name is " , name
print(a , " - " , b , " - " , c
# if whe use + whe must convert to string
print(str(a) + "," + str(b) + "," + str(c)
print(prayer

# del unbinds variable values
del prayer
# print(prayer would now fail

```


### Conditional
Python offers if, if-else, if-elsif-else but <b>there is NO switch/case</b>.

```python
# conditional #########################
# single if
if godExists:
	print("God is real unless declared integer"

## single line if
if True:print('I am single lined if'

anything = '1'
if anything:
	print("Yeah, anything different to 0 means True"

# 0, None, "", '', empty structures (),[],{} are the same as False
numberZero = 0
if not numberZero:
	print("And 0 is False"

# we can omit or put parenthesis
if (a&lt;b or b==c):
	print("a less than b or b equals c"


# if-else
if a &gt; b:
	print("a is bigger than b"
else:
	print("a is NOT bigger than b"

# elif
if a &gt; b:
	print("a is bigger than b"
elif a &lt; b:
	print("a is less than b"
elif a == b:
	print("a and b are equal"
elif a == 0:
	pass  # this a way to do NOTHING , as we can't leave a block empty
else:
	print("a and b are alien"

# THERE IS NO switch case
# but you can do it with a elif structure
```


### Loops

for and while loops as always but... <b>there is no do-while</b>. for is very simple and works well as foreach.


```python
# loops ###########################
# while loop
c = 3
while c&gt;0 :
	print("a loop with c" , c
	c-=1

# for loop
# for i in range(begin,end), does not reach end
for x in range(0,5):
	print("for loop with x " , x

# with different step
# range(5) = [0, 1, 2, 3, 4]
# for (i in range(begin,end, step))
for x in range(0,10,2):
	print("for loop inc 2 with x " , x
for x in range(5,0,-1):
	print("for loop dec with x " , x

# xrange(number): from 0 to number
for x in xrange(5):  #  0..4
	print("testing xrange: " , x

name = 'Python'
for x in name:
	print("for loop with string: " , x

# break and continue works in python as well
# applied to while and for
# with break we stop and exit the loop
findTheX = 'sdfXsaf'
for x in findTheX:
	if x == "X":
		print("found the X, now exit"
		break

# with continue we finish current iteration and go for next
someVocals = '0a00i0e00u000a'
for x in someVocals:
	if x =='0':
		continue
	elif x =='a':
		print("a found"
	elif x=='e':
		print("e found"

# else clause ###### after for and while is executed after the normal
# execution of the iteration, but NOT when the execution has been
# interrupted by break, exceptions or returns.
counter = 0
for x in someVocals:
	if x == 'a':
		counter += 1
else:
	print("Total a letters found in " , someVocals , ": " , counter

# THERE IS NO do-while structure

```

### Arguments and read from console

The most basic way to pass arguments to a python script is using the sys.argv list. But, there are other richer modules available to get arguments in getopt style.


```python
print('Total arguments: ' , number ,  len(sys.argv)
for a in sys.argv:
	print(a

# reading from console
value = raw_input("write something")
print(value
```
### Tuples, lists, and dictionaries

We have three kind of basic structures, but beware, once defined tuples can't be changed: they are immutable


```python
# STRUCTURES #############################
# Tuples = IMMUTABLE, ordered, sequence of arbitrary items
someValues = (42, 15, 69)
otherValues = ('Meaning', 42, True, -0.3)
newTuple = tuple('aeiou') # this creates ('a','e','i','o','u')
emptyTuple= ()

print("First: " , otherValues[0]
print("Last: " , otherValues[-1]

# This is a way to add an elemtn
otherValues+= (34,56)
# THIS IS NOT ALLOWED as a tuple is IMMUTABLE
# otherValues[0] = 'Satan'

# of course is iterable
for v in otherValues:
	print("Tuple: " , v

# Lists = MUTABLE, ordered, sequence of arbitrary items
superList = ['Python','Ruby','Go']
otherList = ['God',666, True]
emptyList = []

print("First: " , superList[0]
print("Last: " , superList[-1]

# This is a way to add an elemtn
superList+= ['NodeJS']
otherList[0] = 'Satan'

for x in superList:
	print("Superlist : " , x

# Dictionaries = MUTABLE, arbitrary collection of items
# indexed by arbitrary items = similar to hashtables, hash, maps, you name it.
ages = {'Gandalf':1432, 'Aragorn':543, 'Bilbo':112}
emptyDictionary = {}
# using the builtin function:
trigValues = dict(sin=34,cos=353.23,tan=34)
otherAges = dict([['Frodo',34],['Samwise',35]])

ages['Bilbo'] = 120
ages['Radagast'] = 1423

# iterating...
for key in ages:
	print(key , " : " , ages[key]

# SLICING SEQUENCES
# We access an element with sequence[index]
# to get a slice of if: sequence[begin:length:stride]
# stride is the distance or leap
ports = [20, 21, 25, 80, 443, 110, 143];
webPorts = ports[3:2] 		# [80, 443]
ftpPorts = ports[:2]; 		# [20, 21]
somePorts = ports[1:6:2] 	# [21, 80, 110]

# Strings are IMMUTABLE!! and slicing works the same way
myName = "Pello Xabier Altadill Izura"
# so this is illegal
#myName[0] = 'L'

print(myName[0] , " name: " , myName[:5]
```


If we want to manipulate these structures, we have many built-in methods available.

### Functions

def, function name and parameters, that's all.


```python
# function definition #################
def hello():
	print("hello"

def add(a,b):
	return a+b

def isEven(a):
	return (a%2==0)

def withDefaultValues(a, b=0, c=42):
	result = a + b - c
	print("Parameter values: "
	print("a is " , a
	print("b is " , b
	print("c is " , c
	return result

# calling functions
hello
hello()
a = add(600,66)
print("Result of addition: " , add(a,b)
b = isEven(a)
print("Result of isEven for " , a , ": " , b

withDefaultValues(5)
withDefaultValues(15,-5)
```

### Modules

Put code in a file called filename.py and we can reuse it in other files just by doing import filename.
Of course, apart from OOP, there are other options to package and reuse code more efficiently.



This is our super module, which has one super function

```python
# hello.py
def sayHello(name=""):
	return "Hello " , name
```

And this is the code to import and use that module

```python
# importing an external 'hello.py' source
import hello as myModule

print(myModule.sayHello("my little friend")
```

### Editors

You may heard something about IDLE. Run, don't look back.. fly you fools! We could always use eclipse with plugins, aptana,... or pycharm by jetbrains if we prefer a simpler sintax-highlighted text editor check these out:

- [pycharm](http://www.jetbrains.com/pycharm/)
- [pydev](http://pydev.org)
- [sublime](http://www.sublimetext.com)
- [atom](https://atom.io/)


One of the complains you may have heard about python is that [version 3 and 2](https://wiki.python.org/moin/Python2orPython)] are not compatible. Apart from that it is one of the languages that any coder should know (in addition to all object oriented c-style languages imho). What about the OOP? well, I was horrified when I saw some code. It looked as dirty as perl, or even more (I like perl btw).
