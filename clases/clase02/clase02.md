# Clase 2 (16/09/2024)

En esta clase vimos gran parte del tema 2 (aunque muchos conceptos ya los habíamos utilizado de manera informal durante el tema 1). A modo de repaso conceptos y aspectos que deben quedar claros son:
* Los conceptos de variables, identificadores y tipos.
* El uso que tienen los tipos `int`, `float` y parcialmente `str` (este lo veremos en más detalle la próxima clase).
* Cómo escribir con el `print(...)`.
* Expresiones aritméticas y los operadores permitidos en python (especialmente la potencia `**`, división entera `//` y resto/módulo `%`).  

## Ejercicio de practicar el `print(...)`

Este ejercicio sirve para practicar el `print(..)` escribiendo varias líneas y que en alguna línea se deba escribir varias cosas y que haya que separarlas por comillas. También en el último apartado se indica que al final de cada línea se pongan 2 saltos de líneas. Eso se puede implementar de diferentes maneras pero la más adecuada es usando en `end` de la siguiente forma: `print(..., end="\n\n")`.

```python
# Con el end forzamos los dos saltos
print("Hola Gabriel!", end="\n\n") 

# En este caso como por defecto el print añade un salto y en el texto pongo manualmente otro, tengo los dos saltos
print("Este es mi primer programa en Python ... de este tema\n") 

horas: int = 0
minutos: int = 21
# En este caso los dos saltos los logro con 2 print que cada uno hace uno (en el siguiente no escribo nada, solo el salto).
print("Han pasado", horas*3600 + minutos*60,"segundos desde el inicio de clase")
print()
```

## Expresiones aritméticas

Este ejercicio sirve para practica el uso de los diferentes operadores matemáticos facilitado por defecto por Python y ver cómo crear expresiones complejas que debemos tener cuidado como las creamos y para evitar problemas usamos paréntesis para asegurar que se hacen en el orden adecuado.

```python
n: int = 2
numero: int = 3
x: int = 4
y: int = 2
x1: int = 1
y1: int = 0
x2: int = 0
y2: int = -1
print("Resultados de las expresiones utilizando los valores indicados en el enuciado:")
print("Expresión 1:", 3**7)
print("Expresión 2:", (2*n)**0.5)
print("Expresión 3:", 20**(-7*numero))
e: float = 2.72
print("Expresión 4:", (7*x)/(e**(20*y)))
print("Expresión 5:", ((x1-x2)**2 + (y1-y2)**2)**0.5)
```
