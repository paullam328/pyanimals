class BaseService(object):
    def get(self):
        raise NotImplementedError
    
    def get_all(self):
        raise NotImplementedError

    def update(self, title, msg, expiry_date, level):
        raise NotImplementedError

    def remove(self, id):
        raise NotImplementedError