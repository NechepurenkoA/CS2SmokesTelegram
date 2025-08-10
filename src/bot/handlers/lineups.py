from aiogram import Router

from services import APIRequests

# from aiogram.filters.command import Command
# from aiogram.types import Message
# from aiohttp import ClientConnectorError


lineups_router = Router()

LineupsAPI = APIRequests(api_route="lineups/")


# @lineups_router.message(Command("lineups"))
# async def handle_lineups(message: Message) -> None:
#     """/lineups command handler."""
#     try:
#         response: dict = await LineupsAPI.get_data()
#     except ClientConnectorError:
#         await message.answer("The service currently unavailable.")
