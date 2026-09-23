import os
import requests

TOKEN = os.getenv("GITHUB_TOKEN")

if not TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable is not set.")

url = "https://models.github.ai/inference/chat/completions"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

requirement = input("Enter a product requirement: ")

prompt = f"""
You are a Senior QA Engineer.

Analyze the following product requirement:

{requirement}

Generate concise QA test scenarios in these categories:

1. Positive Tests
2. Negative Tests
3. Edge Cases
4. API Checks
5. Usability Checks

Focus on realistic risks and avoid generic test cases.
"""

data = {
    "model": "openai/gpt-4.1-mini",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.3
}

response = requests.post(
    url,
    headers=headers,
    json=data,
    timeout=30
)

response.raise_for_status()

result = response.json()

print("\n--- AI Generated QA Test Scenarios ---\n")
print(result["choices"][0]["message"]["content"])
