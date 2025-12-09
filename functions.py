import re
from transformers import pipeline
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

