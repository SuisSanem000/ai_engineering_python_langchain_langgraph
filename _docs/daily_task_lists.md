# ✅ Daily Task Lists — 30-Day AI Engineering Roadmap
> **4 hours per day | 120 hours total**
> Each task list is a plain checklist — no categories, just do them in order.

---

## 📅 PHASE 1 — Python for AI Foundations (Days 1–6)

---

### Day 1 (2026-06-13) — Environment Setup + First Gemini Call

> **Status:** Code and environment setup implemented; user is currently studying the concepts.


- [x] Install Python 3.11+
- [x] Install VS Code
- [x] Install `pip` and set up `venv`
- [x] Go to [Google AI Studio](https://aistudio.google.com/) and get your Gemini API key
- [/] Read [What is an LLM?](https://www.cloudflare.com/learning/ai/what-is-a-large-language-model/) (~30 min)
- [/] Read [What is a token?](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) (~15 min)
- [x] Create a GitHub repo named `ai-engineering-journey`
- [x] Create a Python virtual environment inside the repo
- [x] Run `pip install google-generativeai python-dotenv openai`
- [x] Create a `.env` file and store your Gemini API key in it
- [x] Write `hello_gemini.py` — call the Gemini API with any prompt, print the response
- [x] Load the `.env` key using `python-dotenv` in your script
- [ ] Sign up for a free [OpenAI API account](https://platform.openai.com/) (even $5 credits is enough)
- [x] Write a basic README for the repo
- [x] Push everything to GitHub

---

### Day 2 (2026-06-14) — NumPy + Embeddings from Scratch

> **Status:** Not started


- [ ] Open [Kaggle Pandas course](https://www.kaggle.com/learn/pandas) and complete lessons 1–3 (DataFrames, indexing, summary functions)
- [ ] Watch [What are Embeddings? — Josh Starmer (12 min)](https://www.youtube.com/watch?v=viZrOnJclY0)
- [ ] Run `pip install numpy`
- [ ] Write a Python script that generates embeddings for 10 sentences using the Gemini Embedding API
- [ ] Compute cosine similarity between all sentence pairs manually using NumPy
- [ ] Print the most similar pair with their score: `"Most similar: [A] ↔ [B] — score: 0.94"`
- [ ] Push the script as a folder named `day2-embeddings-scratch`

---

### Day 3 (2026-06-15) — Pandas + ML Vocabulary

> **Status:** Not started


- [ ] Open [Kaggle Pandas course](https://www.kaggle.com/learn/pandas) and complete the remaining lessons
- [ ] Open [Kaggle Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) and complete lessons 1–4 only
- [ ] Internalize these vocab words: training/test split, overfitting, accuracy, model
- [ ] Run `pip install pandas scikit-learn`
- [ ] Download the [Titanic CSV dataset](https://www.kaggle.com/c/titanic/data)
- [ ] Load the CSV with Pandas
- [ ] Handle null values, select relevant columns, inspect data types
- [ ] Run a `scikit-learn` decision tree classifier on the cleaned data
- [ ] Print the accuracy score
- [ ] Export predictions to a new CSV file
- [ ] Push as `day3-pandas-basics`

---

### Day 4 (2026-06-16) — Prompt Engineering Fundamentals

> **Status:** Not started


- [ ] Open [DL.AI: Prompt Engineering for Developers](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng) and complete the full course (~1.5h)
- [ ] Understand these patterns: zero-shot, few-shot, chain-of-thought, JSON/structured output
- [ ] Create a new file `cli_assistant.py`
- [ ] Add user input loop (accepts text from terminal)
- [ ] Write an intent classifier — one LLM call classifies the input as: `technical`, `creative`, or `factual`
- [ ] Write 3 prompt templates, one per intent category
- [ ] Route the user input to the correct template based on classification
- [ ] Make the response a structured JSON: `{"answer": "...", "category": "...", "confidence": 0.9}`
- [ ] Use the **OpenAI API** for this (not Gemini — you need experience with both)
- [ ] Test with at least 3 different types of questions
- [ ] Push as `day4-prompt-engineering`

---

### Day 5 (2026-06-17) — Multi-Step LLM Pipelines

> **Status:** Not started


- [ ] Open [DL.AI: Building Systems with the ChatGPT API](https://learn.deeplearning.ai/courses/chatgpt-building-system) and complete the full course (~2h)
- [ ] Understand: classification chains, multi-step pipelines, moderation layers
- [ ] Create `pipeline_cli.py`
- [ ] Add Step 1 — Moderation: check for harmful content (OpenAI moderation endpoint or Gemini safety check)
- [ ] Add Step 2 — Classification: route to the correct prompt template
- [ ] Add Step 3 — Generation: produce a structured JSON answer
- [ ] Add Step 4 — Validation: check the output is valid JSON before printing
- [ ] Wrap everything in a `while True` loop for multi-turn terminal conversation
- [ ] Test the pipeline with edge cases (harmful input, ambiguous input, normal input)
- [ ] Push as `day5-llm-pipeline-cli`

---

### Day 6 (2026-06-18) — Hugging Face + Certificates + LinkedIn

> **Status:** Not started


- [ ] Open [Hugging Face NLP Course — Chapter 1](https://huggingface.co/learn/nlp-course/chapter1/1) and complete it (~1h)
- [ ] Open [Hugging Face NLP Course — Chapter 2](https://huggingface.co/learn/nlp-course/chapter2/1) and complete it (~1h)
- [ ] Understand: what Transformers are, how models are hosted on HF, and how to use `pipeline()`
- [ ] Run `pip install transformers torch`
- [ ] Create `model_compare.py`
- [ ] Use a Hugging Face `pipeline("sentiment-analysis")` to classify 5 movie reviews
- [ ] Send the same 5 reviews to the Gemini API with a sentiment classification prompt
- [ ] Print both results side by side in a formatted table
- [ ] Push as `day6-hf-vs-gemini`
- [ ] Claim your **Kaggle Pandas certificate**
- [ ] Claim your **Kaggle Intro to ML certificate**
- [ ] Claim your **DL.AI Prompt Engineering certificate**
- [ ] Write README files for all projects built this week (Days 1–6)
- [ ] Post on LinkedIn: *"Week 1 of my AI Engineering journey complete — 3 certificates earned. Here's what I built..."*

---
---

## 📅 PHASE 2 — LLMs, LangChain, RAG & FastAPI (Days 7–16)

---

### Day 7 (2026-06-19) — LangChain Foundations Part 1

> **Status:** Not started


- [ ] Open [LangChain Academy: Introduction to LangChain](https://academy.langchain.com/courses/intro-to-langchain) and complete Modules 1–2
- [ ] Understand the LCEL mental model: `prompt | model | parser`
- [ ] Run `pip install langchain langchain-google-genai langchain-openai langchain-core`
- [ ] Recreate your Day 4 pipeline using LangChain LCEL
- [ ] Use `ChatGoogleGenerativeAI(model="gemini-2.0-flash")` as the model
- [ ] Use `ChatPromptTemplate.from_template()` for the prompt
- [ ] Use `StrOutputParser()` for output
- [ ] Chain them with `|` and invoke with `.invoke()`
- [ ] Print the result
- [ ] Push as `day7-langchain-intro`

---

### Day 8 (2026-06-20) — LangChain + Pydantic Structured Outputs

> **Status:** Not started


- [ ] Open [LangChain Academy: Introduction to LangChain](https://academy.langchain.com/courses/intro-to-langchain) and complete Modules 3–4
- [ ] Understand: Pydantic output parsers, conversation memory, `with_structured_output()`
- [ ] Run `pip install pydantic`
- [ ] Create a `ClassificationResult` Pydantic model with fields: `category`, `confidence`, `reason`
- [ ] Use `ChatOpenAI(model="gpt-4o-mini")` as the LLM
- [ ] Call `.with_structured_output(ClassificationResult)` on the LLM
- [ ] Invoke the structured LLM with a document text
- [ ] Print the result using `.model_dump_json(indent=2)`
- [ ] Test with at least 3 different document inputs
- [ ] Push as `day8-langchain-classifier`

---

### Day 9 (2026-06-21) — LangChain Complete + Memory Chatbot

> **Status:** Not started


- [ ] Open [LangChain Academy: Introduction to LangChain](https://academy.langchain.com/courses/intro-to-langchain) and complete all remaining modules
- [ ] Claim your **LangChain Academy: Introduction to LangChain certificate**
- [ ] Build a multi-turn chatbot with a customizable system prompt (passed as a variable)
- [ ] Add conversation history that persists across turns using `ChatMessageHistory`
- [ ] Add a `/clear` command that resets the conversation memory
- [ ] Add a `/summarize` command that asks the LLM to summarize the conversation so far
- [ ] Test the chatbot through multiple turns, then test `/clear` and `/summarize`
- [ ] Push as `day9-memory-chatbot`

---

### Day 10 (2026-06-22) — RAG Part 1: Document Loading & Chunking

> **Status:** Not started


- [ ] Open [DL.AI: Chat with Your Data](https://learn.deeplearning.ai/courses/langchain-chat-with-your-data) and complete Modules 1–3
- [ ] Understand: Document loaders, `RecursiveCharacterTextSplitter`, chunk size vs. overlap
- [ ] Run `pip install pypdf langchain-community chromadb`
- [ ] Pick a PDF to use (your roadmap PDF is fine)
- [ ] Load the PDF using `PyPDFLoader`
- [ ] Split it with 3 different chunk settings: (500/50), (1000/200), (2000/400)
- [ ] For each setting, print the total chunk count and average chunk size
- [ ] Save all chunks from one setting to a JSON file for inspection
- [ ] Push the script to a new folder `day10-rag-chunking`

---

### Day 11 (2026-06-23) — RAG Part 2: Embeddings + Vector Store

> **Status:** Not started


- [ ] Open [DL.AI: Chat with Your Data](https://learn.deeplearning.ai/courses/langchain-chat-with-your-data) and complete Modules 4–5
- [ ] Understand: similarity search, MMR retrieval, metadata filtering
- [ ] Extend yesterday's chunking script
- [ ] Embed all chunks using `GoogleGenerativeAIEmbeddings(model="models/embedding-001")`
- [ ] Store the embedded chunks in ChromaDB with `persist_directory="./chroma_db"`
- [ ] Write a query against the vector store using `similarity_search_with_score()`
- [ ] Print the top 3 chunks with their similarity scores
- [ ] Push as `day11-vector-store`

---

### Day 12 (2026-06-24) — RAG Part 3: Full Pipeline (Flagship Project ⭐)

> **Status:** Not started


- [ ] Open [DL.AI: Chat with Your Data](https://learn.deeplearning.ai/courses/langchain-chat-with-your-data) and complete Module 6
- [ ] Claim your **DL.AI "Chat with Your Data" certificate**
- [ ] Create a new repo `day12-rag-chatbot`
- [ ] Build the Ingest step: Load PDF → chunk → embed → store in ChromaDB
- [ ] Build the Retrieve step: User question → embed → return top-3 similar chunks
- [ ] Build the Generate step: Chunks + question → Gemini → streamed answer
- [ ] Build a terminal interface with `/ingest [path]` and `/ask [question]` commands
- [ ] Make the code clean, modular, and well-commented
- [ ] Test with at least 5 different questions about your PDF
- [ ] Push as `day12-rag-chatbot`

---

### Day 13 (2026-06-25) — RAG Evaluation with RAGAS

> **Status:** Not started


- [ ] Open [DL.AI: Building & Evaluating Advanced RAG](https://learn.deeplearning.ai/courses/building-evaluating-advanced-rag) and complete the full course (~2h)
- [ ] Understand these RAGAS metrics: Faithfulness, Answer Relevancy, Context Recall
- [ ] Run `pip install ragas datasets`
- [ ] Create a test set of 5 question + expected answer pairs based on your PDF
- [ ] Run your Day 12 RAG pipeline on each question
- [ ] Score each result with RAGAS
- [ ] Print a summary table showing all scores
- [ ] Add the evaluation results table to your `day12-rag-chatbot` README
- [ ] Push the evaluation script to the same repo

---

### Day 14 (2026-06-26) — Advanced RAG: Cloud Vector DB + Better Retrieval

> **Status:** Not started


- [ ] Open [DL.AI: Advanced Retrieval for AI with Chroma](https://learn.deeplearning.ai/courses/advanced-retrieval-for-ai) and complete the full course (~2h)
- [ ] Understand these patterns: HyDE, multi-query retrieval, contextual compression, reranking
- [ ] Sign up for a [Pinecone free account](https://www.pinecone.io/)
- [ ] Run `pip install langchain-pinecone pinecone-client`
- [ ] Create a Pinecone index named `rag-demo`
- [ ] Reindex your PDF chunks into Pinecone using `PineconeVectorStore.from_documents()`
- [ ] Run the same queries you used with ChromaDB and compare results
- [ ] Pick one advanced retrieval pattern to implement: **HyDE** or **Multi-query**
- [ ] Add the chosen pattern to your retrieval step
- [ ] Push the Pinecone integration to your `day12-rag-chatbot` repo as a separate script

---

### Day 15 (2026-06-27) — RAG README + LinkedIn Post

> **Status:** Not started


- [ ] Open your `day12-rag-chatbot` README and write a clear problem statement
- [ ] Draw and add an architecture diagram using Mermaid syntax
- [ ] Write step-by-step installation instructions
- [ ] Add a `requirements.txt` to the repo
- [ ] Add instructions for how to run with any custom PDF
- [ ] Add the RAGAS evaluation results as a table
- [ ] Add a comparison section: ChromaDB vs. Pinecone — what you found
- [ ] Add a "What I'd improve next" section
- [ ] Take a screenshot of your chatbot working in the terminal
- [ ] Post on LinkedIn: *"I just built a RAG chatbot that answers questions about any PDF — here's the architecture..."*
- [ ] Attach the screenshot and your GitHub link to the post

---

### Day 16 (2026-06-28) — FastAPI: Serve Your RAG as a REST API

> **Status:** Not started


- [ ] Read [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) — focus on: path operations, request bodies, async endpoints, background tasks, StreamingResponse
- [ ] Understand: why `async/await` matters for LLM APIs (non-blocking = handles multiple users)
- [ ] Run `pip install fastapi uvicorn python-multipart`
- [ ] Create a new project folder `day16-rag-fastapi`
- [ ] Create `app.py` with a `FastAPI()` instance
- [ ] Create a `QueryRequest` Pydantic model with `question` and `top_k` fields
- [ ] Add `POST /ingest` endpoint — accepts a PDF upload, chunks, embeds, stores in ChromaDB
- [ ] Add `POST /query` endpoint — accepts a question, streams the RAG answer token by token
- [ ] Run the server: `uvicorn app:app --reload`
- [ ] Open `http://localhost:8000/docs` and test both endpoints in Swagger UI
- [ ] Push as `day16-rag-fastapi`
- [ ] Claim your **DL.AI Advanced RAG certificate**
- [ ] Claim your **DL.AI Building Systems with ChatGPT API certificate**

---
---

## 📅 PHASE 3 — Agents & Google Tools (Days 17–24)

---

### Day 17 (2026-06-29) — LangGraph Foundations Part 1

> **Status:** Not started


- [ ] Open [LangChain Academy: Intro to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) and complete Modules 1–2
- [ ] Understand: nodes = Python functions, edges = routing logic, state = shared TypedDict
- [ ] Run `pip install langgraph`
- [ ] Create a new project `day17-langgraph-basics`
- [ ] Define a state TypedDict with at least a `query` and `route` field
- [ ] Build a `classify` node — uses an LLM to decide: `simple` or `needs_search`
- [ ] Build a `simple_answer` node — LLM answers directly
- [ ] Build a `needs_search` node — placeholder that prints `"[Would search: {query}]"`
- [ ] Connect nodes with conditional edges based on the `classify` output
- [ ] Run `graph.get_graph().print_ascii()` to visualize the graph
- [ ] Test with 2 questions: one simple, one that needs search
- [ ] Push as `day17-langgraph-basics`

---

### Day 18 (2026-06-30) — LangGraph Agents + Tool Calling

> **Status:** Not started


- [ ] Open [LangChain Academy: Intro to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) and complete Modules 3–4
- [ ] Open [DL.AI: Functions, Tools & Agents](https://learn.deeplearning.ai/courses/functions-tools-agents-langchain) and complete the first half (~1.5h)
- [ ] Understand: `@tool` decorator, tool binding, ReAct loop, `ToolNode`
- [ ] Run `pip install duckduckgo-search langchain-community`
- [ ] Create a `web_search` tool using DuckDuckGo
- [ ] Create a `calculator` tool
- [ ] Create a `get_current_date` tool
- [ ] Build a ReAct agent in LangGraph that uses all 3 tools
- [ ] Add a print statement at each step (thought → tool call → observation → final answer)
- [ ] Test: *"How many days until the new year? What is 25% of that number?"*
- [ ] Verify the agent loops correctly until it reaches a final answer
- [ ] Push as `day18-research-agent`

---

### Day 19 (2026-07-01) — Advanced Agents + Human-in-the-Loop

> **Status:** Not started


- [ ] Open [LangChain Academy: Intro to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) and complete all remaining modules
- [ ] Claim your **LangChain Academy: Intro to LangGraph certificate**
- [ ] Open [DL.AI: Functions, Tools & Agents](https://learn.deeplearning.ai/courses/functions-tools-agents-langchain) and complete the remaining half
- [ ] Claim your **DL.AI Functions, Tools & Agents certificate**
- [ ] Understand: checkpointing and human-in-the-loop in LangGraph
- [ ] Open your `day18-research-agent` project
- [ ] Add a human approval step before every web search: *"About to search: '{query}'. Approve? (y/n)"*
- [ ] If `n`, make the agent skip the search and attempt a direct answer instead
- [ ] Test the approval flow with a question that would trigger a web search
- [ ] Push the update to `day18-research-agent`

---

### Day 20 (2026-07-02) — LLMOps: LangSmith Tracing

> **Status:** Not started


- [ ] Open [DL.AI: LLMOps](https://learn.deeplearning.ai/courses/llmops) and complete the full course (~2h)
- [ ] Sign up for a free [LangSmith account](https://smith.langchain.com)
- [ ] Get your LangSmith API key
- [ ] Add LangSmith env variables to your `.env` file: `LANGCHAIN_TRACING_V2`, `LANGCHAIN_API_KEY`, `LANGCHAIN_PROJECT`
- [ ] Connect LangSmith to your `day16-rag-fastapi` app
- [ ] Connect LangSmith to your `day18-research-agent`
- [ ] Run both apps and generate some traces
- [ ] Open the LangSmith UI and explore the traces
- [ ] Note the token count and cost per query in the LangSmith dashboard
- [ ] Take a screenshot of a trace in LangSmith
- [ ] Add the LangSmith trace screenshot to your `day12-rag-chatbot` README

---

### Day 21 (2026-07-03) — Google AI Studio Deep Dive

> **Status:** Not started


- [ ] Go to [Google AI Studio](https://aistudio.google.com/) and explore the UI
- [ ] Try setting a custom system instruction and see how it changes responses
- [ ] Try sending an image as input (multimodal) in the AI Studio playground
- [ ] Try the function calling UI in AI Studio
- [ ] Read the [Gemini API Python Quickstart](https://ai.google.dev/gemini-api/docs/quickstart?lang=python)
- [ ] Create a new project `day21-multimodal-analyzer`
- [ ] Write a script using the raw `google-generativeai` SDK (no LangChain)
- [ ] Accept an image path from the user as input
- [ ] Send the image to Gemini with the prompt: *"Describe this image and suggest 3 blog post titles about it"*
- [ ] Return a structured JSON response: `{"description": "...", "titles": ["...", "...", "..."]}`
- [ ] Export the result to a `.json` file automatically
- [ ] Test with at least 2 different images
- [ ] Push as `day21-multimodal-analyzer`

---

### Day 22 (2026-07-04) — Firebase Genkit (JavaScript) + Web Frontend

> **Status:** Not started


- [ ] Read [Firebase Genkit Getting Started (Node.js)](https://firebase.google.com/docs/genkit/get-started)
- [ ] Understand: Genkit flows = deployable AI functions with tracing and streaming built in
- [ ] Run `npm install -g firebase-tools`
- [ ] Create a new project folder `day22-firebase-ai-app`
- [ ] Run `firebase init` — select Hosting + Functions
- [ ] Run `npm install @genkit-ai/firebase @genkit-ai/googleai`
- [ ] Write a Genkit flow that accepts a topic and returns a blog post intro as JSON
- [ ] Test the flow locally using the Genkit dev UI
- [ ] Build a simple web frontend: HTML page with a text input and a "Generate" button
- [ ] Wire the frontend to call your Genkit flow via HTTP on button click
- [ ] Display the returned JSON result on the page
- [ ] Run `firebase deploy` to deploy to Firebase Hosting
- [ ] Confirm your app is live at its public Firebase URL
- [ ] Push everything as `day22-firebase-ai-app`

---

### Day 23 (2026-07-05) — Firestore Vector Search + Full-Stack RAG

> **Status:** Not started


- [ ] Read [Firestore Vector Search Docs](https://firebase.google.com/docs/firestore/vector-search)
- [ ] Understand: Firestore supports KNN vector queries natively — no separate vector DB needed
- [ ] Write a Python ingest script: chunk + embed a PDF → store embeddings in Firestore (GCP project `crypto-snow-426714-f1`)
- [ ] Run the ingest script and verify documents appear in Firestore console
- [ ] Update your Genkit flow: on "Generate", query Firestore with KNN vector search
- [ ] Pass the retrieved chunks to Gemini along with the user question
- [ ] Return the Gemini answer as a JSON response
- [ ] Update the web frontend to display retrieved source chunks alongside the answer
- [ ] Test the full flow end to end: ingest a PDF → ask a question → see answer + sources
- [ ] Push updates to `day22-firebase-ai-app`

---

### Day 24 (2026-07-06) — Connect Python FastAPI to Web Frontend

> **Status:** Not started


- [ ] Read [CORS in FastAPI](https://fastapi.tiangolo.com/tutorial/cors/)
- [ ] Open your `day16-rag-fastapi` project
- [ ] Add `CORSMiddleware` to your FastAPI app with `allow_origins=["*"]`
- [ ] Build a new web frontend (HTML/CSS/JS — use your web dev skills):
- [ ] Add a file upload button that calls `POST /ingest` on your FastAPI backend
- [ ] Add a chat text input that calls `POST /query` on submit
- [ ] Stream the RAG response token by token into the chat UI
- [ ] Style it to look clean and professional
- [ ] Run FastAPI locally (`uvicorn app:app --reload`) and open the HTML page
- [ ] Test the full flow: upload a PDF → ask a question → read the streamed answer
- [ ] Record a short screen capture of the full demo (upload + question + answer)
- [ ] Push the frontend HTML/CSS/JS files to your `day16-rag-fastapi` repo

---
---

## 📅 PHASE 4 — Deploy, Certify & Showcase (Days 25–30)

---

### Day 25 (2026-07-07) — Docker Basics + Cloud Run Deployment

> **Status:** Not started


- [ ] Watch [Docker in 100 Seconds — Fireship](https://www.youtube.com/watch?v=Gjnup-PuquQ) (2 min)
- [ ] Watch [Docker Tutorial for Beginners — TechWorld with Nana](https://www.youtube.com/watch?v=3c-iBn73dDE) (~45 min — watch until "running a container")
- [ ] Read [Cloud Run Python Quickstart](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)
- [ ] Install Docker Desktop on your machine
- [ ] Open your `day16-rag-fastapi` project
- [ ] Create a `Dockerfile` with: base image `python:3.11-slim`, copy `requirements.txt`, install deps, copy app, expose 8080, run uvicorn
- [ ] Build the Docker image: `docker build -t rag-api .`
- [ ] Run the container locally: `docker run -p 8080:8080 rag-api`
- [ ] Test the containerized app at `http://localhost:8080/docs`
- [ ] Deploy to Google Cloud Run: `gcloud run deploy rag-api --source . --region us-central1 --allow-unauthenticated`
- [ ] Copy and save your permanent Cloud Run public HTTPS URL
- [ ] Test the live deployed URL
- [ ] Add the live URL to your `day16-rag-fastapi` README

---

### Day 26 (2026-07-08) — Google Developer Profile + Certificates

> **Status:** Not started


- [ ] Go to [me.developers.google.com](https://me.developers.google.com/) and complete your profile (fill all fields)
- [ ] Link your GitHub account on the Google Developer Profile
- [ ] Go to [skills.google](https://www.skills.google/) and complete the Generative AI learning path
- [ ] Enroll in [Google AI Essentials on Coursera](https://www.coursera.org/google-certificates/google-ai) (audit = free)
- [ ] Start and make progress on the Google AI Essentials course
- [ ] Go to LinkedIn → Licenses & Certifications and add every certificate earned so far
- [ ] Activate [NotebookLM](https://notebooklm.google/)
- [ ] Upload this roadmap file to NotebookLM as a source
- [ ] Upload your project READMEs to NotebookLM as sources
- [ ] Explore asking NotebookLM questions about your own learning journey

---

### Day 27 (2026-07-09) — GitHub Portfolio Polish

> **Status:** Not started


- [ ] Go through each project repo from the 30 days
- [ ] For each repo: write or update the README with a clear problem statement
- [ ] For each repo: add an architecture diagram (Mermaid or image)
- [ ] For each repo: add step-by-step setup and installation instructions
- [ ] For each repo: add a screenshot or GIF of the working app
- [ ] For each repo: add tech stack badges from [shields.io](https://shields.io/)
- [ ] For each repo: add a "What I learned" section
- [ ] For each repo: add a "What I'd improve next" section
- [ ] Pin your 3 best projects on your GitHub profile page
- [ ] Write a GitHub profile README with a short bio: position yourself as an "AI Application Engineer"
- [ ] Review all repos are public and have a license file

---

### Day 28 (2026-07-10) — LinkedIn & Personal Branding

> **Status:** Not started


- [ ] Update LinkedIn headline to: "AI Application Developer | Python · LangChain · RAG"
- [ ] Rewrite your LinkedIn About section (see roadmap for exact template)
- [ ] Add all AI skills to LinkedIn: LangChain, LangGraph, RAG, FastAPI, Pydantic, Gemini API, OpenAI API, ChromaDB, Pinecone, LangSmith, Firebase, Vector Databases, Python, Prompt Engineering
- [ ] Add your RAG chatbot to the LinkedIn Featured section (screenshot or video + deployed URL)
- [ ] Write one LinkedIn post (300–400 words):
  - [ ] Hook: *"I just built a chatbot that answers questions about ANY PDF — and deployed it live. Here's the exact tech stack..."*
  - [ ] Explain the 8-step RAG pipeline in plain language
  - [ ] Attach your architecture diagram and a screenshot
  - [ ] Close with a link to your GitHub
- [ ] Publish the post

---

### Day 29 (2026-07-11) — Interview Prep: Talk Through Your Stack

> **Status:** Not started


- [ ] Set a timer and answer out loud: *"What is an embedding? Why is cosine similarity used instead of Euclidean distance for text?"*
- [ ] Set a timer and answer out loud: *"What is the difference between fine-tuning and RAG? When do you choose each?"*
- [ ] Set a timer and answer out loud: *"What is temperature? What does top-p do? What is a context window?"*
- [ ] Set a timer and answer out loud: *"What are hallucinations and what are 3 ways to reduce them?"*
- [ ] Set a timer and answer out loud: *"Walk me through a RAG pipeline end to end, step by step"*
- [ ] Set a timer and answer out loud: *"What is chunk size and why does the chunking strategy matter?"*
- [ ] Set a timer and answer out loud: *"What is RAGAS and what metrics does it measure?"*
- [ ] Set a timer and answer out loud: *"What is HyDE and when is it useful?"*
- [ ] Set a timer and answer out loud: *"What is the difference between ChromaDB and Pinecone?"*
- [ ] Set a timer and answer out loud: *"What is LCEL? What does the | operator do?"*
- [ ] Set a timer and answer out loud: *"What is the difference between a chain and an agent?"*
- [ ] Set a timer and answer out loud: *"What is LangGraph? What is a node, an edge, and state?"*
- [ ] Set a timer and answer out loud: *"What is human-in-the-loop in LangGraph?"*
- [ ] Set a timer and answer out loud: *"Why do we use async/await in a FastAPI AI endpoint?"*
- [ ] Set a timer and answer out loud: *"What is Pydantic and why is it important for LLM outputs?"*
- [ ] Set a timer and answer out loud: *"How do you trace and monitor LLM calls? What is LangSmith?"*
- [ ] Set a timer and answer out loud: *"What is Docker and why is it useful for deploying AI services?"*
- [ ] Record yourself answering 3 of the hardest questions above
- [ ] Watch the recording back and identify what to improve

---

### Day 30 (2026-07-12) — Final Review + Celebration 🎉

> **Status:** Not started


- [ ] Do a live demo check: demo your RAG chatbot → FastAPI → deployed Cloud Run URL in under 3 minutes
- [ ] If anything breaks during the demo, fix it now
- [ ] Do a final README pass on your top 3 repos — fix any gaps
- [ ] Write a personal note in your `ai-engineering-journey` README: what you built, what you learned, what's next
- [ ] Post a "Day 30" LinkedIn update
- [ ] Decide your next project — pick one:
  - [ ] Multi-agent workflow: one agent researches, one writes, one reviews
  - [ ] Structured document extraction: LLM extracts JSON from PDFs using Pydantic + `instructor`
  - [ ] Persistent memory chatbot: long-term user memory stored in a database
- [ ] Write a brief plan for your chosen next project in a new file

---
---

## 📋 WEEKLY SUMMARIES

---

### ✅ Week 1 Complete — Python for AI Foundations (Days 1–6)

- [ ] `hello_gemini.py` — first Gemini API call working
- [ ] `day2-embeddings-scratch` — cosine similarity with NumPy pushed to GitHub
- [ ] `day3-pandas-basics` — Titanic decision tree pushed to GitHub
- [ ] `day4-prompt-engineering` — CLI assistant with intent routing pushed to GitHub
- [ ] `day5-llm-pipeline-cli` — 4-step LLM pipeline pushed to GitHub
- [ ] `day6-hf-vs-gemini` — HF vs Gemini comparison pushed to GitHub
- [ ] 3 certificates claimed: Kaggle Pandas, Kaggle Intro to ML, DL.AI Prompt Engineering
- [ ] All Week 1 READMEs written
- [ ] LinkedIn post published: Week 1 update

---

### ✅ Week 2 Complete — LangChain, RAG & FastAPI (Days 7–16)

- [ ] `day7-langchain-intro` — LCEL chain working
- [ ] `day8-langchain-classifier` — Pydantic structured output working
- [ ] `day9-memory-chatbot` — multi-turn chatbot with memory working
- [ ] `day10-rag-chunking` — PDF loading and chunking script done
- [ ] `day11-vector-store` — ChromaDB vector store with similarity search working
- [ ] `day12-rag-chatbot` — full RAG pipeline with terminal interface working ⭐
- [ ] `day13-ragas-eval` — RAGAS evaluation scores printed in table
- [ ] `day14-advanced-rag` — Pinecone + one advanced retrieval pattern working
- [ ] `day15-rag-readme` — full README for flagship project written + LinkedIn post
- [ ] `day16-rag-fastapi` — FastAPI serving RAG via REST with streaming working
- [ ] 4 certificates claimed: LangChain Academy, DL.AI Chat with Data, Advanced RAG, Building Systems
- [ ] LinkedIn post published: RAG chatbot showcase

---

### ✅ Week 3 Complete — Agents & Google Tools (Days 17–24)

- [ ] `day17-langgraph-basics` — 3-node LangGraph with conditional routing working
- [ ] `day18-research-agent` — ReAct agent with 3 tools working
- [ ] `day19-human-in-loop` — approval checkpoint added to agent
- [ ] `day20-langsmith` — LangSmith tracing connected to RAG API + agent
- [ ] `day21-multimodal-analyzer` — image → Gemini → structured JSON working
- [ ] `day22-firebase-ai-app` — Genkit flow + web frontend deployed to Firebase Hosting
- [ ] `day23-firestore-rag` — full-stack RAG: Python ingest → Firestore → Genkit → frontend
- [ ] `day24-web-ui` — FastAPI RAG + streaming web chat UI working
- [ ] 3 certificates claimed: LangGraph, Functions/Tools/Agents, LLMOps
- [ ] Screen recording of full Day 24 demo saved

---

### ✅ Week 4 Complete — Deploy, Certify & Showcase (Days 25–30)

- [ ] `day25-docker` — RAG API containerized and deployed to Google Cloud Run
- [ ] Public Cloud Run URL is live and working
- [ ] Google Developer Profile completed and GitHub linked
- [ ] skills.google Generative AI learning path completed
- [ ] Google AI Essentials (Coursera) enrolled and started
- [ ] All certificates added to LinkedIn
- [ ] All GitHub project READMEs polished with diagrams, badges, and screenshots
- [ ] LinkedIn profile fully updated (headline, about, skills, featured, post)
- [ ] All interview questions practiced out loud and recorded
- [ ] Day 30 LinkedIn post published
- [ ] Next project chosen and planned

---
---

## 🏁 PHASE MILESTONES

---

### 🐍 Phase 1 Done — Python for AI Foundations
> **Complete when:** All 6 Day-checklist boxes above are fully checked AND all 9 Week 1 summary boxes are checked.

**You can now:**
- Call the Gemini and OpenAI APIs from Python
- Work with embeddings and cosine similarity
- Load, clean, and analyze data with Pandas
- Apply prompt engineering patterns (zero-shot, few-shot, chain-of-thought)
- Build multi-step LLM pipelines with validation
- Run open-source models via Hugging Face `pipeline()`

---

### 🧠 Phase 2 Done — LLMs, LangChain, RAG & FastAPI
> **Complete when:** All 10 Day-checklist boxes for Days 7–16 are fully checked AND all 10 Week 2 summary boxes are checked.

**You can now:**
- Build LCEL chains and Pydantic-validated LLM pipelines
- Build a complete RAG system from PDF to streamed answer
- Use ChromaDB and Pinecone for vector storage
- Evaluate RAG quality with RAGAS
- Serve AI features as async REST APIs with FastAPI

---

### 🤖 Phase 3 Done — Agents & Google Tools
> **Complete when:** All 8 Day-checklist boxes for Days 17–24 are fully checked AND all 8 Week 3 summary boxes are checked.

**You can now:**
- Build stateful agentic workflows with LangGraph
- Implement the ReAct pattern with custom tools
- Add human-in-the-loop approval to agents
- Trace and monitor LLM calls with LangSmith
- Build full-stack Firebase + Genkit AI apps with a web frontend

---

### 🚢 Phase 4 Done — Deploy, Certify & Showcase
> **Complete when:** All 6 Day-checklist boxes for Days 25–30 are fully checked AND all 11 Week 4 summary boxes are checked.

**You can now:**
- Containerize AI services with Docker
- Deploy to Google Cloud Run with a permanent HTTPS URL
- Present a complete GitHub portfolio with polished READMEs
- Talk confidently through your full stack in an interview
- Claim the title: **Junior AI Application Engineer** ✅

---

> 🎉 **All 4 phases done = 30-Day Roadmap Complete.**
> You built real things. You have receipts. Go get hired.
