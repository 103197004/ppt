from datetime import datetime
from typing import List, Dict
import tiktoken

class ConversationMemory:
    def __init__(self, max_tokens: int = 2000):
        self.messages: List[Dict] = []
        self.max_tokens = max_tokens
        self.encoder = tiktoken.get_encoding("cl100k_base")
        
    def add_message(self, role: str, content: str):
        """添加消息"""
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now()
        })
        self._compress_if_needed()
        
    def _compress_if_needed(self):
        """压缩历史消息"""
        current_tokens = self._count_tokens()
        if current_tokens > self.max_tokens:
            self._summarize_old_messages()
            
    def _count_tokens(self) -> int:
        """计算当前消息的token数量"""
        all_text = " ".join([msg["content"] for msg in self.messages])
        return len(self.encoder.encode(all_text))
        
    def _summarize_old_messages(self):
        """总结旧消息"""
        # TODO: 使用LLM对早期消息进行摘要
        pass

    def get_recent_messages(self, n: int = 10) -> List[Dict]:
        """获取最近的n条消息"""
        return self.messages[-n:] 