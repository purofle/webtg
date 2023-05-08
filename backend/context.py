from typing import Dict

from loguru import logger
from pyrogram import Client


class ContextManager:
    def __init__(self):
        self._client: Dict[str, Client] = {}

    @property
    def client_number(self) -> int:
        return len(self._client)

    def get_client(self, phone: str) -> Client | None:
        logger.debug(self._client)
        return self._client.get(phone, None)

    def add_client(self, client: Client, phone: str):
        self._client[phone] = client
        logger.debug(self._client)
