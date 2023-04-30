from contextvars import ContextVar

from pyrogram import Client

pyrogram_context: ContextVar[Client] = ContextVar("pyrogram_client")


def get_pyrogram() -> Client:
    return pyrogram_context.get()


def set_pyrogram(client: Client):
    pyrogram_context.set(client)
