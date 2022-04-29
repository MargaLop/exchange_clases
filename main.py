import time
from cotizacion import Cotizacion
from pantalla import Pantalla


if __name__ == "__main__":
    cotizacion = Cotizacion('EUR','USD')
    pantalla = Pantalla()

    while True:
        pantalla.buffer = cotizacion.dame_txt()
        pantalla.dibujar()

        time.sleep(1)