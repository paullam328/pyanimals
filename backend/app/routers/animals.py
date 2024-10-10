from fastapi import APIRouter
from . import RouterUtils
from ..services.animals import AnimalService
from ..schemas.animals import PostAnimalRequest

animal_router = APIRouter()
animal_service = AnimalService()

@animal_router.get("/animals/details", tags=["Fetch all Animal details, transform a few fields in the Animal details"])
async def get_all_animal_details(pages_of_ten_animals_to_fetch: int = -1, pagination: int = -1):
    try:
        res = await animal_service.get_all_animal_details(pages_of_ten_animals_to_fetch, pagination)
        return RouterUtils.handle_success_response(res)
    except Exception as e:
        return RouterUtils.handle_failed_response(e)
        
@animal_router.post("/animals/homes", tags=["POST batches of Animals /animals/v1/home, up to 100 at a time"])
async def create_animal_homes(req: list[PostAnimalRequest]):
    try:
        res = animal_service.create_animal_homes(req)
        return RouterUtils.handle_success_response(res)
    except Exception as e:
        return RouterUtils.handle_failed_response(e)


