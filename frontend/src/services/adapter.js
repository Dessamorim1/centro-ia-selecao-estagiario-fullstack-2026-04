export function adaptarEmpresa(response) {
  if (response.dados) {
    const dados = response.dados;

    return {
      tipo: "normal",
      cnpj: response.cnpj,
      nome: dados.company?.name,
      status: dados.status?.text,
      cidade: dados.address?.city,
      estado: dados.address?.state,
      atividade: dados.mainActivity?.text,
      capital: dados.company?.equity,
      analise: null,
      meta: null,
    };
  }

  if (response.analise) {
    return {
      tipo: "ia",
      cnpj: response.cnpj,
      nome: null, 
      status: null,
      cidade: null,
      estado: null,
      atividade: null,
      capital: null,
      analise: response.analise,
      meta: response.meta,
    };
  }

  return null;
}