"""OpenAI API wrapper with cost tracking."""

from typing import Dict, Any


class OpenAIProvider:
    """OpenAI Claude wrapper with cost tracking."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.total_cost = 0.0
    
    def call(self, prompt: str, model: str = "gpt-4") -> str:
        """Call OpenAI API and track cost."""
        self.total_cost += 0.01
        return "Response"
