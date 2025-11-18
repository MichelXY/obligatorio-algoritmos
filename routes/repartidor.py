from fastapi import APIRouter

router_repartidor = APIRouter()


@router_repartidor.post("/repartidor/agregar")
async def agregar_repartidor(nombre: str, telefono: str):
    print(f"Agregando repartidor: {nombre}, Teléfono: {telefono}")
    repartidor = Repartidor(nombre=nombre, telefono=telefono)
    print(f"Repartidor creado: {repartidor}")
    Gestora().agregar_repartidor(repartidor)
    return {"mensaje": "Repartidor agregado exitosamente"}
