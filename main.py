from openai import OpenAI
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load data (RAG)
with open("data.json") as f:
    data = json.load(f)

# Mock function
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")

# Memory
conversation_history = []

# GPT function
def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant for AutoStream SaaS product."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Intent detection (fixed)
def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["buy", "subscribe", "purchase", "start", "try"]):
        return "high_intent"

    elif any(word in user_input for word in ["price", "pricing", "plan", "cost"]):
        return "inquiry"

    elif any(word in user_input.split() for word in ["hi", "hello", "hey"]):
        return "greeting"

    else:
        return "other"

# RAG function
def get_pricing_info():
    basic = data["pricing"]["basic"]
    pro = data["pricing"]["pro"]

    return f"""
We have two plans:

Basic Plan:
Price: {basic['price']}
Videos: {basic['videos']}
Resolution: {basic['resolution']}

Pro Plan:
Price: {pro['price']}
Videos: {pro['videos']}
Resolution: {pro['resolution']}
Features: AI captions included
"""

# Chatbot
def chatbot():
    print("Agent: Hello! How can I help you?")

    user_data = {"name": None, "email": None, "platform": None}
    collecting_lead = False

    while True:
        user = input("You: ")
        conversation_history.append(user)

        # 🔥 Step 1: Handle lead collection FIRST
        if collecting_lead:
            if user_data["name"] is None:
                user_data["name"] = user
                print("Agent: Please enter your email:")

            elif user_data["email"] is None:
                user_data["email"] = user
                print("Agent: Which platform do you create content on? (YouTube/Instagram)")

            elif user_data["platform"] is None:
                user_data["platform"] = user

                # Call tool only after full data
                mock_lead_capture(
                    user_data["name"],
                    user_data["email"],
                    user_data["platform"]
                )

                print("Agent: Thank you! Our team will contact you soon 😊")
                break

            continue  # important

        # 🔥 Step 2: Detect intent
        intent = detect_intent(user)

        if intent == "greeting":
            print("Agent: Hi! 😊 You can ask me about pricing or features.")

        elif intent == "inquiry":
            print("Agent:", get_pricing_info())

        elif intent == "high_intent":
            print("Agent: Great! You're interested in getting started 🚀")
            print("Agent: Can I have your name?")
            collecting_lead = True

        else:
            response = ask_gpt(user)
            print("Agent:", response)

# Run
chatbot()