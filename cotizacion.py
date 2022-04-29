class Cotizacion:
    def __init__(self,moneda_ref,moneda_cambio,valor=98893, tiempo_ref=60):
        self.moneda_ref = moneda_ref
        self.moneda_cambio = moneda_cambio
        self.valor = valor
        self.tiempo_ref = tiempo_ref
        self.actualizar()

    def actualizar(self):
        # self.valor = solicita_nuevo_precio_de(self.moneda_ref, self.moneda_cambio)
        self.valor = 34

    def dame_txt(self):
        return self.moneda_ref + '-' + f"{self.valor}"+ self.moneda_cambio