from fastapi import APIRouter
from . import RouterUtils
from ..services.animals import AnimalService

animal_router = APIRouter()
animal_service = AnimalService()

@animal_router.get("/animals/details", tags=["Get Animals"])
async def get_all_animal_details(pages_to_fetch: int = -1, page_to_fetch_multiplier: int = -1):
    try:
        res = await animal_service.get_all_animal_details(pages_to_fetch, page_to_fetch_multiplier)
        return RouterUtils.handle_success_response(res)
    except Exception as e:
        print(e)
        return RouterUtils.handle_failed_response(e)
        
@animal_router.post("/animals/homes", tags=["Receive Animals"])
async def create_animal_homes():
    try:
        res = animal_service.create_animal_homes()
        return RouterUtils.handle_success_response(res)
    except Exception as e:
        return RouterUtils.handle_failed_response(e)


