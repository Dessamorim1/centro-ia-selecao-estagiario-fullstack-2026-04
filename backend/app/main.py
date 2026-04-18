import logging

from fastapi import FastAPI
from backend.routes.cnpja_routes import router_cnpj
from backend.routes.ai_routes import router_ai

from backend.models.database import engine
from backend.models.models import Base

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"), 
        logging.StreamHandler() 
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_cnpj)
app.include_router(router_ai)

@app.get("/")
def home():
    return {"status": "API funcionando"}
