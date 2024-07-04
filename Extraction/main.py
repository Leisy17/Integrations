import json
import requests
from fastapi import FastAPI
from pydantic import BaseModel


class Extracted(BaseModel):
    name: str
    hp: int
    speed: int
    attack: int
    defense: int
    picture: str

app = FastAPI()


@app.get("/extraction/")
async def extraction(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_context = response.json()
        stats_context = {stat["stat"]["name"]:stat["base_stat"] for stat in pokemon_context["stats"]}
        
        result = Extracted(name=name,
                           hp=stats_context["hp"],
                           speed=stats_context["speed"],
                           picture=pokemon_context["sprites"]["other"]["home"]["front_default"],
                           attack=stats_context["attack"],
                           defense=stats_context["defense"])
    else:
        result = f"Error on request: {response.status_code}"
    return result