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
    let ativo = true;

    async function fetchData() {
      try {
        setErro(null);
        setLoading(true);
        
        const cache = sessionStorage.getItem(`empresa_${cnpj}_${tipo}`);

        if (cache) {
          console.log("USANDO CACHE");
          setEmpresa(JSON.parse(cache));
          setLoading(false);
          return;
        }

        let data;

        if (tipo === "ia") {
          const [dados, ia] = await Promise.all([
            analisarCNPJ(cnpj),
            analisarCNPJComIA(cnpj),
          ]);

          if (!ativo) return;

          data = {
            ...dados,
            analise: ia.analise,
            meta: ia.meta,
          };
        } else {
          data = await analisarCNPJ(cnpj);
        }

        if (!ativo) return;

        const empresaFormatada = adaptarEmpresa(data);

        sessionStorage.setItem(
          `empresa_${cnpj}_${tipo}`,
          JSON.stringify(empresaFormatada)
        );

        setEmpresa(empresaFormatada);
      } catch (err) {
        if (!ativo) return;

        console.error(err);
        setErro(err.message);
      } finally {
        if (ativo) setLoading(false);
      }
    }

    fetchData();

    return () => {
      ativo = false;
    };
  }, [cnpj, tipo]);

  if (loading) return <LoadingSpinner />;

  if (erro) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger">{erro}</div>
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

      <button
        className="btn btn-outline-secondary mb-3"
        onClick={() => router.push("/")}
      >
        ← Voltar
      </button>

      <h5 className="mb-3">
        {empresa.tipo === "ia"
          ? "Resultado da Análise com IA"
          : "Dados retornados da Empresa"}
      </h5>

      <EmpresaCard empresa={empresa} />

      {empresa.meta?.popularidade && (
        <button
          className="btn btn-info mt-3"
          onClick={() => {
            sessionStorage.setItem(
              `empresa_${cnpj}_${tipo}`,
              JSON.stringify(empresa)
            );

            router.push(
              `/insights?consultas=${empresa.meta.popularidade.consultas}&nivel=${empresa.meta.popularidade.nivel}`
            );
          }}
        >
          Ver Insights
        </button>
      )}
    </div>
  );
}