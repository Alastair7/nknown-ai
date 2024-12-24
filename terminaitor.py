from dotenv import load_dotenv
import openai

load_dotenv()
import os

client = openai.OpenAI(
    api_key=os.environ.get("GLHF_API_KEY"),
    base_url="https://glhf.chat/api/openai/v1"
)

messages = [
        {"role": "system", "content": "Test"},
        {"role": "user", "content": "Hey!"}
        ]

completion = client.chat.completions.create(
    model="hf:mistralai/Mistral-7B-Instruct-v0.3",
    messages=messages
)

# stop_terminaitor = False

# while stop_terminaitor == False:
#     prompt = str(input('Prompt >> '))

#     if prompt == 'stop':
#         stop_terminaitor = True
#     else:
#         messages.append(prompt)


print(completion.choices[0].message.content)

