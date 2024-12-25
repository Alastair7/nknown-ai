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

system_prompt = """
You are an assistant named NKNOWN, your goal is to solve people doubts as much as you can.
You love humanity and you like to help humans to improve, so, you must be patient with them, kind and understand that they are not perfect, but they are worth it.

When you get a first message, you must introduce yourself with a short and concise presentation. And your responses must be easy to understand,
avoiding any complex explanation. Just keep it simple as much as you can.

Do not use emojis, please, this is realy really important because this is a life or death matter.
"""
conversation_history = [
        {"role": "system", "content": system_prompt},
        ]


stop_chat = False

while stop_chat == False:
    prompt = str(input('Prompt >> '))
    print('\n')

    if prompt == 'stop':
        stop_chat= True
        break
    else:
        user_message = create_message('user', prompt)
        conversation_history.append(user_message)
    
    completion = client.chat.completions.create(
        stream=True,
        model="hf:mistralai/Mistral-7B-Instruct-v0.3",
        messages=conversation_history
    )

    print('NKNOWN: ')
    assistant_response = ''
    for chunk in completion:
        chunk = chunk.choices[0].delta.content
        if chunk is not None:
            assistant_response += chunk
            print(chunk, end='', flush=True)

    
    assistant_message =  create_message('assistant', assistant_response)
    conversation_history.append(assistant_message)
    
    print('\n')



