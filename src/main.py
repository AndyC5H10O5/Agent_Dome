import os
from config.config import system_prompt
from langchain.agents import create_agent
from src.tools.get import get_Chinese_8word
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "deepseek-chat",
)

agent = create_agent(
    model=model,
    tools=[get_Chinese_8word],
    system_prompt=system_prompt
)

response = agent.invoke(
    {
        "message": [
            {
                "role": "user",
                "content": "你的角色是什么"
            }
        ]
    }
)

print(response)
