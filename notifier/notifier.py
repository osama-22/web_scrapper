from .base import NotifierStrategy
from .console_notifier import ConsoleNotifier

class Notifier:
    def __init__(self, strategy: NotifierStrategy = ConsoleNotifier()):
        self.strategy = strategy  # Allows dynamic strategy setting

    def set_strategy(self, strategy: NotifierStrategy):
        """Change the notification strategy at runtime."""
        self.strategy = strategy  

    def notify(self, count):
        """Send notification using the selected strategy."""
        self.strategy.notify(count)
