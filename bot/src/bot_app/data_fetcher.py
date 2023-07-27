import aiohttp
from .local_setings import EVENTS_API_URL_ALL

async def get_all():
    async with aiohttp.Clientsession() as session:
        async with session.get(EVENTS_API_URL_ALL) as response:
            return await response.json()