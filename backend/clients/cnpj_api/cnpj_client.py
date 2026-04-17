import httpx

class CNPJClient:
    def __init__(self,conn):
        self.conn = conn
    
    async def get_cnpj(self, cnpj: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    url=f"{self.conn.url}/{cnpj}",
                    headers=self.conn.headers
                )

                response.raise_for_status()
                return response.json()
            
            except httpx.HTTPStatusError as e:
                raise Exception(f"Erro API CNPJ: {e.response.text}")

            except httpx.RequestError:
                raise Exception("Erro de conexão com API de CNPJ")