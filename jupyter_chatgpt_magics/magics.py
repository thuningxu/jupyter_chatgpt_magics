import os
import openai
import json
from IPython.core.magic import register_cell_magic

openai.api_key = os.environ.get('OPENAI_API_KEY')

# Dictionary to store chat sessions
chat_sessions = {}

@register_cell_magic
def chatgpt(line, cell):
    global chat_sessions
    
    # Parse the input line for parameters
    params = line.split()
    
    # Check if there is a session_id parameter
    session_id = None
    for param in params:
        if param.startswith("session_id="):
            session_id = param[10:]
            break
    
    # Prepare API call
    prompt = cell.strip()
    if session_id is not None and session_id in chat_sessions:
        # Resume the chat session if it exists
        chat_log = chat_sessions[session_id]
        prompt = f"{chat_log}\n\n{prompt}"
    else:
        # Start a new chat session
        chat_log = ""
    
    # Call the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Extract the generated text
    generated_text = response.choices[0].text.strip()
    
    # Update chat_log
    chat_log += f"\nUser: {prompt}\nChatGPT: {generated_text}"
    
    if session_id is not None:
        chat_sessions[session_id] = chat_log
    
    # Return the generated text
    return generated_text

def load_ipython_extension(ipython):
    ipython.register_magic_function(chatgpt, magic_kind='cell')
