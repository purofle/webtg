import uvicorn
from fastapi import FastAPI

import utils

app = FastAPI()
logger = utils.init_logging()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.on_event("startup")
async def on_startup():
    await utils.pyrogram_init()
    logger.info("Pyrogram initialized")


if __name__ == "__main__":
    config = uvicorn.Config("main:app", host="localhost", port=8000, reload=True)
    server = uvicorn.Server(config)
    server.run()
