import os

from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)