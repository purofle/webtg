from loguru import logger
from pyrogram.types import Message


async def hello(client, message: Message):
    logger.debug(message)
