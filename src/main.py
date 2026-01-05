import os
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

# from src.tools.get import get_Chinese_8word

os.environ["DEEPSEEK_API_KEY"] = "sk-3a740dbac47d4f599c2708ee0b52fb76"

model = init_chat_model(
    "deepseek-chat",
)

system_prompt = "你是一个起名师傅，擅长给中国宝宝古法取名"


def get_Chinese_8word() -> str:
    """获得生辰八字"""
    return "甲申 丙子 庚辰 甲申"


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
