"use client";

import { useState } from "react";

export default function CnpjForm({ onSubmit }) {
  const [cnpj, setCnpj] = useState("");

  function limparCNPJ(valor) {
    return valor.replace(/\D/g, "");
  }

  const handleSubmit = (e, tipo) => {
    e.preventDefault();

    const cnpjLimpo = limparCNPJ(cnpj);

    if (cnpjLimpo.length !== 14) {
      alert("CNPJ inválido");
      return;
    }

    onSubmit(cnpjLimpo, tipo);
  };

  return (
    <div className="card p-4">

      <h4 className="mb-3">Consulta de Empresa</h4>

      <div className="mb-3">
        <label className="form-label">CNPJ</label>
        <input
          type="text"
          className="form-control"
          value={cnpj}
          onChange={(e) => setCnpj(e.target.value)}
          placeholder="00.000.000/0000-00"
        />
      </div>

      <div className="mb-4">

        <div className="mb-3 p-3 border rounded">
          <strong>Análise Normal</strong>
          <p className="mb-0 text-muted">
            Retorna dados públicos da empresa, como nome, status, endereço e atividade.
          </p>
        </div>

        <div className="mb-3 p-3 border rounded">
          <strong> Análise com IA</strong>
          <p className="mb-0 text-muted">
            Gera uma análise inteligente com resumo da empresa, nível de risco e pontos fortes,
            além de métricas de popularidade.
          </p>
        </div>

      </div>

      <div className="d-flex gap-2">
        <button
          className="btn btn-primary w-100"
          onClick={(e) => handleSubmit(e, "normal")}
        >
          Analisar Dados
        </button>

        <button
          className="btn btn-dark w-100"
          onClick={(e) => handleSubmit(e, "ia")}
        >
          Analisar com IA
        </button>
      </div>
    </div>
  );
}