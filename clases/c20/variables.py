# Ejercicio 1 y 2

Málaga: dict = {"enero": 12, "febrero": 12, "marzo": 14, "abril": 16, "mayo": 19, "junio": 23, "julio": 26, "agosto": 26,"septiembre": 23, "octubre": 19, "noviembre": 15, "diciembre": 13}

Yakustk: dict = {"enero": -38, "febrero": -34, "marzo": -20, "abril": -5, "mayo": 8, "junio": 16, "julio": 20, "agosto": 15, "septiembre": 6, "octubre": -8, "noviembre": -27, "diciembre": -37}

# Ejercicio 3
Salud: dict = {
  "Bioquímica estructural": [0.66, 0.61, 0.47, 0.64, 0.92, 1.0, 0.84, 0.61, 0.79, 0.87], 
  "Cálculo": [0.55, 0.52, 0.48, 0.29, 0.29, 0.11, 0.36, 0.77, 0.63, 0.71], 
  "Fundamentos de la programación": [0.58, 0.66, 0.53, 0.76, 0.7, 0.74, 0.58, 0.81, 0.74, 0.89], 
  "Física I": [0.23, 0.41, 0.38, 0.45, 0.37, 0.48, 0.62, 0.51, 0.67, 0.75], 
  "Álgebra lineal": [0.48, 0.44, 0.46, 0.54, 0.61, 0.49, 0.57, 0.72, 0.73, 0.79]
}

# Ejercicio 4
peli = "en Deadpool & Wolverine == Action, Comedy, Science Fiction == Shawn Levy == Lewis Tan, Ed Kear, Nick Pauley, Hugh Jackman == 128.0 200000000.0 1337900827.0 7.7 24-7-2024 == A listless Wade Wilson toils away in civilian life with his days as the morally flexible mercenary, Deadpool, behind him. But when his homeworld faces an existential threat, Wade must reluctantly suit-up again with an even more reluctant Wolverine. "

# Código inicial: ejercicio 4
# FUnciones
def analizar_peli(peli_texto: str) -> dict:
    # Separar datos
    idioma: str = peli_texto[:2]
    resto: str = peli_texto[3:]
    titulo, generos, directores, actores, datos, descripción = resto.split("==")
    generos: list = generos.split(",")
    directores: list = directores.split(",")
    actores: list = actores.split(",")
    duración, coste, recaudación, puntuación, fecha = datos.split()
    dia, mes, año = fecha.split("-")
    # Limpiar los datos y convertir
    idioma = idioma.strip()
    titulo = titulo.strip()
    for i in range(len(generos)):
        generos[i] = generos[i].strip()
    for i in range(len(directores)):
        directores[i] = directores[i].strip()
    for i in range(len(actores)):
        actores[i] = actores[i].strip()
    duración = float(duración)
    coste = float(coste)
    recaudación = float(recaudación)
    puntuación = float(puntuación)
    dia = int(dia)
    mes = int(mes)
    año = int(año)
    descripción = descripción.strip()
    # Creamos diccionario
    peli: dict = {
        "idioma": idioma,
        "título": titulo,
        "géneros": generos,
        "directores": directores,
        "actores": actores,
        "duración": duración,
        "presupuesto": coste,
        "recaudación": recaudación,
        "puntuación": puntuación,
        "día": dia,
        "mes": mes,
        "año": año
    }
    # Devolver diccionario
    return peli

def leer_fichero_pelis(nombre: str) -> list:
    # abrir el fichero
    fichero = open(nombre, encoding="utf-8")
    lista_pelis: list = []
    # Leer el fichero línea a línea
    for peli in fichero:
        lista_pelis.append(analizar_peli(peli))     
    # Cerrar el fichero
    fichero.close()
    return lista_pelis
    
    
# Programa principal
peli = "en Deadpool & Wolverine == Action, Comedy, Science Fiction == Shawn Levy == Lewis Tan, Ed Kear, Nick Pauley, Hugh Jackman == 128.0 200000000.0 1337900827.0 7.7 24-7-2024 == A listless Wade Wilson toils away in civilian life with his days as the morally flexible mercenary, Deadpool, behind him. But when his homeworld faces an existential threat, Wade must reluctantly suit-up again with an even more reluctant Wolverine. "
print(analizar_peli(peli))
lista_películas: list = leer_fichero_pelis("pelis.txt")
print(lista_películas[0])
