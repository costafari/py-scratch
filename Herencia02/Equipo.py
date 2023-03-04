from Computadora import Computadora
from Software import Software
from Hardware import Hardware

#Ejercicio de herencia multiple. Caso 02: parametros en los objetos padres
print("Ejercicio de herencia multiple. Caso 02: parametros en los objetos padres")

equipo = Computadora("Linux", "32", "Ryzen 5")
print("La PC posee un sistema operativo: " + equipo.so + " y un procesador " + equipo.cpu + " y cuenta con " + equipo.ram + " de memoria RAM.")
