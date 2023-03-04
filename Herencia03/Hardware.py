class Hardware(object):
    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu
        
    def imprimirCaracteristicas(self):
        print("Se posee " + self.ram + " GB de memoria interna junto a un procesador " + self.cpu)
