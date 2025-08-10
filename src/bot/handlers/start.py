from typing import Optional

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiohttp import ClientConnectorError

from services import APIRequests

start_router = Router()

TelegramUserAPI = APIRequests(api_route="users/")


@start_router.message(CommandStart())
async def handle_start(message: Message) -> None:
    """/start command handler."""
    payload = {"telegram_id": message.from_user.id}
    try:
        response: Optional[dict] = await TelegramUserAPI.post_data(**payload)
        if response:
            await message.answer(f"{response["message"]}")
    except ClientConnectorError:
        await message.answer("The service currently unavailable.")
