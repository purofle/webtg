import logging

import richuru
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend import routers
from backend.context import ContextManager

logging.getLogger("pyrogram").setLevel("INFO")
richuru.install(level="DEBUG")
app = FastAPI()

app.include_router(routers.user_router)
app.include_router(routers.websocket_router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def app_startup():
    app.state.context_manager = ContextManager()


if __name__ == "__main__":
    config = uvicorn.Config("main:app", host="localhost", port=8000, reload=True)
    server = uvicorn.Server(config)
    server.run()
