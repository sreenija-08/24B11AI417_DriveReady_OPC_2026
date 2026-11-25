# Agentic AI – Day 2

## Overview
This notebook explores practical applications of Large Language Models (LLMs) using Groq API and LangChain. It demonstrates how to build AI assistants with conversation memory, function calling, message classification, and structured data extraction.

## Technologies Used
- Python
- Groq API
- LangChain
- OpenAI GPT-OSS 120B
- Meta Llama Prompt Guard 2
- Google Colab

## Tasks Implemented

### 1. Groq LLM Setup
- Installed required dependencies.
- Configured Groq API key.
- Initialized the language model.

### 2. Bakery Customer Support Assistant
- Created an AI assistant for Sweet Crumbs Home Bakery.
- Added system instructions.
- Handled customer queries about bakery products and orders.

### 3. Prompt Guard
- Explored prompt security using Meta Llama Prompt Guard 2.
- Tested potentially malicious prompts.

### 4. Price Calculation Function
- Created Python functions to calculate product prices.
- Used a logging decorator to track function execution.

### 5. Conversation History
- Implemented multi-turn conversations.
- Maintained previous messages as context.
- Explored API error handling.

### 6. Customer Message Classification
Classified customer messages into:
- Order
- Question
- Complaint

### 7. Structured Order Extraction
Extracted customer order details into JSON format, including:
- Customer name
- Product
- Quantity
- Date
- Eggless preference

### 8. Dragon Fruit Farm Assistant
- Created an AI assistant for a Dragon Fruit Farm.
- Added product information and pricing.
- Implemented product price calculation.

## Learning Outcomes
- Understanding LLM applications.
- Creating AI-powered assistants.
- Working with conversation history.
- Implementing Python functions with LLMs.
- Performing text classification.
- Extracting structured information using JSON.
- Understanding prompt security.

## How to Run
1. Open the notebook in Google Colab.
2. Configure the Groq API key.
3. Install the required dependencies.
4. Run all cells in sequence.
5. Test the AI assistant with different queries.

## Conclusion
Day 2 focuses on developing practical AI assistant applications using LLMs. It introduces conversation memory, function execution, message classification, structured data extraction, and prompt security.
