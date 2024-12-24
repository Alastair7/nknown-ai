from dotenv import load_dotenv
import openai

load_dotenv()
import os

client = openai.OpenAI(
    api_key=os.environ.get("GLHF_API_KEY"),
    base_url="https://glhf.chat/api/openai/v1"
)

def create_message(role, content):
    return {"role": role, "content": content}

meta_prompt = """
WRITE YOUR META-PROMPT HERE. eg: You're a kind assistant.
"""
messages = [
        {"role": "system", "content": meta_prompt}
        ]


stop_terminaitor = False

while stop_terminaitor == False:
    prompt = str(input('Prompt >> '))
    print('\n')

    if prompt == 'stop':
        stop_terminaitor = True
        break
    else:
        message = create_message('user', prompt)
        messages.append(message)
    
    completion = client.chat.completions.create(
        stream=True,
        model="hf:mistralai/Mistral-7B-Instruct-v0.3",
        messages=messages
    )

    print('ASSISTANT NAME: ')
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end='', flush=True)
    
    print('\n')



