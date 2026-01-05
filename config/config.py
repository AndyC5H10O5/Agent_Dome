import os
from dotenv import load_dotenv


# system_prompt = "你是一个起名师傅，擅长给中国宝宝古法取名，你需要调用”get_Chinese_8word“工具来获得生辰八字"

# 加载 .env 文件到系统环境变量中
load_dotenv()

# 从环境变量中读取配置项
DATABASE_URL = os.getenv("DATABASE_URL")
