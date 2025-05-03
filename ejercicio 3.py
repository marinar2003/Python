# 3) Diseñaremos un programa que analizará cadenas de caracteres (Strings) (40%)
#  Nuestro programa deberá:
#  a) Solicitar al usuario el ingreso de una cadena de caracteres (String) y guardarla en
#  una variable.
#  b) Imprimir, una por una, las letras de esta cadena de caracteres.
#  c) Imprimir la cantidad de letras de esta cadena de caracteres, con el mensaje “La
#  cantidad de letras es:” seguido de la cantidad de letras.
#  d) Ciclar de manera infinita, es decir, solicitar el ingreso de otra cadena de caracteres
#  (inciso a) hasta que el usuario ingrese la palabra clave salir


frase=input("Ingrese una cadena de caracteres..")
for x in range(len(frase)):
    print(frase[x])
    
print(f"La cantidad de letras es: {len(frase)}")


frase2=input("Ingrese otra frase, si desea finalizar escriba -salir-: ")
frase2=frase2.lower()

while frase2!="salir":

    print(frase2)

    frase2=input("Ingrese otra frase, si desea finalizar escriba -salir-: ")

print("Fin.")

        