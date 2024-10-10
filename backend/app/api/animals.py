from . import BaseAPI

class AnimalsAPI(BaseAPI):
    def get(self, id):
        return self.url + "/animals?id={0}".format(id)

    def get_all(self, page):
        return self.url + "/animals?page={0}".format(page)

    def create_home(self, payload):
        raise NotImplementedError