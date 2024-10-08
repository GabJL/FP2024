# Práctica 3

## [p3e01.notas1.py] (★✰✰✰✰)  
*Escribe un programa que lea las notas de 80 alumnos y nos diga la cantidad de aprobados que hay (nota >= 5). NOTA: Para probar como 80 valores es muy tedioso de meterlos, pruebe a cambiar el bucle y que pare cuando lea 4-5 valores (use una constante para indicar la cantidad de alumnos y así sea sencillo cambiarlo). Ejemplo:*

```
 Introduce 5 notas: 
 Nota: 3.2  
 Nota: 9  
 Nota: 5.5  
 Nota: 7  
 Nota: 4.9 
 Hay 3 alumnos aprobados 
```

*__OBJETIVOS:__ Realizar un bucle determinista (`for`) y usando un contador que depende de una condición.*

```python
MAX_NOTAS: int = 5

print("Introduce", MAX_NOTAS,"notas:")

aprobados: int = 0
for i in range(MAX_NOTAS):
  nota: float = float(input("Nota: "))
  if nota >= 5:
    aprobados += 1
    
print("Hay", aprobados, "alumnos aprobados")
```
 
## [p3e02.notas2.py] (★✰✰✰✰) 
*Haga una copia del programa previo y modifícalo para que calcule la nota media de los alumnos aprobados.  Ejemplo:*
 
```
 Introduce 5 notas: 
 Nota: 3.2  
 Nota: 9  
 Nota: 5.5  
 Nota: 7  
 Nota: 4.9 
 Hay 3 alumnos aprobados con nota media de 7.166666 
```

*__OBJETIVOS:__ Uso de acumuladores.*
 
```python
MAX_NOTAS: int = 5

print("Introduce", MAX_NOTAS,"notas:")

aprobados: int = 0
suma: flota = 0
for i in range(MAX_NOTAS):
  nota: float = float(input("Nota: "))
  if nota >= 5:
    aprobados += 1
    suma += nota
        
if aprobados == 0:
  print("No hay alumnos aprobados")
else:
  print("Hay", aprobados, "alumnos aprobados con nota media de ", suma/aprobados)
```

## [p3e03.notas3.py] (★★★✰✰) 
*Modifique el programa previo para que, en vez de ser un número fijo de notas, acabe cuando se introduzca una nota inválida (fuera del rango \[0,10\]). Ejemplo:*

```
 Introduce notas (acabe con una incorrecta): 
 Nota: 3.2 
 Nota: 9  
 Nota: 5.5  
 Nota: 7  
 Nota: 4.9  
 Nota: 11.6 
 Hay 3 alumnos aprobados con nota media de 7.166666 
```
 
*__OBJETIVOS__: Uso de la lectura adelantada para crear un bucle no determinista (`while`).*
 
*__NOTA__: Ya que la condición para salir/entrar en el bucle depende por los números introducidos por el usuario, use lectura adelantada:*

```
Leer nota 
while condición: # Si la nota es correcta 
 Procesar nota # Ver si es aprobado o no y hacer lo oportuno  
 Leer otra nota 
```

```python
print("Introduce notas (acabe con una incorrecta): ")

aprobados: int = 0
suma: float = 0
nota: float = float(input("Nota: "))
while nota >= 0 and nota <= 10:
    if nota >= 5:
        aprobados += 1
        suma += nota
    nota = float(input("Nota: "))
        
if aprobados == 0:
    print("No hay alumnos aprobados")
else:
    print("Hay", aprobados, "alumnos aprobados con nota media de ", suma/aprobados)
```


## [p3e04.notas4.py] (★★★✰✰) 
*Modifique el programa previo para que almacene la mejor nota. Ejemplo:*
 
```
 Introduce notas (acabe con una incorrecta): 
 Nota: 3.2 
 Nota: 9  
 Nota: 5.5  
 Nota: 7  
 Nota: 4.9  
 Nota: 11.6 
 Hay 3 alumnos aprobados con nota media de 7.166666 
 La mejor nota fue un 9 
```
 
*__OBJETIVOS__: Cálculo de valores destacados.*

*__NOTA__: Debido a que las notas deben estar en un rango, es fácil inicializar la mejor, pero intente pensar alguna forma de inicializar ese valor sin depende de saber que los valores están en ese rango.*

```python
print("Introduce notas (acabe con una incorrecta): ")

aprobados: int = 0
suma: float = 0
nota: float = float(input("Nota: "))
mejor: float = nota
while nota >= 0 and nota <= 10:
    if nota >= 5:
        aprobados += 1
        suma += nota
    if nota > mejor:
        mejor = nota
    nota = float(input("Nota: "))
        
if aprobados == 0:
    print("No hay alumnos aprobados")
else:
    print("Hay", aprobados, "alumnos aprobados con nota media de ", suma/aprobados)
    
if mejor >= 0 and mejor <= 10:
    print("La mejor nota fue un", mejor)
else:
    print("No se introdujeron valores correctos")
```


## [p3e05.figura.py] (★★★★✰) 
*Realice un programa que lea la altura de la figura (realmente la altura representa media figura) y la dibuje tal como muestra el ejemplo:*
```
 Diga la altura: 5 
     * 
    *** 
   ***** 
  ******* 
 ********* 
  ******* 
   ***** 
    *** 
     *  
```

*__OBJETIVOS__: Trabajo con bucles anidados.*
 
*__NOTAS__: Divida la figura en dos sub-figuras y resuélvalos por separado.*

```python
n: int = int(input("Dime la altura: "))

num_espacios: int = n - 1
num_asteriscos: int = 1

# Triángulo superior
for linea in range(n):
    # Dibujamos la línea:
    # Primero espacios
    for i in range(num_espacios):
        print(" ", end="")
    # Luego asteriscos
    for i in range(num_asteriscos):
        print("*", end= "")
    # Y acabamos con un salto de línea
    print()
    # Ahora actualizamos los espacios y asteriscos para la siguiente línea
    num_espacios -= 1
    num_asteriscos += 2
    
# Triángulo superior
num_espacios += 2 
num_asteriscos -= 4

for linea in range(n):
    # Dibujamos la línea:
    # Primero espacios
    for i in range(num_espacios):
        print(" ", end="")
    # Luego asteriscos
    for i in range(num_asteriscos):
        print("*", end= "")
    # Y acabamos con un salto de línea
    print()
    # Ahora actualizamos los espacios y asteriscos para la siguiente línea
    num_espacios += 1
    num_asteriscos -= 2
```

## [p3e06.mcm.py]  (★★★✰✰)  
*Escribir  un  programa  para  hallar  el  valor  del  mcm  (mínimo  común  múltiplo)  de  dos números enteros positivos que se leen como entrada (n1 y n2). El mcm es el menor valor que es divisible entre los dos números. Ejemplo:* 
 
```
Diga un número: 20  
Diga otro número: 6 
El mcm es 60 
```
 
*__OBJETIVOS__: Diseño de algoritmos con bucles que requieren pensar.*
 
*__NOTA__:  Haga  un  bucle  que  vaya  generando  números  cada  vez  más  grandes  hasta  encontrar  uno  que  cumpla  la condición.*

```python
n1: int = int(input("Diga un número: "))
n2: int = int(input("Diga otro número: "))

if n1<n2:
    mayor: int = n2
else:
    mayor: int = n1

mcm: int = mayor

while mcm % n1 !=0 or mcm % n2 !=0:
    mcm += mayor
    
print("El mcm es", mcm)
```

