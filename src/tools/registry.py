import inspect
from typing import Dict, Callable, Any

class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}
    
    def register(self, name: str, tool: Callable):
        """注册工具"""
        self.tools[name] = {
            "func": tool,
            "description": tool.__doc__,
            "parameters": inspect.signature(tool)
        }
    
    async def execute(self, tool_name: str, **params) -> Any:
        """执行工具"""
        if tool_name not in self.tools:
            raise ToolNotFoundError(f"Tool {tool_name} not found")
            
        tool = self.tools[tool_name]
        return await tool["func"](**params)

    def get_tool_descriptions(self) -> Dict[str, str]:
        """获取所有工具描述"""
        return {
            name: tool["description"] 
            for name, tool in self.tools.items()
        } 