from Computadora import Computadora
from Software import Software
from Hardware import Hardware

#Ejercicio de herencia multiple. Caso 01: parametro en el objeto hijo
print("Ejercicio de herencia multiple. Caso 03: herencia de metodos")

equipo = Computadora("Windows", "16", "Intel i7")
equipo.imprimirCaracteristicas()
equipo.imprimirSoftware()
equipo.imprimirHardware()
equipo.imprimirSoftware()
