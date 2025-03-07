import json
import os
from .base import StorageStrategy

class JSONStorage(StorageStrategy):
    def __init__(self, file_name="data/scraped_data.json"):
        self.file_name = file_name
        dir_name = os.path.dirname(self.file_name)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

    def save(self, data):
        try:
            with open(self.file_name, "r") as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        new_count = len(data)
        with open(self.file_name, "w") as f:
            json.dump(existing_data + data, f, indent=4)

        return new_count
