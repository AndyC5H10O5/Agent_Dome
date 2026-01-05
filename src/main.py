import os
from langchain.agents import create_agent
from src.tools.get import get_Chinese_8word

os.environ["DEEPSEEK_API_KEY"] = "sk-3a740dbac47d4f599c2708ee0b52fb76"

agent = create_agent(
    model="deepseek-reasoner",
    tools=[get_Chinese_8word],
    system_prompt="你是一个起名师傅，擅长给中国宝宝古法取名"
)

agent.invoke(
    {
        "message": [
            {
                "role": "user",
                "content": "我的生辰八字是什么"
            }
        ]
    }
)
