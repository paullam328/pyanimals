from fastapi import FastAPI
from .routers import root_router, animals

app = FastAPI()
app.include_router(root_router)
app.include_router(animals.animal_router)
