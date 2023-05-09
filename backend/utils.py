from typing import TYPE_CHECKING

from loguru import logger
from pyrogram import idle, Client
from starlette.requests import Request

if TYPE_CHECKING:
    from context import ContextManager


def make_filter(name: str):
    def filter_(record):
        return record["extra"].get("name") == name

    return filter_


async def run_pyrogram(client: Client):
    """
    运行 pyrogram 的 :class:`Client`
    :param client: :class:`pyrogram.Client`
    :return:
    """
    logger.info(f"Starting {client.name}")
    await idle()
    logger.info(f"{client.name} has been started")
    await exit()


def get_context_manager(request: Request) -> "ContextManager":
    """
    从 request 中获取 :class:`ContextManager`
    :param request: :class:`starlette.requests.Request`
    :return:
    """
    return request.app.state.context_manager
