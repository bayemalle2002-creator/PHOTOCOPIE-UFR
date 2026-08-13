import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-moi-en-production")

    # Par défaut : PostgreSQL. Défini via variable d'environnement DATABASE_URL, ex :
    #   postgresql://utilisateur:motdepasse@localhost:5432/plateforme_ufrsi
    # Si aucune variable n'est définie, on retombe sur SQLite pour pouvoir tester
    # immédiatement sans installer PostgreSQL.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "plateforme.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100 Mo max par fichier

    ALLOWED_EXTENSIONS = {
        "pdf", "doc", "docx", "ppt", "pptx", "xls", "xlsx",
        "jpg", "jpeg", "png", "mp4", "mov", "zip", "dwg"
    }
