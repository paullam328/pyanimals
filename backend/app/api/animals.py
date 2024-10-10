import aiohttp
import asyncio
import requests
from tenacity import retry, stop_after_attempt, wait_random
from ..mappers.animals import AnimalMapper
from ..utils.constants import MAX_WORKERS
from . import BaseAPI

class AnimalsAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.max_workers = MAX_WORKERS

    async def get(self, id: int, session: aiohttp.ClientSession):
        url = self.url + "/animals?id={0}".format(id)
        async with session.get(url) as resp:
            return await resp.json()

    def get_all_tasks(self, total_pages: int, starting_page: int, pages_to_fetch: int, session: aiohttp.ClientSession): # there are 500 pages, so without using async it would be very, very slow
        get_all_tasks = []
        if starting_page > -1 and pages_to_fetch > -1:
            pages_to_fetch_range = range(starting_page, starting_page + pages_to_fetch)
        else:
            pages_to_fetch_range = range(0, total_pages)
        for page in pages_to_fetch_range:
            url = self.url + "/animals?page={0}".format(page)
            get_all_tasks.append(session.get(url, ssl=False))
        return get_all_tasks

    @retry(
        stop=stop_after_attempt(5),
        # wait=wait_random(min=1, max=5),
        # retry=(lambda r: r.status in [500, 502, 503, 504])
    )
    async def get_all_async(self, total_pages: int, starting_page: int, pages_to_fetch: int):
        res = []
        async with aiohttp.ClientSession() as session:
            print(pages_to_fetch)
            tasks = self.get_all_tasks(total_pages, starting_page, pages_to_fetch, session)
            resps = await asyncio.gather(*tasks)
            for resp in resps:
                if resp.status == 200:
                    data = await resp.json()  # Await the response to extract JSON data
                    if "items" in data:
                        res.extend(data["items"])
        return res

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_random(min=1, max=5),
        # retry=(lambda r: r.status in [500, 502, 503, 504])
    )
    def get_all_sync(self, page: int):
        url = self.url + "/animals?page={0}".format(page)
        return requests.get(url).json()
    
    def get_all_details_task(self, animals, session: aiohttp.ClientSession): # there are 500 pages, so without using async it would be very, very slow
        tasks = []
        for animal in animals:
            if animal["id"]:
                url = self.url + "/animals/{0}".format(animal["id"])
                tasks.append(session.get(url, ssl=False))
        return tasks

    async def get_all_details_async(self, pages, starting_page, pages_to_fetch):
        animals = await self.get_all_async(pages, starting_page, pages_to_fetch)
        res = []
        async with aiohttp.ClientSession() as session:
            tasks = self.get_all_details_task(animals, session)
            resps = await asyncio.gather(*tasks)
            for resp in resps:
                if resp.status == 200:
                    data = await resp.json()  # Await the response to extract JSON data
                    res.append(AnimalMapper.map_resp_to_output(data))
        return res

    def create_home(self, payload):
        raise NotImplementedError