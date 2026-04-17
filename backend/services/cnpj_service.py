from backend.clients.cnpj_api.cnpj_client import CNPJClient
from backend.clients.cnpj_api.cnpj_connection import CNPJConnection

async def buscar_info_cnpj(cnpj: str):
    conn = CNPJConnection()
    client = CNPJClient(conn)

    dados = await client.get_cnpj(cnpj)
    return dados

    