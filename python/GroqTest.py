import os

from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Hello",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)