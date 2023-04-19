import logging

from fastapi import FastAPI, WebSocket

app = FastAPI()

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info("WebSocket connection started")
    try:
        while True:
            await websocket.receive_bytes()
    finally:
        logger.info("WebSocket connection finished")
