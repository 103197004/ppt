import asyncio
from src.core.assistant import Assistant
from src.config.settings import Settings

async def main():
    # 初始化配置
    settings = Settings()
    
    # 创建助手实例
    assistant = Assistant(settings.dict())
    
    # 注册工具
    assistant.tools.register(SearchTool())
    
    # 对话循环
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
            
        response = await assistant.chat(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    asyncio.run(main()) 