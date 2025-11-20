import os
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
import google.generativeai as genai
from dotenv import load_dotenv


def configure_genai():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
    else:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")


def initialize_agent():
    return Agent(
        name="Video Summarizer Agent",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True
    )
