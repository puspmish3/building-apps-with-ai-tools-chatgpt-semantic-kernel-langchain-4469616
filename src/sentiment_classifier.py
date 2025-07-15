import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

while True:
    user_input= input("Enter your response and I will tell you about your mood. Else enter 'quit' or 'exit' to quit\n")
    if user_input=="exit" or user_input=="quit":
        break
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a sentiment classification bot. Interpret if the user is happy or sad"},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=150,
    )

response_message = response["choices"][0]["message"]
print(response_message)