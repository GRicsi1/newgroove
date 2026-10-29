"""gunicorn -w 2 -b 127.0.0.1:8000 "app.app:app"  (+ HTTPS reverse proxy)"""
from app.app import app, gallery_files
from app.config import Config
from app.site_config import SITE, PLACEHOLDER


def main():
    left = sum(1 for k, v in SITE.items() if v == PLACEHOLDER)
    left += sum(1 for a in SITE["artists"] for v in a.values() if v == PLACEHOLDER)
    if left:
        print("Kihagytál valamit")
    print(f"ℹ  Referencia képek: {len(gallery_files())} db (max. {Config.GALLERY_MAX_IMAGES}) a 'referenciak' mappából")
    print("→ http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)


if __name__ == "__main__":
    main()
