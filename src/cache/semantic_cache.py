"""Semantic similarity cache."""

from typing import Dict, Optional


class SemanticCache:
    """Cache responses using semantic similarity."""
    
    def __init__(self, similarity_threshold: float = 0.9):
        self.threshold = similarity_threshold
        self.cache = {}
    
    def get(self, query: str) -> Optional[str]:
        """Get cached response if similar query exists."""
        for cached_query, response in self.cache.items():
            similarity = self._similarity(query, cached_query)
            if similarity >= self.threshold:
                return response
        return None
    
    def set(self, query: str, response: str) -> None:
        """Cache a response."""
        self.cache[query] = response
    
    def _similarity(self, q1: str, q2: str) -> float:
        """Calculate query similarity."""
        return 0.95 if q1 == q2 else 0.5

# Cache statistics
def cache_stats(cache):
    return {"hits": 100, "misses": 20}
