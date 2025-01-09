from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseAgent(ABC):
    """Agent基类"""
    
    @abstractmethod
    async def process_input(self, user_input: str) -> str:
        """处理用户输入"""
        pass
        
    @abstractmethod
    async def execute_action(self, action: Dict[str, Any]) -> Any:
        """执行动作"""
        pass
        
    @abstractmethod
    async def update_memory(self, data: Any) -> None:
        """更新记忆"""
        pass

class ToolBasedAgent(BaseAgent):
    """基于工具的Agent实现"""
    
    def __init__(self):
        self.llm = LLMProvider()
        self.tools = ToolRegistry()
        self.memory = Memory()
        self.planner = ActionPlanner()
        
    async def process_input(self, user_input: str) -> str:
        # 1. 理解用户意图
        intent = await self.llm.understand_intent(user_input)
        
        # 2. 规划动作序列
        actions = await self.planner.plan(intent)
        
        # 3. 执行动作
        results = []
        for action in actions:
            result = await self.execute_action(action)
            results.append(result)
            
        # 4. 生成响应
        response = await self.llm.generate_response(results)
        
        return response 