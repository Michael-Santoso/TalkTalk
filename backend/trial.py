from openai import OpenAI

client = OpenAI(
  api_key=""
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "Can you write a character about dave?"},
  ]
)

print(completion.choices[0].message);