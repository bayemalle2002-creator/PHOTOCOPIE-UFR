from extensions import db
from models import Filiere, UE, Matiere

FILIERES = [
    ("DIC Génie Civil", "Département Génie Civil"),
    ("DIC Géomètre-Topographe", "Département Génie Civil"),
    ("Licence Pro Géo-mesures et Aménagement (LP GMA)", "Département Génie Civil"),
    ("Licence Géomatique (L-GMT)", "Département Génie Civil"),
    ("Master Architecture", "Département Génie Civil"),
    ("DIC Géotechnique", "Département Géotechnique"),
    ("Master Recherche Mécanique des Sols, Géotechnique et Modélisation des Terrains", "Département Géotechnique"),
    ("Licence Pro Prospection et Exploitation des Ressources Minérales (L-ResMin)", "Département Génie Géologique, Mines et Eau"),
    ("Master QHSE et Énergie (M-QHS2E)", "Département Génie Géologique, Mines et Eau"),
    ("Licence QHSE", "Département Génie Géologique, Mines et Eau"),
]

# NOTE sur "Semestre 1" / "Semestre 2" : label générique = 1er / 2nd semestre de
# l'année sélectionnée. La numérotation officielle réelle (S1, S3, S5...) varie
# selon la filière et l'année ; on ne la fait plus apparaître dans la clé pour
# garder un seul jeu de sélecteurs valable pour toutes les filières.

# ============================================================
# Ingénieur Géomètre-Topographe — maquette officielle complète
# (source : PDF fourni par l'utilisateur)
# ============================================================
MAQUETTE_GTP = {
    ("Licence 3", "Semestre 1"): [
        ("GTP351", "Anglais – Information et communication", 4, [
            ("GTP3511", "Anglais", 40, 2),
            ("GTP3512", "Information et Communication", 40, 2)]),
        ("GTP352", "Mathématiques-Informatique", 6, [
            ("GTP3521", "Informatique appliquée", 40, 2),
            ("GTP3522", "Probabilité - Statistiques", 40, 2),
            ("GTP3523", "Analyse / Algèbre", 40, 2)]),
        ("GTP353", "Droit", 4, [
            ("GTP3531", "Droit Général", 40, 2),
            ("GTP3532", "Droit Foncier", 40, 2)]),
        ("GTP354", "Géodésie-Astronomie", 4, [
            ("GTP3541", "Géodésie et Techniques Spatiales 1", 40, 2),
            ("GTP3542", "Astronomie 1", 40, 2)]),
        ("GTP355", "Instruments et Méthodes", 2, [
            ("GTP3551", "Instruments et Méthodes 1", 40, 2)]),
        ("GTP356", "DAO I", 3, [
            ("GTP3561", "DAO 1", 60, 3)]),
        ("GTP357", "Topographie-Topométrie", 7, [
            ("GTP3571", "Topométrie 1C", 60, 3),
            ("GTP3572", "TP Topographie 1C", 80, 4)]),
    ],
    ("Licence 3", "Semestre 2"): [
        ("GTP361", "Anglais - Économie et Stratégie d'Entreprise", 4, [
            ("GTP3611", "Anglais", 40, 2),
            ("GTP3612", "Économie et Stratégie d'entreprise", 40, 2)]),
        ("GTP362", "Calcul Scientifique", 2, [
            ("GTP3621", "Matlab", 40, 2)]),
        ("GTP363", "Géomatique", 7, [
            ("GTP3631", "Photogrammétrie 1", 40, 2),
            ("GTP3632", "Cartographie", 40, 2),
            ("GTP3633", "Système d'information Géographique 1", 60, 3)]),
        ("GTP364", "Instruments et Méthodes", 3, [
            ("GTP3641", "Instruments et Méthodes 2", 60, 3)]),
        ("GTP365", "Topographie et Topométrie 1", 10, [
            ("GTP3651", "Projet de Topographie 1", 60, 3),
            ("GTP3652", "TP Topographie 2C", 80, 4),
            ("GTP3653", "Topométrie 2", 60, 3)]),
        ("GTP366", "Pratiques Professionnelles du Géomètre Expert", 2, [
            ("GTP3661", "Pratiques Professionnelles du Géomètre Expert", 20, 2)]),
        ("GTP367", "Cadastre", 2, [
            ("GTP3671", "Cadastre", 40, 2)]),
    ],
    ("Master 1", "Semestre 1"): [
        ("GTP411", "Anglais - Gestion", 4, [
            ("GTP4111", "Anglais", 40, 2),
            ("GTP4112", "Gestion Financière d'Entreprise", 40, 2)]),
        ("GTP412", "Géodésie et Astronomie", 6, [
            ("GTP4121", "Géodésie et Techniques Spatiales 2", 40, 2),
            ("GTP4122", "GNSS", 40, 2),
            ("GTP4123", "Astronomie 2", 40, 2)]),
        ("GTP413", "Géomatique", 5, [
            ("GTP4131", "Photogrammétrie 2", 40, 2),
            ("GTP4132", "Système d'information Géographique 2", 60, 3)]),
        ("GTP414", "Expertise", 6, [
            ("GTP4141", "Expertise foncière", 40, 2),
            ("GTP4142", "Technologie Génie Civil", 40, 2),
            ("GTP4143", "Génie Civil des Réseaux Divers", 40, 2)]),
        ("GTP415", "Instruments et Méthodes-Calcul d'erreurs", 4, [
            ("GTP4151", "Instruments et Méthodes 3", 40, 2),
            ("GTP4152", "Calcul d'erreurs et compensation 1", 40, 2)]),
        ("GTP416", "Topographie-Topométrie 2", 5, [
            ("GTP4161", "TP Topographie 3 (1S+2S)", 40, 2),
            ("GTP4162", "Projet de Topographie 2a", 60, 3)]),
    ],
    ("Master 1", "Semestre 2"): [
        ("GTP421", "Anglais et Dimension Humaine des Organisations", 4, [
            ("GTP4211", "Anglais", 40, 2),
            ("GTP4212", "Dimension Humaine des Organisations", 40, 2)]),
        ("GTP422", "Urbanisme", 2, [
            ("GTP4221", "Expertise et droit de l'urbanisme", 40, 2)]),
        ("GTP423", "DAO II", 3, [
            ("GTP4231", "DAO 2", 60, 3)]),
        ("GTP424", "Géomatique", 4, [
            ("GTP4241", "Système d'information Géographique 3", 40, 2),
            ("GTP4242", "Télédétection 1", 40, 2)]),
        ("GTP425", "Topographie-Topométrie", 5, [
            ("GTP4251", "Méthodes Topographiques et GNSS opérationnel", 40, 2),
            ("GTP4252", "Projet de Topographie 2b", 60, 3)]),
        ("GTP426", "Aménagement", 2, [
            ("GTP4261", "Évaluation Foncière-Agronomie", 40, 2)]),
        ("GTP427", "Stage", 10, [
            ("GTP4271", "Stage ST1", 200, 1)]),
    ],
    ("Master 2", "Semestre 1"): [
        ("GTP531", "Éthique et Management", 6, [
            ("GTP5311", "Éthique", 40, 2),
            ("GTP5312", "Management de Projet", 40, 2),
            ("GTP5313", "Ingénieur et Société", 40, 2)]),
        ("GTP532", "Géodésie", 4, [
            ("GTP5321", "Géodésie et Techniques Spatiales 4", 40, 2),
            ("GTP5322", "Calcul d'erreurs et Compensation 3", 40, 2)]),
        ("GTP533", "Géomatique", 4, [
            ("GTP5331", "Photogrammétrie / MNT4", 40, 2),
            ("GTP5332", "Télédétection 2 / Laser-Radar-grammétrie", 40, 2)]),
        ("GTP534", "Projets", 5, [
            ("GTP5341", "Projet de recherche Technologique", 60, 3),
            ("—", "Projet Topographie", 40, 2)]),
        ("GTP535", "Génie Civil et Topographie", 4, [
            ("GTP5351", "Tracé en Travaux Publics", 40, 2),
            ("GTP5352", "Réorganisation Foncière et Hydraulique", 40, 2)]),
        ("GTP536", "Séminaires et Stages", 6, [
            ("GTP5361", "Séminaires", 20, 1),
            ("GTP5362", "Stage ST2", 120, 5)]),
    ],
    ("Master 2", "Semestre 2"): [
        ("GTP541", "Projet de Fin d'Études", 30, [
            ("GTP5411", "Projet de Fin d'Études d'Ingénieur", 600, 1)]),
    ],
}

