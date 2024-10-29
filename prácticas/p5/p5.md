# Práctica 5: Funciones

En práctica se aborda el tema de funciones funciones. Se hizo una serie de ejercicios básicos para practicar los conceptos de funciones.

## Ejercicio 1
*__Función:__ recibe un número que indica los grados centígrados y debe devolver los grados Kelvin (ºK = ºC + 273.15).*

*__Programa principal:__ lea los grados centígrados, llame a la función de conversión y posteriormente escriba los grados Kelvin.*

*__Objetivos:__ Utilización y definición de una función sencilla que recibe un único parámetro y devuelve un valor real. Dónde colocar las funciones.*

```python
def convertir_a_kelvin(grados_cent: float) -> float:
  return grados_cent + 273.15

# Programa principal
grados: float = float(input("Dime los grados centígrados: "))
print(grados, "º centígrados son ", convertir_a_kelvin(grados), "º kelvin", sep= "")
```

## Ejercicio 2
*__Función:__ recibe el precio de un objeto y el impuesto (en porcentaje) y nos devuelve cuál será el precio total a pagar con dicho impuesto agregado (recuerde que el importe total a pagar será precio*(1+impuesto/100)).*

*__Programa principal:__ lea el precio y el impuesto y llame de forma correcta a la función y muestre por pantalla el importe total.*

*__Objetivos:__ Utilización y definición de una función que recibe varios parámetros y devuelve un valor real.*

```python
def calcular_precio(precio: float, impuesto: float) -> float:
  return precio*(1+impuesto/100)

# Programa principal
precio: float = float(input("Dime el precio: "))
iva: float = float(input("Dime el IVA: "))

precio_final: float = calcular_precio(precio, iva)

print("El precio final es", precio_final)
```


## Ejercicio 3

*__Función:__ recibe un único número y nos devuelve si el número es par o impar (un bool).*

*__Programa principal:__ Lea 10 números y nos indique al final cuántos números son pares (para comprobar si son pares utilice la función realizada).*

*__Objetivos:__ Funciones que devuelven un valor booleano.*

```python
def es_par1(x: int) -> bool:
  par: bool = False
  if x%2 == 0:
    par = True
  return par

def es_par2(x: int) -> bool:
  if x%2 == 0:
    return True
  else:
    return False
    
def es_par3(x: int) -> bool:
  return x%2 == 0

# Programa principal
contador: int = 0
for i in range(10):
  número = int(input("Número: "))
  if es_par1(número):
    contador += 1
print("Se han leído", contador, "pares")
```

## Ejercicio 4
*__Función:__ no recibe nada, pero internamente lee números de teclado hasta leer un 0 y que nos devuelve el porcentaje de positivos leídos.*

*__Programa principal:__ Invoca a la función anterior y escriba por pantalla el porcentaje de números positivos leídos.*

*__Objetivos:__ Funciones que no reciben parámetros.*

```python
def leer_números() -> float:
  contador_total: int = 0
  contador_positivos: int = 0
  num = int(input("Número: "))
  while num != 0:
    contador_total += 1
    if num > 0:
      contador_positivos += 1
    num = int(input("Número: "))
  if contador_total == 0:
    return 100
  else:
   return contador_positivos*100 / contador_total
    
porcentaje: float = leer_números()
print("Se leyeron ", porcentaje, "% de positivos")
```

## Ejercicio 5
*__Función:__ recibe un número X y escribe por pantalla todos los números entre 1 y X.*

*__Programa principal:__ lee un número y que invoque a la función anterior con el número leído.*

*__Objetivos:__ Funciones que no devuelvan nada. Dentro de la función no ponga return.*

```python
def escribir_números(X: int) -> None:
  for i in range(1, X+1):
    print(i,end=" ")
  print()
    
N: int = int(input("Dime un número: "))
print("Los N primeros números son: ")
escribir_números(N)
```


## Ejercicio 6
*__Función 1:__ recibe el lado de un triángulo equilátero (triángulo con todos los lados iguales) y nos devuelva la altura del mismo (altura = lado*raiz_cuadrada(3)/2).*

*__Función 2:__ recibe el lado del triángulo y nos devuelva su área (área = lado*altura/2). Llame desde esta función a la anterior para calcular la altura.*

*__Programa principal:__ lee el lado del triángulo y nos muestre por pantalla el área.*

*__Objetivos:__ Funciones que utilizan otras funciones.*

```python
from math import sqrt

def altura_triángulo(lado: float) -> float:
  return lado*sqrt(3)/2

def área_triángulo(lado: float) -> float:
  return lado*altura_triángulo(lado)

# Programa principal
l: float = float(input("Dime el lado del triángulo: "))
print("Su área es: ", área_triángulo(l))
```


## Ejercicio 7
*__Función:__ Realice un subprograma que reciba la temperatura en grados centígrados y nos la devuelva la temperatura en grados kelvin (K = C + 273.15) y grados farenheit (F = C*9/5 + 32).*

*__Programa principal:__ lea una temperatura y mostrar los grados kelvin y farenheit de esa temperatura.*

*__Objetivos:__ Funciones que devuelven varios valores.*

```python
def convertir_temperatura(cent: float) -> (float, float):
  kelvin: float = cent + 273.15
  farenheit: float = cent*9/5 +32
  return kelvin, farenheit

# Programa principal
grados_cent: float = float(input("Dame los grados centígrados: "))
grados_k, grados_f = convertir_temperatura(grados_cent)
print("Los grados kelvin son:", grados_k, "y los farenheit son:", grados_f)
```



