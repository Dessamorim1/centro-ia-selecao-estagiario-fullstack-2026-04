"use client";

import { useEffect, useState } from "react";
import {
  useParams,
  useSearchParams,
  useRouter,
} from "next/navigation";

import {
  analisarCNPJ,
  analisarCNPJComIA,
} from "../../../services/api";

import { adaptarEmpresa } from "../../../services/adapter";
import EmpresaCard from "../../../components/EmpresaCard";
import LoadingSpinner from "../../../components/LoadingSpinner";

export default function Resultado() {
  const params = useParams();
  const searchParams = useSearchParams();
  const router = useRouter();

  const cnpj = params.cnpj;
  const tipo = searchParams.get("tipo");

  const [empresa, setEmpresa] = useState(null);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        setErro(null);
        setLoading(true);

        const data =
          tipo === "ia"
            ? await analisarCNPJComIA(cnpj)
            : await analisarCNPJ(cnpj);

        const empresaFormatada = adaptarEmpresa(data);

        setEmpresa(empresaFormatada);
      } catch (err) {
        console.error(err);
        setErro(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, [cnpj, tipo]);

  if (loading) return <LoadingSpinner />;

  if (erro) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger">
          <div className="alert alert-danger">
            {erro}
          </div>
        </div>
      </div>
    );
  }

  if (!empresa) {
    return (
      <div className="container mt-5">
        <div className="alert alert-warning">
          Nenhum dado encontrado
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <EmpresaCard empresa={empresa} />

      {empresa.meta?.popularidade && (
        <button
          className="btn btn-info mt-3"
          onClick={() =>
            router.push(
              `/insights?consultas=${empresa.meta.popularidade.consultas}&nivel=${empresa.meta.popularidade.nivel}`
            )
          }
        >
          Ver Insights
        </button>
      )}
    </div>
  );
}