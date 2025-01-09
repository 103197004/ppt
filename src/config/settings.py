from pydantic import BaseSettings
from typing import Dict, Any

class Settings(BaseSettings):
    """配置类"""
    
    # LLM配置
    LLM_MODEL: str = "gpt-4"
    LLM_TEMPERATURE: float = 0.7
    LLM_MAX_TOKENS: int = 2000
    
    # 记忆配置
    MEMORY_MAX_ITEMS: int = 1000
    MEMORY_TTL: int = 3600  # 1小时
    
    # 向量存储配置
    VECTOR_DIMENSION: int = 1536
    VECTOR_SIMILARITY_THRESHOLD: float = 0.8
    
    # API配置
    API_TIMEOUT: int = 30
    API_MAX_RETRIES: int = 3
    
    class Config:
        env_file = ".env" 