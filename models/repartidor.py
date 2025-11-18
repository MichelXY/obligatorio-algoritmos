from pydantic import BaseModel, Field


class Repartidor(BaseModel):
    def __init__(self, nombre, telefono):
        nombre: str = Field(..., description="El nombre del repartidor")
        telefono: str = Field(..., description="El telefono del repartidor")
