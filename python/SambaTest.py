import os
import openai

client = openai.OpenAI(
    api_key="079e0597-f447-4b89-af13-96e50ab491ea",
    base_url="https://api.sambanova.ai/v1",
)

response = client.chat.completions.create(
    model="DeepSeek-R1",
    messages=[{"role":"system","content":"You are a helpful assistant"},{"role":"user","content":"What's 2+2?"}],
    temperature=0.1,
    top_p=0.1
)

print(response.choices[0].message.content)