import openai

openai.api_key = "YOUR_API_KEY"

content = "Give me a response to the prompt 'Say hello to the viewers' in the following format. DO NOT GIVE ANY OTHER CHARACTERS, ONLY JSON: { 'Name': '[INSERT RANDOM NAME]', 'Message': '[INSERT MESSAGE]' }"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": content
        }
    ]
)

print(response.choices[0].message.content)