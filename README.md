# Campus UT — Plateforme d'accompagnement des étudiants (UFR-SI)

Application Flask + SQLAlchemy avec comptes utilisateurs (étudiant / enseignant / admin),
maquette pédagogique dynamique, upload de documents et forum communautaire.

La maquette **Ingénieur Géomètre-Topographe** (L3 → M2, 6 semestres) est déjà chargée
avec les vraies UE/matières. Les autres filières UFR-SI existent dans la base
(sélectionnables à l'inscription) mais sans UE — ajoute leur PDF officiel et je fais pareil.

## Installation

```bash
cd plateforme
python3 -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

## Base de données

Par défaut l'app utilise **SQLite** (fichier `plateforme.db`, créé automatiquement) —
pratique pour tester tout de suite sans rien installer.

Pour utiliser **PostgreSQL** (recommandé en production) :

```bash
# 1. Crée la base
createdb plateforme_ufrsi

# 2. Définis la variable d'environnement avant de lancer l'app
export DATABASE_URL="postgresql://utilisateur:motdepasse@localhost:5432/plateforme_ufrsi"
```

Sur Windows (PowerShell) : `$env:DATABASE_URL="postgresql://..."`

Au premier lancement, les tables sont créées automatiquement et la base est peuplée
avec les filières UFR-SI et la maquette Géomètre-Topographe (`seed_data.py`).

## Lancer l'application

```bash
python app.py
```

Puis ouvre **http://localhost:5000**

⚠️ Si tu avais déjà lancé l'app avant l'ajout des maquettes Génie Civil,
Géotechnique et Licence QHSE : le peuplement ne se relance pas automatiquement
sur une base existante. Supprime `plateforme.db` (SQLite) — ou vide les tables
si tu es sur PostgreSQL — puis relance `python app.py` pour recharger tout.

## Comptes

- Inscris-toi via "Créer un compte" en choisissant le rôle **Étudiant** ou **Enseignant**.
- Un compte **Enseignant** a accès à l'espace enseignant (`/espace-enseignant`) pour
  publier des cours, TD, corrigés, examens, tutoriels, TP et documents.
- Pour un rôle **Admin**, modifie manuellement le champ `role` de l'utilisateur en base
  (`admin` au lieu de `enseignant`) — il n'y a pas encore d'interface de promotion.

## Fichiers uploadés

Stockés dans `uploads/` (créé automatiquement), avec un nom unique généré pour éviter
les collisions. Le nom d'origine est conservé pour le téléchargement.
⚠️ Ce dossier n'est pas fait pour la production à grande échelle — pour un vrai
déploiement, migre vers un stockage objet (S3 / MinIO) quand le volume grossira.

## Structure

```
app.py            → routes et logique
models.py         → schéma de la base (User, Filiere, UE, Matiere, Ressource, Favori, ForumPost)
seed_data.py       → filières réelles + maquette Géomètre-Topographe
config.py          → configuration (base de données, dossier upload, extensions autorisées)
templates/          → pages HTML (thème visuel "carnet d'arpenteur")
static/css/style.css → styles
uploads/            → fichiers déposés par les enseignants
```

## Prochaines étapes possibles

- Suivi de progression réel par étudiant (ressources consultées)
- Modération du forum (signalement, rôle délégué)
- Notifications (nouveau document déposé, réponse à un post)
- Recherche transversale par mot-clé
- Promotion admin via interface au lieu de modifier la base à la main
