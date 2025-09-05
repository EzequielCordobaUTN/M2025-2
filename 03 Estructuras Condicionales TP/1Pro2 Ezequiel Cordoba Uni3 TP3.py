#Punto 1
edad =int(input("Ingrese su edad: "))                                        #variable "edad"

if edad <= 0 or edad >= 100:                                                 #Limites de edad
    print("Ingrese una edad valida")
elif edad >= 18:                                                             #Mayor de edad
    print("Eres mayor de edad")
else:                                                                        #Menor de edad
    print("No eres mayor de edad")
print("-------------------------")

#Punto 2
nota =int(input("Ingrese su nota: "))                                        #variable "nota"

if nota <= 0 or nota > 10:                                                   #Limites de nota
    print("Ingrese una nota valida")
elif nota >= 6:                                                              #Aprobado
    print("Esta aprobado")
else:                                                                        #Desaprobado
    print("Esta desaprobado")
print("-------------------------")

#Punto 3
num =int(input("Ingrese un numero: "))                                       #variable "num"

if (num % 2) == 0:                                                           #numero par
    print("Ha ingresado un numero par")
else:                                                                        #numero impar
    print("Por favor, ingrese un numero par")
print("-------------------------")

#Punto 4
edad =int(input("Ingrese su edad: "))                                        #variable "edad"

if edad <= 0 or edad >= 100:                                                 #Limite de edad
    print("Ingrese una edad valida")
elif edad < 12:                                                              #Niño/a
    print("Niño/a")
elif edad >= 12 and edad < 18:                                               #Adolescente
    print("Adolescente")
elif edad >= 18 and edad < 30:                                               #Adulto/a joven
    print("Adulto/a joven")
else:                                                                        #Adulto/a
    print("Adulto/a")
print("------------------------")

#Punto 5
contrasena =str(input("Ingrese una contraseña: "))                           #variable "contraseña"

if len(contrasena) >= 8 and len(contrasena) <= 14:                           #contraseña valida
    print("Ha ingresado una contraseña correcta")
else:                                                                        #contraseña invalida/fuera de los limites
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("------------------------")

#Punto 6
import random
from statistics import mode, median, mean                                    #Importacion de funciones de librerias

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]             #Lista con 50 numeros random que pueden ser del 1 al 100

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)                                         #funciones pasan a ser variables para llamarlas
media = mean(numeros_aleatorios)                                             #una sola vez y que sea mas claro

if media > mediana and mediana > moda: 
    print("Sesgo positivo o a la derecha")             
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")
print("------------------------")

#Punto 7
frase = input("Ingresa una frase o palabra: ")                                #variable "frase"
vocales = "aeiouAEIOU"                                                        #variable "vocales" con las vocales

if len(frase) == 0:                                                           #Error por si el usuario no pone nada
    print("Por favor, ingrese una palabra o frase.")
elif frase[-1] in vocales:                                                    #vocal detectada + ! al final
    print(frase + "!")
else:                                                                         #frase sin vocal al final
    print(frase)
print("------------------------")

#Punto 8
nombre = input("Ingrese su nombre: ")                                         #variable "nombre"
print("Ingrese 1, 2 o 3 para seleccionar una opción:")
print("1. Nombre en mayusculas")
print("2. Nombre en minusculas")
print("3. Nombre con la primera letra en mayuscula")
opcion = int(input("Su opcion: "))                                            #variable "opcion"

if opcion == 1:                                                               #opcion 1: nombre en mayusculas
    nombre_modificado = nombre.upper()
    print(nombre_modificado)
elif opcion == 2:                                                             #opcion 2: nombre en minusculas
    nombre_modificado = nombre.lower()
    print(nombre_modificado)
elif opcion == 3:                                                             #opcion 3: nombre con la primera letra en mayusculas
    nombre_modificado = nombre.title()
    print(nombre_modificado)
else:                                                                         #ninguna de las anteriores
    print("Opción no valida. Por favor, ingrese 1, 2 o 3.") 
print("------------------------")

#Punto 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))                #variable "magnitud"

if magnitud <= 0 or magnitud >= 10:                                           #limites de magnitud
    print("Ingrese un valor valido")
elif magnitud < 3:                                                            #Muy leve
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:                                          #Leve
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:                                          #Moderado
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:                                          #Fuerte
    print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:                                          #Muy fuerte
    print("Muy fuerte (puede causar daños significativos)")
else:                                                                         #Extremo
    print("Extremo (puede causar graves daños a gran escala)")
print("------------------------")

#Punto 10
mes = input("¿Qué mes del año es?: ").lower()
dia = int(input("¿Qué día del mes es?: "))
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()

if (mes == 'diciembre' and dia >= 21) or mes == 'enero' or mes == 'febrero' or (mes == 'marzo' and dia <= 20):
    if hemisferio == 'N':
        print("Invierno")
    elif hemisferio == 'S':
        print("Verano")
elif (mes == 'marzo' and dia >= 21) or mes == 'abril' or mes == 'mayo' or (mes == 'junio' and dia <= 20):
    if hemisferio == 'N':
        print("Primavera")
    elif hemisferio == 'S':
        print("Otoño")
elif (mes == 'junio' and dia >= 21) or mes == 'julio' or mes == 'agosto' or (mes == 'septiembre' and dia <= 20):
    if hemisferio == 'N':
        print("Verano")
    elif hemisferio == 'S':
        print("Invierno")
elif (mes == 'septiembre' and dia >= 21) or mes == 'octubre' or mes == 'noviembre' or (mes == 'diciembre' and dia <= 20):
    if hemisferio == 'N':
        print("Otoño")
    elif hemisferio == 'S':
        print("Primavera")
else:
    print("Entrada no válida. Por favor, revisa tus datos.")
print("------------------------")