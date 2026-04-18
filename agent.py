import requests
import json
import re

def process_email(email_text):
    prompt = f"""
You are a highly intelligent AI assistant.

Analyze the email carefully and extract meaningful information.

Return ONLY valid JSON in this format:

{{
  "summary": "clear and short summary in your own words",
  "intent": "choose one: meeting / request / information",
  "priority": "choose one: high / medium / low",
  "tasks": ["list ALL actionable tasks clearly"],
  "reply": "write a complete professional email reply"
}}

IMPORTANT RULES:
- DO NOT copy the email text directly
- Understand and rewrite the summary
- Extract ALL tasks (not partial)
- Tasks must be a proper JSON list of strings
- Reply must be realistic and professional
- DO NOT return placeholder text like "text"
- DO NOT add anything outside JSON

Email:
{email_text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    text = response.json()["response"]

    try:
        # Extract JSON from response (even if extra text exists)
        json_text = re.search(r"\{.*\}", text, re.DOTALL).group()
        return json.loads(json_text)
    except Exception as e:
        return {"error": str(e), "raw": text}