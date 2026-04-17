from fastapi import APIRouter, HTTPException
from backend.services.ai_service import analisar_empresa
from backend.services.cnpj_service import buscar_info_cnpj

router_ai = APIRouter(
    prefix="/api/analisar_empresa",
    tags=["analise"]
)

@router_ai.get("/{cnpj}")
async def analisar_empresa_rota(cnpj: str):
    try:
        dados = await buscar_info_cnpj(cnpj)
        analise = await analisar_empresa(dados)

        return {
            "cnpj": cnpj,
            **analise
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))