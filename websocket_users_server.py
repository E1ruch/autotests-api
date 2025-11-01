import asyncio
import websockets
from websockets.server import ServerConnection
num = 0

async def echo(websocket: ServerConnection):
    global num
    async for message in websocket:
        num += 1
        print(f"{num}. Получено сообщение от пользователя: {message}")
        response = "Сервер получил: {message}"

        for _ in range(5):
            await websocket.send(response)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("websocket server started")
    await server.wait_closed()

asyncio.run(main())