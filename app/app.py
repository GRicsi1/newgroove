import os
import re
from urllib.parse import quote

from flask import Flask, jsonify, send_from_directory, abort

from .config import Config
from .site_config import SITE


def _natural_key(name):
    return [int(p) if p.isdigit() else p.lower() for p in re.split(r"(\d+)", name)]


def gallery_files():
    """"""
    try:
        names = [n for n in os.listdir(Config.GALLERY_DIR)
                 if os.path.splitext(n)[1].lower() in Config.GALLERY_EXTENSIONS
                 and os.path.isfile(os.path.join(Config.GALLERY_DIR, n))]
    except OSError:
        return []
    return sorted(names, key=_natural_key)[:Config.GALLERY_MAX_IMAGES]


def create_app():
    app = Flask(__name__, static_folder=None)

    @app.after_request
    def security_headers(r):
        r.headers["X-Content-Type-Options"] = "nosniff"
        r.headers["X-Frame-Options"] = "DENY"
        r.headers["Referrer-Policy"] = "no-referrer"
        r.headers["Permissions-Policy"] = "geolocation=(), camera=(), microphone=()"
        r.headers["Content-Security-Policy"] = (
            "default-src 'self'; img-src 'self' data:; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "font-src https://fonts.gstatic.com; script-src 'self' 'unsafe-inline'; "
            "frame-ancestors 'none'; base-uri 'self'; form-action 'none'")
        return r

    @app.get("/")
    def index():
        return send_from_directory(Config.FRONTEND_DIR, "index.html")

    @app.get("/referenciak/<path:filename>")
    def gallery_image(filename):
        if filename not in gallery_files():
            abort(404)
        return send_from_directory(Config.GALLERY_DIR, filename, max_age=3600)

    @app.get("/api/site")
    def api_site():
        return jsonify(SITE)

    @app.get("/api/gallery")
    def api_gallery():
        items = []
        for n in gallery_files():
            v = int(os.path.getmtime(os.path.join(Config.GALLERY_DIR, n)))   # képcsere után frissül
            items.append({"url": f"/referenciak/{quote(n)}?v={v}"})
        return jsonify({"items": items})

    return app


app = create_app()
