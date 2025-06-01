
#Definimos la funcion datos empleados para obtener los datos sobre nombre y sueldo
def datos_empleado():
#Creamos las listas vacias
    nombre=[]
    sueldo=[]
#Pedimos la cantidad de empleados a ingresar para usar ese dato como condicion en el bucle for
    cantidad=int(input("Los datos de cuantos empleados va a ingresar?: "))
    for x in range (cantidad):
#Pedimos el nombre del empleados con un imput
        txt=input("Ingrese el nombre del empleado: ")
#Guardamos la informacion de la variable en la lista correspondiente
        nombre.append(txt)
#Pedimos el sueldo del empleados mediante otro imput
        monto=float(input(f"Cual es el sueldo de {nombre[x]}: "))
#Guardamos la informacion de la variable en la lista correspondiente
        sueldo.append(monto)
#Retornamos a las listas nombre y sueldo
    return [nombre, sueldo]

#Definimos una funcion para obtener el promedio de los sueldos cargados
def calcular_promedios_sueldos(sueldo):
#Inicializamos la variable suma en 0
    suma=0
#Recorremos la lista sueldo para obtener la suma de todos sus valores
    for x in range(len(sueldo)):
#Los guardamos en la varable suma
        suma=suma+sueldo[x]
#Creamos la variable promedio que sera el resultado de la varible suma dividido la cantidad de elementos de la variable sueldo
    promedio=suma/len(sueldo)
#Mostramos por pantalla el resultado
    print("------------------------------------------------------")
    print(f"El promedio de los sueldos cargados es: {promedio}")
    print("------------------------------------------------------")

#Definimos la funcion para obtener el mayor sueldo ingresado, la funcion necesita de dos parametros, nombre y sueldo.
def obtener_empleado_sueldo_maximo(nombre, sueldos):
#inicializamos las varibles en la posicion 0
    sueldo_maximo=sueldos[0]
    nombre_maximo=nombre[0]
#Recorremos la lista nombre desde la posicion 1, ya que la posicion 0 esta declarada anteriormente
    for x in range(1,len(nombre)):
#Ponemos una condicion para actualizar las variables
        if sueldos[x] > sueldo_maximo:
            sueldo_maximo = sueldos[x]
            nombre_maximo= nombre[x]
#Mostramos por pantalla el resultado del if
    print(f"El mayor sueldo es {sueldo_maximo} y corresponde a {nombre_maximo}.")
    print("------------------------------------------------------")
#Algoritmo de ordenamiento burbuja
def ordenar_por_sueldos(nombre, sueldo):
    n=len(sueldo)#cantidad de elementos de la lista
    for y in range(n -1):#bucle externo
        for z in range(n -1 -y):#bucle interno,controla las comparaciones en cada vuelta
            if sueldo[z] > sueldo[z+1]:
                #si el elemento actual es mayor al siguiente los intercambia
                aux=sueldo[z]
                sueldo[z]=sueldo[z+1]
                sueldo[z+1]=aux
                aux1=nombre[z]
                nombre[z]=nombre[z+1]
                nombre[z+1]=aux1
    print("Los sueldo ordenados de menor a mayor son:")
    print(f"Nombre: {nombre}")
    print(f"Sueldo: {sueldo}")
    print("------------------------------------------------------")


#bloque principal
#Llamar a esta funcion nos permite ingresar los datos
nombre, sueldo=datos_empleado()
#Llamamos a la funcion pasando el parametro de sueldo
calcular_promedios_sueldos(sueldo)
#Llamamos a la funcion pasando dos parametros
obtener_empleado_sueldo_maximo(nombre, sueldo)
#Llamamos a la funcion pasandole dos parametros
ordenar_por_sueldos(nombre,sueldo)
