# 🗺️ Project Roadmap: DocBrain API

Este documento estabelece a ordem lógica de desenvolvimento. O objetivo é construir o sistema em camadas, onde cada fase desbloqueia a funcionalidade da próxima.

## 🏁 Fase 1: Fundação & Segurança (Auth System)
*O sistema precisa saber **quem** está fazendo a requisição antes de processar qualquer dado.*

- [ ] **Configuração de Ambiente**
    - [ ] Definir variáveis de ambiente no `.env` (API Keys, Secret Key JWT, Hash Algorithm).
    - [ ] Configurar conexão com banco de dados relacional (SQLite/Postgres) para armazenar usuários.

- [ ] **Modelagem de Dados (Usuários)**
    - [ ] Criar Schemas Pydantic para `UserCreate`, `UserLogin` e `UserResponse`.
    - [ ] Criar Modelo ORM (SQLAlchemy) para a tabela de usuários.

- [ ] **Lógica de Autenticação**
    - [ ] Implementar utilitário de *hashing* de senhas (bcrypt).
    - [ ] Implementar utilitário de geração e decodificação de tokens JWT.
    - [ ] Criar dependência `get_current_user` para proteger rotas.

- [ ] **Endpoints de Auth**
    - [ ] Rota `POST /auth/signup`: Registro de novos usuários.
    - [ ] Rota `POST /auth/token`: Login (retorna o Access Token).
    - [ ] Rota `GET /auth/me`: Teste de rota protegida (retorna dados do usuário logado).

---

## 🧠 Fase 2: Ingestão de Dados (RAG Core)
*O sistema precisa processar documentos e associá-los estritamente ao usuário autenticado.*

- [ ] **Preparação do VectorDB**
    - [ ] Instanciar cliente do ChromaDB (persistência local).
    - [ ] Configurar função de *Embeddings* (OpenAIEmbeddings).

- [ ] **Processamento de Arquivos**
    - [ ] Implementar leitura de PDF (`pypdf`) a partir de upload em memória.
    - [ ] Implementar *Text Splitter* (LangGraph) para quebrar o texto em chunks otimizados.

- [ ] **Endpoint de Upload**
    - [ ] Rota `POST /ingest/upload` (Protegida).
    - [ ] Lógica de vetorização: Gerar embeddings dos chunks com LangGraph.
    - [ ] **Ponto Crítico:** Salvar vetores no ChromaDB injetando o `user_id` nos metadados de cada chunk.

---

## 💬 Fase 3: Recuperação & Chat (RAG Inference)
*O sistema precisa buscar informações, mas apenas dentro do escopo do usuário.*

- [ ] **Lógica de Recuperação (Retriever)**
    - [ ] Configurar busca por similaridade no ChromaDB.
    - [ ] **Ponto Crítico:** Implementar filtro obrigatório na query do VectorDB (`where={"user_id": current_user.id}`).

- [ ] **Orquestração com LLM**
    - [ ] Criar *Prompt Template* para instruir a IA a usar o contexto fornecido.
    - [ ] Configurar o Graph (LangGraph) de resposta: Retriever -> Prompt -> LLM.

- [ ] **Endpoint de Chat**
    - [ ] Rota `POST /chat/message` (Protegida).
    - [ ] Receber pergunta, executar o graph e retornar a resposta gerada.

---

## 🚀 Fase 4: Refinamento & Deploy
*Preparação para "o mundo real".*

- [ ] **Tratamento de Erros**
    - [ ] Adicionar tratativas para arquivos inválidos ou corrompidos.
    - [ ] Tratar erros de limite de token ou falha na API da OpenAI.

- [ ] **Containerização**
    - [ ] Criar `Dockerfile` otimizado para Python.
    - [ ] Criar `docker-compose.yml` (opcional, se decidir usar banco externo depois).

- [ ] **Documentação**
    - [ ] Revisar documentação automática do Swagger (`/docs`).