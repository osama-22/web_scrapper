from .base import NotifierStrategy

class EmailNotifier(NotifierStrategy):
    def notify(self, count):
        # TODO: Implement email sending logic
        print(f"📧 Sending email: {count} new products added.")
