from fastapi import FastAPI
from app.controllers.places_controller import router as places_router

def register_routes(app: FastAPI):
    app.include_router(places_router)
