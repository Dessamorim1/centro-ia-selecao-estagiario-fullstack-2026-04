from fastapi import APIRouter, HTTPException
from backend.services.cnpj_service import buscar_info_cnpj

router_cnpj = APIRouter(prefix="/api/cnpj",tags=["cnpj"])

@router_cnpj.get("/{cnpj}")
async def analisar(cnpj: str):
    try:
        dados = await buscar_info_cnpj(cnpj)

        return {
            "empresa": dados
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))