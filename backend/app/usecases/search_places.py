from app.services.maps_service import MapsService

class SearchPlacesUseCase:
    def __init__(self, maps_service: MapsService):
        self.maps_service = maps_service

    def execute(self, query: str, location: str = None):
        if not query or query.strip() == "":
            return []
        return self.maps_service.search(query=query, location=location)
