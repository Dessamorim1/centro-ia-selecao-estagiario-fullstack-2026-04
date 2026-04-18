# DOCS.md

##  Nome da Solução

**Sistema Inteligente de Análise de Empresas por CNPJ**

---

## Problema Escolhido

A dificuldade em avaliar rapidamente a confiabilidade, relevância e risco de empresas com base apenas em dados públicos de CNPJ.
Os dados brutos existem, mas não são interpretados de forma acessível para tomada de decisão.

---

## Objetivo da Aplicação

Desenvolver uma aplicação que:

* Consulte dados públicos de empresas via CNPJ
* Utilize Inteligência Artificial para gerar análises interpretativas
* Apresente insights sobre popularidade e relevância da empresa
* Auxilie na tomada de decisão de forma rápida e visual

---

## Descrição do Caso de Uso

### Usuário:

* Analista
* Estudante
* Investidor
* Curioso

### Fluxo:

1. Usuário digita um CNPJ
2. Escolhe:

   * Análise normal (dados brutos)
   * Análise com IA
3. Sistema retorna:

   * Informações da empresa
   * Análise inteligente (se selecionado)
4. Usuário pode acessar:

   * Página de insights baseada na popularidade

---

## Tecnologias Utilizadas

### Front-end:

* Next.js (React)
* JavaScript
* Bootstrap

### Back-end:

* FastAPI (Python)
* SQLAlchemy
* Banco de dados relacional

### IA:

* Integração com API Gemini (Google AI)

---

## Arquitetura Geral da Solução

```
Frontend (Next.js)

Backend (FastAPI)
       
Serviços:
  - API de CNPJ
  - Serviço de IA (Gemini)

Banco de Dados
```

### Componentes:

* Front: interface e navegação
* Backend: regras de negócio
* IA: análise inteligente
* DB: armazenamento de histórico e popularidade

---

## Instruções de Instalação e Execução

### Backend

```bash
# criar ambiente virtual
python -m venv venv

# ativar 
venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# rodar servidor
uvicorn app.main:app --reload
```

Servidor disponível em:

```
http://localhost:8000
```

---

###  Frontend

```bash
cd frontend

npm install

npm run dev
```

Aplicação disponível em:

```
http://localhost:3000
```

---

## Explicação da Integração com IA

A IA é utilizada para:

* Interpretar dados da empresa
* Gerar:

  * resumo
  * nível de risco
  * pontos fortes

### Fluxo:

1. Backend busca dados do CNPJ
2. Dados são enviados para o serviço de IA
3. IA retorna análise estruturada
4. Resultado é salvo no banco

---

##  Exemplos de Uso

### Análise Normal

Entrada:

```
CNPJ: 07526557011659
```

Saída:

* Nome da empresa
* Status
* Atividade
* Endereço
* Capital

---

###  Análise com IA

Saída adicional:

* Resumo da empresa
* Classificação de risco
* Pontos fortes
* Popularidade

---

###  Insights

Com base em:

* quantidade de consultas

Exemplo:

* Poucas consultas → baixa relevância
* Muitas consultas → alta relevância ou possível risco

---

##  Limitações Atuais do MVP

* Validação de CNPJ simplificada
* UI básica (sem dashboard avançado)
* Insights baseados em regras simples
* Dependência de API externa para dados
* IA pode gerar respostas inconsistentes

---

##  Possíveis Evoluções Futuras

*  Dashboard com gráficos
*  Sistema de login e usuários
*  Histórico completo de consultas
*  IA mais sofisticada (score de risco)
*  Versão mobile
*  Busca por nome da empresa
*  Análise comparativa entre empresas
*  Cache mais eficiente

---

## Conclusão

A aplicação entrega uma solução funcional que:

* integra dados reais
* utiliza IA para análise
* apresenta insights úteis

Mesmo sendo um MVP, já demonstra:

* arquitetura sólida
* integração de múltiplas camadas
* potencial de evolução para produto real

---
