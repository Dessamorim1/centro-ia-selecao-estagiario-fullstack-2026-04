from backend.core.config import settings

class CNPJConnection:
    def __init__(self):
        self.url = settings.CNPJ_URL
        self.headers = {
            "Authorization": settings.CNPJ_API_KEY
        }
