from fastapi import APIRouter
from webauthn import generate_registration_options

from backend.config import Settings
from backend.utils import create_client

router = APIRouter(prefix="/user", tags=["user"])


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


@router.get("/login_code")
async def get_login_code(
        phone: str
):
    client = await create_client()
    # noinspection PyBroadException
    try:
        await client.send_code(phone_number=phone)
        return True
    except Exception as e:
        return False
