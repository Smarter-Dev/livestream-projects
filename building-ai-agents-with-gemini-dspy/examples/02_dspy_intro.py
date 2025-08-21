"""
Introduction to DSPy and why it's useful for building with LLMs
This example shows how DSPy can help structure and optimize your prompts.
"""

import os
from dotenv import load_dotenv
import dspy
from dspy import Gemini

def setup_dspy():
    """Initialize DSPy with Gemini as the language model."""
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    # Configure DSPy to use Gemini
    gemini_lm = Gemini(model="gemini-1.5-flash", api_key=api_key)
    dspy.settings.configure(lm=gemini_lm)
    
    return gemini_lm

class BasicQA(dspy.Signature):
    """Answer questions about AI agents clearly and concisely."""
    question = dspy.InputField()
    answer = dspy.OutputField(desc="A clear, informative answer")

class CodeGenerator(dspy.Signature):
    """Generate Python code based on a description."""
    description = dspy.InputField()
    code = dspy.OutputField(desc="Clean, well-commented Python code")

def basic_dspy_example():
    """Show how DSPy structures prompts better than raw text."""
    setup_dspy()
    
    # Create a predictor using our signature
    qa = dspy.Predict(BasicQA)
    
    questions = [
        "What is the difference between an AI agent and a chatbot?",
        "How do AI agents make decisions?",
        "What are some real-world applications of AI agents?"
    ]
    
    for question in questions:
        result = qa(question=question)
        print(f"Q: {question}")
        print(f"A: {result.answer}\n")

def code_generation_example():
    """Show DSPy for code generation tasks."""
    setup_dspy()
    
    code_gen = dspy.Predict(CodeGenerator)
    
    descriptions = [
        "A simple function that calculates the factorial of a number",
        "A class that represents a basic to-do item with title and completion status",
        "A function that finds the most common word in a text string"
    ]
    
    for desc in descriptions:
        result = code_gen(description=desc)
        print(f"Description: {desc}")
        print("Generated Code:")
        print(result.code)
        print("-" * 50)

class ChainOfThought(dspy.Signature):
    """Answer complex questions with step-by-step reasoning."""
    question = dspy.InputField()
    reasoning = dspy.OutputField(desc="Step-by-step reasoning process")
    answer = dspy.OutputField(desc="Final answer based on the reasoning")

def chain_of_thought_example():
    """Demonstrate how DSPy can structure complex reasoning."""
    setup_dspy()
    
    cot = dspy.Predict(ChainOfThought)
    
    question = "How would you design an AI agent that can help users manage their daily schedule?"
    
    result = cot(question=question)
    print(f"Question: {question}")
    print(f"\nReasoning: {result.reasoning}")
    print(f"\nAnswer: {result.answer}")

def main():
    """Run all the DSPy introduction examples."""
    print("=== Basic DSPy Q&A ===")
    basic_dspy_example()
    
    print("\n=== Code Generation with DSPy ===")
    code_generation_example()
    
    print("\n=== Chain of Thought Reasoning ===")
    chain_of_thought_example()

if __name__ == "__main__":
    main()