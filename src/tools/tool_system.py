from typing import Protocol, Dict, Any
from dataclasses import dataclass

@dataclass
class ToolSpec:
    name: str
    description: str
    parameters: Dict[str, Any]
    returns: Any

class Tool(Protocol):
    """工具协议"""
    
    @property
    def spec(self) -> ToolSpec:
        """工具规格"""
        pass
        
    async def execute(self, **params) -> Any:
        """执行工具"""
        pass

class ToolRegistry:
    """工具注册中心"""
    
    def __init__(self):
        self._tools: Dict[str, Tool] = {}
        
    def register(self, tool: Tool):
        """注册工具"""
        self._tools[tool.spec.name] = tool
        
    async def execute(self, tool_name: str, **params) -> Any:
        """执行工具"""
        tool = self._tools.get(tool_name)
        if not tool:
            raise ToolNotFoundError(tool_name)
        return await tool.execute(**params) 