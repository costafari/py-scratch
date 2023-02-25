from Hardware import Hardware
from Software import Software

class Computadora(Software, Hardware):

    def __init__(self):
        print("Construyendo computadora")

    def imprimirSoftware(self):
        print("El sistema operativo es: " + self.so)

    def imprimirHardware(self):
        print("El harware de la computadora es: " + self.cpu + " y " + self.ram)