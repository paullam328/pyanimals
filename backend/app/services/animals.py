from . import BaseService

class AnimalService(BaseService):
    def get(self):
        raise NotImplementedError

    def update(self, title, msg, expiry_date, level):
        raise NotImplementedError

    def remove(self, id):
        raise NotImplementedError