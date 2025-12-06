import os
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent

DATA_DIR: Path = BASE_DIR / "data"

USERS_FILE: Path = DATA_DIR / "users.json"

SECRET_KEY: str = "change-this-secret-key"
