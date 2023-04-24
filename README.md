This is a Jupyter Notebook extension to interact with ChatGPT, created with the help of ChatGPT itself!

**Install:**
```
pip install -U git+https://github.com/thuningxu/jupyter_chatgpt_magics.git/
```

**Usage:**
You should obtain an OpenAI API Key and set it in environment variable `OPENAI_API_KEY`. In your notebook, run this first to load the extension:
```
%load_ext jupyter_chatgpt_magics
```

In a cell:
```
%%chatgpt [param=value]
<enter your text>
```

Parameters follow the exact definition in OpenAI API documents: `model`, `max_tokens`, `temperature`, `n`. `reset` (no value needed) will reset the message log in this conversation.


See example in `example.ipynb`.
