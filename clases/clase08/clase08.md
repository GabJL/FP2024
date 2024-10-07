# Clase del 07 de octubre

Primero repasamos el bucle `while` y la lectura adelantada usando como base el ejercicio 5 de la actividad semanal

En esta clase empezamoss el bucle `for` cuyo componente más importante es el rango sobre el que itera. Por ello, empezamos con algunos ejemplos en el que vamos configurando diferentes versiones del `range`. 

Una vez ya entendido el bucle `for` pasamos a realizar diferentes ejercicios típicos para practicar principalmente el bucle `for` aunque también se pueden hacer usando el `while` (incluso en algún caso se pueden hacer versiones indeterministas que sean más eficientes).

## Repaso del while (actividad semanal, ejercicio 5)
*Nos han contratado para desarrollar un programa (a03e05.reloj.py) para un reloj inteligente para que cuando se inicie una actividad deportiva tome cada minuto las pulsaciones y al final nos devuelva las pulsaciones máximas y la media. Nuestro programa irá leyendo valores constantemente hasta que se acabe el ejercicio, momento en el que leerá un 0. Note que puede darse el caso que puede darse el caso de que inicie el ejercicio, pero acabe en menos de un minuto por lo que no se leerá ningún valor correcto (lo primero que se leerá será 0). En ese caso debe mostrar un mensaje indicando La actividad fue demasiado corta. Un ejemplo del funcionamiento esperado es:*

```
Iniciando la medición del pulso:
Pulsaciones actuales: 120 
Pulsaciones actuales: 125
Pulsaciones actuales: 130 
Pulsaciones actuales: 125 
Pulsaciones actuales: 0 
Las máximas pulsaciones fueron 130 y la media fue 125.0
```

Otra posible ejecución del programa podría ser:

```
Iniciando la medición del pulso:
Pulsaciones actuales: 0 
La actividad fue demasiado corta
```

Variante con 10 lecturas

```python
num_veces: int = 0 # contador -> número de valores leídos
suma: int = 0 # acumulador -> suma de los valores leídos hasta el momento
mayor: int = 0 # valor especial -> mayor hasta el momento (podemos usar 0 inicialmente, porque las pulsaciones siempre son > 0)

while num_veces < 10:
  pulsación: int = int(input("Pulsaciones actuales: "))
  suma += pulsación # es equivalente a suma = suma + pulsación
  num_veces += 1
  if mayor < pulsación:
    mayor = pulsación

print("Las máximas pulsaciones fueron", mayor, "y la media fue", suma/num_veces)
```
Variante leyendo hasta encontrar 0
```python
num_veces: int = 0 # contador -> número de valores leídos
suma: int = 0 # acumulador -> suma de los valores leídos hasta el momento
mayor: int = 0 # valor especial -> mayor hasta el momento (podemos usar 0 inicialmente, porque las pulsaciones siempre son > 0)

pulsación: int = int(input("Pulsaciones actuales: "))
while pulsación != 0:
  suma += pulsación # es equivalente a suma = suma + pulsación
  num_veces += 1
  if mayor < pulsación:
    mayor = pulsación
  pulsación = int(input("Pulsaciones actuales: "))

if num_veces == 0:
  print("La actividad fue demasiado corta")
else:
  print("Las máximas pulsaciones fueron", mayor, "y la media fue", suma/num_veces)
```

## Tabla del 7 (con for)
*El siguiente bucle while escribe la tabla de multiplicar del 7:*

```python
num = 1
while num <= 10:
  print("7 x", num, "=", 7*num)
  num += 1
```

*Modifique el código para usar el bucle for. Tenga en cuenta que `num` es una variable que toma los valores enteros 1, 2, 3, 4,..., 10*

Este ejercicio cuadra mucho con un `for`, lo único que hay que plantear es como generar esos valores. El `range` nos permite generar exactamente esos valores indicando que empiece en 1 y que llegue hasta 11 (sin incluirlo): `range(1,11)`.

```python
for i in range(1, 11):
  print("7 x", i, "=", 7*i)
```

## Ejercicios cortos de for
*Basándonos en el siguiente código:*

```python
for i in range(1,11):
  print(i, "->", i*i)
```

*Se piden realizar las siguientes modificaciones:*

### `for` hasta número leído de teclado
*Modifique el programa para que en vez de hacer un número fijo de iteraciones, le pida al usuario el número (N) y muestre todos los cuadrados entre el 1 y el número leído (incluído).*

En este caso, tras leer el valor, hay que hacer que el rango vaya hasta este valor y eso se hace cambiando el segundo parámetro que indica el límite superior. Cuidado que el valor indicado no se incluye en el rango y si queremos hacerlo hay que poner el rango hasta uno más: `range(1, N+1)`

```python
N: int = int(input("Dime el límite: "))

for i in range(1, N+1):
  print(i,"->",i*i)
```


### `for` solo impares
*Modifique el programa anterior para que sólo muestre los cuadrados de los números impares (1, 3, 5, 7, ...).*

Aquí hay que modificar el paso para que en vez de ir de uno en uno vaya de 2 en 2: `range(1, N+1, 2)`

```python
N: int = int(input("Dime el límite: "))

for i in range(1, N+1, 2):
  print(i,"->",i*i)
```


### `for` con orden inverso
*Modifique el programa anterior para que muestre los cuadrados pero de manera inversa (N, N-1, N-2, ..., 1)*

En este caso, hay que modificar los tres parámetros del `range`:
* El inicio será `N`
* El final será `0` (esto escribe el 1 pero no el 0)
* El paso será `-1` para que vaya "bajando"

```python
N: int = int(input("Dime el límite: "))

for i in range(N, 0, -1):
  print(i,"->",i*i)
```


