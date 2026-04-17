import json
from backend.services.ai_service import PROMPT_ANALISE, extrair_json
from backend.clients.gemini_api.ai_connection import AIConnection
from backend.clients.gemini_api.ai_client import AIClient

def classificar_popularidade(qtd):
    if qtd < 3:
        return "baixa"
    elif qtd < 10:
        return "media"
    else:
        return "alta"

async def reanalisar_com_contexto(dados, logs, quantidade):
    nivel_popularidade = classificar_popularidade(quantidade)

    contexto = "\nContexto adicional:\n"
    contexto += f"- Esta empresa foi consultada {quantidade} vezes.\n"
    contexto += f"- Nível de interesse: {nivel_popularidade}.\n"
    contexto += "- Use isso como indicador indireto, não determinante.\n"

    if logs:
        contexto += "\nAnálises anteriores:\n"
        for log in logs:
            contexto += f"- {log.analise}\n"

        contexto += "\nGere uma nova análise diferente das anteriores.\n"

    prompt = PROMPT_ANALISE.replace(
        "{json_empresa}",
        json.dumps(dados, indent=2, ensure_ascii=False)
    ) + contexto

    conn = AIConnection()
    client = AIClient(conn)

    resposta = await client.analisar_empresa(prompt)
    analise = extrair_json(resposta)

    return analise, nivel_popularidade