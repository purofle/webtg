from typing import List, Dict

from pydantic import BaseModel


class SignUpRequest(BaseModel):
    phone: str
    phone_hash: str
    code: str
    password: str = ""


class VerifyRegistrationRequest(BaseModel):
    class RegistrationResponse(BaseModel):
        attestationObject: str
        clientDataJSON: str
        transports: List[str]

    id: str
    rawId: str
    response: RegistrationResponse
    type: str
    clientExtensionResults: Dict[str, str]
    authenticatorAttachment: str
