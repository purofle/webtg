import base64
import json
from datetime import timedelta

from fastapi import APIRouter, Depends
from loguru import logger
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.types import User
from redis.asyncio.client import Redis
from webauthn import generate_registration_options, verify_registration_response, options_to_json
from webauthn.helpers.structs import AuthenticatorSelectionCriteria, ResidentKeyRequirement, \
    UserVerificationRequirement, RegistrationCredential

from backend.config import Settings
from backend.context import ContextManager
from backend.database import get_redis
from backend.model.request import VerifyRegistrationRequest, SignUpRequest
from backend.model.response import SignUpResponse
from backend.secure import create_access_token, get_current_user
from backend.utils import get_context_manager

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/generate_registration_options")
async def generate_registration_options_api(
        user_id: int,
        username: str,
        redis: Redis = Depends(get_redis)
):
    publickey_credential_creation_options = generate_registration_options(
        rp_id=Settings().domain,
        rp_name="WebTelegram",
        user_id=str(user_id),
        user_name=username,
        authenticator_selection=AuthenticatorSelectionCriteria(
            resident_key=ResidentKeyRequirement.REQUIRED,
            user_verification=UserVerificationRequirement.PREFERRED
        )
    )

    await redis.set(str(user_id), base64.b64encode(publickey_credential_creation_options.challenge))

    return json.loads(options_to_json(publickey_credential_creation_options))


@router.post("/verify_registration")
async def verify_registration(
        verify: VerifyRegistrationRequest,
        user_id: str = Depends(get_current_user),
        redis: Redis = Depends(get_redis)
):
    challenge = base64.b64decode(await redis.get(user_id))

    logger.debug(f"verify: id: {verify.id}")

    verify_registration_response(
        credential=RegistrationCredential.parse_obj(verify),
        expected_challenge=challenge,
        expected_rp_id=Settings().domain,
        expected_origin="WebTelegram",
    )


@router.get("/login_code")
async def get_login_code(
        phone: str,
        cm: ContextManager = Depends(get_context_manager),
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
        information: SignUpRequest,
        cm: ContextManager = Depends(get_context_manager),
):
    # 获取 Client
    client = await cm.get_client(information.phone, create_new=False)
    if client is not None:
        raise Exception(f"Client has been created, please use sign_in. phone: {information.phone}, cm: {cm.client}")

    client = await cm.create_client(phone=information.phone)
    #
    # client = await cm.get_client(information.phone)
    # if client is None:
    #     raise Exception(f"Client has been created, please use sign_in. phone: {information.phone}, cm: {cm.client}")

    if user := await cm.user_is_logged(client=client):
        signed_in = user
    else:

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
        # Save to cookie

        return SignUpResponse(
            username=signed_in.username,
            user_id=signed_in.id,
            phone=signed_in.phone_number,
            token=create_access_token(
                data={"user_id": signed_in.id},
                expires_delta=timedelta(minutes=float(Settings().ACCESS_TOKEN_EXPIRE_MINUTES)))
        )


@router.post("/sign_in")
async def sign_in():
    pass
