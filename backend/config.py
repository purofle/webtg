from pydantic import BaseSettings


class Settings(BaseSettings):
    userbot_id: int = 1946684
    userbot_hash: str = "7455cdbbe121e3a9f7d6a4d4399c126b"
    domain: str = "localhost"  # 必须使用 https 或 localhost
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: str = 114514



    class Config:
        env_file = ".env"
