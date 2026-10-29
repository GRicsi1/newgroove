import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
    GALLERY_DIR = os.path.join(BASE_DIR, "referenciak")
    GALLERY_MAX_IMAGES = 10
    GALLERY_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
