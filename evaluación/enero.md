# Primera convocatoria ordinaria (16/1/25)

## [e1.potencia.py] (2.5 puntos)
*Dada una relación, es decir, un conjunto de pares de números A = {(a,b):a,b∈N}, se denomina potencia de la relación a aquel que se crea aplicando la propiedad transitiva. Es decir, A^n= {(a,b):(a,x)∈A^(n-1) y (x,b)∈A}. Podemos representar un conjunto de pares como una lista de listas que contienen 2 números, como, por ejemplo, `A = [[1,2], [2,5], [3,4], [4,2]]`. Cree una función que reciba una lista de pares de números y devuelva otra lista de pares que represente A2. En el ejemplo anterior, `A^2` sería `[[1,5], [3,2], [4,5]]`.*

```python

def calcular_potencia_a2(relacion: list) -> list:
    a2: list = []
    for r in relacion:
        a: int = r[0]
        x1: int = r[1]
        for r2 in relacion:
            x2: int = r2[0]
            b: int = r2[1]
            if x1 == x2: 
                if [a, b] not in a2:
                    a2.append([a, b])
    return a2

# Programa principal
A = [[1, 2], [2, 5], [3, 4], [4, 2]]
resultado: list = calcular_potencia_a2(A)
print(f"A^2: {resultado}")
```

## [e2.palíndromos.py] (2.5 puntos)
*Dada una frase como cadena de caracteres, escribe una función que indique si se trata de una frase palíndroma (se leen igual del derecho y del revés). A la hora de procesarlo, nótese que habrá letras en mayúsculas y minúsculas que deben tratarse como si fuesen la misma letra. Observe también que la misma puede contener espacios, comas y puntos, que también deberán obviarse. Escriba las funciones auxiliares que considere necesarias. Por ejemplo, `“A mi loca Colima”` y `“Somos, o no somos”` devuelven `True`.*

```python
def limpiar_frase(frase: str) -> str:
    frase = frase.lower()
    frase_limpia: str = ""
    for l in frase:
        if l not in [" ", ",", "."]:
            frase_limpia += l
    return frase_limpia

def es_palindromo(frase: str) -> bool:
    frase_limpia: str = limpiar_frase(frase)
    return frase_limpia == frase_limpia[::-1]


frases = [
    "Mal si le das la fe falsa del Islam",
    "Somos o no somos",
    "Esto no es un palíndromo",
    "A man, a plan, a canal: Panama"
]

for frase in frases:
    print(f'"{frase}" es palíndroma: {es_palindromo(frase)}')
```

## [e3.ong.py] (5 puntos) 
*Una ONG se encarga de organizar carreras solidarias en ciudades españolas e internacionales para recaudar fondos para la investigación del cáncer de mama. La ONG nos pasará un fichero con múltiples líneas con el siguiente formato:*
```text
Ciudad - es_española(0,1): participantes cuota_inscripción
``` 
*Un ejemplo de contenido de ese fichero sería:*
```text
Málaga - 1: 400 10
París - 0: 300 12.5
Sevilla - 1: 267 11
Córdoba - 1: 382 10
Roma - 0: 624 5
```
*Se pide realizar las siguientes funciones (y el programa principal apropiado para probarlas):*

*	*__(1.25p)__ Una función que, recibiendo el nombre del fichero, nos cree una lista de diccionarios con la siguiente forma:*
```python
{
“ciudad”: “Málaga”,
“es_española”: True,
“participantes”: 400,
“cuota”: 10.0,
“recaudado”: 4000.0
}
```
* *__(1.25p)__ Crear una función para calcular el dinero recaudado en total. En el ejemplo, la recaudación sería `17627.0` €*
* *__(1.25p)__ Realizar una función para calcular los porcentajes de recaudación de las ciudades españolas o no españolas con respecto al total. Es decir, dadas las listas anteriores, y un argumento adicional que indica si las ciudades son españolas o no, debe generar una un diccionario que tenga como clave el nombre de la ciudad y como valor el porcentaje (con 2 decimales a lo sumo) que representa su recaudación respecto al total. En el ejemplo, si pedimos las ciudades españolas sería `{'Málaga': 22.69, 'Sevilla': 16.66, 'Córdoba': 21.67}` y si pedimos las no españolas sería `{'París': 21.27, 'Roma': 17.7}`. Nota: para redondear puedes usar la función `round(número,n_decimales)`.*
* *__(1.25p)__ Desarrollar una función que nos devuelva el nombre de la ciudad con mayor recaudación. En el ejemplo, sería `Málaga`.*

```python
def leer_fichero(nombre_fichero: str) -> list:
    lista_ciudades: list = []
    f = open(nombre_fichero, encoding='utf-8')
    for linea in f:
        # Separar la línea por los delimitadores
        ciudad, datos = linea.strip().split(' - ')
        es_española, datos_carrera = datos.split(':')
        participantes, cuota = datos_carrera.split()
        
        # Crear el diccionario
        ciudad_info: dict = {
            "ciudad": ciudad.strip(),
            "es_española": bool(int(es_española)),
            "participantes": int(participantes),
            "cuota": float(cuota),
            "recaudado": int(participantes) * float(cuota)
        }
        lista_ciudades.append(ciudad_info)
    return lista_ciudades

def calcular_recaudacion_total(lista_ciudades: list) -> float:
    suma: float = 0
    for ciudad in lista_ciudades:
        suma += ciudad["recaudado"]
    return suma

def calcular_porcentaje_recaudacion(lista_ciudades: list, es_española: bool) -> dict:
    recaudacion_total: float = calcular_recaudacion_total(lista_ciudades)
    porcentajes: dict = {}
    for ciudad in lista_ciudades:
        if ciudad["es_española"] == es_española:
            porcentajes[ciudad["ciudad"]] = round(ciudad["recaudado"]*100.0 / recaudacion_total, 2)
    return porcentajes

def ciudad_mayor_recaudacion(lista_ciudades: list) -> str:
    mayor_ciudad: str = lista_ciudades[0]["ciudad"]
    mayor_recaudado: float = lista_ciudades[0]["recaudado"]
    for ciudad in lista_ciudades:
        if ciudad["recaudado"] > mayor_recaudado:
            mayor_ciudad = ciudad["ciudad"]
            mayor_recaudado = ciudad["recaudado"]
    return mayor_ciudad

# Programa principal para probar las funciones
nombre_fichero: str = "ong.txt" 
lista_ciudades: list = leer_fichero(nombre_fichero)
    
print("Lista de ciudades:", lista_ciudades)
    
total_recaudado: float = calcular_recaudacion_total(lista_ciudades)
print(f"Recaudación total: {total_recaudado} €")
    
porcentaje_españolas: dict = calcular_porcentaje_recaudacion(lista_ciudades, True)
print("Porcentajes de ciudades españolas:", porcentaje_españolas)
    
porcentaje_no_españolas: dict = calcular_porcentaje_recaudacion(lista_ciudades, False)
print("Porcentajes de ciudades no españolas:", porcentaje_no_españolas)
    
mayor_recaudacion: str = ciudad_mayor_recaudacion(lista_ciudades)
print(f"Ciudad con mayor recaudación: {mayor_recaudacion}")
```
