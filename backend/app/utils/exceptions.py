from fastapi import status

class DataNotExistException(Exception):
    def __init__(self, message: str = "Fetched data does not exist.", status_code: int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class ExceedBatchLimitException(Exception):
    def __init__(self, max_size, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.message = "You may only operate on a batch of {0} items within a request. Please reduce batch size.".format(max_size)
        self.status_code = status_code
        super().__init__(self.message)