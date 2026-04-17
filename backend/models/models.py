from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///database/banco.db")

Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresa"

    cnpj = Column(String, primary_key=True)
    quantidade = Column(Integer, default=0)

class EmpresaLog(Base):
    __tablename__ = "empresa_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cnpj = Column(String)
    data_consulta = Column(String)
    potencial = Column(String)
    risco = Column(String)
    analise = Column(String)  

Base.metadata.create_all(engine)