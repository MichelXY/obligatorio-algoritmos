from .repartidor import Repartidor
from typing import List


class Gestora:
    def __init__(self, lista_repartidores: List[Repartidor] = []):
        self.lista_repartidores = lista_repartidores

    def agregar_repartidor(self, repartidor: Repartidor):
        self.lista_repartidores.append(repartidor)
