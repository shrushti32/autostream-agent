# AutoStream Conversational AI Agent

## Project Overview
This project is a Conversational AI Agent built for AutoStream, a SaaS platform for automated video editing.

The agent can:
- Understand user intent (greeting, inquiry, high-intent)
- Answer pricing questions using a local knowledge base (RAG)
- Identify high-intent users
- Collect user details and simulate lead capture

## Tech Stack
- Python
- OpenAI GPT (gpt-4o-mini)
- JSON (for knowledge base)
- dotenv

## How to Run

1. Install dependencies:
   python -m pip install openai python-dotenv

2. Add your API key in `.env` file:
   OPENAI_API_KEY=your_key_here

3. Run the project:
   python main.py

## Features
- Intent Detection
- RAG-based responses
- Lead Capture System
- GPT-based responses
- Conversation Memory

## Architecture Explanation

This project uses a simple yet effective architecture to build a conversational AI agent. The system is designed using Python with modular functions for intent detection, response generation, and lead handling.

The agent first processes user input and identifies intent using rule-based logic. Based on the detected intent, it routes the conversation flow accordingly. For informational queries, the agent uses a Retrieval-Augmented Generation (RAG) approach by fetching relevant data from a local JSON knowledge base.

For general queries, GPT is used to generate intelligent responses. State is managed using in-memory variables such as conversation history and user data dictionary.

The system ensures that the lead capture function is only triggered after collecting all required user details.

## WhatsApp Integration

To integrate this AI agent with WhatsApp, we can use WhatsApp Business API or services like Twilio.

A webhook will be created using a backend framework like Flask. When a user sends a message on WhatsApp, it is sent to the webhook.

The chatbot processes the message and sends a response back through the API.

This enables real-time communication between the user and the AI agent.