"use client";

import { useSearchParams } from "next/navigation";

export default function Insights() {
  const params = useSearchParams();

  const consultas = Number(params.get("consultas")) || 0;
  const nivel = params.get("nivel") || "Desconhecido";

  function gerarInsight() {
    if (consultas < 5)
      return "Pouca relevância no mercado";

    if (consultas < 15)
      return "Empresa com interesse moderado";

    if (consultas < 30)
      return "Empresa bastante consultada";

    return "Empresa altamente relevante ou sob forte análise";
  }

  function corNivel() {
    if (nivel === "Alta") return "text-danger";
    if (nivel === "Média") return "text-warning";
    return "text-success";
  }

  return (
    <div className="container mt-5">
      <h2>Insights de Popularidade</h2>

      <div className="card p-4 mt-4">

        <p>
          <strong>Consultas:</strong> {consultas}
        </p>

        <p className={corNivel()}>
          <strong>Nível:</strong> {nivel}
        </p>

        <hr />

        <h5>Insight gerado </h5>
        <p>{gerarInsight()}</p>

      </div>
    </div>
  );
}