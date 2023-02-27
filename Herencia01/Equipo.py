from Computadora import Computadora
from Software import Software
from Hardware import Hardware

#Ejercicio de herencia multiple. Caso 01: parametro en el objeto hijo
print("Ejercicio de herencia multiple. Caso 01: parametro en el objeto hijo")

equipo = Computadora("Windows", "16", "Intel i7")
equipo.imprimirHardware()
equipo.imprimirSoftware()
