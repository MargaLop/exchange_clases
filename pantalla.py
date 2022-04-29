import py_compile


class Pantalla:
    def __init__(self,buffer="",tiempo_ref=1):
        self.buffer = buffer
        self.tiempo_ref = tiempo_ref

    def dibujar (self):
        print(self.buffer)

    def actualizar(self):
        # cada self.tiempo_ref:
        self.dibujar()
