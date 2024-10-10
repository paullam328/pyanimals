from . import BaseRouter
from ..services.animals import AnimalService

class AnimalsRouter(BaseRouter):
    animal_service = AnimalService

    @BaseRouter.router.get("/animals/", tags=["Get Animals"])
    async def get_animals(self):
        try:
            res = self.animal_service.get()
            return self.handle_success_response(res)
        except Exception as e:
            return self.handle_failed_response(e)

    @BaseRouter.router.get("/animals/{id}", tags=["Get Animal"])
    async def get_animal(self, id: int):
        try:
            res = self.animal_service.get()
            return self.handle_success_response(res)
        except Exception as e:
            return self.handle_failed_response(e)
        
    @BaseRouter.router.post("/animals/home", tags=["Receive Animals"])
    async def create_animals(self):
        try:
            res = self.animal_service.get()
            return self.handle_success_response(res)
        except Exception as e:
            return self.handle_failed_response(e)


