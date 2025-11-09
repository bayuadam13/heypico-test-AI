from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.core.config import settings
from app.routes import register_routes
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(
    title="Local LLM Google Maps API",
    description="API for search places and get link of Google Maps.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # atau lebih aman: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],
)

register_routes(app)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

