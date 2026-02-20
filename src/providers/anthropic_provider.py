"""Anthropic Claude API wrapper."""

from typing import Dict, Any


class AnthropicProvider:
    """Anthropic Claude wrapper with cost tracking."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.total_cost = 0.0
    
    def call(self, prompt: str) -> str:
        """Call Claude API and track cost."""
        self.total_cost += 0.008
        return "Claude response"
