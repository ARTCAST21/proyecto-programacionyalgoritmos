import modulo_peliculas41024preliminar as mod
pelicula1 = mod.crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
pelicula2 = mod.crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")  
pelicula3 = mod.crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
pelicula4 = mod.crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
pelicula5 = mod.crear_pelicula("The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")   
print(pelicula1)
ejecutando = True
while ejecutando:            
    print("\n\nMi agenda de peliculas para la semana de receso" +"\n"+("-"*50))
    print("Pelicula 1")
    mod.mostrar_informacion_pelicula(pelicula1)
    print("-"*50)
    
    print("Pelicula 2")
    mod.mostrar_informacion_pelicula(pelicula2)
    print("-"*50)
    
    print("Pelicula 3")
    mod.mostrar_informacion_pelicula(pelicula3)
    print("-"*50)
    
    print("Pelicula 4")
    mod.mostrar_informacion_pelicula(pelicula4)
    print("-"*50)
    
    print("Pelicula 5")
    mod.mostrar_informacion_pelicula(pelicula5)
    print("-"*50)
    
    ejecutando = mod.mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

    if ejecutando:
        input("Presione cualquier tecla para continuar ... ")
