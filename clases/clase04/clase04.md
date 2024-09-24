# Clase 04: 23 de septiembre de 2024

En la primera parte de la clase vimos algunos detalles sobre las cadenas de caracteres (string) y que operaciones podemos hacer. De especial interés es cómo acceder a una letra concreta dentro del texto completo mediante su posición.

Luego, empezamoe sl tema 3 donde comenzamos viendo cómo expresar condiciones y las variables booleanas o lógicas (tipo `bool`).

## Generando correos
*La UMA está pensando en autogenerar los correos de los alumnos y estápensando dos posible esquemas:*

* *Primera letra del nombre + un punto + primer apellido + 2 últimas cifras del añode nacimiento*
* *3 primeras letras del nombre + 3 primeras letras del primer apellido + 2 últimascifras del añode nacimiento.*

*Realice un programa que lea el nombre, el apellido y su año de nacimiento (como texto) y genere los dos posibles correos.*

En este ejercicio queremos practica las operaciones sobre cadenas (`str`):
* Para unir textos usamos `+`
* Para acceder a una letra usamos `[pos]`. Por ejemplo, la primera del nombre es `nombre[0]`. Recuerde que las posiciones se numeran empezando en 0.
* Para acceder a subcadenas usamos `[inicio:fin]`. Por ejemplo, los dos últimos de la año sería `año[-2:]` (año debe ser un texto) o las tres primeras del nombre es `nombre[:3]`. 

```python
nombre: str = input("Nombre: ")
apellido: str = input("Apellido: ")
edad_nacimiento: str = input("Edad de nacimiento: ")

correo1: str = nombre[0] + "." + apellido + edad_nacimiento[-2:] + "@uma.es"
correo2: str = nombre[:3] + apellido[:3] + edad_nacimiento[-2:] + "@uma.es"
"""
Algunas observaciones:
* nombre[:3] es equivalente nombre[0:3] o lo que es lo mismo: nombre[0] + nombre[1] + nombre[2]
* edad_nacimiento[-2:] son las dos últimas letras de la edad  
"""

print("Correos:", correo1, "y", correo2)
```

## Ejercicio 1: Evaluación de expresiones lógicas

En este ejercicio se inicializaban ciertas variables y luego se daban una serie de expresiones que usaban operadores lógicos (`and`, `or` y `no`) y había que decir si su evaluación daba verdadero (`True`) o falso (`False`). A continuación se facilita un código para probarlas, aunque la idea importante es saber porqué dan esos valores.

```python
# Valores
s: str = "hola"
x: int = 5
T: bool = x != 10
F: bool = x > 10

# Expresiones lógicas
print("x se evalúa a", bool(x))
print("x - 5 se evalúa a", bool(x-5))
print('s < "adios" se evalúa a', s < "adios")
print('s < "home" se evalúa a', s < "home")
print('s >= "hola!" se evalúa a', s >= "hola!")
print('s >= "Hola" se evalúa a', s >= "Hola")
print("not T se evalúa a",  not T)
print("not not F se evalúa a", not not F)
print("not (T and F) se evalúa a", not (T and F))
print("not T or not F se evalúa a", not T or not F)
print("not (not T or not T) se evalúa a", not (not T or not T))
print("not F or not (F and F) se evalúa a", not F or not (F and F))
```

## Ejercicio 2: Escribir expresiones lógicas

En este ejercicio se dan una serie de condiciones y se pide que se expresen en código Python.

```python
x: int = int(float(input("x = ")))
y: int = int(input("y = "))
c: str = input("c = ")

print("x (", x, ") no es 0:", x != 0)
print("x (", x, ") es un número par:", x%2 == 0)
print("x (", x, ") es un número positivo de tres dígitos:", x > 99 and x < 1000)
print("x (", x, ") termina en dos ceros:", x%100 == 0 and x != 0)
print("x (", x, ") no está en [10, 50]:", x < 10 or x > 50)
print("Ni x (", x, ") ni y (", y, ") son mayores de 10:", x <= 10 and y <= 10)
print("c (", c, ") es una letra mayúscula:", c >= "A" and c <= "Z")
print("c (", c, ") es una letra:", (c >= "A" and c <= "Z") or (c >= "a" and c <= "z"))
print("c (", c, ") es una vocal minúscula:", c == "a" or c == "e" or c == "i" or c == "o" or c == "u")
```
