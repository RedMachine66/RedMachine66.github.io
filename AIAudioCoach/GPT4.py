import openai
import os



# Replace 'YOUR_API_KEY' with your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def start_or_continue_conversation(ongoing):
    if ongoing:
        with open('messages.txt', 'r') as file:
            conversation_history = file.readlines()
        
        with open('transcript.txt', 'r') as file:
            user_question = file.read().strip()
        
        conversation_history.append({"role": "user", "content": user_question})
    else:
        with open('config.txt', 'r') as file:
            system_message = file.read().strip()
        
        with open('initial_prompt.txt', 'r') as file:
            user_message = file.read().strip()
        
        conversation_history = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    with open('gpt_answer.txt', 'w') as file:
        file.write(response['choices'][0]['message']['content'])

    with open('messages.txt', 'w') as file:
        for message in conversation_history + response['messages']:
            file.write(f"{message['role']}: {message['content']}\n")

# Example usage:
# Start a new conversation
start_or_continue_conversation(ongoing=False)

# Continue an ongoing conversation
# start_or_continue_conversation(ongoing=True)

