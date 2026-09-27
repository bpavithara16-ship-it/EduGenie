"""
learning_path.py
------------------
Generates a structured, personalized learning path (beginner to
advanced) for any topic the learner requests, using Gemini 1.5 Pro.
"""

import os
import traceback
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")


def get_learning_recommendations(topic):
    prompt = f"""
You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics, order of learning, and resources (videos, articles, or books).
Include beginner, intermediate, and advanced levels if needed.
"""
    try:
        response = model.generate_content(prompt)
        print("🧠 Gemini raw response:", response)

        if hasattr(response, "text"):
            return response.text
        elif hasattr(response, "parts") and response.parts:
            return response.parts[0].text
        else:
            return "❌ Could not extract content from Gemini response."
    except Exception as e:
        traceback.print_exc()  # ✅ This gives full error trace
        return f"❌ Error occurred: {str(e)}"
