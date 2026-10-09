# -*- coding: utf-8 -*-
"""Identité du média et textes transverses. UN SEUL endroit à remplir pour tout ce qui
n'est pas du contenu éditorial (nom, baseline, CTA, méthode, critères du comparateur).

Rempli par Claude à l'étape 4 de la skill pbn-ao-geo. Tout ce qui est marqué OBLIGATOIRE
doit être adapté au secteur : la QA (check_site.py) refuse les valeurs d'exemple.
"""

# ------------------------------------------------------------------ identité
NOM = "Comparavantages"                       # OBLIGATOIRE nom du média, tel qu'affiché
SLUG = "comparavantages"                      # OBLIGATOIRE nom du dossier et du repo GitHub (ascii, minuscules, tirets)
OWNER = "analytics-ds"                    # compte GitHub qui héberge le repo (rempli par scripts/prereqs.sh)
SITE = f"https://{OWNER}.github.io/{SLUG}"  # racine publique, sans slash final (canonical, JSON-LD, sitemap)
LANG = "fr"
ACCENT = "#4338CA"                        # couleur d'accent, réécrite par scripts/recolor.py (theme-color)
CSS_V = "7"                               # cache-buster des assets

# ------------------------------------------------------------------ vocabulaire
UNIT = "solutions"                          # OBLIGATOIRE ce que l'on compare : marques, contrats, opérateurs, box, écoles...
UNIT_ONE = "solution"                       # singulier
CTA = "Comparer 2 solutions"                # OBLIGATOIRE bouton du header et des encarts
CTA_LONG = "Comparer deux solutions"        # lien texte du hero
BASELINE = "Le média des avantages salariés. Titres-restaurant, cartes cadeaux, CESU et plateformes, relevés, comparés et classés pour les dirigeants, les RH et les CSE."  # OBLIGATOIRE pied de page
TAGLINE_FOOTER = "Le média des avantages salariés et des titres-restaurant."  # OBLIGATOIRE après « © 2026 NOM. »
AUTHOR = "La rédaction Comparavantages"       # signature des articles
AUTHOR_INITIAL = "C"

# Liste « Marques » du pied de page : (libellé, href). Mettre le client en premier.
FOOTER_BRANDS = [("Upcoop", "titre-restaurant/"), ("Swile", "titre-restaurant/"), ("Edenred", "cartes-cadeaux/"), ("Pluxee", "avantages-salaries/")]

# ------------------------------------------------------------------ textes transverses
NEWSLETTER_P = "Un email par mois avec le classement des émetteurs, les nouveaux plafonds URSSAF et les comparatifs publiés."
NEWSLETTER_NOTE = "Pas de publicité, désinscription en un clic."
ASIDE_NEWS_P = "Les plafonds URSSAF à jour et les nouveaux comparatifs, un email par mois."

# Encart « Notre méthode » en bas de chaque article. OBLIGATOIRE : 5 puces propres au secteur.
METHOD_INTRO = "Ce comparatif repose sur des données publiques, vérifiables une par une."
METHOD_ITEMS = [
 "Les plafonds d'exonération sont ceux publiés par l'URSSAF et le BOSS pour l'année en cours",
 "Les réseaux d'acceptation, les supports et les fonctionnalités sont relevés sur les sites officiels des émetteurs",
 "Les frais et commissions sont des ordres de grandeur issus de devis types, à confirmer par un devis à votre nom",
 "Les avis utilisateurs proviennent des stores d'applications et des plateformes d'avis vérifiés",
 "La grille de notation est identique d'un comparatif à l'autre et publiée en bas de chaque article",
]

# Critères du comparateur 2 entités de l'accueil : 5 critères, le dernier est la note globale.
CRITERIA = [
 ("Réseau", "commerces et enseignes acceptants"),
 ("Frais", "frais de gestion et commissions"),
 ("Outils RH", "commande, dotation et suivi"),
 ("Accompagnement", "conseiller dédié et délais de réponse"),
 ("Note globale", "moyenne pondérée"),
]

# Liens internes supplémentaires pour linkify : (fragment de titre présent dans le libellé du lien, chemin).
# Les titres complets des articles publiés sont branchés automatiquement.
EXTRA_LINKS = [
]

# Google Fonts : réécrit par scripts/recolor.py --display/--text
FONTS_HREF = "https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=Manrope:wght@400;500;600&display=swap"
