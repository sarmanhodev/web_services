# 🧠 WebService de Sumarização de Textos -- FastAPI + Transformers

Este projeto é um **WebService em FastAPI** responsável por **sumarizar
textos longos** utilizando modelos de Deep Learning da biblioteca
**Hugging Face Transformers**.

A API expõe endpoints que recebem um texto bruto e retornam um **resumo
coerente, curto e informativo**, utilizando o modelo:

    facebook/bart-large-cnn

Esse é um dos modelos **SOTA (state-of-the-art)** mais utilizados no
mundo para tarefas de **text summarization**.

------------------------------------------------------------------------

## 🧩 Como funciona a sumarização?

A aplicação usa o pipeline:

``` python
from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
```

O pipeline realiza automaticamente: - tokenização do texto - segmentação
em partes (se for muito grande) - geração do resumo com técnica
*Sequence-to-Sequence* - pós-processamento do texto

O modelo BART: - é baseado em Transformer Encoder-Decoder - foi treinado
em milhões de artigos e notícias - entende contexto longo - escreve
resumos coerentes em linguagem natural

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

### **Backend**

-   FastAPI (Framework moderno e rápido)
-   Starlette (ASGI core)
-   Pydantic (validação de dados)
-   Transformers (Hugging Face)
-   Tokenizers / Safetensors
-   Python 3.11

### **Infraestrutura**

-   Docker
-   Gunicorn + UvicornWorker
-   Pip / Virtualenv

------------------------------------------------------------------------

## 📁 Exemplo de Estrutura do Projeto

    /
    ├── main.py
    ├── requirements.txt
    ├── Dockerfile
    └── README.md

------------------------------------------------------------------------

## 📌 Exemplo de Endpoint

### POST `/summarize`

**Entrada:**

``` json
{
  "texto": "No Brasil, os impactos são igualmente alarmantes, com a Amazônia enfrentando desmatamento recorde, o que não só libera carbono na atmosfera, mas também ameaça a capacidade vital da floresta de regular o clima regional e global. A questão não é apenas ecológica, mas profundamente social e econômica, afetando a segurança alimentar, o acesso à água potável e a saúde pública."
}
```

**Saída:**

``` json
{
  "resumo": "A Amazônia enfrenta um desmatamento recorde. A questão não é apenas ecológica, mas profundamente social e económica. Afeta a segurança alimentar, o acesso à água potável e a saúde pública."
}
```

------------------------------------------------------------------------

## ▶️ Rodando Localmente

### 1. Criar ambiente virtual

``` bash
python -m venv venv
source venv/bin/activate
```

### 2. Instalar dependências

``` bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Executar a API

``` bash
fastapi dev main.py
```

Acesse:

👉 http://localhost:8000/docs\
👉 http://localhost:8000/redoc

------------------------------------------------------------------------

# 🐳 Usando Docker

### 1. Build da imagem

``` bash
docker build -t fastapi-summarizer .
```

### 2. Rodar o container

``` bash
docker run -p 8000:8000 fastapi-summarizer
```

------------------------------------------------------------------------

# 🏭 Produção com Gunicorn + UvicornWorker

O container sobe com:

``` bash
gunicorn main:app   -k uvicorn.workers.UvicornWorker   -w 2   -b 0.0.0.0:8000
```

Benefícios: - Mais rápido que uvicorn standalone - Gerência múltiplos
workers - Escalável - Altamente estável

------------------------------------------------------------------------

# 🧪 Modelo de Código do Summarizer

``` python
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def gerar_resumo(texto: str) -> str:
    resultado = summarizer(
        texto,
        max_length=200,
        min_length=50,
        do_sample=False
    )
    return resultado[0]["summary_text"]
```

------------------------------------------------------------------------

# 📦 Dependências Principais

-   fastapi
-   transformers
-   tokenizers
-   safetensors
-   uvicorn
-   gunicorn
-   httpx
-   numpy
-   regex
-   lxml
-   pydantic
-   python-multipart

Lista completa → `requirements.txt`

------------------------------------------------------------------------

# 🔒 Variáveis de Ambiente (opcional)

    MODEL_NAME=facebook/bart-large-cnn
    MAX_LENGTH=200
    MIN_LENGTH=50

------------------------------------------------------------------------

# 🤝 Contribuindo

Pull Requests são bem-vindos!\
Sinta-se livre para abrir Issues para bugs e melhorias.

------------------------------------------------------------------------

# 📝 Licença

Este projeto está sob a licença MIT.

------------------------------------------------------------------------

# ⭐ Gostou do projeto?

Deixe uma estrela ⭐ no GitHub!
