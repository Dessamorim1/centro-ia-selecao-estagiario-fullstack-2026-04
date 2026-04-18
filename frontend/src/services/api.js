const BASE_URL = "http://localhost:8000";

export async function analisarCNPJ(cnpj) {
  const res = await fetch(`${BASE_URL}/api/cnpj/${cnpj}`);

  if (!res.ok) {
    const erro = await res.json();
    throw new Error(erro.detail || "Erro ao consultar CNPJ");
  }

  return res.json();
}

export async function analisarCNPJComIA(cnpj) {
  const res = await fetch(`${BASE_URL}/api/analisar_empresa/${cnpj}`, {
    method: "POST",
  });

  if (!res.ok) {
    const erro = await res.json();
    throw new Error(erro.detail || "Erro na análise com IA");
  }

  return res.json();
}