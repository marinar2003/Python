# Marina Revol, DNI 35258880

# El programa permitirá:
# Cargar películas (título, año, calificación).
# Mostrar películas ordenadas por calificación (mayor a menor).
# Mostrar la película con la mejor calificación, con su año de estreno.
# Calcular el promedio de calificaciones.


#Funcion para cargar los datos de las peliculas
def cargar_peliculas():
    peliculas=[]#Inicializamos la lista en cero
    print("---Bienvenido/a a nuestro programa, a continuación pediremos información sobre sus peliculas favoritas---")
    print("---Esperamos ansiosos sus recomenaciones---")
    cantidad=int(input("Cuantas peliculas va a cargar?: "))#declaramos esta variable para controlar la cantidad de datos a ingresar por el usuario
    for x in range(cantidad):#al for le pasamos como parametro la varibale cantidad indicada por el usuario
        titulo=input("Nombre de la pelicula: ")#pedimos titulo de la pelicula
        año=int(input("Año de estreno: "))#pedimos año de estreno de la pelicula
        calificacion=int(input(f"Del 1 al 5, que calificación obtiene el titulo, {titulo}: "))#pedimos clasificacion de la pelicula
        peliculas.append((titulo,año,calificacion))#agregamos a la lista una tupla con tres datos
    return peliculas#retornamos a la lista

#Funcion para ordenar a las peliculas de mayor a menor calificacion
def peliculas_ordenadas(peliculas):
    indice=0#iniciazilamos esta variable para luego utilizarla en el ordenamiento
    n=len(peliculas)#declaramos la variable n para mayor facilidad de manipulacion en los proximos pasos, inidca cantidad de elementos
    print(f"---------------------------------------------------")
    print(f"Las peliculas ordenadas de mayor a menor valoracion son: ")
    for x in range (n-1):#bucle externo 
        for y in range (n-1-x):#bucle interno, controla las comparaciones en cada vuelta
            if peliculas[y][2]<peliculas[y+1][2]:#si el elemnto actual es menor al siguiente lo intercambia
                aux=peliculas[y]#declaramos una variable auxiliar para guardar el resultado
                peliculas[y]=peliculas[y+1]
                peliculas[y+1]=aux
    for pelicula in peliculas:#Recorremos la lista peliculas para obtener los valores que necesitamos de las tuplas
        indice+=1
        print(f"{indice}. {pelicula[0]}, calificacion: {pelicula[2]}")#mostramos por pantalla la lista ordenamos de mayor a menor con los datos de nombre y valoracion
    print(f"---------------------------------------------------")

#Funcion para mostrar solo la pelicula o las peliculas mejores calificadas. Adicionando el año de estreno
def pelicula_mejor_calificada(peliculas):
    mayor_calificacion=peliculas[0][2]#Establecemos la mayor calificacion en el primer elemento de la lista
    for x in range(1,len(peliculas)):#recorremos la lista para comparar los elementos y asi establecer la mayor calificacion
        if peliculas[x][2]>mayor_calificacion:#comparamos los elemenos en cada vuelta cn la variable 
            mayor_calificacion=peliculas[x][2]#en el caso se el elemento a comparar sea mayor que la variable establecemos ese valor como mayor
    print(f"Película/s con la mayor calificacion indicada de {mayor_calificacion} puntos: ")#anunciamos por pantalla cual es la calificacion mayor obtenida
    for pelicula in peliculas:#recorremos la lista para averiguar si tenemos mas de un elemento o no con la mayor calificacion
        if pelicula[2] == mayor_calificacion:#si el elemento es igual a la mayor calificacion lo imprimimos por pantalla sino no
            print(f"Título: {pelicula[0]}, Año: {pelicula[1]}.")#mostramos lo/s titulo/s con mayor calificacion
    print(f"---------------------------------------------------")

#creamos la funcion para calcular el promedio de calificacion de las peliculas cargadas    
def promedio_calificaciones(peliculas):
    suma=0#creamos la variable suma para almacenar los valores
    for pelicula in peliculas:#recorremos la lista para obtener los valores de las calificaciones
        suma+=pelicula[2]#en cada vuelta tomamos el valor y lo sumamos en la variable suma
        promedio=suma/len(peliculas)#creamos la variable promedio(suma dividido la cantidad de elementos de la lista)
    print(f"El promedio de calificacion de las peliculas cargadas es: {promedio}")#mostramos por pantalla el resultado de la variable promedio
    print(f"---------------------------------------------------")
    print(f"Gracias por cargar sus peliculas favoritas!..")
    print(f"---------------------------------------------------")

#bloque principal

peliculas = cargar_peliculas()#llamamos a la funcion para poder ingresar los datos
peliculas_ordenadas(peliculas)#pasamos el parametro a la variable para invocarla
pelicula_mejor_calificada(peliculas)#pasamos el parametro pelicula para invocarla
promedio_calificaciones(peliculas)#volvemos a pasar el parametro peliculas para invocar a la funcion
