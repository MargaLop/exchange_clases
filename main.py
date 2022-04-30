import time
from cotizacion import Cotizacion
from pantalla import Pantalla
from salida import Salida


if __name__ == "__main__":
    cotizaciones = [
            Cotizacion('EUR', 'USD'),
            Cotizacion('EUR', 'BTC'),
            Cotizacion('EUR', 'RUB'),
        ]
    pantalla = Pantalla()

    salida= Salida()
    salida.exit_on_keypress()
    

    while True:
        pantalla.buffer = []
        for cotizacion in cotizaciones:
            pantalla.buffer.append(cotizacion.dame_txt())
        pantalla.buffer.append(salida.dame_txt())
        pantalla.dibujar()
        time.sleep(30)
