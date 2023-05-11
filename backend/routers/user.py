from fastapi import APIRouter, Depends
from loguru import logger
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.types import User
from webauthn import generate_registration_options
from webauthn.helpers.structs import AuthenticatorSelectionCriteria, ResidentKeyRequirement, UserVerificationRequirement

from backend.config import Settings
from backend.context import ContextManager
from backend.model.Response import SignUp, SignUpResponse
from backend.utils import get_context_manager

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/generate_registration_options")
async def generate_registration_options_api(
        user_id: int,
        username: str
):
    return (generate_registration_options(
        rp_id=Settings().domain,
        rp_name="WebTelegram",
        user_id=str(user_id),
        user_name=username,
        authenticator_selection=AuthenticatorSelectionCriteria(
            resident_key=ResidentKeyRequirement.REQUIRED,
            user_verification=UserVerificationRequirement.PREFERRED
        )
    ))


@router.get("/verify_registration")
async def verify_registration():
    pass


@router.get("/login_code")
async def get_login_code(
        phone: str,
        cm: ContextManager = Depends(get_context_manager)
):
    client = await cm.get_client(phone)

    if client is None:
        logger.info("Client not found, create new one.")
        client = await cm.create_client(phone)

    # noinspection PyBroadException
    try:
        send_phone = await client.send_code(phone_number=phone)
        return send_phone.phone_code_hash
    except Exception as e:
        return str(e)


@router.post("/sign_up")
async def sign_up(
        information: SignUp,
        cm: ContextManager = Depends(get_context_manager)
):
    # 获取 Client
    client = await cm.get_client(information.phone)
    if client is None:
        raise Exception(f"Client not found, phone: {information.phone}, cm: {cm.client}")

    if user := await cm.user_is_logged(client=client):
        return SignUpResponse(
            username=user.username,
            user_id=user.id,
            phone=user.phone_number
        )

    # 登录
    try:
        signed_in = await client.sign_in(
            phone_number=information.phone,
            phone_code_hash=information.phone_hash,
            phone_code=information.code
        )
    except SessionPasswordNeeded as e:
        if information.password == "":
            logger.error(e)
            return str(e)

        signed_in = await client.check_password(information.password)

    if isinstance(signed_in, User):
        return SignUpResponse(
            username=signed_in.username,
            user_id=signed_in.id,
            phone=signed_in.phone_number
        )
