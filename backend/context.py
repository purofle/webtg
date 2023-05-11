import asyncio
from typing import Dict

from loguru import logger
from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import User

from backend.handlers import hello
from backend.utils import run_pyrogram


class ContextManager:
    def __init__(self):
        self._client: Dict[str, Client] = {}

    @property
    def client_number(self) -> int:
        return len(self._client)

    async def get_client(
            self, phone: str,
            create_new: bool = True
    ) -> Client | None:
        """
        从手机号获取 Client.
        :param create_new: 是否创建新的 Client
        :param phone: 手机号码, 要求包含加号.
        :return: :class:`pyrogram.Client`
        """
        logger.debug(f"get: {self._client}")

        # 判断 session 是否存在
        if (cached_client := self._client.get(phone[1:], None)) is not None:
            logger.debug(f"return a cached client for {phone}")
            return cached_client

        if create_new:
            new_client = Client(f"webtg_{phone[1:]}")
            await new_client.connect()

            if await self.user_is_logged(client=new_client):
                self.add_client(client=new_client, phone=phone)
                return new_client

            raise Exception(f"user {phone} is not logged_in")

    def add_client(self, client: Client, phone: str):
        """
        添加一个新的 Client.
        :param client: :class:`pyrogram.Client`
        :param phone: 手机号码, 要求包含加号.
        :return:
        """

        logger.debug(f"add: {phone}")
        self._client[phone[1:]] = client
        logger.debug(self._client)

    async def user_is_logged(self,
                             phone: str | None = None,
                             client: Client | None = None
                             ) -> User | bool:
        """
        判断用户是否登录, client 跟 phone 参数二选一.
        :param client: :class:`pyrogram.Client`
        :param phone: 手机号
        :return: 是否登录, 已登录为 True, 未登录为 False.
        """
        if client is None:
            client = await self.get_client(phone)
        try:
            return await client.get_me()
        except KeyError:
            return False

    async def create_client(self, phone: str) -> Client:
        """
        创建一个新的 Client, 并且建立连接
        :param phone: 手机号
        :return: :class:`pyrogram.Client`
        """
        from config import Settings

        userbot_id = Settings().userbot_id
        userbot_hash = Settings().userbot_hash

        client = Client(name=f"webtg_{phone[1:]}", api_id=userbot_id, api_hash=userbot_hash)
        self.add_client(client, phone)
        logger.info(f"Client {client.name} created")

        client.add_handler(MessageHandler(hello))
        asyncio.create_task(run_pyrogram(client))

        await client.connect()

        return client

    @property
    def client(self):
        return self._client
