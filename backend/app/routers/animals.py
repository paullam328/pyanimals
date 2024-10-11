from fastapi import APIRouter
from . import RouterUtils
from ..services.animals import AnimalService
from ..schemas.animals import PostAnimalRequest
from ..utils.constants import NOT_SUPPLIED

animal_router = APIRouter()
animal_service = AnimalService()

# Router serving the purpose to fetch all Animal details, transform a few fields in the Animal details
# Optional pagination with params pages_of_ten_animals_to_fetch and pagination; Please refer to README.md for more details regarding how it works
@animal_router.get("/animals/details", tags=["Fetch all Animal details, transform a few fields in the Animal details"])
async def get_all_animal_details(pages_of_ten_animals_to_fetch: int = NOT_SUPPLIED, pagination: int = NOT_SUPPLIED):
    try:
        res = await animal_service.get_all_animal_details(pages_of_ten_animals_to_fetch, pagination)
        return RouterUtils.handle_success_response(res)
    except Exception as e:
        return RouterUtils.handle_failed_response(e)

# Router serving the purpose to POST batches of Animals /animals/v1/home, up to 100 at a time
@animal_router.post("/animals/homes", tags=["POST batches of Animals /animals/v1/home, up to 100 at a time"])
async def create_animal_homes(req: list[PostAnimalRequest]):
    try:
        res = animal_service.create_animal_homes(req)
        return RouterUtils.handle_success_response(res)
    except Exception as e:
        return RouterUtils.handle_failed_response(e)


