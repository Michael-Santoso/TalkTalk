from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv(".env")

client = OpenAI(
  api_key=os.environ.get("OPEN_AI_KEY")
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "Can you summarise today's news on finance?"},
  ]
)

print(completion.choices[0].message);