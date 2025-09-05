#Programa 1
print("Hola Mundo!")
print("-----------------------------------")

#Programa 2
nombre = input("Dime tu nombre:")
print(f"Hola {nombre}!")
print("-----------------------------------")

#Programa 3
nombre = input("Dime tu nombre:")
apellido = input("Dime tu apellido:")
edad = input("Dime tu edad:")
LugarDeResidencia = input("Dime tu lugar de residencia:")

print(f"Hola {nombre} {apellido}, tienes {edad} y vives en {LugarDeResidencia}")
print("----------------------------------")

#Programa 4
from math import pi

radio = float(input("Ingrese el radio del circulo: "))
area = float(pi * radio**2)
perimetro = float(2 * pi * radio)

print(f"El area del circulo es {round(area, 2)} y el perimetro es {round(perimetro, 2)}")
print("----------------------------------")

#Programa 5
segundos = int(input("Ingrese una cantidad de segundos: "))
minutos = int(segundos / 60)
horas = int(minutos / 60)

print(f"{segundos} segundos equivalen a {horas} horas")
print("----------------------------------")

#Programa 6
tabla = int(input("Ingrese un numero: "))
print(" ")
print(f"{tabla} x 1 es {tabla * 1}")
print(f"{tabla} x 2 es {tabla * 2}")
print(f"{tabla} x 3 es {tabla * 3}")
print(f"{tabla} x 4 es {tabla * 4}")
print(f"{tabla} x 5 es {tabla * 5}")
print(f"{tabla} x 6 es {tabla * 6}")
print(f"{tabla} x 7 es {tabla * 7}")
print(f"{tabla} x 8 es {tabla * 8}")
print(f"{tabla} x 9 es {tabla * 9}")
print(f"{tabla} x 10 es {tabla * 10}")
print("----------------------------------")

#Programa 7
num1 =int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 == 0 or num2 == 0:
    print("No ingrese ceros solos")
else:
    print(" ")
    print(f"{num1} + {num2} es {num1 + num2}")
    print(f"{num1} - {num2} es {num1 - num2}")
    print(f"{num1} . {num2} es {num1 * num2}")
    print(f"{num1} : {num2} es {num1 // num2}")
print("----------------------------------")

#Programa 8
altura = float(input("Ingrese su altura (en metros): "))
peso = float(input("Ingrese su peso: "))
imc = float(peso // (altura**2))

print(" ")
print(f"Su Indice de Masa Corporal es {round(imc, 2)}")
print("---------------------------------")

#Programa 9
celsius = float(input("Ingrese los grados Celsius que quiere pasar a Fahrenheit: "))
fahrenheit = float((celsius * 9/5) + 36)
print(" ")
print(f"{celsius} °C son {round(fahrenheit, 2)} °F")
print("---------------------------------")

#Programa 10
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

promedio =float((num1 + num2 + num3) / 3)

print(f"El promedio de los 3 numeros que ingreso es {round(promedio, 2)}")