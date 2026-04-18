from backend.clients.gemini_api.ai_connection import AIConnection
from backend.clients.gemini_api.ai_client import AIClient

from pathlib import Path
import json
import re

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROMPT_PATH = BASE_DIR / "backend" / "prompts" / "prompt_analise.txt"

PROMPT_ANALISE = PROMPT_PATH.read_text(encoding="utf-8")

def extrair_json(resposta: str) -> dict:
    resposta = resposta.strip()

    try:
        return json.loads(resposta)
    except:
        match = re.search(r"\{[\s\S]*\}", resposta)
        if match:
            return json.loads(match.group())

    raise Exception("Não foi possível extrair JSON da IA")

async def analisar_empresa(dados_empresa: dict, client):

    json_formatado = json.dumps(dados_empresa, indent=2, ensure_ascii=False)

    prompt = PROMPT_ANALISE.replace("{json_empresa}", json_formatado)

    resposta = await client.analisar_empresa(prompt)

    try:
        if isinstance(resposta, str):
            return extrair_json(resposta)
        return resposta
    except Exception as e:
        raise Exception(f"Erro ao processar resposta da IA: {str(e)}")