# ============================================================
# Ingénieur Génie Civil — maquette (source : PDF fourni)
# NB : le PDF source ne fait apparaître clairement que les colonnes
# Cours/TD-TP pour la plupart des semestres (les colonnes TPE, volume
# total, coefficient et crédit par matière ont été perdues à
# l'extraction). volume_horaire ci-dessous = Cours + TD/TP quand les
# deux sont disponibles ; crédit/coefficient laissés à 0 (non fournis
# de façon fiable) — à corriger si tu renvoies une version plus propre.
# ============================================================
MAQUETTE_GCU = {
    ("Licence 3", "Semestre 1"): [
        ("GCU351", "Anglais-Information Communication", 0, [
            ("GCU3511", "Anglais", 28, 0),
            ("GCU3512", "Information et Communication", 14, 0)]),
        ("GCU352", "Mathématiques - Informatique", 0, [
            ("GCU3521", "Informatique", 28, 0),
            ("GCU3522", "Analyse", 28, 0),
            ("GCU3523", "Algèbre", 28, 0)]),
        ("GCU353", "Mécanique des Milieux Continus et Mécanique des Fluides", 0, [
            ("GCU3531", "Mécanique des Milieux Continus", 42, 0),
            ("GCU3532", "Mécanique des fluides et Hydraulique", 28, 0)]),
        ("GCU354", "Mécanique des Sols", 0, [
            ("GCU3541", "Mécanique des sols", 56, 0)]),
        ("GCU355", "Structures I", 0, [
            ("GCU3551", "Théorie des Poutres", 56, 0)]),
        ("GCU356", "Topographie", 0, [
            ("GCU3561", "Topographie", 28, 0)]),
        ("GCU357", "Dessin et Technologie de Construction", 0, [
            ("GCU3571", "Règles de représentations graphiques", 42, 0),
            ("GCU3572", "Systèmes Constructifs et Sécurité", 42, 0)]),
    ],
    ("Licence 3", "Semestre 2"): [
        ("GCU361", "Économie et Stratégie d'Entreprise", 0, [
            ("GCU3611", "Économie et Stratégie d'Entreprise", 28, 0)]),
        ("GCU362", "Analyse Numérique I", 0, [
            ("GCU3621", "Analyse Numérique", 28, 0),
            ("GCU3622", "Probabilité - Statistiques", 28, 0)]),
        ("GCU363", "Matériaux de Construction et Rhéologie", 0, [
            ("GCU3631", "Matériaux de Construction", 28, 0),
            ("GCU3632", "Loi de comportement", 14, 0)]),
        ("GCU364", "Béton Armé", 0, [
            ("GCU3641", "Béton Armé 1", 56, 0),
            ("GCU3642", "Performance des bétons", 28, 0)]),
        ("GCU365", "Géologie - Ressource en Eau et Hydraulique", 0, [
            ("GCU3651", "Géologie de l'Ingénieur", 28, 0),
            ("GCU3652", "Gestion de la Ressource en Eau", 28, 0),
            ("GCU3653", "Projet de Mécanique des Fluides et Hydraulique", 14, 0)]),
        ("GCU366", "Calcul des ouvrages I", 0, [
            ("GCU3661", "Calcul des Fondations", 42, 0)]),
        ("GCU367", "Structures II", 0, [
            ("GCU3671", "Systèmes de poutres", 56, 0),
            ("GCU3672", "Construction métallique 1", 42, 0)]),
    ],
    ("Master 1", "Semestre 1"): [
        ("GCU411", "Anglais & Gestion", 0, [
            ("GCU4111", "Anglais", 18, 0),
            ("GCU4112", "Gestion financière d'entreprise", 10, 0)]),
        ("GCU412", "Analyse numérique II", 0, [
            ("GCU4121", "Algorithmes Appliquées aux Méthodes Numériques", 20, 0),
            ("GCU4122", "Éléments Finis et Applications", 20, 0)]),
        ("GCU413", "Béton armé II", 0, [
            ("GCU4131", "Béton armé 2", 30, 0)]),
        ("GCU414", "Structure III", 0, [
            ("GCU4141", "Mécanique des Éléments", 18, 0),
            ("GCU4142", "Dynamique des structures", 18, 0),
            ("GCU4143", "Structures et Logiciels", 0, 0)]),
        ("GCU415", "Construction métallique", 0, [
            ("GCU4151", "Construction métallique 2", 28, 0),
            ("GCU4152", "Projet de Construction Métallique", 0, 0)]),
        ("GCU416", "Physique du Bâtiment et VRD", 0, [
            ("GCU4161", "Physique du Bâtiment", 18, 0),
            ("GCU4162", "Thermique", 18, 0),
            ("GCU4163", "Génie Civil des Réseaux Enterrés", 18, 0)]),
    ],
    ("Master 1", "Semestre 2"): [
        ("GCU421", "Management - Innovation", 0, [
            ("GCU4211", "Management de Projet", 28, 0),
            ("GCU4212", "Méthode et Organisation", 14, 0),
            ("GCU4213", "Conception et Innovation", 28, 0)]),
        ("GCU422", "Mathématiques de la décision pour Ingénieurs", 0, [
            ("GCU4221", "Recherche Opérationnelle", 28, 0),
            ("GCU4222", "Différences Finies", 28, 0)]),
        ("GCU423", "Modélisation des structures", 0, [
            ("GCU4231", "Calcul non linéaire des Structures", 28, 0),
            ("GCU4232", "Modélisation avancée des matériaux et des structures", 42, 0)]),
        ("GCU424", "Estimation quantitative et financière des projets", 0, [
            ("GCU4241", "Métré et Étude de Prix", 28, 0)]),
        ("GCU425", "Béton armé et précontraint", 0, [
            ("GCU4251", "Béton précontraint 1", 56, 0),
            ("GCU4252", "Projet de Béton Armé", 28, 0),
            ("GCU4253", "Projet de Béton Précontraint", 28, 0)]),
        ("GCU426", "Infrastructures de Transport I", 0, [
            ("GCU4261", "Trafic & Géométrie routière", 42, 0),
            ("GCU4262", "Transport", 14, 0)]),
        ("GCU427", "Stage", 0, [
            ("GCU4271", "Stage en Entreprise", 28, 0)]),
    ],
    ("Master 2", "Semestre 1"): [
        ("GCU531", "Éthique – Droit", 0, [
            ("GCU5311", "Éthique", 14, 0),
            ("GCU5312", "Droit Général", 28, 0),
            ("GCU5313", "Ingénieur & Société", 14, 0),
            ("GCU5314", "Dimension Humaine des Organisations", 14, 0)]),
        # Option "Structures / Ouvrages"
        ("GCU533", "Structure IV (Option Structures)", 0, [
            ("GCU5331", "Béton Précontraint 2", 28, 0),
            ("GCU5332", "Construction Bois", 28, 0),
            ("GCU5333", "Construction Métallique et Mixte", 28, 0)]),
        ("GCU534", "Dynamique des Sols (Option Structures)", 0, [
            ("GCU5341", "Dynamique des Sols et Parasismique", 28, 0)]),
        ("GCU535", "Calcul des ouvrages II (Option Structures)", 0, [
            ("GCU5351", "Soutènements & Stabilité des pentes", 28, 0)]),
        ("GCU536", "Projets (Option Structures)", 0, [
            ("GCU5361", "Projet Construction Mixte", 28, 0),
            ("GCU5362", "Projet de Construction Bois", 28, 0),
            ("GCU5363", "Projet de Géotechnique", 28, 0),
            ("GCU5364", "PRT - Projet de Recherche Technologique (Anglais)", 28, 0)]),
        ("GCU537", "Infrastructures de transport II (Option Structures)", 0, [
            ("GCU5371", "Géotechnique routière", 56, 0)]),
        ("GCU538", "Technologies des grands ouvrages", 0, [
            ("GCU5381", "Technologies des grands ouvrages", 42, 0)]),
        # Option "Aménagements Hydrauliques"
        ("GCU533H", "Aménagements Hydrauliques (Option Hydraulique)", 0, [
            ("GCU5331H", "Aménagement des bassins et des rivières", 42, 0),
            ("GCU5332H", "Barrage", 42, 0)]),
        ("GCU534H", "Hydrodynamique & hydraulique (Option Hydraulique)", 0, [
            ("GCU5341H", "Hydrodynamique environnementale des fluides", 42, 0),
            ("GCU5342H", "Projet d'Aménagement Hydraulique", 28, 0)]),
        ("GCU535H", "Mécanique des Terrains (Option Hydraulique)", 0, [
            ("GCU5351H", "Mécanique des Roches", 28, 0),
            ("GCU5352H", "Soutènements & Stabilité des pentes", 28, 0)]),
        ("GCU536H", "Projets (Option Hydraulique)", 0, [
            ("GCU5361H", "Projet Routes", 28, 0),
            ("GCU5362H", "PRT - Projet de Recherche Technologique + Anglais", 28, 0)]),
        ("GCU537H", "Ouvrages et urbanisme (Option Hydraulique)", 0, [
            ("GCU5371H", "Technologie des Grands Ouvrages", 42, 0),
            ("GCU5372H", "Urbanisme", 42, 0)]),
    ],
    ("Master 2", "Semestre 2"): [
        ("GCU541", "PFE", 0, [
            ("GCU5411", "Projet de fin d'études", 600, 0)]),
    ],
}

