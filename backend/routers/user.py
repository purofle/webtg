from fastapi import APIRouter
from webauthn import generate_registration_options

from backend.config import Settings

router = APIRouter()


@router.get("/generate-registration-options")
async def generate_registration_options_api(
        user_id: int,
        username: str
):
    return (generate_registration_options(
        rp_id=Settings().domain,
        rp_name="WebTelegram",
        user_id=str(user_id),
        user_name=username
    ))
