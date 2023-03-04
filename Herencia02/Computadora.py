from Hardware import Hardware
from Software import Software

class Computadora(Software, Hardware):
    def __init__(self, so, ram, cpu):
        Software.__init__(self, so)
        Hardware.__init__(self, ram, cpu)
