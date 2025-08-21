"""
Getting started with the Gemini API
This example shows how to set up and use Google's Gemini API for basic text generation.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

def setup_gemini():
    """Initialize the Gemini API with your API key."""
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash-exp')

def basic_generation_example():
    """Basic text generation with Gemini."""
    model = setup_gemini()
    
    prompt = "Explain what an AI agent is in simple terms"
    response = model.generate_content(prompt)
    
    print("Prompt:", prompt)
    print("\nResponse:", response.text)

def conversation_example():
    """Example of having a conversation with Gemini."""
    model = setup_gemini()
    
    # Start a chat session
    chat = model.start_chat(history=[])
    
    messages = [
        "Hi! I'm learning about AI agents.",
        "What are the key components of an AI agent?",
        "Can you give me an example of a simple agent?"
    ]
    
    for message in messages:
        print(f"\nYou: {message}")
        response = chat.send_message(message)
        print(f"Gemini: {response.text}")

def main():
    """Run all the basic Gemini examples."""
    print("=== Basic Text Generation ===")
    basic_generation_example()
    
    print("\n\n=== Conversation Example ===")
    conversation_example()

if __name__ == "__main__":
    main()