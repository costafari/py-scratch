from Hardware import Hardware
from Software import Software

class Computadora(Software, Hardware):

    def __init__(self, so, ram, cpu):
        Software.__init__(self, so)
        Hardware.__init__(self, ram, cpu)

    def imprimirSoftware(self):
        print("El sistema operativo es: " + self.so)

    def imprimirHardware(self):
        print("El harware de la computadora es: " + self.cpu + " de CPU y " + self.ram + " GB de memoria aleatoria.")