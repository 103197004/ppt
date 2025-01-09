from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.memory import ConversationBufferMemory

class LangChainAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0)
        self.memory = ConversationBufferMemory()
        self.tools = self._setup_tools()
        
    def _setup_tools(self):
        return [
            Tool(
                name="Search",
                func=self._search,
                description="Useful for searching information"
            ),
            Tool(
                name="Calculator",
                func=self._calculate,
                description="Useful for math calculations"
            )
        ] 