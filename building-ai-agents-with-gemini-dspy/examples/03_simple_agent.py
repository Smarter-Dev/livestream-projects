"""
Building a practical AI agent from scratch
This example shows how to create a simple but functional AI agent that can perform tasks.
"""

import os
from dotenv import load_dotenv
import dspy
from dspy import Gemini
import json
from datetime import datetime, timedelta

def setup_dspy():
    """Initialize DSPy with Gemini as the language model."""
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    gemini_lm = Gemini(model="gemini-2.5-flash-lite", api_key=api_key)
    dspy.settings.configure(lm=gemini_lm)
    
    return gemini_lm

class TaskAnalyzer(dspy.Signature):
    """Analyze a user request and determine what action to take."""
    user_request = dspy.InputField()
    task_type = dspy.OutputField(desc="One of: reminder, calculation, question, weather, unknown")
    extracted_info = dspy.OutputField(desc="Key information needed to complete the task")

class Calculator(dspy.Signature):
    """Perform mathematical calculations."""
    expression = dspy.InputField(desc="Mathematical expression to calculate")
    result = dspy.OutputField(desc="The calculated result with explanation")

class QuestionAnswerer(dspy.Signature):
    """Answer general knowledge questions."""
    question = dspy.InputField()
    answer = dspy.OutputField(desc="Informative and accurate answer")

class ReminderCreator(dspy.Signature):
    """Create reminders from natural language."""
    request = dspy.InputField(desc="Natural language reminder request")
    reminder_text = dspy.OutputField(desc="Clear reminder message")
    suggested_time = dspy.OutputField(desc="Suggested reminder time based on context")

class SimpleAgent:
    """A simple AI agent that can handle multiple types of tasks."""
    
    def __init__(self):
        setup_dspy()
        self.task_analyzer = dspy.Predict(TaskAnalyzer)
        self.calculator = dspy.Predict(Calculator)
        self.qa = dspy.Predict(QuestionAnswerer)
        self.reminder_creator = dspy.Predict(ReminderCreator)
        self.reminders = []  # Simple in-memory storage
    
    def process_request(self, user_request):
        """Main method to process user requests."""
        print(f"\n📨 Processing: '{user_request}'")
        
        # First, analyze what type of task this is
        analysis = self.task_analyzer(user_request=user_request)
        print(f"🔍 Task Type: {analysis.task_type}")
        print(f"📋 Extracted Info: {analysis.extracted_info}")
        
        # Route to appropriate handler
        if analysis.task_type == "calculation":
            return self._handle_calculation(analysis.extracted_info)
        elif analysis.task_type == "question":
            return self._handle_question(user_request)
        elif analysis.task_type == "reminder":
            return self._handle_reminder(user_request)
        elif analysis.task_type == "weather":
            return self._handle_weather(user_request)
        else:
            return self._handle_unknown(user_request)
    
    def _handle_calculation(self, expression):
        """Handle mathematical calculations."""
        print("🧮 Performing calculation...")
        result = self.calculator(expression=expression)
        return f"📊 Calculation Result: {result.result}"
    
    def _handle_question(self, question):
        """Handle general knowledge questions."""
        print("❓ Answering question...")
        result = self.qa(question=question)
        return f"💡 Answer: {result.answer}"
    
    def _handle_reminder(self, request):
        """Handle reminder creation."""
        print("⏰ Creating reminder...")
        result = self.reminder_creator(request=request)
        
        # Store the reminder (in a real app, you'd use a database)
        reminder = {
            "text": result.reminder_text,
            "suggested_time": result.suggested_time,
            "created_at": datetime.now().isoformat()
        }
        self.reminders.append(reminder)
        
        return f"✅ Reminder created: {result.reminder_text}\n⏱️  Suggested time: {result.suggested_time}"
    
    def _handle_weather(self, request):
        """Handle weather requests (mock implementation)."""
        print("🌤️ Checking weather...")
        return "🌤️ Weather: I don't have access to real weather data yet, but I can help you set up a weather API integration!"
    
    def _handle_unknown(self, request):
        """Handle unknown request types."""
        print("🤔 Handling unknown request...")
        fallback = self.qa(question=f"How can I help with this request: {request}")
        return f"🤷 I'm not sure exactly what you need, but here's my best attempt to help: {fallback.answer}"
    
    def list_reminders(self):
        """List all stored reminders."""
        if not self.reminders:
            return "📝 No reminders stored yet."
        
        reminder_list = "📝 Your reminders:\n"
        for i, reminder in enumerate(self.reminders, 1):
            reminder_list += f"{i}. {reminder['text']} (suggested: {reminder['suggested_time']})\n"
        
        return reminder_list

def demo_agent():
    """Demonstrate the agent with various requests."""
    agent = SimpleAgent()
    
    test_requests = [
        "What is 15 multiplied by 23?",
        "Remind me to call mom tomorrow at 2 PM",
        "What is the capital of Australia?",
        "What's the weather like today?",
        "Remind me to buy groceries this evening",
        "Calculate the square root of 144",
        "Who invented the telephone?",
        "I need to finish my project by Friday"
    ]
    
    print("🤖 Simple AI Agent Demo")
    print("=" * 50)
    
    for request in test_requests:
        response = agent.process_request(request)
        print(f"✨ Response: {response}")
        print("-" * 50)
    
    # Show all reminders
    print("\n" + agent.list_reminders())

def interactive_mode():
    """Run the agent in interactive mode."""
    agent = SimpleAgent()
    
    print("🤖 Simple AI Agent - Interactive Mode")
    print("Type 'quit' to exit, 'reminders' to see all reminders")
    print("=" * 50)
    
    while True:
        user_input = input("\n🎯 Your request: ").strip()
        
        if user_input.lower() == 'quit':
            print("👋 Goodbye!")
            break
        elif user_input.lower() == 'reminders':
            print(agent.list_reminders())
        elif user_input:
            response = agent.process_request(user_input)
            print(f"✨ Response: {response}")

def main():
    """Choose between demo mode and interactive mode."""
    print("Choose mode:")
    print("1. Demo mode (predefined examples)")
    print("2. Interactive mode (chat with the agent)")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        demo_agent()
    elif choice == "2":
        interactive_mode()
    else:
        print("Invalid choice. Running demo mode...")
        demo_agent()

if __name__ == "__main__":
    main()