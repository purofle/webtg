import logging
import sys
from pprint import pformat
from typing import TYPE_CHECKING

from loguru import logger
# noinspection PyProtectedMember
from loguru._defaults import LOGURU_FORMAT
from pyrogram import idle, Client
from starlette.requests import Request

if TYPE_CHECKING:
    from context import ContextManager

class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentation.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record: logging.LogRecord):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def format_record(record: dict) -> str:
    """
    Custom format for loguru loggers.
    Uses pformat for log any data like request/response body during debug.
    Works with logging if loguru handler it.
    Example:
    # >>> payload = [{"users":[{"name": "Nick", "age": 87, "is_active": True}, {"name": "Alex", "age": 27, "is_active": True}], "count": 2}]
    # >>> logger.bind(payload=).debug("users payload")
    # >>> [   {   'count': 2,
    # >>>         'users': [   {'age': 87, 'is_active': True, 'name': 'Nick'},
    # >>>                      {'age': 27, 'is_active': True, 'name': 'Alex'}]}]
    """

    format_string = LOGURU_FORMAT
    if record["extra"].get("payload") is not None:
        record["extra"]["payload"] = pformat(
            record["extra"]["payload"], indent=4, compact=True, width=88
        )
        format_string += "\n<level>{extra[payload]}</level>"

    format_string += "{exception}\n"
    return format_string


def make_filter(name: str):
    def filter_(record):
        return record["extra"].get("name") == name

    return filter_


def init_logging():
    """
    初始化 loguru
    :return:
    """
    loggers = (
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if name.startswith("uvicorn.")
    )
    for uvicorn_logger in loggers:
        uvicorn_logger.handlers = []

    # change handler for default uvicorn logger
    intercept_handler = InterceptHandler()
    logging.getLogger("uvicorn").handlers = [intercept_handler]
    # set logs output, level and format
    logger.add(sys.stdout,
               level=logging.DEBUG,
               format=format_record,
               filter=make_filter("stdout")
               )

    # 配置loguru的日志句柄，sink代表输出的目标
    logger.configure(
        handlers=[
            {"sink": sys.stdout, "level": logging.DEBUG, "format": format_record},
        ]
    )
    return logger


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
