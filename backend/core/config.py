import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    CNPJ_API_KEY = os.getenv("API_KEY")
    CNPJ_URL = os.getenv("URL_API")

    GEMINI_API_KEY = os.getenv("API_KEY_AI")

settings = Settings()