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
        zero_page = self.animal_api.get_all(0) # this returns the zeroth page
        print(zero_page)
        if zero_page and "total_pages" in zero_page:
            return zero_page["total_pages"]
        else:
            raise DataNotExistException("Total pages data does not exist.")

    def get_all_animal_details(self):
        total_pages = self.get_total_pages()
        self.animal_api.get_all(0)

    def create_animal_homes(self):
        pass

    def update(self, title, msg, expiry_date, level):
        raise NotImplementedError

    def remove(self, id):
        raise NotImplementedError