import json
import os
from typing import Any

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser


# ---------------------------------------------------------------------
# 1. GEMINI API CONFIGURATION
# ---------------------------------------------------------------------

def load_api_key() -> str:
    """Load the Gemini API key from Colab Secrets or environment variables."""
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
    temperature=0.3,
)

parser = StrOutputParser()


# ---------------------------------------------------------------------
# 2. CAMPUSMATE AI STUDENT ASSISTANT WITH CONVERSATION MEMORY
# ---------------------------------------------------------------------

SYSTEM_PROMPT = """
You are CampusMate, a friendly AI learning assistant for college students.

You can:
- Explain academic topics in simple language.
- Give examples for difficult concepts.
- Help students organize assignments and exam preparation.
- Suggest practical study and revision techniques.
- Answer general student productivity questions.

Rules:
- Do not invent college-specific rules, dates, marks, or deadlines.
- If important information is missing, ask a short follow-up question.
- Keep answers clear, accurate, and student-friendly.
- Use bullet points when they make an answer easier to understand.
"""

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

chat_chain = chat_prompt | llm | parser
conversation_history: list[tuple[str, str]] = []


def ask_campusmate(question: str) -> str:
    """Answer a student question and remember recent conversation turns."""
    answer = chat_chain.invoke({
        "history": conversation_history[-10:],
        "question": question,
    })

    conversation_history.extend([
        ("human", question),
        ("ai", answer),
    ])
    return answer


# ---------------------------------------------------------------------
# 3. STUDENT QUERY CLASSIFICATION
# ---------------------------------------------------------------------

classification_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Classify the student's message into exactly one category:
ACADEMIC, STUDY_PLANNING, ASSIGNMENT, CAMPUS, or OTHER.
Return only the category name, without explanation."""
    ),
    ("human", "{message}"),
])

classification_chain = classification_prompt | llm | parser


def classify_query(message: str) -> str:
    """Classify a student query into one predefined category."""
    result = classification_chain.invoke({"message": message}).strip().upper()
    allowed = {"ACADEMIC", "STUDY_PLANNING", "ASSIGNMENT", "CAMPUS", "OTHER"}
    return result if result in allowed else "OTHER"


# ---------------------------------------------------------------------
# 4. PERSONALIZED STUDY PLAN GENERATOR
# ---------------------------------------------------------------------

study_plan_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Create a realistic day-wise study plan for a college student.
Include focused study sessions, short breaks, revision, and practice.
Do not schedule more study hours than the student has available."""
    ),
    (
        "human",
        """Subject: {subject}
Topics to cover: {topics}
Days available: {days}
Study hours per day: {hours}

Prepare a practical day-wise study plan."""
    ),
])

study_plan_chain = study_plan_prompt | llm | parser


def generate_study_plan(
    subject: str,
    topics: str,
    days: int,
    hours: float,
) -> str:
    """Generate a study plan using the student's available time."""
    if days <= 0 or hours <= 0:
        raise ValueError("Days and study hours must be greater than zero.")

    return study_plan_chain.invoke({
        "subject": subject,
        "topics": topics,
        "days": days,
        "hours": hours,
    })


# ---------------------------------------------------------------------
# 5. PRACTICE QUIZ GENERATOR
# ---------------------------------------------------------------------

quiz_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Create multiple-choice practice questions on the given topic.
Each question must have four options (A, B, C, D).
Provide the correct answer and a short explanation after each question.
Match the requested difficulty level."""
    ),
    (
        "human",
        """Topic: {topic}
Number of questions: {count}
Difficulty: {difficulty}

Generate the quiz."""
    ),
])

quiz_chain = quiz_prompt | llm | parser


def generate_quiz(topic: str, count: int, difficulty: str) -> str:
    """Generate a multiple-choice quiz for a student."""
    if count <= 0:
        raise ValueError("Number of questions must be greater than zero.")

    return quiz_chain.invoke({
        "topic": topic,
        "count": count,
        "difficulty": difficulty,
    })


# ---------------------------------------------------------------------
# 6. ASSIGNMENT INFORMATION EXTRACTION
# ---------------------------------------------------------------------

assignment_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Extract assignment information from the student's message.
Return valid JSON only with these keys:
subject, assignment_title, deadline, priority.
Use null for details that are not provided.
Priority must be High, Medium, Low, or null.
Do not guess missing information."""
    ),
    ("human", "{message}"),
])

assignment_chain = assignment_prompt | llm | parser


def extract_assignment_details(message: str) -> dict[str, Any]:
    """Extract assignment details and return them as a Python dictionary."""
    response = assignment_chain.invoke({"message": message}).strip()

    if response.startswith("```"):
        response = response.replace("```json", "", 1)
        response = response.replace("```", "").strip()

    details = json.loads(response)
    keys = ("subject", "assignment_title", "deadline", "priority")
    return {key: details.get(key) for key in keys}


# ---------------------------------------------------------------------
# 7. STUDY-HOUR CALCULATOR
# ---------------------------------------------------------------------

def calculate_study_hours(days: int, hours_per_day: float) -> float:
    """Calculate the total available study hours."""
    if days < 0 or hours_per_day < 0:
        raise ValueError("Days and hours cannot be negative.")

    return round(days * hours_per_day, 2)


# ---------------------------------------------------------------------
# 8. INTERACTIVE APPLICATION MENU
# ---------------------------------------------------------------------

def main() -> None:
    print("\n========================================")
    print("       CAMPUSMATE – AI STUDY ASSISTANT")
    print("========================================")

    while True:
        print("\nChoose an option:")
        print("1. Chat with CampusMate")
        print("2. Classify a student query")
        print("3. Generate a personalized study plan")
        print("4. Generate a practice quiz")
        print("5. Extract assignment details")
        print("6. Calculate total study hours")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        try:
            if choice == "1":
                question = input("\nAsk your question: ").strip()
                if question:
                    print("\nCampusMate:", ask_campusmate(question))

            elif choice == "2":
                message = input("\nEnter a student query: ").strip()
                if message:
                    print("\nCategory:", classify_query(message))

            elif choice == "3":
                subject = input("\nSubject: ").strip()
                topics = input("Topics to cover: ").strip()
                days = int(input("Days available: "))
                hours = float(input("Study hours per day: "))
                print("\nYour Study Plan:\n")
                print(generate_study_plan(subject, topics, days, hours))

            elif choice == "4":
                topic = input("\nQuiz topic: ").strip()
                count = int(input("Number of questions: "))
                difficulty = input("Difficulty (easy/medium/hard): ").strip()
                print("\nPractice Quiz:\n")
                print(generate_quiz(topic, count, difficulty))

            elif choice == "5":
                message = input(
                    "\nDescribe your assignment and deadline if known: "
                ).strip()
                details = extract_assignment_details(message)
                print("\nAssignment Details:")
                print(json.dumps(details, indent=4, ensure_ascii=False))

            elif choice == "6":
                days = int(input("\nNumber of days: "))
                hours = float(input("Study hours per day: "))
                total = calculate_study_hours(days, hours)
                print(f"\nTotal available study time: {total} hours")

            elif choice == "7":
                print("\nThank you for using CampusMate. Happy learning!")
                break

            else:
                print("\nInvalid choice. Please enter a number from 1 to 7.")

        except ValueError as error:
            print("\nInput or JSON error:", error)
        except Exception as error:
            print("\nAn error occurred:", error)


if __name__ == "__main__":
    main()
