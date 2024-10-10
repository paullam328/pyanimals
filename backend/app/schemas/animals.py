from . import BaseSchema

class Animal(BaseSchema):
    def __init__(self, id: int, name: str, born_at: str, friends: list[str]):
        self.id = id
        self.name = name
        self.born_at = born_at
        self.friends = friends
