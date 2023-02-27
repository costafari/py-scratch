from Hardware import Hardware
from Software import Software

class Computadora(Software, Hardware):

    def __init__(self, so, ram, cpu):
        print("Construyendo computadora")
        self.so = so
        self.ram = ram
        self.cpu = cpu

    def imprimirSoftware(self):
        print("El sistema operativo es: " + self.so)

    def imprimirHardware(self):
        print("El harware de la computadora es: " + self.cpu + " y " + self.ram + " de memoria aleatoria.")