# ============================================================
# Ingénieur Géotechnique — maquette (source : PDF fourni)
# volume_horaire = VHT (volume horaire total) de la matière quand
# disponible ; crédit/coefficient = valeurs indiquées au niveau de
# l'UE dans le PDF (appliquées à toutes les matières de l'UE).
# ============================================================
MAQUETTE_GGT = {
    ("Licence 3", "Semestre 1"): [
        ("GGT351", "Anglais-Information-Communication", 3, [
            ("GGT3511", "Anglais", 40, 2),
            ("GGT3512", "Information et Communication", 20, 2)]),
        ("GGT352", "Mathématiques - Informatique", 6, [
            ("GGT3521", "Informatique", 40, 5),
            ("GGT3522", "Analyse", 40, 5),
            ("GGT3523", "Algèbre", 40, 5)]),
        ("GGT353", "Mécanique des Milieux Continus", 4, [
            ("GGT3531", "Mécanique des Milieux Continus", 80, 4)]),
        ("GGT354", "Mécanique des Sols", 6, [
            ("GGT3541", "Mécanique des sols", 80, 5),
            ("GGT3542", "Identification Physique des Sols", 40, 5)]),
        ("GGT355", "Résistance des matériaux", 4, [
            ("GGT3551", "Résistance des matériaux", 80, 4)]),
        ("GGT356", "Topographie", 2, [
            ("GGT3561", "Topographie", 40, 2)]),
        ("GGT357", "Géologie", 5, [
            ("GGT3571", "Géologie Générale", 60, 4),
            ("GGT3572", "TP Cartographie", 40, 4)]),
    ],
    ("Licence 3", "Semestre 2"): [
        ("GGT361", "Économie et Stratégie d'Entreprise", 2, [
            ("GGT3611", "Économie et Stratégie d'Entreprise", 40, 2)]),
        ("GGT362", "Analyse numérique I", 4, [
            ("GGT3621", "Analyse Numérique", 40, 4),
            ("GGT3622", "Probabilité - Statistiques", 40, 4)]),
        ("GGT363", "Matériaux de construction – Hydraulique des terrains", 4, [
            ("GGT3631", "Matériaux de Construction", 40, 4),
            ("GGT3632", "Hydraulique des Terrains", 40, 4)]),
        ("GGT364", "Structure et Béton Armé", 5, [
            ("GGT3641", "Béton Armé 1 – Calcul BA", 60, 4),
            ("GGT3642", "TP Résistance des Matériaux", 40, 4)]),
        ("GGT365", "Dessin & Technique de Travaux", 6, [
            ("GGT3661", "Dessin Génie Civil et DAO", 60, 3),
            ("GGT3662", "Technique de travaux et Visite Technique", 60, 3)]),
        ("GGT366", "Calcul des Ouvrages I", 4, [
            ("GGT3663", "Calcul des Fondations", 80, 4)]),
        ("GGT367", "Exploration du Milieu", 5, [
            ("GGT3671", "Géophysique 1", 60, 5),
            ("GGT3672", "Essais in Situ", 40, 5)]),
    ],
    ("Master 1", "Semestre 1"): [
        ("GGT411", "Anglais et Gestion", 3, [
            ("GGT4111", "Anglais", 40, 2),
            ("GGT4112", "Gestion Financière d'Entreprise", 20, 2)]),
        ("GGT412", "Analyse Numérique II", 4, [
            ("GGT4121", "Algorithmes Appliquées aux Méthodes Numériques", 40, 4),
            ("GGT4122", "Éléments Finis et Applications", 40, 4)]),
        ("GGT413", "Mécanique des Roches", 3, [
            ("GGT4131", "Mécanique des Roches", 60, 3)]),
        ("GGT414", "Modélisation des sols et Structures", 8, [
            ("GGT4141", "Calculs de Structures", 80, 5),
            ("GGT4142", "Modélisation des Sols", 80, 5)]),
        ("GGT415", "Géologie Appliquée", 5, [
            ("GGT4151", "Géologie Appliquée", 60, 4),
            ("GGT4152", "Géologie Appliquée aux Mouvements de Terrains", 40, 4)]),
        ("GGT416", "Hydrologie & Hydrogéologie", 4, [
            ("GGT4161", "Hydrologie Générale", 40, 4),
            ("GGT4162", "Hydrogéologie", 40, 4)]),
        ("GGT417", "Géophysique II", 3, [
            ("GGT4171", "Géophysique 2", 60, 4)]),
    ],
    ("Master 1", "Semestre 2"): [
        ("GGT421", "Management", 2, [
            ("GGT4211", "Management de Projets", 40, 2)]),
        ("GGT422", "Ingénierie des Roches et Cartographie de Terrains", 5, [
            ("GGT4221", "Ingénierie des Roches", 60, 5),
            ("GGT4222", "Stage de Cartographie de Terrain", 40, 5)]),
        ("GGT423", "Mathématiques de la Décision pour Ingénieurs", 6, [
            ("GGT4231", "Recherche Opérationnelle", 40, 5),
            ("GGT4232", "Différences finies", 40, 5),
            ("GGT4233", "Fiabilité des Ouvrages en Terre", 40, 5)]),
        ("GGT424", "Béton Armé II", 3, [
            ("GGT4241", "Béton Armé 2", 60, 3)]),
        ("GGT425", "Calcul des Ouvrages II", 8, [
            ("GGT4251", "Digues et Barrages", 60, 5),
            ("GGT4252", "Stabilité des Pentes", 40, 5),
            ("GGT4253", "Ouvrages de Soutènement", 60, 5)]),
        ("GGT426", "Infrastructures de Transport I", 4, [
            ("GGT4261", "Trafic & Géométrie Routière", 60, 4),
            ("GGT4262", "Transport", 20, 4)]),
        ("GGT427", "Métrologie", 2, [
            ("GGT4271", "Électronique et Capteurs & Métrologie", 40, 2)]),
    ],
    ("Master 2", "Semestre 1"): [
        ("GGT531", "Éthique et Droit", 3, [
            ("GGT5311", "Éthique", 20, 2),
            ("GGT5312", "Droit Général", 40, 2)]),
        ("GGT532", "Projets", 6, [
            ("GGT5321", "Projet Géophysique", 40, 5),
            ("GGT5322", "Projet Route", 40, 5),
            ("GGT5323", "Projet de Recherche Technologique (Anglais)", 40, 5)]),
        ("GGT533", "Risques Naturels et Dynamique des Sols", 4, [
            ("GGT5331", "Risques Naturels", 40, 3),
            ("GGT5332", "Dynamique des sols et Parasismique", 40, 3)]),
        ("GGT534", "Amélioration des Sols & Géotechnique de l'Environnement", 5, [
            ("GGT5341", "Amélioration et Renforcement des Sols", 60, 5),
            ("GGT5342", "Pollution des Sols - Environnement", 60, 5)]),
        ("GGT535", "Géophysique Appliquée", 2, [
            ("GGT5351", "Géophysique Appliquée", 40, 4)]),
        ("GGT536", "Infrastructures de Transport II", 4, [
            ("GGT5361", "Géotechnique Routière", 80, 5)]),
        ("GGT537", "Technologie des Ouvrages", 6, [
            ("GGT5371", "Géotechnique ferroviaire & Aérodromes", 60, 4),
            ("GGT5372", "Ouvrages souterrains", 40, 4)]),
    ],
    ("Master 2", "Semestre 2"): [
        ("GGT541", "PFE", 30, [
            ("GGT5411", "Projet de Fin d'Études d'Ingénieur", 600, 5)]),
    ],
}

