# Clase 5 (25/09/2024)

En esta clase vemos la estructura de control selectiva que nos permitirá decidir si un código se ejecuta o no atendiendo a una condición.

## Repaso rápido de visto hasta ahora:
Estructura tradiciconal de un programa en python
* Leer datos
    * ¿Qué datos me da el usuario?
    * Para cada dato:
        * `input`
        * ¿Qué mensaje se debe poner?
        * ¿Qué tipo es el dato? ¿se debe convertir?
* Calculos
    * Variables, tipos e identificadores
        * Solo indicar el tipo la primera vez
    * Expresiones
        * Asegurarse que los tipos son correctos o convertirlos
        * `int` -> `//` y `%` (cuando debo separar algo en 2 elementos: minutos -> minutos/hora, número -> en dos partes...)
        * `float` -> `**`
        * `str` -> concatenar (`+`) y obtener parte del texto con `[]` 
    * Cuidado con el orden, las cosas deben ponerse de forma que si una expresión necesita algo, ese algo se calcula antes
    * Cambiar el orden de ejecución -> `bool`, condiciones (`==`, `!=`, ..., `and`, `or`, `not`), selección y bucles
* Escribir resultado
    * ¿Qué resultados debo dar?
    * `print`
    * ¿deben cambiarse los resultados? ¿unidades? ¿redondeo?
    * Generar el formato de salida

## Ejemplo 1: Ecuación de segundo grado

Se muestra como ejemplo un código básico para resolver una ecuación de orden 2. Esta solución se indica que puede tener posibles problemas si se aplica la raíz cuadrada a un número negativo (aunque Python maneja de forma nativa los números complejos con el tipo `complex`) o si se intenta dividir entre 0, si a vale 0 (esto si es provoca un error). Esto demuestra que para ejecutar ciertos códigos, primero sus componentes deben cumplir ciertas condiciones

```python
a: float = float(input("Valor de a: "))
b: float = float(input("Valor de b: "))
c: float = float(input("Valor de c: "))

x1: float = (-b + (b*b - 4*a*c)**0.5)/(2*a)
x2: float = (-b - (b*b - 4*a*c)**0.5)/(2*a)

print("x1 =", x1)
print("x2 =", x2)
```

## Ejemplo 2: Valor absoluto

Como ejemplo de uso de la sentencia de selección simple, se muestra el código del valor absoluto que debe cambiar el signo si el número es negativo pero no hacer nada si es positivo.

```python
num: int = int(input("Dime un numero: "))

if num < 0:
	num = -num

print("El valor absoluto es", num)
```

## Ejemplo 3: Positivo o negativo

Como próximo ejemplo se muestra un código que clasifica el número leído en positivo (incluyendo al 0) o negativo. Para esto es necesario utilizar una sentencia de selección binaria donde el mensaje puede ser uno entre dos posibles

```python
número: int = int(input("Indique un número: "))

if número < 0:
    print("El número es negativo")
else:
    print("El número es positivo o 0")
```

## Ejercicio 1: Menor de dos valores

En este caso se muestran varias alternativas para calcular el menor de dos números leídos de teclado. Todos son correctos, pero hay algunos mejores que otros:

Uno de los código a evitar es:

```python
if a < b:
    b = a
else:
    b = b
print("El menor es:", b)
```

El principal problema de este código es que usa `b = b` que realmente es código que no hace nada y no debería utilizarle.

Otro código poco recomendable es:

```python
if a < b:
    print("El menor es:", a)
else:
    print("El menor es:", b)
```

En este caso repite el `print` en ambas opciones del `if`, lo cual no es recomendable. Si hay partes comunes, lo mejor es evitar repeticiones y sacarlo fuera (antes o después del `if ` atendiendo a la necesidad) y solo ponerlas una vez.

El resto de soluciones son adecuadas y quizás dependiendo del caso podría convenir una más que otra.

# Ejercicio 2: Hora

Realice un programa que pregunte la hora en formato 24h y nos devuelva esa misma hora en formato am/pm. am (Ante meridiem) representa las 12 primeras horas del día y pm (Post meridiem) las últimas 12 horas. 

Aunque se pueden considerar más situaciones, en este caso hay dos posibles casos diferenciados:
* Menor de 12: las horas no cambian y se pone "am"
* Mayor o igual de las 12: a las horas se les resta 12 y se pone "pm"

