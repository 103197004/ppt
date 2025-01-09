from typing import List, Dict, Any
import numpy as np
from datetime import datetime

class Memory:
    """记忆系统"""
    
    def __init__(self):
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
        
    async def add(self, data: Any):
        """添加记忆"""
        # 短期记忆
        self.short_term.add(data)
        
        # 重要信息存入长期记忆
        if self._is_important(data):
            await self.long_term.store(data)
            
    async def query(self, context: str) -> List[Dict]:
        """查询相关记忆"""
        # 合并短期和长期记忆的查询结果
        st_results = self.short_term.search(context)
        lt_results = await self.long_term.search(context)
        
        return self._merge_results(st_results, lt_results) 