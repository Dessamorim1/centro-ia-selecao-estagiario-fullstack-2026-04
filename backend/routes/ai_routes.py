from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from backend.utils.validacao_cnpj import validar_cnpj
from backend.utils.popularidade import classificar_popularidade
from backend.services.reanalisar_service import reanalisar_com_contexto

import json
import logging

from backend.models.database import get_db
from backend.models.models import Empresa, EmpresaLog
from backend.services.ai_service import analisar_empresa
from backend.services.cnpj_service import buscar_info_cnpj
from backend.dependencies.ai import get_ai_client
from backend.clients.gemini_api.ai_client import AIClient

router_ai = APIRouter(
    prefix="/api/analisar_empresa",
    tags=["analise"]
)

logger = logging.getLogger(__name__)

@router_ai.post("/{cnpj}")
async def analisar_empresa_rota(cnpj: str, db: Session = Depends(get_db), ai_client: AIClient = Depends(get_ai_client)):
    try:
        validar_cnpj(cnpj)

        dados = await buscar_info_cnpj(cnpj)
        analise = await analisar_empresa(dados, ai_client)

        analise_json = json.dumps(analise, sort_keys=True)

        empresa = db.query(Empresa).filter(Empresa.cnpj == cnpj).first()

        if empresa:
            empresa.quantidade += 1
            if not empresa.dados_cnpj:
                empresa.dados_cnpj = json.dumps(dados)
        else:
            empresa = Empresa(
                cnpj=cnpj,
                quantidade=1,
                dados_cnpj=json.dumps(dados)
            )
            db.add(empresa)
            db.flush() 

        quantidade = empresa.quantidade
        nivel = classificar_popularidade(quantidade)

        ultimo_log = (
            db.query(EmpresaLog)
            .filter(EmpresaLog.cnpj == cnpj)
            .order_by(EmpresaLog.id.desc())
            .first()
        )

        if ultimo_log and ultimo_log.analise_completa == analise_json:
            db.commit()
            return {
                "cnpj": cnpj,
                "fonte": "cache",
                "analise": analise,
                "meta": {
                    "popularidade": {
                        "consultas": quantidade,
                        "nivel": nivel
                    }
                }
            }

        log = EmpresaLog(
            cnpj=cnpj,
            data_consulta=datetime.now().isoformat(),
            risco=analise.get("risco"),
            analise=analise.get("resumo"),
            pontos_fortes=json.dumps(analise.get("pontos_fortes", [])),
            analise_completa=analise_json
        )

        db.add(log)
        db.commit()

        return {
            "cnpj": cnpj,
            "fonte": "nova",
            "analise": analise,
            "meta": {
                "popularidade": {
                    "consultas": quantidade,
                    "nivel": nivel
                }
            }
        }

    except Exception as e:
        db.rollback()
        logger.error(f"Erro ao analisar CNPJ {cnpj}: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail="Erro ao analisar empresa"
        )


@router_ai.post("/reanalisar/{cnpj}")
async def reanalisar_com_historico(cnpj: str, db: Session = Depends(get_db), ai_client: AIClient = Depends(get_ai_client)):
    try:
        validar_cnpj(cnpj)

        empresa = db.query(Empresa).filter(Empresa.cnpj == cnpj).first()

        if not empresa or not empresa.dados_cnpj:
            raise HTTPException(status_code=404, detail="Dados não encontrados")

        dados = json.loads(empresa.dados_cnpj)

        logs = (
            db.query(EmpresaLog)
            .filter(EmpresaLog.cnpj == cnpj)
            .order_by(EmpresaLog.id.desc())
            .limit(3)
            .all()
        )

        quantidade = empresa.quantidade

        analise, nivel = await reanalisar_com_contexto(
            dados, logs, quantidade, ai_client
        )

        return {
            "cnpj": cnpj,
            "fonte": "reanalisado_com_historico",
            "analise": analise,
            "meta": {
                "popularidade": {
                    "consultas": quantidade,
                    "nivel": nivel
                }
            }
        }

    except Exception as e:
        logger.error(f"Erro ao reanalisar CNPJ {cnpj}: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail="Erro ao reanalisar empresa"
        )