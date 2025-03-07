from .base import NotifierStrategy

class ConsoleNotifier(NotifierStrategy):
    def notify(self, count):
        print(f"✅ Scraping completed. {count} new products added.")
