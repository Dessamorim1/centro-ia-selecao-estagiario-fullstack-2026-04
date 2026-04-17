from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import json

from backend.models.database import get_db
from backend.models.models import Empresa, EmpresaLog
from backend.services.reanalisar_service import reanalisar_com_contexto

router_reanalisar = APIRouter(
    prefix="/api/analisar_empresa",
    tags=["analise"]
)

@router_reanalisar.post("/reanalisar-com-historico/{cnpj}")
async def reanalisar_com_historico(cnpj: str, db: Session = Depends(get_db)):
    try:
        empresa = db.query(Empresa).filter_by(cnpj=cnpj).first()

        if not empresa or not empresa.dados_cnpj:
            raise HTTPException(status_code=404, detail="Dados não encontrados")

        dados = json.loads(empresa.dados_cnpj)

        logs = (
            db.query(EmpresaLog)
            .filter_by(cnpj=cnpj)
            .order_by(EmpresaLog.id.desc())
            .limit(3)
            .all()
        )

        quantidade = empresa.quantidade

        analise, nivel_popularidade = await reanalisar_com_contexto(
            dados, logs, quantidade
        )

        return {
            "cnpj": cnpj,
            "fonte": "reanalisado_com_historico",
            **analise,
            "popularidade": {
                "consultas": quantidade,
                "nivel": nivel_popularidade
            }
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))