# DocBrain API 🧠

API backend para chat com documentos PDF utilizando RAG (Retrieval-Augmented Generation), LangChain e OpenAI. O sistema conta com autenticação de usuários para garantir que cada um acesse apenas seus próprios documentos.

## 🛠 Stack Tecnológica

* **Backend:** FastAPI + Uvicorn
* **IA & Orquestração:** LangChain, OpenAI API
* **Banco Vetorial:** ChromaDB (Persistência local)
* **Autenticação:** JWT (python-jose + passlib)
* **Processamento de Arquivos:** pypdf

## 📋 Funcionalidades Principais

1.  **Autenticação (JWT):** Cadastro e Login de usuários.
2.  **Upload de Documentos:** Ingestão de PDFs e vetorização isolada por usuário.
3.  **Chat com RAG:** Conversa contextualizada com os documentos do usuário logado.

## 🚀 Como Rodar

1.  **Crie o ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows: venv\Scripts\activate
    # Linux/Mac: source venv/bin/activate
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure o ambiente:**
    Crie um arquivo `.env` na raiz com sua chave da OpenAI e um segredo para o JWT:
    ```env
    OPENAI_API_KEY="sk-..."
    SECRET_KEY="sua_chave_secreta_super_segura"
    ALGORITHM="HS256"
    ```

4.  **Rode a API:**
    ```bash
    uvicorn main:app --reload
    ```