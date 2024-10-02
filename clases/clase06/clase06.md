# Clase 6: 30 de septiembre de 2024

En esta clase se repasó la parte de condiciones, sentencias de selección y se empezó a trabajar con sentencias de repetición.

A continuación se muestran los códigos trabajados en clase o aquellos que se dejaron para que los intentase el alumnado.

Especialmente importante para la parte de bucles son los [ejercicios cortos finales](#ejercicios-cortos).

## Ejercicio 5: Sonda Rosetta:

*Un problema al que se enfrentan los ingenieros para el control remoto de estas sondas es que los mensajes sufren un enorme retraso debido a las distancias. Por ejemplo, las comunicaciones entre la tierra y la sonda Rosetta tenían un retraso de 24 minutos. Se nos solicita que se realice un programa que lea la hora de
recepción de un mensaje (hora y minutos) y nos diga la hora en la que fue enviado y si fue en el mismo día o el anterior.*

Existen múltiples soluciones, voy a plantear una sencilla con `if` anidados donde se van evaluando por niveles diferentes aspecto (cambio de hora -en el nivel externo- y cambio de día -en el nivel interno):
```python
# Lectura de valores
hora: int = int(input("Hora de la recepción: "))
minutos: int = int(input("Minutos de la recepción: "))

# Constantes
RETRASO: int = 24

# Cálculos de valores
# Valores más probables
if minutos > RETRASO:
    dia: str = "hoy"
    minutos_finales: int = minutos - RETRASO
    horas_finales: int = hora
else: # Cambio de hora
    minutos_finales: int = minutos - RETRASO + 60 # Ajustamos los minutos de forma apropiada
    if horas == 0: # Cambio de día
        horas_finales: int = 23
        dia: str = "ayer"
    else:
        horas_finales: int = horas -1
        dia: str = "hoy"

# Escritura de valores

# Ponemos 2 cifras siempre
if horas_finales < 10:
    horas_finales = "0" + str(horas_finales)
if minutos_finales < 10:
    minutos_finales = "0" + str(minutos_finales)
print("El mensaje fue enviadoa las ", horas_finales, ":", minutos_finales, " (", dia, ")", sep="")
```

También se puede plantear como un caso donde tenemos tres posibles acciones y plantearlo como una sentencia de selección múltiple:

```python
# Lectura de valores
hora: int = int(input("Hora de la recepción: "))
minutos: int = int(input("Minutos de la recepción: "))

# Constantes
RETRASO: int = 24

# Cálculos de valores
if minutos > RETRASO: # Sin cambio de hora
    dia: str = "hoy"
    minutos_finales: int = minutos - RETRASO
    horas_finales: int = hora
elif hora > 0: # Cambio de hora pero no día
    dia: str = "hoy"
    minutos_finales: int = minutos - RETRASO
    horas_finales: int = hora - 1
else: # Con cambio de hora
    horas_finales = 23
    minutos_finales: int = minutos - RETRASO
    dia = "ayer"

# Escritura de valores

# Ponemos 2 cifras siempre
if horas_finales < 10:
    horas_finales = "0" + str(horas_finales)
if minutos_finales < 10:
    minutos_finales = "0" + str(minutos_finales)
print("El mensaje fue enviadoa las ", horas_finales, ":", minutos_finales, " (", dia, ")", sep="")
```

Como alternativa también se muestra otra solución con un `if` simple en este caso trabajos los datos en minutos:

```python
# Lectura de valores
hora: int = int(input("Hora de la recepción: "))
minutos: int = int(input("Minutos de la recepción: "))

# Constantes
RETRASO: int = 24

# Cálculos de valores
# Valores más probables
dia: str = "hoy"

# Convertimos todo a minutos
minutos_totales: int = hora*60 + minutos - RETRASO

# Ajustamos si no son los valores probables
if minutos_totales < 0: # Cambio de día
    minutos_totales = minutos_totales + 60*24 # Sumamos un día entero para que sea positivo
    dia = "ayer"

# Reconvertimos los minutos a horas y minutos
horas_finales: int = minutos_totales // 60
minutos_finales: int = minutos_totales % 60

# Escritura de valores

# Ponemos 2 cifras siempre
if horas_finales < 10:
    horas_finales = "0" + str(horas_finales)
if minutos_finales < 10:
    minutos_finales = "0" + str(minutos_finales)
print("El mensaje fue enviadoa las ", horas_finales, ":", minutos_finales, " (", dia, ")", sep="")
```

## Ejercicio 8: Días por año:

*Realice un programa que lea el nombre de un mes (entero en minúsculas) y nos día la cantidad de días que tiene ese mes.*

Aunque podríamos hacer un if con 12 casos, realmente hay 3 posibles valores resultantes válidos y podemos agrupar las condiciones. También es recomendable usar primero las condiciones más cortas y dejar para el `else` la más larga ya que no hay que ponerla.

```python
mes: str = input("Dime el mes ")

if mes == "febrero":
    dias = 28
elif mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre":
    dias = 30
else:
    dias = 31

print("El mes", mes, "tiene", dias, "días")
```

## Calculadora

*Realice un programa que actúe como una calculadora simple. Para ello debemos leer dos valores reales, que serán los operadores y una letra, operador. Las posibles operaciones permitidas son +, -, \* o /.*

*Como resultado debe dar el valor de evaluar la operación o ERROR si no fue posible realizarla.*

Es un ejemplo típico de sentencia de selección múltiple.

```python
perando1: float = float(input("Dime el primer operando: "))
operando2: float = float(input("Dime el segundo operando: "))
operación: str = input("Dime qué operación hacer: ")

es_correcto: bool = True
if operación == "+":
  resultado = operando1 + operando2
elif operación == "-":
  resultado = operando1 - operando2
elif operación == "*":
  resultado = operando1 * operando2
elif operación == "/":
  if operando2 == 0:
    print("No se puede dividir entre 0")
    es_correcto = False
  else:
    resultado = operando1 / operando2
else:
  print("Operación inválida")
  es_correcto = False

if es_correcto:
  print(operando1, operación, operando2, "=", resultado)
```

## Ecuación de segundo grado

*Modifique el ejemplo del principio del tema, para que como respuesta el programa indique cuántas soluciones reales tiene (0, 1, 2 o infinitas) y en caso de tener un número contable que indíquelas.*

*Antes de empezar a programar piense los posibles casos:*
* *Hay una situación en la que hay infinitas soluciones*
* *Hay dos situaciones en las que no hay solución (al menos real)*
* *Hay dos situaciones en las que solo hay una solución*
* *Hay una situación en las que hay dos soluciones diferentes*

*Lea los coeficientes y calcule el discriminante (b*b-4ac). Posteriormente use una sentencia de selección múltiple para identificar los casos (únalos cuando sea posible) y calcule las soluciones.*

En este caso no se desarrolló el código pero se da pistas sobre los casos correspondientes:
* Hay una situación en la que hay infinitas soluciones
    * Si a, b y c son 0
* Hay dos situaciones en las que no hay solución (al menos real)
    * Si es discriminante es negativo
    * Si a y b son 0 y c no lo es
* Hay dos situaciones en las que solo hay una solución
    * a es 0 y b no lo es
    * El discriminante es 0
* Hay una situación en las que hay dos soluciones diferentes
    * El discriminante es positivo y mayor que 0 y a no es 0

## Escribir N "Hola Mundo!"

*Realice un programa que escriba N (siendo N leído de teclado) veces la frase "Hola Mundo!"*

Ejemplo usado para introducir el bucle `while`.

```python
N: int = int(input("Dime cuantas veces quieres que diga hola: "))

num_veces: int = 0
while num_veces < N:
  print("Hola Mundo!")
  num_veces += 1
```

## Tabla del 7

*Realice un programa que escriba la tabla de multiplicar del 7.*

Otro ejemplo usado para introducir el bucle `while`.

```python
num: int = 1
while num <= 10:
  print("7 x", num, "=", 7*num)
  num += 1
```

## Ejercicios cortos

### Ejercicio 1
*Lee 20 números y nos diga cuántos 0s hay*

Un elemento importante a destacar en este ejercicio, es que realmente no nos interesan los números concretos que hemos leído hasta el momento si no hay variable que nos almacene un resumen (de la parte que nos interese) de todos esos valores. Es decir, no nos interesa saber si el usuario ha metido 0 1 3 5 0 2 sino que hemos leído 2 ceros. Por ello, tendremos una variable `contador_de_0s` que nos almacene ese valor mientras que los números leídos los podemos ir machacando. Este tipo de variable que resumen los datos contando los valores que cumplen cierta propiedad se denominan **contadores**.

```python
MAX: int = 20 # Valores a leer para las pruebas se puede bajar a algo más manejable (3 o 4)

contador_de_0s: int = 0 # No hemos leído ningún 0
num_veces: int = 0 # Número de números leídos

while num_veces < MAX:
  num: int = int(input("Dime un número: ")) # Valor actual
  if num == 0:
    contador_de_0s += 1
  num_veces += 1

print("Se han leído", contador_de_0s, "0s")
```


### Ejercicio 2
*Lee 10 números y nos diga su suma*

Similar al ejercicio anterior pero en este caso no nos interesa contar, sino sumar (acumular) todos los valores. Estas variables se denominan **acumuladores**.

```python
MAX: int = 10 # Valores a leer para las pruebas se puede bajar a algo más manejable (3 o 4)

suma: int = 0 # No hemos leído ningún valor por lo tanto la suma actual es 0
num_veces: int = 0 # Número de valores leídos

while num_veces < MAX:
  num: int = int(input("Dime un número: ")) # Valor actual
  suma += num
  num_veces += 1

print("La suma vale", suma)
```


