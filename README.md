# 🗭 Smart Place Finder

[![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-4A90E2?logo=ollama)](https://ollama.com/)
[![WebUI](https://img.shields.io/badge/frontend-Open--WebUI-ff9800?logo=openai)](https://github.com/open-webui/open-webui)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An AI-powered local chatbot that helps users find nearby places (like cafes or restaurants) via natural language prompts.
Built with **FastAPI**, **Ollama**, and **Open-WebUI**.

Example:

> “Find a cafe in Jakarta”

The chatbot queries the FastAPI API and returns a list of places with clickable Google Maps links.

---

---

## 🚀 How to Run

### 1️⃣ Backend (FastAPI)

#### 📦 Install dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

#### ▶️ Run FastAPI server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

FastAPI will start at:
🔗 [http://localhost:8000](http://localhost:8000)

You can also open the API docs:
📘 Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 2️⃣ LLM (Ollama)

#### 🔧 Install Ollama

Follow the installation guide here:
🔗 [https://ollama.com/download](https://ollama.com/download)

#### 🔥 Run your model

Example:

```bash
ollama pull llama3.1
ollama run llama3.1
```

Ensure your LLM is running locally before starting the WebUI.

---

### 3️⃣ Web UI (Open-WebUI)

#### 🧩 Clone & Run WebUI

```bash
cd webui
npm install
npm run dev
```

By default, WebUI will start at
🔗 [http://localhost:3000](http://localhost:3000)

You can configure the backend API URL and LLM endpoint in the `.env` file.

---

## ⚙️ Environment Variables (Example)

Create `.env` files inside each component as needed.

### `backend/.env`

```
API_KEY=your_api_key_here
GOOGLE_MAPS_API_KEY=your_google_api_key_here
```

### `webui/.env`

```
VITE_API_URL=http://localhost:8000
VITE_LLM_URL=http://localhost:11434
```

---

## 🧠 Diagram Overview

```mermaid
flowchart LR
    User["👩 User (Web UI)"] -->|Prompt| WebUI["🌐 Open-WebUI"]
    WebUI -->|Send Query| FastAPI["⚙️ FastAPI Backend"]
    FastAPI -->|Forward Request| Ollama["🧩 LLM (Ollama)"]
    FastAPI -->|Fetch Location Data| Google["🗹️ Google Maps API"]
    Ollama -->|AI Response| FastAPI
    FastAPI -->|Structured JSON| WebUI
    WebUI -->|Display Result| User
```

---

## 🧪 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 💡 Author

**Smart Place Finder** — Developed with ❤️ using FastAPI, Ollama, and Open-WebUI.
