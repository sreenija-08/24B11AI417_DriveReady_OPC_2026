# Agentic AI – Day 1

## Overview
This project demonstrates the basics of building an AI-powered chatbot using **Groq LLMs and LangChain**. It focuses on creating a bakery customer support assistant with predefined instructions and exploring prompt security using a Prompt Guard model.

## Features

- **LLM Integration:** Uses Groq API with LangChain's `ChatGroq`.
- **AI Customer Support:** Creates a chatbot for Sweet Crumbs Home Bakery.
- **Custom System Instructions:** Defines the assistant's role, behavior, and response format.
- **Order Assistance:** Answers customer questions about bakery orders.
- **Prompt Security:** Demonstrates Meta Llama Prompt Guard for identifying potentially unsafe or malicious prompts.

## Technologies Used

- Python
- LangChain
- Groq API
- OpenAI GPT-OSS 120B
- Meta Llama Prompt Guard 2
- Google Colab

## Project Implementation

### 1. Install Dependencies

```bash
pip install langchain_groq
```

### 2. Configure Groq API Key

The project retrieves the Groq API key securely from Google Colab Secrets.

Add your `GROQ_API_KEY` in the Secrets section of Google Colab.

### 3. Initialize the LLM

Uses the `openai/gpt-oss-120b` model through LangChain's `ChatGroq`.

```python
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)
```

### 4. Create an AI Bakery Assistant

The assistant is designed for Sweet Crumbs Home Bakery.

**System Instructions:**
- All orders are baked to order.
- Orders require 24 hours' advance notice.
- All cakes have eggless versions.
- Never promise delivery times.
- If information is unknown, the assistant must say so.
- Responses must be polite and under 60 words.

### 5. Ask Questions

A custom function sends user questions to the LLM and returns its response.

```python
def ask(question):
    return llm.invoke([
        ("system", SYSTEM),
        ("human", question)
    ]).content
```

Example:

```python
print(ask("can i get my order tomorrow"))
```

### 6. Prompt Guard

The notebook also demonstrates the Meta Llama Prompt Guard 2 model using the Groq client to examine a potentially malicious prompt.

## Learning Outcomes

- Understanding LLM integration with LangChain.
- Working with Groq API.
- Creating AI assistants using system prompts.
- Controlling chatbot responses through instructions.
- Understanding basic prompt injection and prompt security concepts.

## How to Run

1. Open the notebook in Google Colab.
2. Install the required dependencies.
3. Add your Groq API key to Colab Secrets.
4. Execute the notebook cells in order.
5. Ask questions to interact with the AI bakery assistant.
6. Run the Prompt Guard example.

## Conclusion

This Day 1 project provides a practical introduction to Agentic AI concepts by building a domain-specific AI assistant and exploring prompt security using Groq-powered language models.
