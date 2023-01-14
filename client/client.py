import json
import asyncio
import websockets
import random

async def temperature_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            temperature = random.randint(0, 100)
            await websocket.send(json.dumps({"temperature": temperature}))
            await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(temperature_client())