Con lo visto hasta el momento este ejercicio hay que hacerlo con `if` y `else`:

```python
hora: int = int(input("Hora: "))

if hora < 12:
    valor: str = "am"
else:
    hora = hora - 12
    valor: str = "pm"

print("Son las", hora, valor)
```

Aunque también se puede hacer con un `if` simple

```python
hora: int = int(input("Hora: "))

valor: str = "am"
if hora >= 12:
    hora = hora - 12
    valor: str = "pm"

print("Son las", hora, valor)
```

## Ejercicio 3: Año bisiesto

*Según la Wikipedia un año es bisiesto si "es divisible entre 4, a menos que sea divisible entre 100. Sin embargo, si un año es divisible entre 100 y además es divisible entre 400, también resulta bisiesto."*

*Escriba un programa que dado un año, indique si es bisiesto o no.*

Primero debemos recordar cómo se indicaba la divilidad en python. Usaremos la definición de que b divide a si al hacer la división entre a/b no da de resto 0 (es decir la división da un cociente entero). Eso en python se pone como `a%b == 0`.

Una vez sabido eso es ver como plantear lo que dice el enunciado. Si observamos bien este código plantea 3 posibilidades
* Si es divisible entre 4 y no entre 100 => Bisiesto
* Si es divisible entre 100 y también entre 400 => En este caso si comprobamos solo entre 400 ya se validan ambas de un tirón => Bisiesto
* Resto de casos => No bisiesto

Las dos primeras se podrían unir en una única condición unidas con el operador `or` o ponerlas como casos diferentes en un `if` múltiple. En la siguiente solución se ofrece la priemra alternativa:

```python
año: int = int(input("Año: "))

if (año%4 == 0 and año%100 != 0) or año%400 == 0:
    print("Bisiesto")
else:
    print("No bisiesto")
```

## Ejercicio 4: Menor de tres números

*Realiza un programa que lea 3 números y diga cuál es el menor (use solo condiciones simples, sin and/or)*

Este ejercicio se ha propuesto para que lo hagáis por vuestra cuenta y además en la práctica se hará uno similar. En todo caso, a continuación se facilita el código:

```python
a: int = int(input("Dime un número: "))
b: int = int(input("Dime otro número: "))
c: int = int(input("Dime otro número: "))

# Se propone una solución usando if anidados y sin condiciones compuestas. Existen otro tipo de soluciones más simples
if a < b:
    if a < c:
        menor: int = a
    else:
        menor: int = c
else:
    if b < c:
        menor: int = b
    else:
        menor: int = c

print("El menor de los tres valores es ", menor)
```
## Ejercicio 5: Sonda Rosetta:
*Retrasado para la siguiente clase*

## Ejercicio 6: Calificación

*Pasar de calificación numérica a texto*

Esto aparece en las transparencias como ejemplo, pero ya que de las transparencias se puede copiar peor y por completitud, también lo pongo aquí.

```python
nota: float = float(input("Dime la nota: "))

if nota < 5:
    print("Suspenso :(")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
elif nota < 10:
    print("Sobresaliente")
else:
    print("Matricula de Honor")
```

## Ejercicio 7: Generación

*Realice un programa que lea el año de nacimiento y diga a qué generación perteneces de acuerdo a la siguiente tabla:*

| Años | Generación |
| ---- | ---- |
| < 1946 | No considerados |
| 1946 - 1961 | Baby Boomer |
| 1962 - 1980 | Generación X |
| 1981 - 1996 | Generación Y (millenials) |
| 1997 - 2010 | Generación Z |
| \> 2010 | Generación T (táctil) |

Este es muy parecido al ejemplo anterior. Y de nuevo, lo importante es utilizar el conocimiento y en vez de usar cosas como `elif 1946 <= año and año <= 1961:` y poner cosas como `elif año <= 1961:` aprovechando el conomiento de que las condiciones previas son falsas.

```python
año: int = int(input("Dime tu año de nacimiento: "))

if año < 1946:
    print("Caso no considerado")
elif año < 1962:
    print("Baby Boomer")
elif año < 1981:
    print("Generación X")
elif año < 1997:
    print("Generación Y (millenials)")
elif año < 2011:
    print("Generación Z")
else:
    print("Generación T (táctil)")
```

