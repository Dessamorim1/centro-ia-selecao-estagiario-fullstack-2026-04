from google import genai
from backend.core.config import settings

class AIConnection:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )