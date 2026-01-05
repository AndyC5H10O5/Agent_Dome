from langchain.agents import create_agent

Chinese_8word="甲申丙子庚辰甲申"


def get_Chinese_8word(date: str, hour: str) -> str:
    """获得生辰八字"""
    return f"生辰八字是 {Chinese_8word}"


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
