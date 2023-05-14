from typing import Any

from fastapi import WebSocket, APIRouter
from loguru import logger

from backend.model.websocket import Payload, OP

router = APIRouter(prefix="/websocket", tags=["websocket"])

_event_handlers = {}


def event(event_name):
    def decorator(func):
        _event_handlers[event_name] = func
        return func

    return decorator


async def dispatch_event(op_code: int, websocket: WebSocket, *args, **kwargs):
    handler_func = _event_handlers.get(op_code)
    if handler_func is None:
        logger.error(f"No handler found for event: {op_code}")
        return
    await handler_func(websocket, *args, **kwargs)


@event(OP.heartbeat)
async def op_ping(websocket: WebSocket, data: Any, seq: int):
    logger.info(str(data), seq)


@event(OP.identify)
async def identify(websocket: WebSocket, data: Any, seq: int):
    pass


@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        # noinspection PyBroadException
        try:
            payload = Payload.parse_raw(data)
        except Exception:
            await websocket.send_text(Payload(
                op_code=OP.invalid_payload
            ).json())
            await websocket.close()
            raise

        await dispatch_event(payload.op_code, payload.data, payload.sequence)
