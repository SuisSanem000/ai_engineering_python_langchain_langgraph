"""
Day 1 — hello_openai.py

Calls the OpenAI API using the official Python client.
Note the structural difference vs Gemini:
  - OpenAI uses a chat completions interface (messages array) as its primary API.
  - Gemini uses generate_content() with an optional system_instruction kwarg.
Both converge on the same LangChain abstraction (ChatOpenAI / ChatGoogleGenerativeAI)
from Day 7 onward — which is the whole point of an orchestration layer.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT = "What is an LLM? Explain in exactly 3 bullet points."

# OpenAI Client endpoint execution. Note the structural requirements:
# 1. API Call: client.chat.completions.create is the standard endpoint.
# 2. Messages Array: A list of dict payloads representing sequential conversation turns.
# 3. Roles: "system" defines instruction behavior; "user" passes the current prompt.
response = client.chat.completions.create(
    model="gpt-4o-mini",   # cheapest capable OpenAI model — ideal for learning exercises
    messages=[
        {
            "role": "system",
            "content": (
                "You are a concise technical explainer. "
                "Use bullet points and plain language. Avoid padding."
            ),
        },
        {"role": "user", "content": PROMPT},
    ],
    temperature=0.3,        # controls randomness: 0.0 is deterministic, 1.0 is creative. 0.3 ensures factual stability.
    max_tokens=300,         # hard cut-off limit on generated tokens to manage API cost exposure.
)

print("=" * 50)
print("Model : gpt-4o-mini")
print("Prompt:", PROMPT)
print("=" * 50)
print(response.choices[0].message.content)
print()
# Usage — OpenAI charges per token; always log this in dev
usage = response.usage
print(f"[Token usage] prompt={usage.prompt_tokens} "
      f"| output={usage.completion_tokens} "
      f"| total={usage.total_tokens}")
