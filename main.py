from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from functions import *
from models import *

app = FastAPI()

# 🔹 Configurar CORS para permitir requisições de domínios externos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello World"}


@app.post("/resumir/")
async def resumir_texto(item: Item):
    try:
        resultado = await resume_text(item.texto)
        return {"resumo": resultado}

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"erro": str(e)}
        )


@app.post("/gerar_query")
async def gerar_query_sql(dados: PerguntaRequest):
    pergunta_usuario = dados.pergunta

    try:
        resposta_en = await converter_texto_en(pergunta_usuario)

        resposta_query = get_sql(resposta_en)

        return {"resposta_sql": resposta_query}

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})
