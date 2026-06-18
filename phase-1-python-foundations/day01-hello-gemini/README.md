# Day 1 — Hello Gemini & OpenAI

First project in the 30-day AI Engineering journey.
Establishes the baseline: calling two LLM APIs with the same prompt and comparing
their output, latency, and token usage side by side.

## What This Covers

- Google Gemini API via `google-generativeai` SDK
- OpenAI API via the official `openai` Python client
- `.env`-based secret management with `python-dotenv`
- Token usage logging (critical for cost awareness from day one)

## Architecture Note

Both SDKs are called directly here — no orchestration layer yet.
From Day 7 onward, LangChain's `ChatGoogleGenerativeAI` and `ChatOpenAI`
wrap these same HTTP calls, letting you swap models with a single string change.
Knowing the raw API first means you're never blindly trusting the abstraction.

## Files

| File | Purpose |
|------|---------|
| `main.py` | Side-by-side comparison runner |
| `hello_gemini.py` | Gemini-only script |
| `hello_openai.py` | OpenAI-only script |
| `requirements.txt` | Dependencies |

## Setup

From the repository root (`d:\projects\ai_engineering_python_langchain_langgraph`), initialize the project environment and run the scripts:

### 1. Configure Secrets
Copy the template and fill in your keys:
```powershell
cp .env.example .env
```
Open the new `.env` file and set `GEMINI_API_KEY` (and `OPENAI_API_KEY` if you have one).

### 2. Set Up Virtual Environment
Create and activate a Python virtual environment:
```powershell
# Create venv
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
# source .venv/bin/activate
```

### 3. Install Dependencies & Run
You can install dependencies and run the scripts directly from the repository root:

```powershell
# Install requirements
pip install -r phase-1-python-foundations/day01-hello-gemini/requirements.txt

# Run the comparative runner
python phase-1-python-foundations/day01-hello-gemini/main.py

# Or run the raw Gemini script
python phase-1-python-foundations/day01-hello-gemini/hello_gemini.py
```

Alternatively, you can navigate into the Day 1 directory first:
```powershell
cd phase-1-python-foundations/day01-hello-gemini
pip install -r requirements.txt
python main.py
```

## Expected Output

```
Prompt: What is an LLM? Explain in exactly 3 bullet points.
────────────────────────────────────────────────
🔵 Gemini 2.0 Flash  [0.82s | 147 tokens]
────────────────────────────────────────────────
• LLMs are neural networks trained on massive text datasets...
...

🟢 GPT-4o-mini       [1.1s | 132 tokens]
────────────────────────────────────────────────
• Large Language Models (LLMs) are AI systems...
...

📊 Comparison
   Latency  — Gemini: 0.82s | OpenAI: 1.1s
   Tokens   — Gemini: 147   | OpenAI: 132
```

## What I Learned

- Gemini uses `generate_content()` with `system_instruction` at model init
- OpenAI uses `chat.completions.create()` with a `messages` array
- Both converge on the same conceptual interface — LangChain unifies them
- Token counts differ because tokenizers differ between providers
