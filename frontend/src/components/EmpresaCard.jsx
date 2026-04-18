export default function EmpresaCard({ empresa }) {
  return (
    <div className="card p-4">

      <h3>{empresa.nome || "Empresa"}</h3>
      <p><strong>CNPJ:</strong> {empresa.cnpj}</p>

      {empresa.tipo === "normal" && (
        <>
          <hr />
          <p><strong>Status:</strong> {empresa.status}</p>
          <p><strong>Local:</strong> {empresa.cidade}/{empresa.estado}</p>
          <p><strong>Atividade:</strong> {empresa.atividade}</p>
          <p>
            <strong>Capital:</strong> R$ {empresa.capital?.toLocaleString("pt-BR")}
          </p>
        </>
      )}

      {empresa.tipo === "ia" && (
        <>
          <hr />
          <h5>Análise com IA</h5>

          <p><strong>Resumo:</strong> {empresa.analise?.resumo}</p>
          <p><strong>Risco:</strong> {empresa.analise?.risco}</p>

          <h6>Pontos fortes:</h6>
          <ul>
            {empresa.analise?.pontos_fortes?.map((p, i) => (
              <li key={i}>{p}</li>
            ))}
          </ul>

          {empresa.meta && (
            <>
              <hr />
              <p>
                <strong>Consultas:</strong>{" "}
                {empresa.meta.popularidade.consultas}
              </p>
              <p>
                <strong>Nível:</strong>{" "}
                {empresa.meta.popularidade.nivel}
              </p>
            </>
          )}
        </>
      )}

    </div>
  );
}