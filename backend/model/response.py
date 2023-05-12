from pydantic import BaseModel


class SignUpResponse(BaseModel):
    username: str
    user_id: int
    phone: str
    token: str
