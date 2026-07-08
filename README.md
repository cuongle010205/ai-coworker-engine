# 🤖 AI Co-worker Engine

> An intelligent AI-powered co-worker built with **FastAPI**, **Gemini**, **RAG**, **FAISS**, and **Conversation Memory**.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-red)
![License](https://img.shields.io/badge/License-MIT-blue)

</p>

---

# 📌 Overview

AI Co-worker Engine is an intelligent conversational assistant that combines:

- 🧠 Google Gemini LLM
- 📚 Retrieval-Augmented Generation (RAG)
- 💾 Long-term Conversation Memory
- 🔍 Vector Search with FAISS
- ⚡ FastAPI Backend
- 🛠 Tool Calling
- 👤 Persona-based Responses

Instead of answering only from the LLM, the assistant retrieves relevant company knowledge before generating responses, producing more accurate and context-aware answers.

---

# ✨ Features

✅ Multi-turn Conversation

✅ Retrieval-Augmented Generation (RAG)

✅ FAISS Vector Database

✅ Conversation Memory (SQLite)

✅ Persona Prompting

✅ Supervisor Module

✅ Tool Calling

✅ Logging

✅ REST API

✅ Docker Ready

---

# 🏗 Architecture

```

                    User

                      │

              Frontend (HTML)

                      │

                      ▼

              FastAPI Backend

                      │

        ┌─────────────┴─────────────┐

        ▼                           ▼

   Supervisor                 Memory Manager

        │                           │

        ▼                           ▼

      Tool Manager            SQLite Database

        │

        ▼

      RAG Engine

        │

FAISS ← Embeddings ← Documents

        │

        ▼

     Gemini 2.5 Flash

        │

        ▼

     AI Response

```

---

# 📂 Project Structure

```text
ai-coworker-engine/

│

├── backend/

│   ├── app.py

│   ├── agent.py

│   ├── llm.py

│   ├── rag.py

│   ├── memory.py

│   ├── prompts.py

│   ├── tools.py

│   ├── supervisor.py

│   ├── logger.py

│   └── config.py

│

├── frontend/

│

├── data/

│   └── gucci_docs.json

│

├── vector_db/

│

├── docker-compose.yml

│

├── requirements.txt

│

└── README.md

```

---

# 🚀 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Backend | FastAPI |
| LLM | Google Gemini |
| RAG | LangChain |
| Embedding | HuggingFace BGE |
| Vector DB | FAISS |
| Database | SQLite |
| Frontend | HTML / CSS / JavaScript |
| Deployment | Docker |

---

# 🧠 Retrieval-Augmented Generation

```
Documents

↓

Chunking

↓

Embedding

↓

FAISS

↓

Similarity Search

↓

Relevant Context

↓

Gemini

↓

Response
```

---

# 💾 Memory System

The assistant stores:

- Conversation History
- Relationship Score
- Progress
- Summary

This enables contextual multi-turn conversations.

---

# 🔌 REST API

## Health Check

```
GET /health
```

Response

```json
{
  "status":"ok"
}
```

---

## Chat

```
POST /chat
```

Request

```json
{
    "session_id":"demo",
    "persona":"chro",
    "message":"Tell me about Gucci."
}
```

Response

```json
{
    "assistant_message":"...",
    "sources":[
        "Gucci History"
    ],
    "latency":0.84,
    "state_update":{
        "turns":5,
        "relationship_score":50
    },
    "safety_flags":[]
}
```

---

# ⚙ Installation

Clone repository

```bash
git clone https://github.com/cuongle010205/ai-coworker-engine.git
```

Install packages

```bash
pip install -r requirements.txt
```

Create environment variables

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run backend

```bash
uvicorn backend.app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 🖥 Demo

Swagger UI

```
http://127.0.0.1:8000/docs
```

Chat Endpoint

```
POST /chat
```

---

# 📈 Future Improvements

- React + Tailwind Frontend
- Streaming Responses
- Source Citation UI
- Docker Deployment
- Authentication
- Redis Memory
- PostgreSQL
- Semantic Cache
- Unit Testing
- CI/CD

---

# 👨‍💻 Author

**Lê Long Cương**

University of Science - VNUHCM

AI / Software Engineer

GitHub:
https://github.com/cuongle010205
LinkedIn:
www.linkedin.com/in/cươnglê-991b01402

---

# ⭐ If you like this project

Please give this repository a ⭐.
