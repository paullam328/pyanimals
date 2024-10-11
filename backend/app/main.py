from fastapi import FastAPI
from .routers import root_router, animals

app = FastAPI() #initalize the app
app.include_router(root_router) # map the router into the FastAPI app
app.include_router(animals.animal_router)
