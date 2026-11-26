import json
import os
from typing import Optional

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_agent


# ---------------------------------------------------------------------
# 1. GEMINI API CONFIGURATION
# ---------------------------------------------------------------------

def load_api_key() -> str:
    """Load the API key from Colab Secrets or an environment variable."""
    try:
        from google.colab import userdata
        key = userdata.get("GOOGLE_API_KEY")
        if key:
            return key
    except Exception:
        pass

    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        raise EnvironmentError(
            "GOOGLE_API_KEY not found. Add it to Google Colab Secrets "
            "or set it as an environment variable."
        )
    return key


os.environ["GOOGLE_API_KEY"] = load_api_key()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
)


# ---------------------------------------------------------------------
# 2. TOOLS BASED ON DAY-2 CAMPUSMATE USE CASES
# ---------------------------------------------------------------------

@tool
def classify_student_query(message: str) -> str:
    """Classify a student message as ACADEMIC, STUDY_PLANNING, ASSIGNMENT, CAMPUS, or OTHER."""
    prompt = f"""
Classify the following student message into exactly one category:
ACADEMIC, STUDY_PLANNING, ASSIGNMENT, CAMPUS, or OTHER.
Return only the category name.

Message: {message}
"""
    result = llm.invoke(prompt).content
    category = str(result).strip().upper()
    allowed = {"ACADEMIC", "STUDY_PLANNING", "ASSIGNMENT", "CAMPUS", "OTHER"}
    return category if category in allowed else "OTHER"


@tool
def create_study_plan(subject: str, topics: str, days: int, hours_per_day: float) -> str:
    """Create a day-wise study plan using the subject, topics, available days, and daily study hours."""
    if days <= 0 or hours_per_day <= 0:
        return "Days and study hours must be greater than zero."

    prompt = f"""
Create a realistic day-wise study plan for a college student.
Include focused study sessions, short breaks, revision, and practice.
Do not exceed the available study hours per day.

Subject: {subject}
Topics: {topics}
Days available: {days}
Study hours per day: {hours_per_day}
"""
    return str(llm.invoke(prompt).content)


@tool
def generate_practice_quiz(topic: str, number_of_questions: int, difficulty: str) -> str:
    """Generate multiple-choice practice questions with four options, answers, and explanations."""
    if number_of_questions <= 0:
        return "Number of questions must be greater than zero."

    prompt = f"""
Create {number_of_questions} multiple-choice questions about {topic}.
Difficulty: {difficulty}
Give four options (A, B, C, D) for every question.
Provide the correct answer and a short explanation after each question.
"""
    return str(llm.invoke(prompt).content)


@tool
def extract_assignment_details(message: str) -> str:
    """Extract assignment subject, title, deadline, and priority from a student's description as JSON."""
    prompt = f"""
Extract assignment information from the message below.
Return valid JSON only with these keys:
subject, assignment_title, deadline, priority.
Use null for missing information.
Priority must be High, Medium, Low, or null.
Do not guess missing details.

Message: {message}
"""
    response = str(llm.invoke(prompt).content).strip()

    if response.startswith("```"):
        response = response.replace("```json", "", 1)
        response = response.replace("```", "").strip()

    try:
        parsed = json.loads(response)
        keys = ("subject", "assignment_title", "deadline", "priority")
        return json.dumps({key: parsed.get(key) for key in keys}, indent=2)
    except json.JSONDecodeError:
        return response


@tool
def calculate_total_study_hours(days: int, hours_per_day: float) -> str:
    """Calculate total available study hours from the number of days and hours per day."""
    if days < 0 or hours_per_day < 0:
        return "Days and hours cannot be negative."

    total = round(days * hours_per_day, 2)
    return f"Total available study time: {total} hours."


# ---------------------------------------------------------------------
# 3. CREATE CAMPUSMATE AGENT
# ---------------------------------------------------------------------

SYSTEM_PROMPT = """
You are CampusMate, an agentic AI learning assistant for college students.

Help students with:
- Academic questions and simple explanations.
- Study planning and exam preparation.
- Practice quizzes.
- Assignment organization.
- Study-hour calculations.
- General campus and student productivity questions.

Use the available tools whenever a request matches their purpose.
For ordinary academic questions, answer clearly and simply.
Ask follow-up questions when required tool inputs are missing.
Never invent college-specific rules, marks, dates, or deadlines.
Explain tool results in a friendly and student-friendly way.
"""

tools = [
    classify_student_query,
    create_study_plan,
    generate_practice_quiz,
    extract_assignment_details,
    calculate_total_study_hours,
]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
)


# ---------------------------------------------------------------------
# 4. CONVERSATION LOOP
# ---------------------------------------------------------------------

def run_campusmate() -> None:
    """Run CampusMate and retain conversation messages during the session."""
    messages = []

    print("\n============================================")
    print("       CAMPUSMATE – AGENTIC AI ASSISTANT")
    print("============================================")
    print("Ask academic questions or request any Day-2 feature.")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("CampusMate: Happy learning. Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        messages.append({"role": "user", "content": question})

        try:
            result = agent.invoke({"messages": messages})
            messages = result["messages"]

            # Display the latest assistant response.
            for message in reversed(messages):
                if getattr(message, "type", "") == "ai" and message.content:
                    content = message.content
                    if isinstance(content, list):
                        content = " ".join(
                            str(part.get("text", "")) if isinstance(part, dict)
                            else str(part)
                            for part in content
                        )
                    print("\nCampusMate:", content, "\n")
                    break

        except Exception as error:
            print("\nAn error occurred:", error)
            # Remove the failed user message so the next turn can continue.
            if messages and messages[-1].get("role") == "user":
                messages.pop()


# ---------------------------------------------------------------------
# 5. MAIN
# ---------------------------------------------------------------------

if __name__ == "__main__":
    run_campusmate()
