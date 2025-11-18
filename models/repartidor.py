from pydantic import BaseModel, Field


class Repartidor(BaseModel):
    nombre: str = Field(..., description="Nombre del repartidor")
    telefono: str = Field(..., description="Teléfono del repartidor")
