# 🧠 WebService de Sumarização de Textos -- FastAPI + Transformers

Este projeto é um **WebService em FastAPI** responsável por **sumarizar
textos longos** utilizando modelos de Deep Learning da biblioteca
**Hugging Face Transformers**, além de um pipeline inteligente de
pré‑processamento que envolve **tradução automática** para otimizar a
qualidade dos resumos.

A API expõe endpoints que recebem um texto bruto e retornam um **resumo
coerente, curto e informativo**, utilizando o modelo:

    facebook/bart-large-cnn

Esse é um dos modelos **SOTA (state-of-the-art)** mais utilizados no
mundo para tarefas de **text summarization**.

------------------------------------------------------------------------

# 🌍 Por que traduzimos o texto antes de resumir?

O modelo **facebook/bart-large-cnn** é extremamente poderoso, porém ele
possui uma característica crucial:

👉 **Foi treinado exclusivamente em textos em inglês.**

Para obter resumos de alta qualidade, o serviço segue um fluxo
inteligente:

1.  **Recebe o texto em português (ou outro idioma);**\
2.  **Converte para inglês**, usando Google Translate ou
    LibreTranslate;\
3.  **Aplica o modelo de sumarização** (que funciona melhor em inglês);\
4.  **Tradução reversa** → converte o resumo de volta para
    **português**.

### ✔️ Benefícios desse processo:

-   Resumos muito mais coerentes\
-   Melhor qualidade semântica\
-   Maior precisão contextual\
-   Frases mais curtas e naturais\
-   Resultados mais próximos do esperado em aplicações reais

### 🧠 Representação visual do fluxo:

    Texto em Português
            ↓ (tradução)
         Texto em Inglês
            ↓ (modelo BART)
         Resumo em Inglês
            ↓ (tradução)
    Resumo Final em Português

Esse método aumenta significativamente a precisão porque o modelo
entende perfeitamente o inglês e gera resumos otimizados quando recebe
entradas no idioma de treinamento.

------------------------------------------------------------------------

## 🧩 Como funciona a sumarização internamente?

A aplicação utiliza:

``` python
from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
```

O pipeline realiza automaticamente: - tokenização do texto\
- segmentação inteligente (caso o texto seja grande)\
- geração do resumo com técnica *Sequence-to-Sequence*\
- pós-processamento da saída

O modelo BART: - utiliza arquitetura Transformer Encoder--Decoder\
- foi treinado em milhões de artigos, notícias e documentos\
- possui entendimento profundo de contexto\
- gera resumos extremamente naturais

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

### **Backend**

-   FastAPI
-   Starlette
-   Pydantic
-   Transformers (Hugging Face)
-   Tokenizers / Safetensors
-   Python 3.11

### **Infraestrutura**

-   Docker
-   Gunicorn + UvicornWorker

### **Tradução**

-   googletrans
-   libretranslatepy
-   requests (fallback)

------------------------------------------------------------------------

## 📁 Estrutura do Projeto (exemplo)

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
uvicorn main:app --reload
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

O container inicia com:

``` bash
gunicorn main:app   -k uvicorn.workers.UvicornWorker   -w 2   -b 0.0.0.0:8000
```

Bom para: - alta performance\
- estabilidade\
- produção real\
- múltiplos workers

------------------------------------------------------------------------

# 🧪 Função de Sumarização (exemplo)

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

-   fastapi\
-   transformers\
-   tokenizers\
-   safetensors\
-   uvicorn\
-   gunicorn\
-   httpx\
-   numpy\
-   regex\
-   lxml\
-   pydantic\
-   python-multipart\
-   googletrans\
-   libretranslatepy

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
