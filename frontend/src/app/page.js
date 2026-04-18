"use client";

import { useRouter } from "next/navigation";
import CnpjForm from "../components/CnpjForm";

export default function Home() {
  const router = useRouter();

  const handleSubmit = (cnpj, tipo) => {
    router.push(`/resultado/${cnpj}?tipo=${tipo}`);
  };

  return (
    <div className="container mt-5">
      <h2>Consulta de CNPJ</h2>
      <CnpjForm onSubmit={handleSubmit} />
    </div>
  );
}