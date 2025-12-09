import re
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from transformers import pipeline
from fastapi import HTTPException
import os
from googletrans import Translator

translator = Translator()


async def converter_texto_en(texto):
    try:
        resultado = await translator.translate(texto, dest='en')
        texto_traduzido = resultado.text

        return texto_traduzido

    except Exception as e:
        return f"❌ Erro na tradução para inglês: {str(e)}"


async def converter_texto_pt(texto):
    try:
        resultado = await translator.translate(texto, dest='pt')
        texto_traduzido = resultado.text

        return texto_traduzido

    except Exception as e:
        return f"❌ Erro na tradução para português: {str(e)}"


def WHITESPACE_HANDLER(k): return re.sub(
    r'\s+', ' ', re.sub(r'\n+', ' ', k.strip()))


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


async def resume_text(texto):
    # 1) Converte o texto original (pt) para inglês
    texto_en = await converter_texto_en(texto)
    texto_en = WHITESPACE_HANDLER(texto_en)

    # 2) Gera a sumarização
    resumo_en = summarizer(
        texto_en,
        max_length=80,       # tamanho máximo do resumo
        min_length=30,       # mínimo razoável
        do_sample=False,
        length_penalty=2.0,
        no_repeat_ngram_size=3,
        early_stopping=True
    )[0]['summary_text']

    # 3) Traduz o resumo para português
    resumo_pt = await converter_texto_pt(resumo_en)

    return resumo_pt


def get_sql(texto_en):
  # Carrega o tokenizer e o modelo
  model_name = "XGenerationLab/XiYanSQL-QwenCoder-3B-2504"
  tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
  model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",       # Usa a GPU se disponível
        trust_remote_code=True,
        torch_dtype="auto"       # Usa float16 se disponível (mais leve)
  )

  # Cria o pipeline de texto
  generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
  
  
  # Prompt de exemplo
  prompt = f"""Convert the following question into a SQL query:
              {texto_en}
              SQL:"""

  try:
    # Geração
    result = generator(
        prompt,
        max_new_tokens=128,
        do_sample=False,
        temperature=0.3,
        pad_token_id=tokenizer.eos_token_id
    )

    resultado_sql = result[0]['generated_text']

    # Remove o prompt da resposta
    if prompt in resultado_sql:
        resultado_sql = resultado_sql.replace(prompt, "").strip()
    else:
        resultado_sql = resultado_sql.strip()

    # Se tiver várias queries, pega a primeira
    if ";" in resultado_sql:
            resultado_sql = resultado_sql.split(";")[0].strip() + ";"


    return resultado_sql

  except Exception as e:
    error_message = "❌ Erro ao gerar query:",e
    
    return error_message
