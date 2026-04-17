import asyncio

class AIClient:
    def __init__(self, conn):
        self.conn = conn

    async def analisar_empresa(self, prompt: str):
        for tentativa in range(3):  # tenta até 3 vezes
            try:
                response = self.conn.client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=prompt
                )

                return response.text

            except Exception as e:
                if "503" in str(e) and tentativa < 2:
                    await asyncio.sleep(2)  
                else:
                    raise Exception(f"Erro na IA: {str(e)}")