from loguru import logger


async def hello(client, message):
    logger.debug(message)
