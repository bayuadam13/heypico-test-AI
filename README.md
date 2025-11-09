# 🧭 Smart Place Finder

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
👉 [http://localhost:8000](http://localhost:8000)

You can also open the API docs:
📘 Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 2️⃣ LLM (Ollama)

#### 🔧 Install Ollama

Follow the installation guide here:
👉 [https://ollama.com/download](https://ollama.com/download)

#### 🔥 Run your model

Example:

```bash
ollama pull llama3
ollama run llama3
```

Ensure your LLM is running locally before starting the WebUI.

---

### 3️⃣ Web UI (Open-WebUI)

#### 🧩 Clone & Run WebUI

First, clone the official Open-WebUI repository:

```bash
git clone https://github.com/open-webui/open-webui.git
cd open-webui
```

#### ▶️ Run WebUI

```bash
python -m open_webui
```

By default, WebUI will start at
👉 [http://localhost:8080](http://localhost:8080)

You can configure the backend API URL and LLM endpoint in the `.env` file.

---

## ⚙️ Environment Variables (Example)

Create `.env` files inside each component as needed.

### `backend/.env`

```
GOOGLE_MAPS_API_KEY={on email}
```


---

## 🧠 Diagram Overview

```mermaid
flowchart LR
    User["🧑 User (Web UI)"] -->|Prompt| WebUI["🌐 Open-WebUI"]
    WebUI -->|Send Prompt| Ollama["🧩 LLM (Ollama)"]
    Ollama -->|Calls Tool / External API| FastAPI["⚙️ FastAPI (Tool)"]
    FastAPI -->|Fetch Location Data| Google["🗺️ Google Maps API"]
    FastAPI -->|Return Data| Ollama
    Ollama -->|Generate Final Response| WebUI
    WebUI -->|Display Result| User
```

---

## 🪪 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 💡 Author

**Smart Place Finder** — Developed with ❤️ using FastAPI, Ollama, and Open-WebUI.
