from fastapi import status

class DataNotExistException(Exception):
    def __init__(self, message: str = "Fetched data does not exist.", status_code: int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)