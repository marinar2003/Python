#  2) Realizar un programa que tomará dos números y nos dirá si el primero es divisible por el
#  segundo. Hará esto ad-infinitum (Es decir, ciclará de forma infinita) hasta que el usuario ingrese
#  un 0(cero) como potencial divisor. (35%)
#  a) Solicitar al usuario un numero entero imprimiendo el mensaje “Ingrese el numero:”.
#  Almacenar este número en una variable.
#  b) Solicitar al usuario otro número entero imprimiendo el mensaje “Es divisible por:”.
#  Almacenar este número en una variable.
#  c) Si el primer número ingresado es divisible por el segundo, imprimir el mensaje “Si”.
#  Delo contrario imprimir “No”.
#  d) Si el segundo número ingresado es un 0 (cero) imprimir “No es posible dividir por 0”
#  y finalizar el programa, de lo contrario repetir el algoritmo desde el punto a


nro1=int(input("Ingrese el numero: "))
nro2=int(input("Es divisible por: "))


while nro2 !=0:

    if nro1%nro2==0:
        print("Si")
    else:
        print("No")

    nro1=int(input("Ingrese el numero: "))
    nro2=int(input("Es divisible por: "))


print("No es posible dividir por 0. Fin del programa")