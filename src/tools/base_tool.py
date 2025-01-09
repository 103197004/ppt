from typing import Protocol, Dict, Any
from abc import ABC, abstractmethod

class BaseTool(ABC):
    """工具基类"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """工具名称"""
        pass
        
    @property
    @abstractmethod
    def description(self) -> str:
        """工具描述"""
        pass
        
    @abstractmethod
    async def execute(self, **params) -> Any:
        """执行工具"""
        pass

class SearchTool(BaseTool):
    """搜索工具示例"""
    
    @property
    def name(self) -> str:
        return "search"
        
    @property
    def description(self) -> str:
        return "搜索互联网上的信息"
        
    async def execute(self, query: str) -> List[Dict]:
        # 实现搜索逻辑
        results = await search_implementation(query)
        return results 