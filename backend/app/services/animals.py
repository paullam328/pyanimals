import math
import time
from . import BaseService
from ..api.animals import AnimalsAPI
from ..utils.exceptions import DataNotExistException

class AnimalService(BaseService):
    animal_api = AnimalsAPI()

    def get(self):
        self.animal_api.get()
    
    def get_all(self, page):
        self.animal_api.get_all(0)
            
    def get_total_pages(self):
        zero_page = self.animal_api.get_all_sync(0) # this returns the zeroth page
        if zero_page and "total_pages" in zero_page:
            return zero_page["total_pages"]
        else:
            raise DataNotExistException("Total pages data does not exist.")

    async def get_all_animal_details(self, pages_to_fetch: int = -1, page_to_fetch_multiplier: int = -1):
        total_pages = self.get_total_pages()
        start = time.time()
        starting_page = page_to_fetch_multiplier * pages_to_fetch - pages_to_fetch + 1
        num_pages = min(total_pages, starting_page + pages_to_fetch) if pages_to_fetch > -1 else total_pages
        all_animals = await self.animal_api.get_all_details_async(num_pages, starting_page, pages_to_fetch)
        print("Total animal details fetching time: " + str(time.time() - start))
        return all_animals

    def create_animal_homes(self):
        pass

    def update(self, title, msg, expiry_date, level):
        raise NotImplementedError

    def remove(self, id):
        raise NotImplementedError