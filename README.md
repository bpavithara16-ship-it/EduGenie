# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant that helps students:
- Ask questions and get concise answers
- Understand complex concepts through simple explanations
- Generate quizzes from any topic or passage
- Get personalized, structured learning paths
- Summarize long educational text

Built with **FastAPI** (backend) + **HTML/CSS/JS** (frontend), powered by **Gemini 1.5 Pro** (cloud) and **LaMini-Flan-T5-783M** (local, CPU-friendly).

## Folder Structure
```
EduGenie/
├── main.py                  # FastAPI app & routes
├── explanation_module.py    # Concept explanation (local model)
├── qna.py                   # Question answering (Gemini)
├── quiz_module.py           # Quiz generation (Gemini)
├── summary_module.py        # Summarization (Gemini)
├── learning_path.py         # Learning path recommendations (Gemini)
├── templates/
│   └── index.html           # Frontend page
├── static/
│   └── style.css            # Styling
├── requirements.txt
├── .env.example
└── .gitignore
```

## Setup

1. Install Python 3.10+.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
5. Copy `.env.example` to `.env` and paste your key:
   ```bash
   cp .env.example .env
   ```

## Run

```bash
uvicorn main:app --reload
```

Open **http://127.0.0.1:8000** in your browser.

## Test

Try each feature from the web page: ask a question, get an explanation, summarize a paragraph, generate a quiz, and get a learning path.

## Future Enhancements
Voice interaction, multilingual support, mobile app, progress dashboards, gamification, LMS integration.

---
