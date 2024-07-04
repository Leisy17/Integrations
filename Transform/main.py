from jinja2 import Environment, FileSystemLoader
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

@app.post("/transform/")
async def transform(request: Extracted):
    environment = Environment(loader=FileSystemLoader("."))
    template = environment.get_template("templates/template.jinja")
    content = template.render(request)
    return content