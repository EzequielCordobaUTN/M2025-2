#Punto 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()
print("------------------------")

#Punto 2
def saludar_usuario(nombre: str) -> str:
    return "Hola " + nombre + "!"

nombre_usuario: str = input("Ingrese su nombre: ")
print()
saludo: str = saludar_usuario(nombre_usuario)
print(saludo)
print("------------------------")

#Punto 3
def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str):
    print("Soy " + nombre + " " + apellido + ", tengo " + str(edad) + " años y vivo en " + residencia)

nombre_persona: str = input("Ingrese su nombre: ")
apellido_persona: str = input("Ingrese su apellido: ")
edad_persona: int = int(input("Ingrese su edad: "))
residencia_persona: str = input("Ingrese su residencia: ")
print()
informacion_personal(nombre_persona, apellido_persona, edad_persona, residencia_persona)
print("------------------------")

#Punto 4
def calcular_area_circulo(radio: float) -> float:
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio: float) -> float:
    return 2 * math.pi * radio

radio_circulo: float = float(input("Ingrese el radio del círculo: "))
print()
area: float = calcular_area_circulo(radio_circulo)
perimetro: float = calcular_perimetro_circulo(radio_circulo)
print("Área del círculo: ", area)
print("Perímetro del círculo: ", perimetro)
print("------------------------")

#Punto 5
def segundos_a_horas(segundos: int) -> float:
    return segundos / 3600

segundos_entrada: int = int(input("Ingrese la cantidad de segundos: "))
print()
horas_resultado: float = segundos_a_horas(segundos_entrada)
print(str(segundos_entrada) + " segundos equivalen a " + str(horas_resultado) + " horas.")
print("------------------------")

#Punto 6
def tabla_multiplicar(numero: int):
    print("Tabla de multiplicar del " + str(numero) + ":")
    for i in range(1, 11):
        print(str(numero) + " x " + str(i) + " = " + str(numero * i))

numero_tabla: int = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print()
tabla_multiplicar(numero_tabla)
print("------------------------")

#Punto 7
def operaciones_basicas(a: float, b: float) -> tuple:
    suma: float = a + b
    resta: float = a - b
    multiplicacion: float = a * b
    division: float = a / b
    return (suma, resta, multiplicacion, division)

num_a: float = float(input("Ingrese el primer número: "))
num_b: float = float(input("Ingrese el segundo número: "))
print()

resultado_suma: float
resultado_resta: float
resultado_multiplicacion: float
resultado_division: float
resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division = operaciones_basicas(num_a, num_b)

print("Resultados de las operaciones:")
print("Suma: " + str(resultado_suma))
print("Resta: " + str(resultado_resta))
print("Multiplicación: " + str(resultado_multiplicacion))
print("División: " + str(resultado_division))
print("------------------------")

#Punto 8
def calcular_imc(peso: float, altura: float) -> float:
    return peso / altura ** 2

peso_usuario: float = float(input("Ingrese su peso en kilogramos: "))
altura_usuario: float = float(input("Ingrese su altura en metros: "))
print()
imc: float = calcular_imc(peso_usuario, altura_usuario)
print("Su Índice de Masa Corporal (IMC) es: {:.2f}".format(imc))
print("------------------------")

#Punto 9
def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

temperatura_celsius: float = float(input("Ingrese la temperatura en grados Celsius: "))
print()
temperatura_fahrenheit: float = celsius_a_fahrenheit(temperatura_celsius)
print("La temperatura en Fahrenheit es: " + str(temperatura_fahrenheit))
print("------------------------")

#Punto 10
def calcular_promedio(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3

num1_promedio: float = float(input("Ingrese el primer número: "))
num2_promedio: float = float(input("Ingrese el segundo número: "))
num3_promedio: float = float(input("Ingrese el tercer número: "))
print()
promedio_resultado: float = calcular_promedio(num1_promedio, num2_promedio, num3_promedio)
print("El promedio es: " + str(promedio_resultado))
print("------------------------")