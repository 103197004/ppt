from typing import List, Dict, Any
from .base_agent import BaseAgent
from ..tools.tool_system import ToolRegistry
from ..memory.memory_system import Memory

class Assistant(BaseAgent):
    """智能助手主类"""
    
    def __init__(self, config: Dict[str, Any]):
        self.llm = self._init_llm(config)
        self.memory = Memory()
        self.tools = ToolRegistry()
        self.parser = IntentParser(self.llm)
        
    async def chat(self, user_input: str) -> str:
        """处理用户输入"""
        try:
            # 1. 意图解析
            intent = await self.parser.parse(user_input)
            
            # 2. 上下文获取
            context = await self.memory.get_relevant_context(intent)
            
            # 3. 工具调用规划
            plan = await self.plan_actions(intent, context)
            
            # 4. 执行工具调用
            results = await self.execute_plan(plan)
            
            # 5. 生成响应
            response = await self.generate_response(results, context)
            
            # 6. 更新记忆
            await self.memory.add({
                'input': user_input,
                'intent': intent,
                'response': response
            })
            
            return response
            
        except Exception as e:
            return f"抱歉，处理您的请求时出现错误: {str(e)}" 