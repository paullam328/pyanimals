# Base service class to separate business logic, and create a layer of segregation between router layer and API layer

class BaseService(object):
    def get(self):
        raise NotImplementedError
    
    def get_all(self):
        raise NotImplementedError

    def update(self, title, msg, expiry_date, level):
        raise NotImplementedError

    def remove(self, id):
        raise NotImplementedError