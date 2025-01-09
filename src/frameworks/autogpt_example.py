class AutoGPTAgent:
    def __init__(self):
        self.memory = PineconeMemory()
        self.tools = ToolManager()
        self.goals = GoalManager()
        
    async def execute_task(self, goal: str):
        """执行任务直到目标完成"""
        while not self.goals.is_completed(goal):
            # 1. 分析当前状态
            current_state = self.memory.get_context()
            
            # 2. 决定下一步行动
            next_action = await self.plan_next_action(current_state)
            
            # 3. 执行行动
            result = await self.tools.execute(next_action)
            
            # 4. 更新记忆
            self.memory.add(result) 