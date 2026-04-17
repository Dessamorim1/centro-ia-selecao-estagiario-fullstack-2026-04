from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import json

from backend.models.database import get_db
from backend.models.models import Empresa, EmpresaLog
from backend.services.ai_service import analisar_empresa
from backend.services.cnpj_service import buscar_info_cnpj

router_ai = APIRouter(
    prefix="/api/analisar_empresa",
    tags=["analise"]
)

def classificar_popularidade(qtd: int):
    if qtd < 3:
        return "baixa"
    elif qtd < 10:
        return "media"
    else:
        return "alta"

@router_ai.post("/{cnpj}")
async def analisar_empresa_rota(cnpj: str, db: Session = Depends(get_db)):
    try:
        dados = await buscar_info_cnpj(cnpj)

        analise = await analisar_empresa(dados)

        analise_json = json.dumps(analise, sort_keys=True)

        empresa = db.query(Empresa).filter_by(cnpj=cnpj).first()

        if empresa:
            empresa.quantidade += 1
            empresa.dados_cnpj = json.dumps(dados)
        else:
            empresa = Empresa(
                cnpj=cnpj,
                quantidade=1,
                dados_cnpj=json.dumps(dados)
            )
            db.add(empresa)

        quantidade = empresa.quantidade
        nivel_popularidade = classificar_popularidade(quantidade)

        ultimo_log = (
            db.query(EmpresaLog)
            .filter_by(cnpj=cnpj)
            .order_by(EmpresaLog.id.desc())
            .first()
        )

        if ultimo_log and ultimo_log.analise_completa == analise_json:
            return {
                "cnpj": cnpj,
                **analise,
                "popularidade": {
                    "consultas": quantidade,
                    "nivel": nivel_popularidade
                }
            }
        
        log = EmpresaLog(
            cnpj=cnpj,
            data_consulta=datetime.now().isoformat(),
            risco=analise.get("risco"),
            analise=analise.get("resumo"),
            potencial=json.dumps(analise.get("pontos_fortes", [])),
            analise_completa=analise_json
        )

        db.add(log)
        db.commit()

        return {
            "cnpj": cnpj,
            **analise,
            "popularidade": {
                "consultas": quantidade,
                "nivel": nivel_popularidade
            }
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))