# ============================================================
# Licence QHSE — maquette (source : fichier Excel fourni)
# NB : le fichier source ne donne ni volume horaire ni crédit/coef
# par matière (seulement UE / sigle / intitulé) — laissés à 0.
# ============================================================
MAQUETTE_QHSE = {
    ("Licence 1", "Semestre 1"): [
        ("PHY1120", "Physique", 0, [
            ("1PHY1120", "Introduction à la physique générale", 0, 0),
            ("2PHY1120", "Métrologie", 0, 0)]),
        ("GSC1121", "Géosciences environnementales", 0, [
            ("1GSC1121", "Géologie de l'environnement", 0, 0),
            ("2GSC1121", "Géomorphologie", 0, 0)]),
        ("CHM1122", "Chimie", 0, [
            ("1CHM1122", "Chimie Physique", 0, 0),
            ("2CHM1122", "Chimie de l'environnement", 0, 0)]),
        ("HYD1123", "Ressources naturelles et Biologie", 0, [
            ("1HYD1123", "Ressources en eau", 0, 0),
            ("2HYD1123", "Ressources minérales et énergétiques", 0, 0),
            ("3HYD1123", "Biologie générale", 0, 0)]),
        ("DRO1124", "Droit", 0, [
            ("1DRE1124", "Droit général", 0, 0),
            ("2DRE1124", "Droit administratif et Droit du travail", 0, 0)]),
        ("MTH1125", "Mathématiques", 0, [
            ("1MTH1125", "Statistiques descriptives et probabilité", 0, 0),
            ("2MTH1125", "Méthodologies encadrées de terrain", 0, 0)]),
        ("TCC1126", "Renforcement/Entreprenariat/Softskills-1", 0, [
            ("1TCC1126", "Anglais-1", 0, 0),
            ("2TCC1126", "Techniques de communication-1", 0, 0),
            ("3TCC1126", "Éthique et aspects juridiques liés à la profession", 0, 0)]),
    ],
    ("Licence 1", "Semestre 2"): [
        ("INFO1220", "Informatique", 0, [
            ("1INF1220", "Outils informatiques", 0, 0),
            ("2INF1220", "Supports de présentation", 0, 0)]),
        ("EST1221", "Initiation à l'environnement et à la SST", 0, [
            ("1EST1221", "Initiation à l'environnement", 0, 0),
            ("2EST1221", "Initiation à la Santé et Sécurité au Travail", 0, 0)]),
        ("HQ1222", "Initiation à l'hygiène et à la qualité", 0, [
            ("1HQ1222", "Initiation à l'hygiène", 0, 0),
            ("2HQ1222", "Initiation à la qualité", 0, 0)]),
        ("INN1223", "Normalisation et certification QHSE", 0, [
            ("1INN1223", "Normes ISO (High-Level Structure)", 0, 0),
            ("2INN1223", "Accréditation et certification", 0, 0)]),
        ("MQS1224", "Management de la qualité QHSE", 0, [
            ("1MQS1224", "Coût d'obtention de la qualité", 0, 0),
            ("2MQS1224", "Management par approche processus/Fiche processus", 0, 0)]),
        ("GER1225", "Gestion des risques", 0, [
            ("1GER1225", "Introduction aux risques majeurs", 0, 0),
            ("2GER1225", "Management du risque (ISO 31000)", 0, 0)]),
        ("TCC1226", "Renforcement/Entreprenariat/Softskills-2", 0, [
            ("1TCC1226", "Anglais-2", 0, 0),
            ("2TCC1226", "Techniques de communication-2", 0, 0),
            ("3TCC1226", "Développement personnel", 0, 0)]),
    ],
    ("Licence 2", "Semestre 1"): [
        ("QPE1320", "Qualité opérationnelle et droit de l'environnement", 0, [
            ("1QPE1320", "Bonnes pratiques d'hygiène en agroalimentaire et en laboratoire", 0, 0),
            ("2QPE1320", "Qualité produit", 0, 0),
            ("3QPE1320", "Droit de l'environnement et Code de l'environnement", 0, 0)]),
        ("ENV1321", "Environnement", 0, [
            ("1ENV1321", "Pollutions environnementales", 0, 0),
            ("2ENV1321", "Normes de rejet", 0, 0),
            ("3ENV1321", "Étude d'Impact Environnemental 1", 0, 0)]),
        ("RIS1322", "Risques Professionnels", 0, [
            ("1RIS1322", "Risques mécaniques et physiques", 0, 0),
            ("2RIS1322", "Risques biologiques et radiologiques", 0, 0),
            ("3RIS1322", "Risques chimiques et ATEX", 0, 0)]),
        ("MRI1323", "Méthodologie d'évaluation des risques", 0, [
            ("1MRI1323", "Démarche d'évaluation et maîtrise des risques", 0, 0),
            ("2MRI1323", "Méthodes d'analyse des risques", 0, 0),
            ("3MRI1323", "Visite d'Entreprise", 0, 0)]),
        ("PER1324", "Performance et Amélioration QSE", 0, [
            ("1PER1324", "Tableau de bord et indicateurs", 0, 0),
            ("2PER1324", "Management et conduite du changement", 0, 0),
            ("3PER1324", "Audit système : principes et techniques", 0, 0)]),
        ("TCC1325", "Renforcement/Entreprenariat/Softskills-1", 0, [
            ("1TCC1325", "Introduction à la Comptabilité/Gestion", 0, 0),
            ("2TCC1325", "Anglais-3", 0, 0),
            ("3TCC1325", "Techniques de communication-3", 0, 0)]),
    ],
    ("Licence 2", "Semestre 2"): [
        ("STT1420", "Sécurité et Conditions de travail", 0, [
            ("1SST1420", "Facteurs d'ambiance au travail", 0, 0),
            ("2SST1420", "Qualité de Vie au Travail et Risques psychosociaux", 0, 0),
            ("3SST1420", "Ergonomie", 0, 0)]),
        ("ETN1421", "Étude détaillée des normes QHSE", 0, [
            ("1ETN1421", "Exigences de l'ISO 9001", 0, 0),
            ("2ETN1421", "Exigences de l'ISO 14001", 0, 0),
            ("3ETN1421", "Exigences de l'ISO 45001", 0, 0)]),
        ("GES1422", "Gestion des risques naturels", 0, [
            ("1GES1422", "Le risque inondation", 0, 0),
            ("2GES1422", "Les risques géologiques", 0, 0),
            ("3GES1422", "Les plans de prévention et de secours des risques naturels", 0, 0)]),
        ("INF1423", "Outils informatiques", 0, [
            ("1INF1423", "SIG appliqué aux risques", 0, 0),
            ("2INF1423", "Office (supports de présentation)", 0, 0),
            ("3INF1423", "Visite d'Entreprise", 0, 0)]),
        ("QOP1424", "Qualité opérationnelle", 0, [
            ("1QOP1424", "Élaboration de manuels QSE", 0, 0),
            ("2QOP1424", "Gestion documentaire", 0, 0)]),
        ("TCC1425", "Renforcement/Entreprenariat/Softskills-1", 0, [
            ("1TCC1425", "Gestion de projet", 0, 0),
            ("2TCC1425", "Anglais-4", 0, 0),
            ("3TCC1425", "Techniques de communication-4", 0, 0)]),
    ],
    ("Licence 3", "Semestre 1"): [
        ("RIS1520", "Gestion des risques industriels", 0, [
            ("1RIS1520", "Risques industriels", 0, 0),
            ("2RIS1520", "Étude de danger", 0, 0),
            ("3RIS1520", "Plans de prévention et de secours", 0, 0)]),
        ("REF1521", "Référentiels de management", 0, [
            ("1REF1521", "Mise en place d'un SMQ selon la norme ISO 9001", 0, 0),
            ("2REF1521", "Mise en place d'un SME selon la norme ISO 14001", 0, 0),
            ("3REF1521", "Mise en place d'un SMSST selon la norme ISO 45001", 0, 0)]),
        ("MAN1522", "Management de projet QSE", 0, [
            ("1MAN1522", "Suivi de la veille réglementaire", 0, 0),
            ("2MAN1522", "Qualité et gestion de la production", 0, 0),
            ("3MAN1522", "Audit : Gestion des non-conformités (Plan de surveillance et de contrôle)", 0, 0)]),
        ("SEC1523", "Santé et Sécurité", 0, [
            ("1SEC1523", "Document d'évaluation des risques professionnels et PMSST", 0, 0),
            ("2SEC1523", "Fiabilité et Sécurité des installations", 0, 0),
            ("3SEC1523", "Transport de Matières Dangereuses (TMD)", 0, 0)]),
        ("TCC1524", "Visite d'entreprise 3", 0, [
            ("1TCC1524", "Rédaction de rapport", 0, 0),
            ("2TCC1524", "Visite d'entreprise", 0, 0)]),
        ("TTC1525", "Renforcement/Entreprenariat/Softskills-1", 0, [
            ("1QSE1525", "Projet d'entreprise", 0, 0),
            ("2QSE1525", "Anglais-5", 0, 0),
            ("3QSE1525", "Techniques de communication-5", 0, 0)]),
    ],
    ("Licence 3", "Semestre 2"): [
        ("GES1621", "Gestion des risques QHSE", 0, [
            ("1GES1620", "Principes généraux d'hygiène alimentaire", 0, 0),
            ("2GES1620", "HACCP - VACCP - TACCP", 0, 0),
            ("3GES1620", "Étude de la norme ISO 22000", 0, 0)]),
        ("ECO1622", "Écotoxicologie", 0, [
            ("1ECO1621", "Établissements et Installations Classées et Étude d'impact environnemental 2", 0, 0),
            ("2ECO1621", "Gestion des déchets", 0, 0),
            ("3ECO1621", "Écotoxicologie", 0, 0)]),
        ("SEC1623", "Sécurité des personnes, des installations et des équipements", 0, [
            ("1SEC1622", "Sécurité incendie", 0, 0),
            ("2SEC1622", "Sécurité électrique (Consignation/Déconsignation)", 0, 0),
            ("3SEC1622", "Secourisme et évacuation d'urgence", 0, 0)]),
        ("DEV1624", "Développement Durable", 0, [
            ("1DEV1623", "Économie circulaire", 0, 0),
            ("2DEV1623", "RSE", 0, 0)]),
        ("QSE1625", "Fonctions QSE", 0, [
            ("1QSE1624", "Management d'équipe et leadership", 0, 0),
            ("2QSE1624", "Système de Management Intégré", 0, 0)]),
        ("TER1626", "Techniques d'expression et de rédaction", 0, [
            ("1TER1625", "Renforcement des cours d'anglais", 0, 0),
            ("2TER1625", "Techniques de rédaction de rapport", 0, 0)]),
        ("PPR1620", "Projet professionnel", 0, [
            ("1PPR1626", "Projet tutoré", 0, 0),
            ("2PPR1626", "Stage en entreprise", 0, 0)]),
    ],
}

