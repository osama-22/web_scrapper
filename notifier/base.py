from abc import ABC, abstractmethod

class NotifierStrategy(ABC):
    @abstractmethod
    def notify(self, count):
        pass
