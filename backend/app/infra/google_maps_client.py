from typing import List, Dict, Any
import googlemaps
from app.core.config import settings

class GoogleMapsClient:
    def __init__(self, api_key: str = None):
        key = api_key or settings.GOOGLE_MAPS_API_KEY
        if not key:
            raise ValueError("Google Maps API key not configured.")
        self.client = googlemaps.Client(key=key)

    def search_places(self, query: str, location: str = None, radius: int = 10000) -> List[Dict[str, Any]]:
        # Use textsearch for flexible queries
        if location:
            # location may be "lat,lng" or an address
            resp = self.client.places(query=f"{query} in {location}")
        else:
            resp = self.client.places(query=query)
        return resp.get("results", [])

    def get_place_details(self, place_id: str) -> Dict[str, Any]:
        r = self.client.place(place_id=place_id)
        return r.get("result", {})
