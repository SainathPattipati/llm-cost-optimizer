"""Mistral API wrapper."""

from typing import Dict, Any


class MistralProvider:
    """Mistral wrapper with cost tracking."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.total_cost = 0.0
    
    def call(self, prompt: str) -> str:
        """Call Mistral API."""
        self.total_cost += 0.002
        return "Mistral response"
