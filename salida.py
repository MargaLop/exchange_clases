import os
from pynput import keyboard

class Salida:
    def __init__(self):
        pass

    def on_release(self,key):
        os._exit(0)
    
    def exit_on_keypress(self):
        listener = keyboard.Listener(on_release=self.on_release)
        listener.start()

    def  dame_txt(self):
        return "\n  Presione cualquier tecla para salir:"



    




