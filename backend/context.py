from contextvars import ContextVar
from typing import List

from pyrogram import Client


class ContextManager:
    def __init__(self):
        self._client: List[Client] = []

    @property
    def client_number(self) -> int:
        return len(self._client)

    def add_client(self, client: Client):
        self._client.append(client)
