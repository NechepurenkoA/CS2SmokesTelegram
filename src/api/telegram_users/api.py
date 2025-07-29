from typing import List

from ninja import Router
from ninja.pagination import paginate

from api.crud import DatabaseCrud
from telegram_users.models import TelegramUser
from telegram_users.schemas import TelegramUserIn, TelegramUserOut

router = Router(tags=["telegram_users"])
USER_CRUD = DatabaseCrud(TelegramUser)


@router.get("/{user_id}", response=TelegramUserOut)
async def get_object(request, user_id: int):
    instance = await USER_CRUD.get(user_id)
    return instance


@router.get("", response=List[TelegramUserOut])
@paginate
async def get_list(
    request,
):
    queryset = await USER_CRUD.list()
    return list(queryset)


@router.post("", response=TelegramUserOut)
async def post(
    request,
    payload: TelegramUserIn,
):
    instance = await USER_CRUD.create(**payload.dict())
    return instance
