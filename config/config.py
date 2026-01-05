import os
from dotenv import load_dotenv

print("Config initialized")

system_prompt = "你是一个起名师傅，擅长给中国宝宝古法取名"

# 加载 .env 文件到系统环境变量中
load_dotenv()

# 从环境变量中读取配置项
