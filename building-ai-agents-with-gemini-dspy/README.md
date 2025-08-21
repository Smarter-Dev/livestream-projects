# Building AI Agents with Gemini & DSPy

**Livestream Date:** August 21, 2025 (Thursday)

## Overview

This project was created for a live coding session where we build AI bots and agents using Google's Gemini and DSPy.

### What We Cover

- **Getting started with the Gemini API** - Learn how to integrate Google's Gemini model into your applications
- **Introduction to DSPy** - Understand why DSPy is useful for building with LLMs and how it simplifies prompt engineering
- **Building a practical AI agent from scratch** - Create a working agent that can perform real tasks
- **Handling common issues and debugging** - Real-world problem solving as we code live

This is a hands-on session where everything is coded live, including any bugs or issues that come up along the way. Perfect for developers who want to see the actual development process.

### Who This Is Good For

- Anyone interested in working with LLMs programmatically
- Developers who want to see DSPy in action
- Those looking to add AI capabilities to their projects

## Setup

1. Copy the environment file and add your API key:
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Run the examples:
   ```bash
   uv run python examples/01_gemini_basics.py
   uv run python examples/02_dspy_intro.py
   uv run python examples/03_simple_agent.py
   ```

## Project Structure

- `examples/` - Step-by-step examples covering each topic
- `main.py` - Main entry point for the livestream demo
- `.env.example` - Template for environment variables

## Getting Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Add it to your `.env` file as `GEMINI_API_KEY`