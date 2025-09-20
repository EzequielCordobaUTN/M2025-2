#Punto 1
for i in range(0, 101):
    print(i)
print("------------------------")

#Punto 2
numero = int(input("Ingrese un número entero: "))
contador = 0

if numero == 0:
    contador = 1
else:
    if numero < 0:
        numero = -numero
    while numero > 0:
        numero = numero // 10
        contador = contador + 1
print("Cantidad de dígitos: ", contador)
print("------------------------")

#Punto 3
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
suma = 0

if num1 > num2:
    num1, num2 = num2, num1
n = num1 + 1
while n < num2:
    suma = suma + n
    n = n + 1
print("La suma es: ", suma)
print("------------------------")

#punto 4
num = int(input("Ingrese un número entero (0 para terminar): "))
suma = 0

while num != 0:
    suma = suma + num
    num = int(input("Ingrese un número entero (0 para terminar): "))
print("La suma total es:", suma)
print("------------------------")

#Punto 5
import random
numero = random.randint(0,9)

intentos = 0
bandera = True

while bandera:
    intento = int(input("Adivine el número (0-9): "))
    intentos = intentos + 1
    if intento == numero:
        bandera = False
print("Acertó en", intentos, "intentos")
print("------------------------")

#Punto 6
for i in range(100, -1, -2):
    print(i)
print("------------------------")

#Punto 7
num = int(input("Ingrese un número entero positivo: "))
suma = 0
i = 1

while i < num:
    suma = suma + i
    i = i + 1
print("La suma es:", suma)
print("------------------------")

#Punto 8
pares = 0
impares = 0
positivos = 0
negativos = 0
cantidad = 100
i = 0

while i < cantidad:
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if num > 0:
        positivos = positivos + 1
    elif num < 0:
        negativos = negativos + 1
    i = i + 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)
print("------------------------")

#Punto 9
suma = 0
cantidad = 100
i = 0

while i < cantidad:
    n = int(input("Ingrese un número entero: "))
    suma = suma + n
    i = i + 1
media = suma / cantidad
print("La media es:", media)
print("------------------------")

#Punto 10
num = int(input("Ingrese un número entero: "))
invertido = 0
negativo = False

if num < 0:
    num = -num
    negativo = True
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10
if negativo:
    invertido = -invertido
print("Número invertido:", invertido)
print("------------------------")