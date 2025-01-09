from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class Intent:
    """意图数据类"""
    action: str
    parameters: Dict[str, Any]
    confidence: float
    raw_input: str

class IntentParser:
    """意图解析器"""
    
    def __init__(self, llm):
        self.llm = llm
        
    async def parse(self, user_input: str) -> Intent:
        """解析用户输入的意图"""
        prompt = self._build_intent_prompt(user_input)
        
        # 调用LLM进行意图分析
        response = await self.llm.analyze(prompt)
        
        # 解析LLM返回的结果
        parsed = self._parse_llm_response(response)
        
        return Intent(
            action=parsed['action'],
            parameters=parsed['parameters'],
            confidence=parsed['confidence'],
            raw_input=user_input
        )
        
    def _build_intent_prompt(self, user_input: str) -> str:
        """构建意图分析的prompt"""
        return f"""
        请分析以下用户输入的意图:
        {user_input}
        
        请以JSON格式返回:
        1. action: 意图对应的动作
        2. parameters: 需要的参数
        3. confidence: 置信度
        """ 