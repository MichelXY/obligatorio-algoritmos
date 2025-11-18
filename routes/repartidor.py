from fastapi import APIRouter

router_repartidor = APIRouter()


@router_repartidor.post("/repartidor/agregar")
async def agregar_repartidor():
    pass
