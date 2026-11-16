
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors

# Load environment variables
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# Retrieve API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")

# Initialise Gemini client with a 30-second timeout
client = genai.Client(
    api_key=api_key,
    http_options={
        "timeout": 30_000
    }
)


def ask_gemini(question):
    """Send a question to Gemini and return its response."""

    try:
        print("Connecting to Gemini...")

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question
        )

        if not response.text:
            return "Gemini returned an empty response."

        return response.text

    except errors.APIError as error:
        return f"Gemini API error ({error.code}): {error.message}"

    except Exception as error:
        return f"Unexpected error: {error}"
