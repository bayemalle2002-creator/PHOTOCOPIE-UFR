import os
import uuid
from functools import wraps

from flask import (Flask, render_template, redirect, url_for, request,
                    flash, send_from_directory, abort, jsonify)
from flask_login import (login_user, logout_user, login_required,
                          current_user)
from werkzeug.utils import secure_filename

from config import Config
from extensions import db, login_manager
from models import (User, Filiere, UE, Matiere, Ressource, Favori,
                     ForumPost, RESOURCE_TYPES)
from seed_data import seed


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    with app.app_context():
        db.create_all()
        seed()

    register_routes(app)
    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def role_required(*roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            if current_user.role not in roles:
                abort(403)
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS


def register_routes(app):

    # ---------------------------------------------------------- ACCUEIL
    @app.route("/")
    def accueil():
        return render_template("accueil.html")

    # ---------------------------------------------------------- AUTH
    @app.route("/inscription", methods=["GET", "POST"])
    def inscription():
        filieres = Filiere.query.order_by(Filiere.departement, Filiere.nom).all()
        if request.method == "POST":
            nom = request.form["nom"].strip()
            email = request.form["email"].strip().lower()
            password = request.form["password"]
            role = request.form.get("role", "etudiant")
            filiere_id = request.form.get("filiere_id") or None
            annee = request.form.get("annee") or None

            if role not in ("etudiant", "enseignant"):
                role = "etudiant"

            if User.query.filter_by(email=email).first():
                flash("Un compte existe déjà avec cet e-mail.", "error")
                return render_template("inscription.html", filieres=filieres)

            user = User(nom=nom, email=email, role=role,
                        filiere_id=filiere_id, annee=annee)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Compte créé, bienvenue !", "success")
            return redirect(url_for("accueil"))

        return render_template("inscription.html", filieres=filieres)

    @app.route("/connexion", methods=["GET", "POST"])
    def connexion():
        if request.method == "POST":
            email = request.form["email"].strip().lower()
            password = request.form["password"]
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password):
                login_user(user)
                flash("Connexion réussie.", "success")
                return redirect(url_for("accueil"))
            flash("E-mail ou mot de passe incorrect.", "error")
        return render_template("connexion.html")

    @app.route("/deconnexion")
    @login_required
    def deconnexion():
        logout_user()
        return redirect(url_for("accueil"))

    # ---------------------------------------------------------- MAQUETTE
    @app.route("/maquette")
    def maquette():
        filieres = Filiere.query.order_by(Filiere.departement, Filiere.nom).all()
        filiere_id = request.args.get("filiere_id", type=int)
        annee = request.args.get("annee", "Licence 3")
        semestre = request.args.get("semestre", "Semestre 1")

        if not filiere_id and filieres:
            filiere_id = next((f.id for f in filieres if f.nom == "DIC Géomètre-Topographe"),
                               filieres[0].id)

        ues = UE.query.filter_by(filiere_id=filiere_id, annee=annee, semestre=semestre).all()

        return render_template("maquette.html", filieres=filieres, ues=ues,
                                filiere_id=filiere_id, annee=annee, semestre=semestre)

    @app.route("/matiere/<int:matiere_id>")
    def matiere_detail(matiere_id):
        matiere = Matiere.query.get_or_404(matiere_id)
        favoris_ids = set()
        if current_user.is_authenticated:
            favoris_ids = {f.ressource_id for f in Favori.query.filter_by(user_id=current_user.id)}
        return render_template("matiere.html", matiere=matiere,
                                resource_types=RESOURCE_TYPES, favoris_ids=favoris_ids)

    @app.route("/ressource/<int:ressource_id>/telecharger")
    @login_required
    def telecharger(ressource_id):
        r = Ressource.query.get_or_404(ressource_id)
        return send_from_directory(app.config["UPLOAD_FOLDER"], r.filename,
                                    as_attachment=True, download_name=r.original_name)

    @app.route("/favori/<int:ressource_id>", methods=["POST"])
    @login_required
    def toggle_favori(ressource_id):
        existing = Favori.query.filter_by(user_id=current_user.id, ressource_id=ressource_id).first()
        if existing:
            db.session.delete(existing)
            db.session.commit()
            return jsonify({"favori": False})
        db.session.add(Favori(user_id=current_user.id, ressource_id=ressource_id))
        db.session.commit()
        return jsonify({"favori": True})

    # ---------------------------------------------------------- ESPACE ETUDIANT
    @app.route("/espace-etudiant")
    @login_required
    def espace_etudiant():
        favoris = Favori.query.filter_by(user_id=current_user.id).all()
        mes_ue = []
        if current_user.filiere_id and current_user.annee:
            mes_ue = UE.query.filter_by(filiere_id=current_user.filiere_id,
                                         annee=current_user.annee).all()
        return render_template("espace_etudiant.html", favoris=favoris, mes_ue=mes_ue)

    # ---------------------------------------------------------- ESPACE ENSEIGNANT
    @app.route("/espace-enseignant")
    @role_required("enseignant", "admin")
    def espace_enseignant():
        filieres = Filiere.query.order_by(Filiere.departement, Filiere.nom).all()
        recentes = Ressource.query.order_by(Ressource.uploaded_at.desc()).limit(15).all()
        return render_template("espace_enseignant.html", filieres=filieres, recentes=recentes,
                                resource_types=RESOURCE_TYPES)

    @app.route("/api/ues")
    @role_required("enseignant", "admin")
    def api_ues():
        filiere_id = request.args.get("filiere_id", type=int)
        annee = request.args.get("annee")
        semestre = request.args.get("semestre")
        q = UE.query.filter_by(filiere_id=filiere_id)
        if annee:
            q = q.filter_by(annee=annee)
        if semestre:
            q = q.filter_by(semestre=semestre)
        return jsonify([{"id": ue.id, "label": f"{ue.code} — {ue.nom}"} for ue in q.all()])

    @app.route("/api/matieres")
    @role_required("enseignant", "admin")
    def api_matieres():
        ue_id = request.args.get("ue_id", type=int)
        matieres = Matiere.query.filter_by(ue_id=ue_id).all()
        return jsonify([{"id": m.id, "label": f"{m.sigle} — {m.nom}"} for m in matieres])

    @app.route("/ressource/ajouter", methods=["POST"])
    @role_required("enseignant", "admin")
    def ajouter_ressource():
        matiere_id = request.form.get("matiere_id", type=int)
        type_ = request.form.get("type")
        titre = request.form.get("titre", "").strip()
        fichier = request.files.get("fichier")

        if not (matiere_id and type_ and titre and fichier and fichier.filename):
            flash("Merci de remplir tous les champs et de choisir un fichier.", "error")
            return redirect(url_for("espace_enseignant"))

        if not allowed_file(fichier.filename):
            flash("Type de fichier non autorisé.", "error")
            return redirect(url_for("espace_enseignant"))

        original_name = secure_filename(fichier.filename)
        stored_name = f"{uuid.uuid4().hex}_{original_name}"
        fichier.save(os.path.join(app.config["UPLOAD_FOLDER"], stored_name))

        db.session.add(Ressource(matiere_id=matiere_id, type=type_, titre=titre,
                                  filename=stored_name, original_name=original_name,
                                  uploaded_by_id=current_user.id))
        db.session.commit()
        flash("Document publié.", "success")
        return redirect(url_for("espace_enseignant"))

    @app.route("/ressource/<int:ressource_id>/supprimer", methods=["POST"])
    @role_required("enseignant", "admin")
    def supprimer_ressource(ressource_id):
        r = Ressource.query.get_or_404(ressource_id)
        try:
            os.remove(os.path.join(app.config["UPLOAD_FOLDER"], r.filename))
        except OSError:
            pass
        db.session.delete(r)
        db.session.commit()
        flash("Document supprimé.", "success")
        return redirect(url_for("espace_enseignant"))

    # ---------------------------------------------------------- COMMUNAUTE
    @app.route("/communaute", methods=["GET", "POST"])
    @login_required
    def communaute():
        if request.method == "POST":
            contenu = request.form.get("contenu", "").strip()
            if contenu:
                db.session.add(ForumPost(author_id=current_user.id, contenu=contenu))
                db.session.commit()
            return redirect(url_for("communaute"))
        posts = ForumPost.query.order_by(ForumPost.epingle.desc(), ForumPost.created_at.desc()).all()
        return render_template("communaute.html", posts=posts)

    # ---------------------------------------------------------- ERREURS
    @app.errorhandler(403)
    def forbidden(e):
        return render_template("erreur.html", code=403,
                                message="Accès réservé aux enseignants et administrateurs."), 403

    @app.errorhandler(404)
    def not_found(e):
        return render_template("erreur.html", code=404, message="Page introuvable."), 404


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
