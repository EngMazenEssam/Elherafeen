import os
from pathlib import Path

# جذر المشروع (Elherafeen/)
BASE_DIR: Path = Path(__file__).resolve().parent.parent

# فولدر الداتا
DATA_DIR: Path = BASE_DIR / "data"

# ملف اليوزرز
USERS_FILE: Path = DATA_DIR / "users.json"

# secret key بتاعة Flask (غيّرها لأي حاجة عشوائية)
SECRET_KEY: str = "change-this-secret-key"
