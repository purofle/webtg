from pydantic import BaseSettings


class Settings(BaseSettings):
    userbot_id: int = 1946684
    userbot_hash: str = "7455cdbbe121e3a9f7d6a4d4399c126b"
    domain: str = "localhost"  # 必须使用 https 或 localhost

    class Config:
        env_file = ".env"
