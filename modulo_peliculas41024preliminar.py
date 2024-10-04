# Lista para almacenar películas
peliculas = []

# Función para agregar una película
def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, clasificacion: str, hora: int, dia: str) -> dict:
    pelicula = {
        'nombre': nombre,
        'genero': genero,
        'duracion': duracion,
        'anio': anio,
        'clasificacion': clasificacion,
        'hora': hora,
        'dia': dia
    }
    return pelicula

# Función para ver la información de una película
def mostrar_informacion_pelicula(pelicula: dict) -> str:
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]

    hora_formato = f"{hora // 100:02}"
    min_formato = f"{hora % 100:02}"

    return (f"Nombre: {nombre} - Año: {anio} - Duración: {duracion} mins - Género: {genero} "
            f"- Clasificación: {clasificacion} - Día: {dia} - Hora: {hora_formato}:{min_formato}")

# Función para encontrar película por nombre
def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    peliculas_dict = {p1['nombre']: p1, p2['nombre']: p2, p3['nombre']: p3, p4['nombre']: p4, p5['nombre']: p5}
    return peliculas_dict.get(nombre_pelicula)

# Función para encontrar la película con mayor duración
def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    peliculas = [p1, p2, p3, p4, p5]
    return max(peliculas, key=lambda x: x['duracion'])

