"""
Day 1 — hello_gemini.py

Calls the Gemini API directly using the google-generativeai SDK.
Architectural note: we use the SDK directly here (no LangChain abstraction)
so you learn the raw API surface first. LangChain wraps this same interface
starting Day 7 — understanding the layer beneath it matters.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # loads GEMINI_API_KEY from ../.env (root) or local .env

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Model selection: gemini-2.0-flash is the fast/cheap model — ideal for dev.
# gemini-1.5-pro has a larger context window (1M tokens) for longer docs.
# Architectural detail: system_instruction is passed at model instantiation rather than per-call.
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=(
        "You are a concise technical explainer. "
        "Use bullet points and plain language. Avoid padding."
    ),
)

PROMPT = "What is an LLM? Explain in exactly 3 bullet points."

# Calling the generate_content API endpoint (HTTP POST payload)
response = model.generate_content(PROMPT)

print("=" * 50)
print("Model : gemini-2.0-flash")
print("Prompt:", PROMPT)
print("=" * 50)
print(response.text)
print()
# Token usage detail: Google's SDK exposes usage_metadata on the response object.
# We access prompt_token_count, candidates_token_count, and total_token_count to track API cost metrics.
print(f"[Token usage] prompt={response.usage_metadata.prompt_token_count} "
      f"| output={response.usage_metadata.candidates_token_count} "
      f"| total={response.usage_metadata.total_token_count}")

