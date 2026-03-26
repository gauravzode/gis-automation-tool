from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def main():
    user_query = input("> ")

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )

    content = response.choices[0].message.content
    if content:
        print(f"🤖: {content}")
    else:
        print("🤖: (no response)")

main()
