from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="TransitTracker API", version="0.1.0")

# Configuración CORS: permitir frontend en localhost:3000
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Modelos Pydantic
class Route(BaseModel):
    id: int
    name: str
    active: Optional[bool] = True

# Datos "fake" para pruebas
routes_db = [
    {"id": 1, "name": "Ruta A"},
    {"id": 2, "name": "Ruta B"},
]

@app.get("/", tags=["root"])
async def read_root():
    return {"message": "TransitTracker API funcionando"}

@app.get("/routes", response_model=List[Route], tags=["routes"])
async def get_routes():
    return routes_db

@app.post("/routes", response_model=Route, tags=["routes"])
async def create_route(route: Route):
    routes_db.append(route.dict())
    return route
