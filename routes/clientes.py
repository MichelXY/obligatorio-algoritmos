from fastapi import APIRouter

router_cliente = APIRouter()


@router_cliente.post("/cliente/agregar")
async def agregar_cliente(nombre: str, telefono: str):
    print(f"Agregando cliente: {nombre}, Teléfono: {telefono}")
    # Lógica para agregar el cliente
    return {"mensaje": "Cliente agregado exitosamente"}
