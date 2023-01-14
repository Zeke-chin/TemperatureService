import asyncio
import json
import websockets

async def temperature_server(websocket, path):
    while True:
        temperature_json = await websocket.recv()
        temperature = json.loads(temperature_json)
        print(f"Temperature received: {temperature['temperature']}")

start_server = websockets.serve(temperature_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
