# DriveReady OPC 2026 – Day 3

## Project: CampusMate – Agentic AI Student Assistant

**LLM:** Google Gemini 2.5 Flash

### 1. Overview
CampusMate is an Agentic AI student assistant developed using Google Gemini API and LangChain.

This project extends the use cases implemented in Day-2 by introducing an AI agent that can understand student requests, select suitable tools, execute them, and provide responses.

### 2. Features
1. **Academic Question Answering:** Provides simple explanations for academic topics.
2. **Student Query Classification:** Classifies student messages into predefined categories.
3. **Study Plan Generation:** Creates personalized day-wise study plans.
4. **Practice Quiz Generation:** Generates MCQs with answers and explanations.
5. **Assignment Information Extraction:** Extracts assignment details in JSON format.
6. **Study Hours Calculation:** Calculates total available study time.
7. **AI Agent:** Selects and uses the appropriate tool based on the student's request.
8. **Conversation History:** Maintains messages during the interaction session.

### 3. Technologies Used
- Python
- Google Gemini 2.5 Flash API
- LangChain
- LangChain Agent (`create_agent`)
- Custom Tools
- Google Colab

### 4. Installation

Install the required dependencies:

```bash
pip install -U langchain-google-genai langchain-core langchain
```

### 5. API Configuration

Set your Google Gemini API key using:

- **Google Colab:** Add `GOOGLE_API_KEY` in the Secrets panel.
- **Local System:** Set `GOOGLE_API_KEY` as an environment variable.

### 6. How to Run

Run the Python file:

```bash
python Day-3-CampusMate.py
```

Enter your request and CampusMate will use the available tools whenever required.

Type `exit` to stop the application.

### 7. Learning Outcomes
- Understanding Agentic AI concepts.
- Creating AI agents using LangChain.
- Integrating Gemini API with an AI agent.
- Implementing custom tools and tool calling.
- Understanding how agents select and execute tools.
- Building interactive AI applications.

### 8. Conclusion
CampusMate demonstrates how an AI application can be upgraded into an Agentic AI system. Instead of only generating responses, the agent can select and execute tools to complete different student-related tasks.
