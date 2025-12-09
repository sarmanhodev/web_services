🧠 WebService Inteligente — Sumarização de Texto & Geração de SQL
FastAPI + Hugging Face Router API + Tradução Automática

Este projeto fornece um WebService em FastAPI com duas funcionalidades principais:

🚀 1) Sumarização de textos longos (PT → EN → PT)

A API recebe um texto em português, traduz para inglês, envia ao modelo de sumarização DistilBART (HuggingFace) e traduz de volta para português com alta fidelidade.

Modelo utilizado via Router HF:

sshleifer/distilbart-cnn-12-6


Esse método permite:

resumos menores e mais informativos

coerência maior

melhor adaptação semântica

qualidade profissional mesmo para textos longos

Fluxo completo do serviço
Texto em Português
        ↓ tradução
Texto em Inglês
        ↓ sumarização (DistilBART)
Resumo em Inglês
        ↓ tradução
Resumo Final em Português


A API utiliza o Hugging Face Router API, que substitui o antigo api-inference.

🧮 2) Geração de Query SQL a partir de linguagem natural

Endpoint que recebe uma pergunta do usuário em texto comum (PT), converte para inglês para otimizar a interpretação e em seguida gera uma instrução SQL usando um modelo especializado.

Exemplo:

Entrada:

Quero todos os usuários cadastrados após 2020.


Saída esperada:

SELECT * FROM users WHERE created_at >= '2020-01-01';


O pipeline é:

Texto PT
 ↓ tradução
Texto EN
 ↓ modelo NL2SQL
Query SQL

📌 Endpoints Disponíveis
🔹 POST /resumir/

Resumo de texto longo.

Exemplo de entrada
{
  "texto": "No Brasil, os impactos são igualmente alarmantes, com a Amazônia enfrentando desmatamento recorde..."
}

Exemplo de saída
{
  "resumo": "A Amazônia enfrenta desmatamento recorde, com impactos ecológicos e sociais graves."
}

🔹 POST /gerar_query

Gera uma query SQL com base em linguagem natural.

Exemplo de entrada
{
  "pergunta": "Liste todos os funcionários ativos do setor financeiro."
}

Exemplo de saída
{
  "resposta_sql": "SELECT * FROM employees WHERE status = 'active' AND department = 'finance';"
}

⚙️ Tecnologias Utilizadas
Backend

FastAPI

Python 3.11

Pydantic

Requests

Hugging Face Router API

Google/Libre Translate

Infraestrutura

Docker

Gunicorn + Uvicorn Worker

Render / qualquer servidor compatível

📁 Estrutura (simplificada)
/
├── main.py
├── functions.py
├── models.py
├── requirements.txt
└── README.md

▶️ Executando Localmente
1. Criar ambiente virtual
python -m venv venv
source venv/bin/activate

2. Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

3. Executar
uvicorn main:app --reload


Acesse:

http://localhost:8000/docs

http://localhost:8000/redoc

🐳 Rodando com Docker
Build
docker build -t fastapi-service .

Run
docker run -p 8000:8000 fastapi-service

📦 Variáveis de Ambiente
HF_API_KEY=seu_token
HF_MODEL=sshleifer/distilbart-cnn-12-6

🧪 Funções Principais (simplificadas)
📝 Sumarização
async def resume_text(texto):
    texto_en = await converter_texto_en(texto)
    response = requests.post(HF_URL, headers=HEADERS, json={"inputs": texto_en})
    resumo_en = response.json()[0]["summary_text"]
    return await converter_texto_pt(resumo_en)

📝 NL2SQL
async def gerar_sql(pergunta):
    pergunta_en = await converter_texto_en(pergunta)
    return get_sql(pergunta_en)

🤝 Contribuições

Pull Requests e Issues são bem-vindos.

📝 Licença

MIT License.

⭐ Gostou do projeto?

Deixe uma estrela ⭐ no GitHub!