### `for` con múltiplos de 2 o 3
*Modifique el programa anterior para que sólo muestre los cuadrados de los números que sean múltiplos de 2 o 3.*

En este caso no lo podemos controlar con el rango generado ya que no tiene un paso general y hay que controlarlo dentro del bucle escribiendo a veces y otras no:

```python
N: int = int(input("Dime el límite: "))

for i in range(1, N+1, 1):
  if i%2 == 0 or i%3 == 0:
    print(i,"->",i*i)
```


## Escribir 10 asteriscos
*Escribir por pantalla 10 asteriscos*

Sabemos escribir fácilmente un asterisco, pero hay que tener cuidado que como no queremos saltar de línea debemos indicarlo: `print("*", end="")`. Luego eso hay que repetirlo 10 veces y al saber cuántas veces se va a repetir lo más sencillo es utilizar el bucle determinista `for` (en la solución también se muestra con `while`). Lo que hay que conseguir que se repita 10 veces hay que crear una colección o rango de 10 valores (los valores realmente nos da igual). Por ejemplo, podemos usar: `range(10)`.

```python
# Versión con for
for i in range(10):
  print("*", end="")
print() # Salto de línea

print()

# Versión con while
n: int = 0
while n < 10:
  print("*", end="")
  n += 1
print()
```


## Sumar números
*Sumar todos los números hasta el 1000*

A diferencia del ejercicio anterior si estamos interesados en generar un rango concreto (los números del 1 al 1000). Eso es fácil con `range(1, 1001)` (recuerde que para que el 1000 esté en el rango debemos ir hasta el 1001). Luego, una vez tenemos los números que necesitamos sumarlos, para ello vamos a usar un acumulador. La forma de pensarla es lo siguiente:
* Imaginemos que ya hemos tratado 15 números (del 1 al 15), ¿de esos 15 números que información nos interesa tener? Lo que nos interesa realmente no son los números sino la suma de todos ellos => variable `suma`
* Muy bien, tenemos una variable que tiene la `suma` de todo lo anterior y tenemos un nuevo `número`, ¿cómo actualizamos las variables (especialmente la importante que es `suma`)? Pues simplemente la siguiente suma será la actual con el nuevo valor: `suma += número` (recuerde que eso es la forma compacta de `suma = suma + número`).
* Finalmente nos queda decir los valores iniciales de la variable, ¿cuánto vale la `suma` al inicio? Pues si no hemos tratado ningún número, la `suma` debe valer 0.

```python
suma: int = 0
for i in range(1, 1001):
  suma += i
print("La suma de los 1000 primeros números es", suma)
```


## Factorial
*Realice un programa que lea un número y calcule el factorial. El factorial de un número n es n! = n*(n-1)*(n-2)*...*3*2*1. El factorial solo está definido para números positivos con el caso especial de que el factorial de 0 es 1 por definición (0! = 1).*

Bastante similar al ejercicio previo pero ahora hay que generar números del 1 al n (incluido) y en vez de sumarlos hay que multiplicarlos.

```python
n: int = int(input("Dime un número: "))

producto: int = 1
for i in range(1, n+1):
  producto *= i
  
print(n, "!= ", producto, sep="")
```

## Figuras

La idea de todos estos ejercicios es practicar los bucles anidados por lo que evitaremos utilizar cosas como `"*"*n`. En general:
* Tendremos un bucle externo que se encarga de dibujar las líneas
* De forma interna hay que pintar cada línea y actualizar las variables para cada línea.
* Hay que decidir qué forma cada línea. Por ejemplo la cuarta línea está formada por: muchos asteriscos + muchoes espacios + nuchos asteriscos + salto de línea:
  *  Muchos asteriscos: `for i in range(num_asteriscos): print("*", end="")`
  *  Muchos espacios: `for i in range(num_espacios): print(" ", end="")`
  *  Salto de línea: `print()`
* Ahora hay que decidir como inicializar las variables que controlan los bucles y como cambian en cada línea. En el mismo ejemplo de antes:
  *  `num_asteriscos` empieza con 1 y cada vez que cambiemos de línea sumamos 1 (en cada lado)
  *  `num_espacios` empieza con 2\*n - 2 (si n es la altura) y cada línea se decrementa en 2

```python
n: int = int(input("Dime la altura: "))

num_asteriscos: int = n

for linea in range(n): # Dibuja líneas
  # Dibujamos una línea
  for i in range(num_asteriscos):
    print("*", end="")
  print()
```

```python
n: int = int(input("Dime la altura: "))

num_asteriscos: int = 1

for linea in range(n): # Dibuja líneas
  # Dibujamos una línea
  for i in range(num_asteriscos):
    print("*", end="")
  print()
  # Actualizamos las variables para la siguiente línea
  num_asteriscos += 1
```

```python
n: int = int(input("Dime la altura: "))

num_asteriscos: int = 1
num_espacios: int = n - 1

for linea in range(n): # Dibuja líneas
  # Dibujamos una línea
  for i in range(num_espacios):
    print(" ", end="")
  for i in range(num_asteriscos):
    print("*", end="")
  print()
  # Actualizamos las variables para la siguiente línea
  num_asteriscos += 1
  num_espacios -= 1
```

```python
n: int = int(input("Dime la altura: "))

num_asteriscos: int = 1
num_espacios: int = 2*n - 2

for linea in range(n): # Dibuja líneas
  # Dibujamos una línea
  for i in range(num_asteriscos):
    print("*", end="")
  for i in range(num_espacios):
    print(" ", end="")
  for i in range(num_asteriscos):
    print("*", end="")
  print()
  # Actualizamos las variables para la siguiente línea
  num_asteriscos += 1
  num_espacios -= 2
```
