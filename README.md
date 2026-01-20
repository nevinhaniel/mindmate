🧠 MindMate AI

MindMate AI is a full-stack Generative AI agent that helps users reflect on their emotional state and receive supportive, non-medical guidance.
The system is built using FastAPI and Pydantic AI, with a clean REST API and a simple frontend interface.

🚀 Features

Accepts free-text user input about mood or feelings

Uses a Generative AI agent to analyze emotional context

Returns:

Detected emotion

Short emotional summary

Supportive advice

Strict response validation using Pydantic models

Defensive parsing and fallback handling for LLM output reliability

Interactive API documentation via Swagger UI

🛠 Tech Stack
Backend

Python 3.11

FastAPI

Pydantic

Pydantic-AI

OpenRouter (LLM provider)

Uvicorn

Frontend

HTML

CSS

JavaScript (Fetch API)

📂 Project Structure
MindMate_AI/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── backend/
    ├── main.py
    ├── agent.py
    ├── models.py
    └── requirements.txt

⚙️ How It Works

User submits a mood description from the frontend

Frontend sends a POST request to the FastAPI backend

Pydantic AI agent processes the input using an LLM

The agent response is parsed and validated using Pydantic schemas

A structured JSON response is returned to the frontend

▶️ Running the Project Locally
1️⃣ Backend Setup
cd backend
pip install -r requirements.txt


Set the OpenRouter API key (Windows):

setx OPENROUTER_API_KEY "your_api_key_here"


Restart the terminal, then run:

uvicorn main:app --reload


Backend will run at:

http://127.0.0.1:8000

2️⃣ API Testing

Open in browser:

http://127.0.0.1:8000/docs


Use the /analyze endpoint to test the API.

3️⃣ Frontend Setup

Open frontend/script.js

Update the backend URL:

fetch("http://127.0.0.1:8000/analyze", {


Open index.html in a browser

🔐 Security & Configuration

API keys are stored in environment variables

No secrets are hard-coded or committed to the repository

Follows secure configuration best practices
