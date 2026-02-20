from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("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"))

def run_llm(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
