
from pydantic import BaseModel

class Item(BaseModel):
    texto: str


class PerguntaRequest(BaseModel):
    pergunta: str