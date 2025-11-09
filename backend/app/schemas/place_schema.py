from pydantic import BaseModel
from typing import Optional

class PlaceOut(BaseModel):
    name: str
    address: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    map_url: str
    map_markdown: Optional[str]  
    place_id: Optional[str]