# ============================================================
# Licence Pro Prospection et Exploitation des Ressources Minérales
# (L-ResMin) — source : fichier Excel fourni.
# NB : les deux feuilles "SEMESTRE 1" et "SEMESTRE 2" du fichier
# source contiennent exactement le même contenu (probable copier-
# coller non corrigé côté UFR-SI) — repris tel quel ici. Envoie une
# version corrigée du semestre 2 si elle existe et je remplace.
# ============================================================
MAQUETTE_RESMIN = {
    ("Licence 3", "Semestre 1"): [
        ("GEO1620", "Géologie 2", 6, [
            ("1GEO1620", "Stratigraphie", 40, 5),
            ("2GEO1620", "Géologie structurale", 40, 5),
            ("3GEO1620", "Pétrologie magmatique et métamorphique", 40, 5)]),
        ("GMA1621", "Géomatique", 6, [
            ("1GMA1621", "Topographie", 50, 5),
            ("2GMA1621", "Télédétection", 50, 5),
            ("3GMA1621", "Systèmes d'Informations Géographiques", 20, 5)]),
        ("RMN1622", "Ressources Minérales et Énergétiques", 6, [
            ("1RMN1622", "Ressources naturelles", 40, 3),
            ("2RMN1622", "Matériaux de construction", 40, 3),
            ("3RMN1622", "Ingénierie des réservoirs", 40, 3)]),
        ("GCH1623", "Géochimie", 4, [
            ("1GCH1623", "Géochimie", 40, 4),
            ("2GCH1623", "Chimie environnementale", 40, 4)]),
        ("CPE1624", "Compétences générales", 2, [
            ("1CPE1624", "Droit", 20, 2),
            ("2CPE1624", "Gestion", 20, 2)]),
        ("TCC1625", "Technique d'expression et Entrepreneuriat", 3, [
            ("1TCC1625", "Entrepreneuriat", 30, 3),
            ("2TCC1625", "Techniques de rédaction scientifique", 30, 3)]),
        ("PFE1626", "Projet de fin de cycle", 3, [
            ("1PFE1626", "Mémoire de fin d'étude", 60, 5)]),
    ],
    ("Licence 3", "Semestre 2"): [
        ("GEO1620", "Géologie 2", 6, [
            ("1GEO1620", "Stratigraphie", 40, 5),
            ("2GEO1620", "Géologie structurale", 40, 5),
            ("3GEO1620", "Pétrologie magmatique et métamorphique", 40, 5)]),
        ("GMA1621", "Géomatique", 6, [
            ("1GMA1621", "Topographie", 50, 5),
            ("2GMA1621", "Télédétection", 50, 5),
            ("3GMA1621", "Systèmes d'Informations Géographiques", 20, 5)]),
        ("RMN1622", "Ressources Minérales et Énergétiques", 6, [
            ("1RMN1622", "Ressources naturelles", 40, 3),
            ("2RMN1622", "Matériaux de construction", 40, 3),
            ("3RMN1622", "Ingénierie des réservoirs", 40, 3)]),
        ("GCH1623", "Géochimie", 4, [
            ("1GCH1623", "Géochimie", 40, 4),
            ("2GCH1623", "Chimie environnementale", 40, 4)]),
        ("CPE1624", "Compétences générales", 2, [
            ("1CPE1624", "Droit", 20, 2),
            ("2CPE1624", "Gestion", 20, 2)]),
        ("TCC1625", "Technique d'expression et Entrepreneuriat", 3, [
            ("1TCC1625", "Entrepreneuriat", 30, 3),
            ("2TCC1625", "Techniques de rédaction scientifique", 30, 3)]),
        ("PFE1626", "Projet de fin de cycle", 3, [
            ("1PFE1626", "Mémoire de fin d'étude", 60, 5)]),
    ],
}

