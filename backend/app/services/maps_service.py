from typing import List, Dict
from app.infra.google_maps_client import GoogleMapsClient
from app.core.config import settings
import urllib.parse

class MapsService:
    def __init__(self, client: GoogleMapsClient):
        self.client = client

    def search(self, query: str, location: str = None) -> List[Dict]:
        if settings.USE_SAMPLE:
            # sample mode - return example data (no API key needed)
            return [
                {
                    "name": "Sample Coffee",
                    "address": "Jl. Contoh No.1",
                    "lat": -6.200000,
                    "lng": 106.816666,
                    "map_url": "https://www.google.com/maps?q=Sample+Coffee",
                    "map_markdown": "[Open in Google Maps](https://www.google.com/maps?q=Sample+Coffee)",
                    "place_id": "sample1"
                }
            ]

        results = self.client.search_places(query=query, location=location)
        mapped = []

        for p in results:
            name = p.get("name")
            loc = p.get("geometry", {}).get("location", {})
            address = p.get("formatted_address") or p.get("vicinity")

            # safe encoded map URL
            q = urllib.parse.quote_plus(f"{name} {address or ''}")
            map_url = f"https://www.google.com/maps/search/?api=1&query={q}"
            map_markdown = f"[Open in Google Maps]({map_url})"

            mapped.append({
                "name": name,
                "address": address,
                "lat": loc.get("lat"),
                "lng": loc.get("lng"),
                "map_url": map_url,
                "map_markdown": map_markdown,
                "place_id": p.get("place_id")
            })

        return mapped
