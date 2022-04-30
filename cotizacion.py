import requests


class Cotizacion:
    def __init__(self,moneda_ref,moneda_cambio,tiempo_ref=60 ):
        self.moneda_ref = moneda_ref
        self.moneda_cambio = moneda_cambio
        self.tiempo_ref = tiempo_ref
        self.base_url = 'https://api.coinbase.com/v2/exchange-rates?currency='
        self.actualizar()

   
    def actualizar(self):
        r = requests.get(self.base_url + self.moneda_cambio)
        self.valor_str = r.json()["data"]["rates"][self.moneda_ref]
        self.valor = "{:.2f}".format(float(self.valor_str))
            # self.valor = solicita_nuevo_precio_de(self.moneda_ref, self.moneda_cambio)
        

    def dame_txt(self):
        self.actualizar()
        return self.moneda_ref + ' - ' + f"{self.valor}" + \
            self.moneda_cambio 
