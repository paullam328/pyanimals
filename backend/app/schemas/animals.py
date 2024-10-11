from pydantic import BaseModel

# For mapping the request object of the post request (for the task - Posting batches of /animals/v1/home)
class PostAnimalRequest(BaseModel):
    id: int
    name: str
    born_at: str
    friends: list[str]