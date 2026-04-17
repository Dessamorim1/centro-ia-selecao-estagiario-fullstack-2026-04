import json
from backend.services.ai_service import PROMPT_ANALISE, extrair_json
from backend.clients.gemini_api.ai_connection import AIConnection
from backend.clients.gemini_api.ai_client import AIClient
from backend.utils.popularidade import classificar_popularidade

async def reanalisar_com_contexto(dados, logs, quantidade):
    nivel_popularidade = classificar_popularidade(quantidade)

    contexto_partes = [
    f"Esta empresa foi consultada {quantidade} vezes.",
    f"Nível de interesse: {nivel_popularidade}.",
    "Use como indicador indireto, não determinante."
    ]

    if logs:
        contexto_partes.append("Análises anteriores:")
        contexto_partes.extend([log.analise for log in logs])
        contexto_partes.append("Gere uma nova análise diferente das anteriores.")

    contexto = "\n".join(contexto_partes)

    prompt = PROMPT_ANALISE.replace(
        "{json_empresa}",
        json.dumps(dados, indent=2, ensure_ascii=False)
    ) + contexto

    conn = AIConnection()
    client = AIClient(conn)

    resposta = await client.analisar_empresa(prompt)
    analise = extrair_json(resposta)

    return analise, nivel_popularidade