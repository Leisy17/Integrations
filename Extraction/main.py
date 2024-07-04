import json
import requests
from fastapi import FastAPI
from pydantic import BaseModel


class Extracted(BaseModel):
    name: str
    abilities: list[str]
    picture: str

app = FastAPI()


@app.get("/extraction/")
async def extraction(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_context = response.json()
        abilities_context = pokemon_context["abilities"]
        abilities = []
        for ab in abilities_context:
            abilities.append(ab["ability"]["name"])
        result = Extracted(name=name,
                           picture=pokemon_context["sprites"]["other"]["home"]["front_default"],
                           abilities=abilities)
    else:
        result = f"Error on request: {response.status_code}"
    return result