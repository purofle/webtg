from enum import IntEnum
from typing import Any

from pydantic import BaseModel


class OP(IntEnum):
    ping = 0
    pong = 1

    hello = 2
    identify = 3
    verify = 4

    invalid_payload = 1000


class Payload(BaseModel):
    """
    Websocket 的负载。
    """
    op_code: OP = OP.invalid_payload  # 操作代码
    data: Any = {}.copy()  # 数据
    sequence: int = 0  # 唯一 id

    class Config:
        fields = {
            "op_code": "op",
            "data": "d",
            "sequence": "s"
        }
