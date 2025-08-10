from http import HTTPStatus
from typing import List

from ninja import Router, Schema
from ninja.errors import HttpError
from ninja.pagination import paginate

from telegram_users.crud import TG_USER_CRUD
from telegram_users.exceptions import UserAlreadyExists
from telegram_users.schemas import TelegramUserIn, TelegramUserOut

router = Router(tags=["telegram_users"])


class Error(Schema):
    error: str


@router.get("/{tg_user_id}", response=TelegramUserOut)
async def get_object(request, tg_user_id: int):
    instance = await TG_USER_CRUD.get(tg_user_id)
    return instance


@router.get("", response=List[TelegramUserOut])
@paginate
async def get_list(
    request,
):
    queryset = await TG_USER_CRUD.list()
    return list(queryset)


@router.post("", response={200: TelegramUserOut})
async def post(
    request,
    payload: TelegramUserIn,
):
    try:
        if await TG_USER_CRUD.check_if_exists(**payload.dict()):
            raise UserAlreadyExists("The telegram_id you passed is already registered.")
        instance = await TG_USER_CRUD.create(**payload.dict())
        return instance
    except UserAlreadyExists as e:
        raise HttpError(HTTPStatus.BAD_REQUEST, str(e))
