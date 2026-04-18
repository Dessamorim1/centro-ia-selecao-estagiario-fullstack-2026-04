export function adaptarEmpresa(response) {
  const dados = response.dados || {};

  return {
    tipo: response.analise ? "ia" : "normal",
    cnpj: response.cnpj,

    nome: dados.company?.name,
    status: dados.status?.text,
    cidade: dados.address?.city,
    estado: dados.address?.state,
    atividade: dados.mainActivity?.text,
    capital: dados.company?.equity,

    analise: response.analise || null,
    meta: response.meta || null,
  };
}