from pydantic import BaseModel


class SignIn(BaseModel):
    phone: str
    phone_hash: str
    code: str
    password: str = ""
