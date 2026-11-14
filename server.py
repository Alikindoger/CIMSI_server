import asyncio
import websockets
import json

ip = "127.0.0.1"
port = 8081



async def handler(websocket):
    print("¡Cliente conectado!")

    saludo = {"type": "INIT", "mensaje":"Bienvenido al server"}
    await websocket.send(json.dumps(saludo)) # Envia el json al cliente

    try:
        async for msg in websocket:
            pass
    except websockets.ConnectionClosed:
        pass

async def main():
    print("Servidor escuchando")
    async with websockets.serve(handler, ip, port): # Abre la conexión con el cliente
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())