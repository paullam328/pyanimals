from . import BaseService
from ..api.animals import AnimalsAPI
from ..utils.exceptions import DataNotExistException, ExceedBatchLimitException
from ..utils.constants import MAX_BATCH_SIZE, NOT_SUPPLIED

# Service class for Animal to separate business logic, and create a layer of segregation between router layer and API layer
class AnimalService(BaseService):
    animal_api = AnimalsAPI()
            
    # Get the total number of pages, by getting the zeroth page and extracting the parent info
    def get_total_pages(self):
        zero_page = self.animal_api.get_all_sync(0) # this returns the zeroth page, hence the pages here
        if zero_page and "total_pages" in zero_page:
            return zero_page["total_pages"]
        else:
            raise DataNotExistException("Total pages data does not exist.")

    # Get all animal details, by providing an option to get number of pages as desired (please refer to README.md for more details regarding how it works)  To fetch all animal details, you may leave both parameters as -1 (NOT_SUPPLIED)
    async def get_all_animal_details(self, pages_to_fetch: int = NOT_SUPPLIED, pagination: int = NOT_SUPPLIED):
        total_pages = self.get_total_pages()
        starting_page = pagination * pages_to_fetch - pages_to_fetch + 1 # Maths to ensure the starting page will be aligned properly
        num_pages = min(total_pages, starting_page + pages_to_fetch) if pages_to_fetch > NOT_SUPPLIED else total_pages # If pages to fetch is not supplied, then use total pages or else do some calculations as of earlier
        all_animals = await self.animal_api.get_all_details_async(num_pages, starting_page, pages_to_fetch)
        return all_animals

    # Create animal homes and see whether the request exceeded the max batch size
    def create_animal_homes(self, req):
        if len(req) > MAX_BATCH_SIZE:
            raise ExceedBatchLimitException(MAX_BATCH_SIZE)
        res = self.animal_api.create_home(req)
        return res