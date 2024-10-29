# Práctica 4

Uso de sentencias de repetición (while y for) en python. 

## p4e01.adn.py (★✰✰✰✰) 
*Escriba un programa que lea una cadena de ADN (texto formado por múltiples letras que puede ser A, C, T y G que representan a los aminoácidos Adenina, Citosina, Timina y Guanina) y un aminoácido
y nos diga cuántas veces aparece ese aminoácido en la cadena de ADN. Ejemplo:*

```
Cadena de ADN: ACCTGGAACTTGC
Aminoácido: C
El aminoácido C aparece 4 veces
```

*__NOTA__: Podemos hacer for letra in texto: y en cada iteración en la variable letra se almacenará una letra de texto. Entonces dentro del bucle podemos hacer comprobaciones y cálculos con la variable letra.*

*__OBJETIVOS__: Usar un bucle for para recorrer una colección de datos (string en este caso).*

```python
cadena: str = input("Cadena de ADN: ")
aminoácido: str = input("Aminoácido: ")
contador: int = 0

for letra in cadena:
  if aminoácido == letra:
    contador += 1

print("El aminoácido", aminoácido,"aparece", contador, "veces")
```

## p4e02.orden.py (★✰✰✰✰) 
*Escriba un programa que lea de forma continua tres valores hasta que los tres números sean valores __estrictamente__ crecientes. Ejemplo:*

```
Diga tres números crecientes: 
20 
22 
19
Diga tres números crecientes: 
-1 
2 
2
Diga tres números crecientes: 
38 
50 
77
¡Gracias!
```

*__OBJETIVOS:__ Realizar un bucle indeterminista simple.*

```python
# Lectura adelantada
print("Diga tres números crecientes: ")
n1: int = int(input())
n2: int = int(input())
n3: int = int(input())

while n1 >= n2 or n2 >= n3:
  print("No son crecientes. Diga tres números crecientes: ")
  n1 = int(input())
  n2 = int(input())
  n3 = int(input())

print("¡Gracias!")
```

## p4e03.primo.py (★★★✰✰) 
*Escribir un programa que lea por teclado un número natural y muestre por pantalla Si el número es primo o no. Dos ejemplos:*

```
Introduce un número natural: 13
El número 13 es primo

Introduce un numero natural: 26
El número 26 no es primo
```

*__NOTA:__ La definición de un número primo es que solo es divisible entre 1 y sí mismo. Genere todos los otros posibles divisores (2, 3, 4, …, numero-1). Será primo si no encuentra nuevos divisores. Intente hacer una versión eficiente.*

*__OBJETIVOS:__ Uso del bucle `for` y contadores.*

```python
n: int = int(input("Introduce un número natural: "))

i: int = 2
while i < n and n % i != 0:
  i += 1

print("El número", n, end=" ")
if i >= n:
  print("es primo")
else:
  print("no es primo")
```

## p4e04.primos2.py (★★★★✰) 
*Haga una copia del programa del ejercicio anterior y modifícalo de la siguiente forma: lea dos valores y muestre todos los primos en el rango (no debe suponer que los valores estén ordenados). Ejemplo:*

```
Introduce dos valores: 10 2
Los primos en el rango son 2 3 5 7
```

*__NOTA:__ Tenga la precaución de a la hora de calcular si un número es primo o no (bucle interno) de reiniciar todas las variables que sean utilizadas por dicho proceso.*

*__OBJETIVOS:__ Bucle anidados.*

```python
n1: int = int(input("Introduce un valor: "))
n2: int = int(input("Introduce un valor: "))

if n2 < n1:
  aux: int = n1
  n1 = n2
  n2 = aux

print("Los primos en el rango son", end=" ")
for n in range(n1, n2):
  i: int = 2
  while i < n and n % i != 0:
    i += 1
  if i >= n:
    print(n, end=" ")
```

## p4e05.figura.py (★★✰✰✰) 
*Partiendo del código del ejercicio anterior, modifícalo de la siguiente forma: lea dos valores y muestre todos los primos en el rango (no debe suponer que los valores estén ordenados). Ejemplo:*

```
Lado: 5

XXXXX
X   X
X   X
X   X
XXXXX
```

*__OBJETIVOS:__ Bucles anidados y ser capaz de dividir el problema en partes y resolverlas por separado*

```python
lado: int = int(input("Lado: "))

# Linea superior
for i in range(lado):
  print("*", end="")
print()

# Parte central
for lineas in range(lado-2):
  print("*", end="")
  for i in range(lado-2):
    print(" ", end="")
  print("*")

# Linea inferior
for i in range(lado):
  print("*", end="")
print()
```

## p4e06.suma_digitos.py (★★★★★) 
*Escribir un algoritmo que lea por teclado un número natural y muestre por pantalla la suma de todos sus dígitos. Ejemplo:*

```
Introduce un número natural: 12321
La suma de los dígitos es 9
```

*__NOTA:__ Las operaciones de división enteras son muy útiles para este caso:*
* *Puedo obtener un dígito de un número con el resto entre 10 (`%10` => `1234 % 10` es `4`).*
* *Una vez tratado el dígito puede eliminarlo con el cociente entero entre 10 (`//10` => `1234 // 10` es `1234`).*
* *Vaya quitando dígito a dígito y sumándolos y cuando el número que nos quede sea 0, ya habremos acabado.*

*__OBJETIVOS:__ Diseño de algoritmos con bucles que requieren pensar. Bucles cuya condición dependen de cálculos.*

```python
n: int = int(input("Introduce un número natural: "))

suma: int = 0

while n != 0:
  ultimo_digito = n % 10
  n = n // 10
  suma += ultimo_digito

print("La suma de los dígitos es:", suma)
```
