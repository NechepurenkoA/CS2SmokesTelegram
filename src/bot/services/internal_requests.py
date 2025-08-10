import os
from http import HTTPStatus
from typing import Dict, Optional
from urllib.parse import urljoin

import aiohttp
from aiohttp import ClientResponseError
from dotenv import load_dotenv

load_dotenv()


class APIRequests:

    API_ADDRESS = os.getenv("API_ADDRESS")

    def __init__(self, api_route):
        self.API_ROUTE = api_route

    async def post_data(self, **payload) -> Optional[Dict[str, str]]:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(
                    urljoin(self.API_ADDRESS, self.API_ROUTE), json=payload
                ) as response:
                    response.raise_for_status()
                    return await response.json()
            except ClientResponseError:
                if response.status == HTTPStatus.BAD_REQUEST:
                    return {"message": "Welcome back!"}
                return {
                    "message": f"Something went wrong, try again later. "
                    f"Error code: {response.status}."
                }

    async def get_data(self) -> dict:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    urljoin(self.API_ADDRESS, self.API_ROUTE)
                ) as response:
                    response.raise_for_status()
                    return await response.json()
            except ClientResponseError:
                return {
                    "message": f"Something went wrong, try again later."
                    f"Error code: {response.status}."
                }
