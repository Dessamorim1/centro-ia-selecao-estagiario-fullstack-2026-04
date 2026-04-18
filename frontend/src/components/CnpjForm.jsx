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
    <form>
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

      <div className="d-flex gap-2">
        <button
          className="btn btn-primary"
          onClick={(e) => handleSubmit(e, "normal")}
        >
          Análise Normal
        </button>

        <button
          className="btn btn-dark"
          onClick={(e) => handleSubmit(e, "ia")}
        >
          Análise com IA
        </button>
      </div>
    </form>
  );
}