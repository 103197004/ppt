import asyncio
from typing import List
from src.core.components import Agent

async def main():
    # 初始化Agent
    agent = Agent()
    
    # 注册工具
    @agent.tools.register("search_docs")
    async def search_docs(query: str) -> List[str]:
        """搜索文档库"""
        # 实现文档搜索逻辑
        pass
    
    # 处理用户输入
    response = await agent.process(
        "帮我找一下关于Python异步编程的文档"
    )
    print(response)

if __name__ == "__main__":
    asyncio.run(main()) 