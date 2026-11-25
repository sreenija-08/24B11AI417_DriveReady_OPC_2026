# Agentic AI – Day 3

## Overview
This project focuses on building an AI-powered Sweets Shop Assistant using Google Gemini and LangChain. It demonstrates conversational memory, automated testing, and the creation of an AI agent.

## Technologies Used
- Python
- Google Gemini API
- Gemini 3.8 Flash
- LangChain
- Google Colab
- CSV

## Tasks Implemented

### 1. Gemini LLM Setup
- Installed and imported the required libraries.
- Configured the Google API key.
- Initialized the Gemini language model using LangChain.

### 2. Sweets Shop AI Assistant
- Created a friendly AI assistant for a Sweets Shop.
- Added product details and pricing:
  - Gulab Jamun – ₹100
  - Rasagulla – ₹150
  - Kaju Katli – ₹200
- Added business rules such as 24 hours' advance notice for orders.
- Ensured short and friendly responses in English or Telugu.

### 3. Conversation Memory
- Implemented conversation history.
- Stored previous user questions and AI responses.
- Enabled the assistant to remember customer details across multiple interactions.
- Tested memory by asking for the customer's name.

### 4. Automated Testing Using CSV
- Used CSV files to store test questions and expected keywords.
- Created a testing function to check chatbot responses.
- Compared AI responses with expected keywords.
- Displayed PASS or FAIL results and the overall test score.

### 5. AI Agent Creation
- Used LangChain's `create_agent()` function.
- Created an AI agent using the Gemini model.
- Configured the agent with the Sweets Shop system instructions.
- Tested customer queries about delivery locations.

## Learning Outcomes
- Understanding Google Gemini integration.
- Building AI assistants using LangChain.
- Implementing conversational memory.
- Performing automated chatbot testing.
- Working with CSV files in Python.
- Understanding AI agent creation.
- Using system prompts to control AI behavior.

## How to Run
1. Open the Python notebook or script in Google Colab.
2. Configure your Google Gemini API key.
3. Install the required dependencies.
4. Execute the code step by step.
5. Test the sweets shop assistant with different questions.
6. Run the automated CSV testing function.
7. Test the AI agent with customer queries.

## Conclusion
Day 3 focuses on developing an AI-powered Sweets Shop Assistant using Google Gemini and LangChain. It introduces conversational memory, automated testing, and AI agent creation, providing practical experience in building intelligent conversational applications.
