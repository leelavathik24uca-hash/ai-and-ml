from openai import OpenAI

# Create client (put your API key here)
client = OpenAI(api_key="YOUR_API_KEY")

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

print("=== Simple Generative AI App ===")

while True:
    user_input = input("Ask AI (type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    result = generate_response(user_input)
    print("\nAI:", result, "\n")