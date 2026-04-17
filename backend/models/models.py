from sqlalchemy import Column, Integer, String
from backend.models.database import Base

class Empresa(Base):
    __tablename__ = "empresa"

    cnpj = Column(String, primary_key=True)
    quantidade = Column(Integer, default=0)
    dados_cnpj = Column(String) 

class EmpresaLog(Base):
    __tablename__ = "empresa_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cnpj = Column(String)
    data_consulta = Column(String)
    pontos_fortes = Column(String)
    risco = Column(String)
    analise = Column(String)
    analise_completa = Column(String)