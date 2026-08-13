from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

ROLES = ["etudiant", "enseignant", "admin"]

RESOURCE_TYPES = [
    ("cours", "📚 Cours"),
    ("td", "📝 TD"),
    ("corrige", "✅ Corrigé"),
    ("examen", "📄 Examen"),
    ("tuto", "🎥 Tutoriel vidéo"),
    ("tp", "📊 Travaux pratiques"),
    ("doc", "📎 Document complémentaire"),
]


class Filiere(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200), unique=True, nullable=False)
    departement = db.Column(db.String(200), nullable=False)
    ues = db.relationship("UE", backref="filiere", lazy=True)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="etudiant", nullable=False)
    filiere_id = db.Column(db.Integer, db.ForeignKey("filiere.id"), nullable=True)
    annee = db.Column(db.String(50), nullable=True)  # ex: "Master 1"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    filiere = db.relationship("Filiere")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class UE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filiere_id = db.Column(db.Integer, db.ForeignKey("filiere.id"), nullable=False)
    annee = db.Column(db.String(50), nullable=False)      # "Licence 3", "Master 1"...
    semestre = db.Column(db.String(50), nullable=False)   # "Semestre 1 (S5)"...
    code = db.Column(db.String(30), nullable=False)
    nom = db.Column(db.String(300), nullable=False)
    credit = db.Column(db.Integer, default=0)

    matieres = db.relationship("Matiere", backref="ue", lazy=True, cascade="all, delete-orphan")


class Matiere(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ue_id = db.Column(db.Integer, db.ForeignKey("ue.id"), nullable=False)
    sigle = db.Column(db.String(30))
    nom = db.Column(db.String(300), nullable=False)
    volume_horaire = db.Column(db.Integer, default=0)
    coefficient = db.Column(db.Integer, default=0)

    ressources = db.relationship("Ressource", backref="matiere", lazy=True, cascade="all, delete-orphan")


class Ressource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matiere_id = db.Column(db.Integer, db.ForeignKey("matiere.id"), nullable=False)
    type = db.Column(db.String(20), nullable=False)  # cours/td/corrige/examen/tuto/tp/doc
    titre = db.Column(db.String(300), nullable=False)
    filename = db.Column(db.String(300), nullable=False)   # nom stocké sur disque
    original_name = db.Column(db.String(300), nullable=False)
    uploaded_by_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    uploaded_by = db.relationship("User")

    def type_label(self):
        return dict(RESOURCE_TYPES).get(self.type, self.type)


class Favori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    ressource_id = db.Column(db.Integer, db.ForeignKey("ressource.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    ressource = db.relationship("Ressource")

    __table_args__ = (db.UniqueConstraint("user_id", "ressource_id", name="uniq_favori"),)


class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    epingle = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    author = db.relationship("User")
