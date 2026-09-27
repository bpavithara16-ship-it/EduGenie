"""
quiz_module.py
---------------
Generates 3 multiple-choice questions (4 options each) from a passage
of text, using Gemini 1.5 Pro. Output is returned as a Python list of
dicts (parsed from the model's JSON response).
"""

import os
import re
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def clean_json_block(text):
    """Remove Markdown ```json code fences if the model wraps its output in them."""
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()


def generate_quiz(text: str) -> list:
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

        prompt = f"""
You are a quiz generator.

From the following passage, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON**, like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{text}
"""
        response = model.generate_content(prompt)
        quiz_text = response.text.strip()

        # Clean markdown code blocks if any
        cleaned_text = clean_json_block(quiz_text)

        quiz_list = json.loads(cleaned_text)
        return quiz_list

    except Exception as e:
        return [{"error": f"⚠️ Error generating quiz: {e}"}]
