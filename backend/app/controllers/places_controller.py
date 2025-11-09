from fastapi import APIRouter, Query, HTTPException
from typing import List
from app.schemas.place_schema import PlaceOut
from app.infra.google_maps_client import GoogleMapsClient
from app.services.maps_service import MapsService
from app.usecases.search_places import SearchPlacesUseCase

router = APIRouter(prefix="/api")

def get_search_usecase():
    client = GoogleMapsClient()
    service = MapsService(client)
    usecase = SearchPlacesUseCase(service)
    return usecase

@router.get("/places", response_model=List[PlaceOut])
def search_places(q: str = Query(..., description="Search query"), location: str = None):
    usecase = get_search_usecase()
    try:
        results = usecase.execute(query=q, location=location)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
