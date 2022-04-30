import py_compile
from datetime import datetime


class Pantalla:
    def __init__(self,buffer="",tiempo_ref=1):
        self.buffer = buffer
        self.tiempo_ref = tiempo_ref

    def dibujar (self):
        for linea in self.buffer:
            print(linea)

    def actualizar(self):
        # cada self.tiempo_ref:
        self.dibujar()

    def fecha(self):
        self.now = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        return 'Cotizacion de las:' + self.now