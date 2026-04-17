import logging

from fastapi import APIRouter, HTTPException
from backend.services.cnpj_service import buscar_info_cnpj
from backend.utils.validacao_cnpj import validar_cnpj

router_cnpj = APIRouter(prefix="/api/cnpj",tags=["cnpj"])

logger = logging.getLogger(__name__)

@router_cnpj.get("/{cnpj}")
async def analisar(cnpj: str):
    try:
        validar_cnpj(cnpj)
        dados = await buscar_info_cnpj(cnpj)

        return {
        "cnpj": cnpj,
        "dados": dados
        }
    
    except Exception as e:
        logger.error(f"Erro ao analisar CNPJ {cnpj}: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))