class Gestora:
    def __init__(self, lista_repartidores: list[Repartidor] = []):
        self.lista_repartidores = list[Repartidor]

    def agregar_repartidor(self, repartidor: Repartidor):
        self.lista_repartidores.append(repartidor)
