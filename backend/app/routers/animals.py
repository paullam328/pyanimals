from . import RouterUtils
from ..services.animals import AnimalService
from fastapi import APIRouter

animal_router = APIRouter()
animal_service = AnimalService()

@animal_router.get("/animals/details", tags=["Get Animals"])
async def get_all_animal_details():
    try:
        res = animal_service.get_all_animal_details()
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


