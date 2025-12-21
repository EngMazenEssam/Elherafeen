import json
import os
from threading import Lock


class JsonHandler:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(JsonHandler, cls).__new__(cls)
        return cls._instance

    def read(self, file_path):
        if not os.path.exists(file_path):
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def write(self, file_path, data):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
