from typing import List, Dict
import numpy as np
from datetime import datetime

class VectorStore:
    """向量存储"""
    
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model
        self.vectors = []
        self.metadata = []
        
    async def add(self, text: str, metadata: Dict):
        """添加文本到向量存储"""
        vector = await self.embedding_model.embed(text)
        self.vectors.append(vector)
        self.metadata.append({
            **metadata,
            'timestamp': datetime.now()
        })
        
    async def search(self, query: str, limit: int = 5) -> List[Dict]:
        """搜索相似内容"""
        query_vector = await self.embedding_model.embed(query)
        
        # 计算相似度
        similarities = [
            np.dot(query_vector, vec) 
            for vec in self.vectors
        ]
        
        # 获取最相似的结果
        top_indices = np.argsort(similarities)[-limit:]
        
        return [self.metadata[i] for i in top_indices] 