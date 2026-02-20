"""Real-time cost tracking and budgeting."""

from typing import Dict, Any


class CostTracker:
    """Tracks LLM costs and manages budgets."""
    
    def __init__(self, budget: float = 1000.0):
        self.budget = budget
        self.spent = 0.0
        self.logs = []
    
    def log_call(self, provider: str, cost: float) -> None:
        """Log API call cost."""
        self.spent += cost
        self.logs.append({
            "provider": provider,
            "cost": cost,
            "total": self.spent
        })
    
    def get_budget_remaining(self) -> float:
        """Get remaining budget."""
        return self.budget - self.spent
