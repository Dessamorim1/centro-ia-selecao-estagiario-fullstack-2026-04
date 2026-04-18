from backend.clients.gemini_api.ai_connection import AIConnection
from backend.clients.gemini_api.ai_client import AIClient

def get_ai_client():
    conn = AIConnection()
    return AIClient(conn)