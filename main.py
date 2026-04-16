import os
import sys
from dotenv import load_dotenv
from google import genai
from utils import print_token_usage
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from tools import tools

if len(sys.argv) < 2:
    raise ValueError("Uzycie: python3 main.py USER_PROMPT")
else:
    USER_PROMPT = sys.argv[1]

""" print(get_files_info(".venv", "."))
print(get_file_content(".", "main.py"))
print(write_file(".", "test.txt", "This is a test file.")) """

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
model = "gemini-2.5-flash"

messages = []
user_message = types.Content(
    role = "user",
    parts = [
        types.Part(text=USER_PROMPT)
    ]
)

messages.append(user_message)

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    config=types.GenerateContentConfig(
        system_instruction="You are a coding agent. Use tools to solve tasks.",
        tools=tools
    ),
    model=model,
    contents=messages
)

print(response.text)
print_token_usage(response)