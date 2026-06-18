# 🤖 30-Day AI Engineering Journey

A structured, 30-day project-based learning path transitioning from web development to AI engineering.
Built with Python, LangChain, LangGraph, FastAPI, Firebase, and the Google Gemini API.

---

## 🗂️ Repository Structure

```
ai_engineering_python_langchain_langgraph/
├── _docs/                        # Roadmaps, planning docs, task lists
├── phase-1-python-foundations/   # Days 1–6:  Python for AI, embeddings, Hugging Face
├── phase-2-langchain-rag/        # Days 7–16: LangChain, RAG pipeline, FastAPI
├── phase-3-agents-google/        # Days 17–24: LangGraph agents, Firebase, Genkit
└── phase-4-deploy/               # Days 25–30: Docker, Cloud Run, portfolio polish
```

---

## 📦 Projects

| Day(s) | Project | Key Skills |
|--------|---------|------------|
| 1 | [hello-gemini](./phase-1-python-foundations/day01-hello-gemini/) | Gemini API, OpenAI API, .env setup |
| 2 | [embeddings](./phase-1-python-foundations/day02-embeddings/) | Embeddings, cosine similarity, NumPy |
| 3 | [pandas-ml](./phase-1-python-foundations/day03-pandas-ml/) | Pandas, scikit-learn, data cleaning |
| 4 | [prompt-engineering](./phase-1-python-foundations/day04-prompt-engineering/) | Prompt patterns, intent routing, OpenAI API |
| 5 | [llm-pipeline](./phase-1-python-foundations/day05-llm-pipeline/) | Multi-step pipelines, moderation, structured output |
| 6 | [huggingface](./phase-1-python-foundations/day06-huggingface/) | HuggingFace Transformers, open-source models |
| 7 | [langchain-intro](./phase-2-langchain-rag/day07-langchain-intro/) | LangChain LCEL, Runnables |
| 8 | [langchain-classifier](./phase-2-langchain-rag/day08-langchain-classifier/) | Pydantic, structured outputs, `with_structured_output()` |
| 9 | [memory-chatbot](./phase-2-langchain-rag/day09-memory-chatbot/) | Conversation history, ChatMessageHistory |
| 10 | [rag-chunking](./phase-2-langchain-rag/day10-rag-chunking/) | Document loaders, RecursiveCharacterTextSplitter |
| 11 | [rag-vectorstore](./phase-2-langchain-rag/day11-rag-vectorstore/) | ChromaDB, similarity search, MMR retrieval |
| 12 | [**rag-chatbot ⭐**](./phase-2-langchain-rag/day12-rag-chatbot/) | Full RAG pipeline — flagship project |
| 13 | [rag-evaluation](./phase-2-langchain-rag/day13-rag-evaluation/) | RAGAS: faithfulness, relevancy, context recall |
| 14 | [advanced-rag](./phase-2-langchain-rag/day14-advanced-rag/) | HyDE, multi-query, Pinecone cloud vector DB |
| 15–16 | [rag-fastapi](./phase-2-langchain-rag/day15-16-rag-fastapi/) | FastAPI, async/await, StreamingResponse, Pydantic |
| 17 | [langgraph-basics](./phase-3-agents-google/day17-langgraph-basics/) | LangGraph nodes, edges, state graphs |
| 18–19 | [research-agent](./phase-3-agents-google/day18-19-research-agent/) | ReAct pattern, tool calling, human-in-the-loop |
| 20 | [langsmith](./phase-3-agents-google/day20-langsmith/) | LangSmith tracing, token cost, prompt versioning |
| 21 | [multimodal](./phase-3-agents-google/day21-multimodal/) | Gemini multimodal (image + text) |
| 22 | [firebase-genkit](./phase-3-agents-google/day22-firebase-genkit/) | Firebase Genkit (JS), web frontend, Firebase Hosting |
| 23 | [firestore-vector](./phase-3-agents-google/day23-firestore-vector/) | Firestore KNN vector search, GCP integration |
| 24 | [web-frontend](./phase-3-agents-google/day24-web-frontend/) | HTML/CSS/JS frontend → FastAPI backend |
| 25 | [docker-cloudrun](./phase-4-deploy/day25-docker-cloudrun/) | Docker, Google Cloud Run, production deployment |

---

## 🔑 Setup

```bash
# Clone and set up environment
git clone https://github.com/SuisSanem000/ai_engineering_python_langchain_langgraph.git
cd ai_engineering_python_langchain_langgraph

# Copy the env template and fill in your keys
cp .env.example .env

# Each project has its own venv and requirements.txt
# Example for Day 1:
cd phase-1-python-foundations/day01-hello-gemini
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
python main.py
```

---

## 📚 Documentation

Full roadmap, planning docs, and daily task lists are in [`_docs/`](./_docs/).

---

## Progress

- [x] Day 1 — Environment setup, Gemini + OpenAI API calls
- [ ] Day 2 — Embeddings from scratch
- [ ] Day 3 — Pandas + ML vocabulary
- [ ] ...
