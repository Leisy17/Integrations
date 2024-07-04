import datetime
import os
from fastapi import FastAPI
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = FastAPI()

@app.post("/load/")
async def load(name: str, content: str):
    filename = f"{datetime.datetime.now()}.html"
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
    container_client = BlobServiceClient.get_container_client(container="pokemoncard")
    with open(file=os.path.join(name, filename), mode="rb") as data:
        container_client.upload_blob(name, data=data, overwrite=True)