# Función para obtener la duración promedio de las películas
def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    duraciones = [p1["duracion"], p2["duracion"], p3["duracion"], p4["duracion"], p5["duracion"]]
    promedio = sum(duraciones) / len(duraciones)
    horas = int(promedio // 60)
    minutos = int(promedio % 60)
    return f"{horas}:{minutos}"

# Función para ordenar películas por duración
def ordenar_por_duracion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> list:
    peliculas = [p1, p2, p3, p4, p5]
    peliculas.sort(key=lambda x: x['duracion'])
    return peliculas

# Función para encontrar estrenos después de una fecha
def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    peliculas = [p1, p2, p3, p4, p5]
    estrenos = [p['nombre'] for p in peliculas if p['anio'] > anio]
    return ", ".join(estrenos) if estrenos else "Ninguna"

# Función para contar películas con clasificación 18+
def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    peliculas = [p1, p2, p3, p4, p5]
    return sum(1 for p in peliculas if p['clasificacion'] == "18+")

# Función para reagendar una película
def reagendar_pelicula(pelicula: dict, nueva_hora: int, nuevo_dia: str, control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    peliculas = [p1, p2, p3, p4, p5]
    duracion_pelicula = pelicula['duracion']
    hora_fin_nueva = nueva_hora + duracion_pelicula

    for p in peliculas:
        if p['dia'] == nuevo_dia and (nueva_hora < p['hora'] + p['duracion'] and hora_fin_nueva > p['hora']):
            return False

    if control_horario:
        if pelicula['genero'] == 'Documental' and nueva_hora >= 2200:
            return False
        if pelicula['genero'] == 'Drama' and nuevo_dia == 'Viernes' and nueva_hora >= 1900:
            return False
        if nuevo_dia in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'] and (nueva_hora >= 2300 or nueva_hora < 600):
            return False
    return True
# Funcion para invitar a alguien
def verificar_autorizacion(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    """Verifica si se necesita autorización de los padres para ver la película."""
    if peli['genero'] != 'Documental' and edad_invitado < peli['clasificacion']:
        return autorizacion_padres

    return True
def decidir_invitar(pelicula: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    if edad_invitado >= 18:
        return True

    if pelicula['genero'] == 'Terror' and edad_invitado < 15:
        return False

    if pelicula['genero'] != 'Familiar' and edad_invitado <= 10:
        return False

    return verificar_autorizacion(pelicula, edad_invitado, autorizacion_padres)

# Función principal para mostrar el menú y ejecutar las opciones
def mostrar_menu_aplicacion():
    print("\nMenú de opciones")
    print(" 1 - Crear película")
    print(" 2 - Listar películas")
    print(" 3 - Encontrar película por nombre")
    print(" 4 - Consultar película más larga")
    print(" 5 - Consultar duración promedio de las películas")
    print(" 6 - Listar películas por duración")
    print(" 7 - Consultar películas de estreno")
    print(" 8 - Consultar cuántas películas tienen clasificación 18+")
    print(" 9 - Reagendar película")
    print(" 10 - Verificar si se puede invitar a alguien")
    print(" 11 - Salir de la aplicación")

# Función principal que ejecuta el menú
def main():
    pelicula1 = crear_pelicula("Inception", "Ciencia Ficción", 148, 2010, 13, 2100, "Viernes")
    pelicula2 = crear_pelicula("Finding Nemo", "Animación", 100, 2003, 7, 1800, "Sábado")
    pelicula3 = crear_pelicula("Icarus", "Documental, Suspenso", 122, 2017, 18, 800, "Domingo")
    pelicula4 = crear_pelicula("Inception", "Acción, Drama", 148, 2010, 13, 1300, "Lunes")
    pelicula5 = crear_pelicula("The Empire Strikes Back", "Familiar, Ciencia Ficción", 124, 1980, 7, 1415, "Miércoles")
    
    peliculas = [pelicula1, pelicula2, pelicula3, pelicula4, pelicula5]
    continuar_ejecutando = True

    while continuar_ejecutando:
        opcion_elegida = input("\nIngrese la opción que desea ejecutar: ").strip()

        if opcion_elegida == "1":
            nombre = input("Ingrese el nombre de la película: ")
            genero = input("Ingrese el género de la película: ")
            duracion = int(input("Ingrese la duración de la película en minutos: "))
            anio = int(input("Ingrese el año de estreno de la película: "))
            clasificacion = input("Ingrese la clasificación de la película: ")
            hora = int(input("Ingrese la hora a la que se planea ver la película (HHMM): "))
            dia = input("Ingrese el día de la semana en el que se planea ver la película: ")
            nueva_pelicula = crear_pelicula(nombre, genero, duracion, anio, clasificacion, hora, dia)
            peliculas.append(nueva_pelicula)
            print("Película creada:", mostrar_informacion_pelicula(nueva_pelicula))

        elif opcion_elegida == "2":
            for pelicula in peliculas:
                print(mostrar_informacion_pelicula(pelicula))

        elif opcion_elegida == "3":
            nombre = input("Ingrese el nombre de la película a buscar: ")
            pelicula_encontrada = encontrar_pelicula(nombre, *peliculas)
            if pelicula_encontrada:
                print(mostrar_informacion_pelicula(pelicula_encontrada))
            else:
                print("Película no encontrada.")

        elif opcion_elegida == "4":
            pelicula_larga = encontrar_pelicula_mas_larga(*peliculas)
            print("Película más larga:", mostrar_informacion_pelicula(pelicula_larga))

        elif opcion_elegida == "5":
            print("Duración promedio:", duracion_promedio_peliculas(*peliculas))

        elif opcion_elegida == "6":
            for pelicula in ordenar_por_duracion(*peliculas):
                print(mostrar_informacion_pelicula(pelicula))

        elif opcion_elegida == "7":
            anio = int(input("Ingrese el año de estreno mínimo: "))
            print("Estrenos después del año", anio, ":", encontrar_estrenos(*peliculas, anio))

        elif opcion_elegida == "8":
            print("Cantidad de películas con clasificación 18+:", cuantas_peliculas_18_mas(*peliculas))

        elif opcion_elegida == "9":
            print("Intentando reagendar película:")
            resultado = reagendar_pelicula(pelicula1, 1700, 'Viernes', True, *peliculas)
            print("Reagendamiento exitoso" if resultado else "No se pudo reagendar.")
        elif opcion_elegida == "10":
            edad_invitado = int(input("Ingrese la edad del invitado: "))
            autorizacion_padres = input("¿Tiene autorización de los padres? (S/N): ").upper() == "S"
            print("Invitación permitida:", decidir_invitar(pelicula1, edad_invitado, autorizacion_padres))
        
        elif opcion_elegida == "11":
            continuar_ejecutando = False
            print("Saliendo de la aplicación...")
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.")


# Ejecutar la aplicación
if __name__ == "__main__":
    main()
