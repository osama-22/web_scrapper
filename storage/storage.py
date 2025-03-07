from .base import StorageStrategy
from .json_storage import JSONStorage

class Storage:
    def __init__(self, strategy: StorageStrategy = JSONStorage()):
        self.strategy = strategy  # Allows dynamic strategy setting

    def set_strategy(self, strategy: StorageStrategy):
        """Change the storage strategy at runtime."""
        self.strategy = strategy  

    def save(self, data):
        """Save data using the selected storage strategy."""
        return self.strategy.save(data)
