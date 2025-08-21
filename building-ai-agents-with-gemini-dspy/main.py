"""
Building AI Agents with Gemini & DSPy - Livestream Demo
Main entry point for the livestream demonstration.
"""

import sys
import os

def show_menu():
    """Display the main menu for the livestream demo."""
    print("🤖 Building AI Agents with Gemini & DSPy")
    print("=" * 50)
    print("Choose what you'd like to explore:")
    print("1. Gemini API Basics")
    print("2. Introduction to DSPy")  
    print("3. Simple AI Agent Demo")
    print("4. Verbose Agent Demo (shows prompts)")
    print("5. Interactive Agent Mode")
    print("6. Verbose Interactive Mode")
    print("0. Exit")
    print("-" * 50)

def run_example(choice):
    """Run the selected example."""
    if choice == "1":
        print("🚀 Running Gemini API Basics...")
        os.system("uv run python examples/01_gemini_basics.py")
    elif choice == "2":
        print("🚀 Running DSPy Introduction...")
        os.system("uv run python examples/02_dspy_intro.py")
    elif choice == "3":
        print("🚀 Running Simple Agent Demo...")
        # Run the simple demo mode (option 1)
        os.system("echo '1' | uv run python examples/03_simple_agent.py")
    elif choice == "4":
        print("🚀 Running Verbose Agent Demo...")
        # Run the verbose demo mode (option 2)
        os.system("echo '2' | uv run python examples/03_simple_agent.py")
    elif choice == "5":
        print("🚀 Starting Interactive Agent...")
        # Run the interactive mode (option 3)
        os.system("echo '3' | uv run python examples/03_simple_agent.py")
    elif choice == "6":
        print("🚀 Starting Verbose Interactive Mode...")
        # Run the verbose interactive mode (option 4)
        os.system("echo '4' | uv run python examples/03_simple_agent.py")
    else:
        print("❌ Invalid choice. Please try again.")

def check_setup():
    """Check if the environment is properly set up."""
    if not os.path.exists('.env'):
        print("⚠️  Warning: .env file not found!")
        print("Please copy .env.example to .env and add your GEMINI_API_KEY")
        print("You can get an API key at: https://aistudio.google.com/")
        return False
    return True

def main():
    """Main function for the livestream demo."""
    print("🎬 Welcome to the Building AI Agents with Gemini & DSPy Livestream!")
    print()
    
    # Check if setup is complete
    if not check_setup():
        print("\n⚙️  Setup incomplete. Please configure your environment first.")
        return
    
    while True:
        show_menu()
        choice = input("🎯 Enter your choice: ").strip()
        
        if choice == "0":
            print("👋 Thanks for joining the livestream!")
            break
        
        print()
        run_example(choice)
        print()
        input("⏸️  Press Enter to continue...")
        print("\n" * 2)

if __name__ == "__main__":
    main()
