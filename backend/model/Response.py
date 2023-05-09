from pydantic import BaseModel


class SignUp(BaseModel):
    phone: str
    phone_hash: str
    code: str
    password: str = ""


class SignUpResponse(BaseModel):
    username: str
    user_id: int
    phone: str
