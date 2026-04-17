from validate_docbr import CNPJ
from fastapi import HTTPException

def validar_cnpj(cnpj: str):
    cnpj_validator = CNPJ()

    if not cnpj_validator.validate(cnpj):
        raise HTTPException(
            status_code=400,
            detail="CNPJ inválido"
        )