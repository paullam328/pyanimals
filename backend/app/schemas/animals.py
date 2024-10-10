from pydantic import BaseModel

class PostAnimalRequest(BaseModel):
    id: int
    name: str
    born_at: str
    friends: list[str]