MAQUETTES_PAR_FILIERE = {
    "DIC Géomètre-Topographe": MAQUETTE_GTP,
    "DIC Génie Civil": MAQUETTE_GCU,
    "DIC Géotechnique": MAQUETTE_GGT,
    "Licence QHSE": MAQUETTE_QHSE,
    "Licence Pro Prospection et Exploitation des Ressources Minérales (L-ResMin)": MAQUETTE_RESMIN,
}


def seed():
    """Peuple la base si elle est vide. Idempotent."""
    if Filiere.query.first():
        return

    filiere_objs = {}
    for nom, dept in FILIERES:
        f = Filiere(nom=nom, departement=dept)
        db.session.add(f)
        filiere_objs[nom] = f
    db.session.flush()

    for filiere_nom, maquette in MAQUETTES_PAR_FILIERE.items():
        f = filiere_objs[filiere_nom]
        for (annee, semestre), ues in maquette.items():
            for code, nom, credit, matieres in ues:
                ue = UE(filiere_id=f.id, annee=annee, semestre=semestre,
                        code=code, nom=nom, credit=credit)
                db.session.add(ue)
                db.session.flush()
                for sigle, mnom, vol, coef in matieres:
                    db.session.add(Matiere(ue_id=ue.id, sigle=sigle, nom=mnom,
                                            volume_horaire=vol, coefficient=coef))

    db.session.commit()
