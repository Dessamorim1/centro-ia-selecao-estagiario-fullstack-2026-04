from backend.clients.gemini_api.ai_connection import AIConnection
from backend.clients.gemini_api.ai_client import AIClient

from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROMPT_PATH = BASE_DIR / "backend" / "prompts" / "prompt_analise.txt"

PROMPT_ANALISE = PROMPT_PATH.read_text(encoding="utf-8")

async def analisar_empresa(dados_empresa: dict):
    conn = AIConnection()
    client = AIClient(conn)

    json_formatado = json.dumps(dados_empresa, indent=2, ensure_ascii=False)

    prompt = PROMPT_ANALISE.replace("{json_empresa}", json_formatado)

    resposta = await client.analisar_empresa(prompt)

    return {
        "analise": resposta
    }