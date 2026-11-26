# DriveReady OPC 2026 – Day 2

## Project: CampusMate – AI Student Learning Assistant

**LLM:** Google Gemini 2.5 Flash

### 1. Overview
CampusMate is an AI-powered student learning assistant designed to help college students with academic questions, study planning, quizzes, assignments, and study-time management.

It uses Google Gemini API and LangChain to provide interactive and personalized assistance.

### 2. Features
1. **Conversational AI Assistant:** Answers academic questions and maintains conversation history.
2. **Student Query Classification:** Classifies queries into Academic, Study Planning, Assignment, Campus, or Other.
3. **Personalized Study Plan:** Generates a day-wise study timetable based on available time and topics.
4. **Practice Quiz Generator:** Creates multiple-choice questions with answers and explanations.
5. **Assignment Information Extraction:** Extracts subject, assignment title, deadline, and priority in JSON format.
6. **Study Hours Calculator:** Calculates total available study hours.

### 3. Technologies Used
- Python
- Google Gemini 2.5 Flash API
- LangChain
- Google Colab

### 4. Installation

Install the required dependencies:

```bash
pip install -U langchain-google-genai langchain-core
```

### 5. API Configuration

Set your Google Gemini API key using:

- **Google Colab:** Add `GOOGLE_API_KEY` in the Secrets panel.
- **Local System:** Set `GOOGLE_API_KEY` as an environment variable.

### 6. How to Run

Run the Python file:

```bash
python Day-2.py
```

Choose an option from the interactive menu to use the available features.

### 7. Learning Outcomes
- Understanding LLM integration using Gemini API.
- Working with LangChain prompts and chains.
- Implementing conversational memory.
- Using AI for student-related tasks.
- Extracting structured information using LLMs.

### 8. Conclusion
CampusMate demonstrates how Large Language Models can be used to build a helpful AI assistant that supports students in their everyday academic activities.
