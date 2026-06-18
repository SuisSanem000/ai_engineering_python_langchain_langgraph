# Day 1 — Environment Setup & First API Calls

Welcome to Day 1 of your 30-day AI Engineering journey. This document provides a high-level conceptual summary of our architectural layout, dependencies, and environment setup for today's learning.

---

## 📅 High-Level Learning Goals
Before starting to code, make sure to read the following conceptual documents located in this directory:
1. **What is an LLM?** (Read: [2_what-is-a-large-language-model.md](file:///d:/projects/ai_engineering_python_langchain_langgraph/phase-1-python-foundations/day01-hello-gemini/docs/2_what-is-a-large-language-model.md)) — Establishes how deep neural network architectures (specifically transformers using self-attention mechanisms) enable text generation.
2. **What are Tokens?** (Read: [3_what-are-tokens.md](file:///d:/projects/ai_engineering_python_langchain_langgraph/phase-1-python-foundations/day01-hello-gemini/docs/3_what-are-tokens.md)) — Understand how textual data is processed in sub-word chunks and how prompt formatting affects tokenization and cost.

---

## 📂 Repository Structure

The project has been organized into a modular scaffolding to support the entire 30-day curriculum:

```text
ai_engineering_python_langchain_langgraph/
├── .env.example                          ← template for local credentials (never commit .env)
├── .gitignore                            ← excludes Python venv, .env, ChromaDB, Node, Docker
├── README.md                             ← root project index and daily progress tracker
├── _docs/                                ← documentation and roadmaps
│   ├── 30_day_ai_engineering_roadmap.md
│   └── daily_task_lists.md
├── phase-1-python-foundations/
│   └── day01-hello-gemini/               ← Day 1 Project Directory
│       ├── docs/                         ← Day 1 notes and explanations
│       │   ├── 1_day-1-explanation.md    ← This file
│       │   ├── 2_what-is-a-large-language-model.md
│       │   └── 3_what-are-tokens.md
│       ├── hello_gemini.py               ← Direct Gemini API implementation
│       ├── hello_openai.py               ← Direct OpenAI API implementation
│       ├── main.py                       ← Comparative latency & token benchmarking script
│       └── requirements.txt              ← Python dependency list (generativeai, openai, dotenv)
```

---

## ⚙️ Running the Day 1 Code

Execute all setup commands from the repository root:

### 1. Environment Setup
Create a virtual environment at the repository root and activate it:
```powershell
# Create venv
python -m venv .venv

# Activate venv (Windows PowerShell)
.venv\Scripts\activate

# Install requirements
pip install -r phase-1-python-foundations/day01-hello-gemini/requirements.txt
```

### 2. Configure Credentials
Copy `.env.example` to `.env` and enter your API keys:
```powershell
cp .env.example .env
```
Inside your `.env` file, populate your key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
*(Leave other API keys blank for now. The benchmarking script is designed to run fine and skip any missing models).*

### 3. Run the Scripts
```powershell
# Run the comparative runner
python phase-1-python-foundations/day01-hello-gemini/main.py

# Or run the individual client scripts
python phase-1-python-foundations/day01-hello-gemini/hello_gemini.py
```

---

## 🧠 Architectural Concepts

* **Comparative Benchmarking:** The runner (`main.py`) evaluates how different underlying models answer the same instructions. This side-by-side verification helps developers evaluate API latency and tokenization costs to select the most optimal models.
* **Direct SDK Usage:** Calling raw API platforms directly teaches you the baseline message-passing payload patterns (Google AI Studio's `generate_content` and OpenAI's `chat.completions`) before we abstract them behind LangChain in Phase 2.
* **Code Implementation Comments:** Specific configuration variables, SDK classes, parameters (e.g. `temperature`, `system_instruction` initialization, and token calculation API details) are documented directly inside the code scripts (`hello_gemini.py`, `hello_openai.py`, and `main.py`).

---

## 💡 Quota & Regional Settings (EEA Developers)

If your Google AI Studio API requests fail with a `429 Quota Exceeded (limit: 0)` error:
* **The AQ. Key Format:** Google AI Studio keys generated now default to the `AQ.` prefix. This is the new authentic developer key format and is correct.
* **EEA Regional Block:** Due to data regulations in the European Economic Area (EEA) and UK, the free tier is unavailable. To lift the zero limit, you must link an active payment method in the [Google Cloud Console Billing Page](https://console.cloud.google.com/billing) for the project (`crypto-snow-426714-f1`). Developer API runs cost only fractions of a cent, but billing connection is required.