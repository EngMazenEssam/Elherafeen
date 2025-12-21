from app.config import DATA_DIR
from app.utils.json_handler import JsonHandler


class ApprovedRepository:
    def __init__(self):
        self.file = DATA_DIR / "products.json"
        self.json_handler = JsonHandler()

    def add(self, product):
        data = self.json_handler.read(self.file)
        if not isinstance(data, list):
            data = []

        data.append(product)

        self.json_handler.write(self.file, data)
