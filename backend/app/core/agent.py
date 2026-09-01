"""Core Agent runtime placeholder."""

class Agent:
    def __init__(self, model_provider, tools=None):
        self.model_provider = model_provider
        self.tools = tools or []

    async def run(self, message: str):
        """Execute agent reasoning loop."""
        return await self.model_provider.chat(message)
