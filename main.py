from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from functions import *

app = FastAPI()



class Item(BaseModel):
    texto: str



@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello World"}


@app.post("/resumir/")
async def resumir_texto(item: Item):
    resultado = await resume_text(item.texto)
    return {"resumo": resultado}
