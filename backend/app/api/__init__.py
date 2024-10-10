from ..config import EXTERNAL_API_SERVER_URL

class BaseAPI(object):

    def __init__(self):
        self.url = EXTERNAL_API_SERVER_URL
    
    def get(self):
        raise NotImplementedError
    
    def get_all(self):
        raise NotImplementedError

    def update(self, title, msg, expiry_date, level):
        raise NotImplementedError

    def remove(self, id):
        raise NotImplementedError