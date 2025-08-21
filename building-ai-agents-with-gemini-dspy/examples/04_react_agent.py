import os
from datetime import datetime

from dotenv import load_dotenv
import dspy


def setup_dspy():
    """Initialize DSPy with Gemini as the language model."""
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")

    # Configure DSPy to use Gemini via LiteLLM
    gemini_lm = dspy.LM(model="gemini/gemini-2.5-flash-lite", api_key=api_key)
    dspy.settings.configure(lm=gemini_lm)

    return gemini_lm


class ReActAgentSignature(dspy.Signature):
    """Simple agent that helps us with dates and weather."""
    question = dspy.InputField()
    today = dspy.InputField(desc="Today's date in ISO format (YYYY-MM-DD)")
    answer = dspy.OutputField(desc="Final answer based on the reasoning, no more than 2 sentences.")


def get_weather(city: str, day_of_week: str) -> str:
    match day_of_week.lower():
        case "monday" | "tuesday" | "friday":
            weather = "rainy"
        case "wednesday" | "thursday":
            weather = "sunny"
        case "saturday" | "sunday":
            weather = "cloudy"
        case _:
            raise ValueError(f"Invalid day of week: {day_of_week}")

    print(f"get_weather({city}, {day_of_week}) -> {weather}")
    return f"The weather in {city} is {weather}."


def get_day_of_week(date_string: str) -> str:
    date = datetime.fromisoformat(date_string)
    day_of_week = date.strftime("%A")
    print(f"get_day_of_week({date}) -> {day_of_week}")
    return day_of_week


def ask_user_question(question: str) -> str:
    return input(f"\nAgent: {question}\nYou: ")


def react_example():
    setup_dspy()
    react = dspy.ReAct(
        signature=ReActAgentSignature,
        tools=[
            get_weather,
            get_day_of_week,
            ask_user_question
        ]
    )
    pred = react(question="Will I need a raincoat for Jame's birthday party?", today=datetime.now().isoformat())
    print(pred.answer)


def interactive_mode():
    """Run the agent in interactive mode."""
    setup_dspy()
    react = dspy.ReAct(
        signature=ReActAgentSignature,
        tools=[
            get_weather,
            get_day_of_week,
            ask_user_question
        ]
    )
    while (user_input := input("\n🎯 Your request: ").strip()).lower() != "quit":
        pred = react(question=user_input, today=datetime.now().isoformat())
        print(f"Answer: {pred.answer}")

    print("👋 Goodbye!")


def main():
    """Run all the DSPy introduction examples."""
    match input("Hi! What would like to do? 1. Demo 2. Interactive\n> "):
        case "1":
            react_example()
        case "2":
            interactive_mode()
        case _:
            print("Invalid choice. Running demo...")

if __name__ == "__main__":
    main()