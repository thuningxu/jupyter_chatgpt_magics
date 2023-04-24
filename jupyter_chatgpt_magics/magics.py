import os
import openai
import json
from IPython.core.magic import register_cell_magic
from IPython.display import display, Markdown

openai.api_key = os.environ.get('OPENAI_API_KEY')

default_messages = [{"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI."}]
messages = default_messages.copy()
model = "gpt-3.5-turbo"
max_tokens=2048
temperature=0.5
n=1

@register_cell_magic
def chatgpt(line, cell):
    global messages, model, max_tokens, temperature, n
    
    # Parse the input line for parameters
    params = line.split()
    
    # Check if there is a session_id parameter
    session_id = None
    for param in params:
        if param.startswith("session_id="):
            session_id = param[11:]
            break
        if param.startswith("engine="):
            engine = param[7:]
            break
        if param.startswith("max_tokens="):
            max_tokens = int(param[11:])
            break
        if param.startswith("temperature="):
            temperature = float(param[12:])
            break
        if param.startswith("n="):
            n = int(param[2:])
            break
        if param.startswith("reset"):
            messages = default_messages.copy()

    # Prepare API call
    messages.append({"role": "user", "content": cell.strip()})

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        n=n,
        stop=None,
        temperature=temperature,
    )

    # Extract the generated text
    generated_text = response.choices[0].message['content'].strip()

    # update chat log
    messages.append({"role": "assistant", "content": generated_text})

    # Return the generated text
    display(Markdown(f'> **User:** {cell.strip()}\n\n **ChatGPT:** {generated_text}'))  # Render as Markdown
    return None  # Return None to prevent displaying the raw output

def load_ipython_extension(ipython):
    ipython.register_magic_function(chatgpt, magic_kind='cell')
