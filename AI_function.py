from dotenv import load_dotenv
from openai import OpenAI
import json
import re
import os


load_dotenv()


client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
You are an AI assistant that responds in STRICT JSON format.

Rules:
- Return EXACTLY ONE JSON object per response.
- Do NOT include any text outside JSON.
- Allowed steps: START, PLAN, OUTPUT.
- PLAN steps must be returned ONE AT A TIME.
- After OUTPUT, stop responding.

JSON FORMAT:
{
  "step": "START | PLAN | OUTPUT",
  "content": "string"
}
"""

def extract_json(text):
    """
    Safely extract ONE JSON object from the model response.
    """
    match = re.search(r'\{[^{}]*\}', text, re.DOTALL)
    if not match:
        raise ValueError("No valid JSON found")
    return json.loads(match.group())

print("\n--- AI Assistant Started ---\n")


message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


user_query = input("👉 ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    print("RAW RESULT:", raw_result)

    
    if raw_result is None:
        print("⚠️ Model returned no content. Stopping.")
        break

    message_history.append({"role": "assistant", "content": raw_result})

    try:
        parsed_result = extract_json(raw_result)
    except Exception as e:
        print("❌ JSON Parsing Error:", e)
        break

    step = parsed_result.get("step")
    content = parsed_result.get("content")

    if step == "START":
        print("🚀", content)
        message_history.append({
            "role": "user",
            "content": "Proceed to the next step."
        })
        continue

    if step == "PLAN":
        print("🧠", content)
        message_history.append({
            "role": "user",
            "content": "Continue to the next step."
        })
        continue

    if step == "OUTPUT":
        print("🤖", content)
        break

print("\n--- Session Ended ---\n")
