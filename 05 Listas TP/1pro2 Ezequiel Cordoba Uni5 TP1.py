#Punto 1
multiplos_de_4 :list = []

for numero in range(1, 101):
    if numero % 4 == 0:
        multiplos_de_4.append(numero)
print(multiplos_de_4)
print("--------------------------")

#Punto 2
lista_favoritos :list = ["Atardecer", "Naturaleza", "Anime", "Aventura", "Videojuegos"]

print(lista_favoritos[-2])
print("--------------------------")

#Punto 3
lista_vacia :list = []

lista_vacia.append("Halo Combat Envolved")
lista_vacia.append("Uncharted")
lista_vacia.append("Call of Duty: War at War")

print(lista_vacia)
print("--------------------------")

#Punto 4
animales :list = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)
print("--------------------------")

#Punto 5
#El codigo en la imagen identifica el numero de mayor valor en la lista con el max() y 
# lo elimina con el .append() para luego imprimir la lista sin el numero eliminado

#Punto 6
lista_numeros :list = list(range(10, 31, 5))

print(lista_numeros[0:2])
print("--------------------------")

#Punto 7
autos :list= ["sedan", "polo", "suran", "gol"]

autos[1] = "Optimus Prime B)"
autos[2] = "Bumblebee B)"
print(autos)
print("--------------------------")

#Punto 8
dobles :list = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)
print("--------------------------")

#Punto 9
compras :list = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)
print("--------------------------")

#Punto 10
lista_anidada :list = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)
