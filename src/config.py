from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    MAX_TOKENS: int = 2000
    TEMPERATURE: float = 0.7
    MODEL_NAME: str = "gpt-4"
    
    class Config:
        env_file = ".env" 