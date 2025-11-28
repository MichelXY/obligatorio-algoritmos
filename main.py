from fastapi import FastAPI, HTTPException, Request
from utils.get_type_message import get_message_type
from models.repartidor import Repartidor
from models.gestora import Gestora
from routes.clientes import router_cliente
from routes.repartidor import router_repartidor
from utils.chat import bot

app = FastAPI()

app.include_router(router_cliente)
app.include_router(router_repartidor)


@app.get("/welcome")
def index():
    return {"mensaje": "welcome developer"}


ACCESS_TOKEN = "EAAMdryqdGbcBQDRL4MVmyZAo1pSgZAiXaymtktqAccoBQIeZAaSNXwgfjZCwfwbEIQ4UOqqqSsFyhm9QsXbNTSEzbQvaUrKzAj3ZAIPO2sGu1qpNfcUh0sqakXZCyi45zOVhx3rbiiUR8rZAZCwgoIJmstAQo94NikIwYaj7tiiHJq53cnKKQ6KFQrhhEZB7l0BIKRJM8t7o2XEKZAZANRZBAkVZBSpAYNd1mrN0WplC5"


@app.get("/whatsapp")
async def verify_token(request: Request):
    try:
        # Obtener los parámetros de la URL (query parameters)
        query_params = request.query_params

        # Extraer el token de verificación y el desafío (challenge)
        verify_token = query_params.get("hub.verify_token")
        challenge = query_params.get("hub.challenge")

        # 1. Comprobar si los parámetros están presentes
        # 2. Comprobar si el token de verificación coincide con el token predefinido
        if (
            verify_token is not None
            and challenge is not None
            and verify_token == ACCESS_TOKEN
        ):
            # Si coincide, se devuelve el desafío (challenge) como un entero
            return int(challenge)
        else:
            # Si no coincide o faltan parámetros, se lanza un error HTTP 400
            raise HTTPException(
                status_code=400,
                detail="Token de verificación inválido o parámetros faltantes",
            )

    except Exception as e:
        # Manejo de errores generales durante el proceso
        raise HTTPException(status_code=400, detail=f"Error en la verificación: {e}")


@app.post("/whatsapp")
async def received_message(request: Request):
    try:
        # Lee el cuerpo de la solicitud POST como JSON
        body = await request.json()

        # Navegación básica en la estructura JSON del webhook de Meta
        # La estructura puede variar, esto es un acceso inicial típico
        entry = body["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]

        # Verifica si hay mensajes reales dentro de la carga útil
        if "messages" in value and len(value["messages"]) > 0:
            # Extrae el primer mensaje de la lista de mensajes
            type_message, content = get_message_type(value["messages"][0])

            message = value["messages"][0]
            # Extrae el número de teléfono del remitente
            number = message["from"]
            bot.user_phone = number
            print(
                f"Mensaje recibido de {number}: Tipo: {type_message}, Contenido: {content}"
            )

            # Aquí podrías agregar lógica adicional para procesar el mensaje recibido
        bot.process_message(content)
        # Es crucial retornar un código HTTP 200 (implícito aquí)
        # o un mensaje de éxito para que Meta no reintente el envío.
        return "EVENT_RECEIVED"

    except Exception:
        # En caso de error, todavía se recomienda devolver una respuesta de éxito (200)
        # para evitar reintentos continuos, aunque se debe registrar el error.
        return "EVENT_RECEIVED"


@app.post("/repartidor")
async def agregar_repartidor(repartidor: Repartidor):
    print(f"Repartidor creado: {repartidor}")
    Gestora().agregar_repartidor(repartidor)
    return {"mensaje": "Repartidor agregado exitosamente"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
