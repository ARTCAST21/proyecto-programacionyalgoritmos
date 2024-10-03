"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
AUTORIA PROPIA

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""
# Definimos una lista para almacenar las películas
peliculas = []

# Función para agregar una película a la lista

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                   clasificacion: str, hora: int, dia: str) -> dict:
    pelicula = {
        'nombre': nombre,
        'genero': genero,
        'duracion': duracion,
        'anio': anio,  # Changed 'año' to 'anio' for consistency
        'clasificacion': clasificacion,
        'hora': hora,
        'dia': dia
    }
    return pelicula

# Función para ver todas las películas

def mostrar_informacion_pelicula(pelicula: dict)-> None:
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
            
    if (hora//100 < 10):
        hora_formato = "0"+ str(hora//100)
    else:
        hora_formato = str(hora//100)
    
    if (hora%100 < 10):
        min_formato = "0"+ str(hora%100)
    else:
        min_formato = str(hora%100)

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    d={p1['nombre']:p1, p2['nombre']:p2, p3['nombre']:p3, p4['nombre']:p4, p5['nombre']:p5}
    if nombre_pelicula not in d:
      return None
    else:
        return d[nombre_pelicula]


# Función para obtener la película con la duración máxima

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
   def encontrar_pelicula(pelicula: dict) -> None:
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print(f"Nombre: {nombre} - Anio: {anio} - Duracion: {duracion} mins")
    print(f"Genero: {genero} - Clasificacion: {clasificacion}")

    hora_formato = f"{hora // 100:02}"
    min_formato = f"{hora % 100:02}"

    print(f"Dia: {dia} Hora: {hora_formato}:{min_formato}")

# Funcion para obtener el promedio de las peliculas (algoritmo burbuja)

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    l=[p1['duracion'], p2['duracion'], p3['duracion'], p4['duracion'], p5['duracion']]
    prom=(sum(l)/len(l))
    horas=int(prom//60)
    minutos=int(prom%60)
    return f'{horas}:{minutos}'

def ordenar_por_duracion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)-> list:
    peliculas=[p1,p2,p3,p4,p5]
    l = len(peliculas)
    for i in range(l-1):
        for j in range(i+1, l):
            if peliculas[i]['duracion'] > peliculas[j]['duracion']:
                # Intercambiar
                peliculas[i], peliculas[j] = peliculas[j], peliculas[i]
    print("Películas ordenadas por duración:")
    return peliculas
        

# Función para encontrar películas estrenadas después de una fecha recibida

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    l=[p1['anio'], p2['anio'], p3['anio'], p4['anio'], p5['anio']]
    peliculas=[p1,p2,p3,p4,p5]
    nombres=[]
    for pelicula in peliculas:
      if pelicula['anio']>anio:
        nombres.append(pelicula['nombre'])
    return ','.join(nombres) if nombres else 'Ninguna'


# Función para contar películas con clasificación 18+

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    cont=0
    for pelicula in [p1,p2,p3,p4,p5]:
      if pelicula['clasificacion']=='18+':
        cont+=1
    return cont    

def reagendar_pelicula(pelicula:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    peliculas = [p1, p2, p3, p4, p5]  # Lista de películas programadas
    duracion_pelicula = pelicula['duracion']
    hora_fin_nueva = nueva_hora + duracion_pelicula

    # Verificar conflictos de horario con otras películas
    for p in peliculas:
        if p['dia'] == nuevo_dia and (nueva_hora < p['hora_fin'] and hora_fin_nueva > p['hora_inicio']):
            return False  # Conflicto de horario detectado

    # Verificar restricciones de horario si el usuario así lo desea
    if control_horario:
        if pelicula['genero'] == 'Documental' and nueva_hora >= 22:
            return False  # No ver documentales después de las 10 PM
        if pelicula['genero'] == 'Drama' and nuevo_dia == 'Viernes' and nueva_hora >= 19:
            return False  # No ver dramas los viernes después de las 7 PM
        if nuevo_dia in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'] and (nueva_hora >= 23 or nueva_hora < 6):
            return False  # No ver películas en días de semana después de las 11 PM o antes de las 6 AM

# Ejemplo de uso
pelicula1 = crear_pelicula("Inception", "Ciencia Ficción", 148, 2010, 13, 2100, "Viernes")
pelicula2 = crear_pelicula("Finding Nemo", "Animación", 100, 2003, 7, 1800, "Sábado")

peliculas = [pelicula1, pelicula2]
    
def decidir_invitar(pelicula: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
     # Si el invitado es mayor de edad, puede ver cualquier película.
    if edad_invitado >= 18:
        return True

    # Restricciones para menores de 15 años para películas de género Terror.
    if edad_invitado < 15 and pelicula['genero'] == 'Terror':
        return False

    # Restricciones para invitados de 10 años o menos, solo pueden ver películas Familiares.
    if edad_invitado <= 10 and pelicula['genero'] != 'Familiar':
        return False
    verificar_autorizacion()
    # Requiere autorización de los padres si la clasificación por edad de la película es superior a la edad del invitado,
    # excepto para documentales.
    if pelicula['genero'] != 'Documental' and edad_invitado < pelicula['clasificacion_edad']:
        return autorizacion_padres

    return True

# Verificar autorización
def verificar_autorizacion(pelicula: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    """Verifica si se necesita autorización de los padres para ver la película."""
    if pelicula['genero'] != 'Documental' and edad_invitado < pelicula['clasificacion']:
        edad_invitado = 10
    
    


def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4:dict, p5:dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente 
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir 
        de la aplicacion.
    """
    print("Menu de opciones")
    print(" 1 - Crear pelicula")
    print(" 2 - Listar peliculas")
    print(" 3 - Encontrar pelicula por dato caracteristico [nombre] ")
    print(" 4 - Consultar pelicula mas larga")
    print(" 5 - Consultar duracion promedio de las peliculas")
    print(" 6 - Listar peliculas por duracion")
    print(" 7 - Consultar peliculas de estreno")
    print(" 8 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 9 - Reagendar pelicula")
    print(" 10 - Verificar si se puede invitar a alguien")    
    print(" 11 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        print(crear_pelicula (peliculas,p1, p2, p3, p4, p5))
    elif opcion_elegida == "2":
        print(mostrar_informacion_pelicula("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" + "Genero: " + genero + " - Clasificacion: " + clasificacion + "Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato))
    elif opcion_elegida == "3":
        print(encontrar_pelicula(peliculas,p1, p2, p3, p4, p5))
    elif opcion_elegida == "4":
        print(encontrar_pelicula_mas_larga(p1,p2,p3,p4,p5))
    elif opcion_elegida == "5":
         print(duracion_promedio_peliculas(p1,p2,p3,p4,p5))
    elif opcion_elegida == "6":
       print(ordenar_por_duracion,f"{p['nombre']}: {p['duracion']} minutos")
    elif opcion_elegida == "7":
        print(encontrar_estrenos(p1,p2,p3,p4,p5,2020))    
    elif opcion_elegida == "8":
        print(cuantas_peliculas_18_mas(p1,p2,p3,p4,p5))    
    elif opcion_elegida == "9":
        print(reagendar_pelicula(p3,1700,'viernes',True,p1,p2,p3,p4,p5))    
    elif opcion_elegida == "10":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "11":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando






