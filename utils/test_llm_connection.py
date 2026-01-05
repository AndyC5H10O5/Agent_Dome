import os
from langchain.chat_models import init_chat_model

os.environ["DEEPSEEK_API_KEY"] = "sk-3a740dbac47d4f599c2708ee0b52fb76"

model = init_chat_model("deepseek-chat")

response = model.invoke("Hello")

print(response)
