export default function EmpresaCard({ empresa }) {
  return (
    <div className="card p-4 mb-4 shadow-sm">

      <div className="d-flex justify-content-between align-items-center mb-3">
        <h3 className="mb-0">
          {empresa.nome || "Empresa não identificada"}
        </h3>

        {empresa.status && (
          <span className="badge bg-success px-3 py-2">
            {empresa.status}
          </span>
        )}
      </div>

      <p className="text-muted mb-3">
        <strong>CNPJ:</strong> {empresa.cnpj}
      </p>

      <hr style={{ opacity: 0.1 }} />

      <div className="row mt-3">

        <div className="col-md-6 mb-3">
          <div className="info-box">
            <small>Localização</small>
            <p>
              {empresa.cidade && empresa.estado
                ? `${empresa.cidade}/${empresa.estado}`
                : "Não informado"}
            </p>
          </div>
        </div>

        <div className="col-md-6 mb-3">
          <div className="info-box">
            <small>Atividade</small>
            <p>{empresa.atividade || "Não informado"}</p>
          </div>
        </div>

        <div className="col-md-6 mb-3">
          <div className="info-box">
            <small>Capital</small>
            <p>
              R${" "}
              {empresa.capital
                ? empresa.capital.toLocaleString("pt-BR")
                : "Não informado"}
            </p>
          </div>
        </div>

      </div>

      {empresa.analise && (
        <div className="card mt-4 p-4 border-0 bg-light">

          <h5 className="mb-3">Análise com IA</h5>

          <p>
            <strong>Resumo:</strong><br />
            {empresa.analise.resumo || "Não disponível"}
          </p>

          {empresa.analise.risco && (
            <p>
              <strong>Risco:</strong>{" "}
              <span
                className={`badge ${
                  empresa.analise.risco.toLowerCase() === "alto"
                    ? "bg-danger"
                    : empresa.analise.risco.toLowerCase() === "medio"
                    ? "bg-warning text-dark"
                    : "bg-success"
                }`}
              >
                {empresa.analise.risco}
              </span>
            </p>
          )}

          {empresa.analise.pontos_fortes?.length > 0 && (
            <>
              <strong>Pontos fortes:</strong>
              <ul className="mt-2">
                {empresa.analise.pontos_fortes.map((p, i) => (
                  <li key={i}>{p}</li>
                ))}
              </ul>
            </>
          )}

        </div>
      )}

    </div>
  );
}