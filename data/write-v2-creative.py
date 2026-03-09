#!/usr/bin/env python3
"""V2.1: Enrich Phase 5 DESIGNER with full creative/UX coverage from docx phases 4+5."""
import os, json

BASE = r"C:\Users\arnau\Documents\projets\skill project-architect"

# ============================================================
# 1. Replace Phase 5 in commands/project-architect.md
# ============================================================

NEW_PHASE_5 = r"""## Phase 5 : DESIGNER

**But** : Cadrer l experience utilisateur ET l identite visuelle. Produire un brief complet pour le designer : UX, DA, design system, assets, handoff.
**Active** : M, L, XL.
**Couvre** : Doc Phases 4 (Conception UX) et 5 (UI Design & DA) -- ~80 items dans le referentiel.

### Questions

**Bloc 1 -- Identite et references visuelles** `[M]`

**Q5.1** : "Tu as deja une identite visuelle ?"
- Options : "Charte graphique complete", "Juste un logo", "Rien, tout est a creer", "On s inspire d un existant"

**Q5.2** : "Quel est l esprit visuel souhaite ?"
- Options : "Minimaliste et epure", "Colore et dynamique", "Corporate et professionnel", "Montre-moi des exemples"

**Q5.3** : "Montre-moi 2-3 sites ou apps dont tu aimes le look"
- Texte libre. Si l utilisateur donne des URLs -> utiliser `WebFetch` pour capturer les references et noter les elements visuels cles.
- Si l utilisateur ne sait pas -> proposer de faire un benchmarking visuel avec `WebSearch` : "[secteur] best design 2026"

**Q5.4** : "Quelles sont tes couleurs de marque ? Ou tes preferences de couleurs ?"
- Options :
  - "J ai deja des couleurs definies (charte)"
  - "J ai des preferences (couleurs chaudes / froides / vives / sobres)"
  - "Aucune idee, le designer decidera"
  - "Laisse-moi decrire..."

**Q5.5** : "Quel style d images pour le projet ?"
- Options :
  - "Photos reelles (stock ou shooting)"
  - "Illustrations (flat, 3D, dessin)"
  - "Icones et pictogrammes principalement"
  - "Mix photos + illustrations"

**Bloc 2 -- Appareils et responsive** `[M]`

**Q5.6** : "Les utilisateurs utiliseront l app/site sur quel(s) appareil(s) ?"
- Options (multiSelect) : "Principalement mobile", "Principalement desktop", "Les deux", "Tablette aussi"

**Bloc 3 -- Architecture UX** `[L+]`

**Q5.7** (L+) : "As-tu besoin de diagrammes de flux utilisateur (qui montrent les chemins possibles a chaque ecran) ?"
- Options :
  - "Oui, pour tous les parcours"
  - "Oui, seulement les parcours critiques"
  - "Non, les wireframes suffisent"
  - "A voir avec le designer"

**Q5.8** (L+) : "Comment gerer la complexite dans l interface ?"
- Options :
  - "Devoilement progressif (montrer le minimum puis plus si besoin)"
  - "Tout visible d un coup"
  - "Mode simplifie + mode avance"
  - "A recommander"

**Q5.9** (L+) : "Y a-t-il des formulaires complexes (multi-etapes, beaucoup de champs) ?"
- Options :
  - "Oui, formulaires multi-etapes (wizard)"
  - "Oui, formulaires longs mais une seule page"
  - "Non, que des formulaires simples"
  - "A definir"
- Si oui -> noter : sauvegarde auto, validation inline, barre de progression

**Bloc 4 -- Wireframing et prototypage** `[L+]`

**Q5.10** (L+) : "As-tu besoin de maquettes fil de fer (wireframes) avant les maquettes finales ?"
- Options :
  - "Oui, des croquis rapides (basse fidelite)"
  - "Oui, des maquettes quasi-reelles (haute fidelite)"
  - "Non, on passe direct aux maquettes finales"
  - "A discuter avec le designer"

**Q5.11** (L+) : "Faut-il un prototype cliquable (navigable) pour tester avant de coder ?"
- Options :
  - "Oui, prototype interactif complet (Figma prototype)"
  - "Oui, prototype des parcours critiques seulement"
  - "Non, les maquettes statiques suffisent"
  - "A voir selon le budget"

**Q5.12** (L+) : "Quels etats d interface faut-il prevoir pour chaque ecran ?"
- Options (multiSelect) :
  - "Vide (premiere utilisation, pas de donnees)"
  - "Chargement (en attente de reponse)"
  - "Erreur (quelque chose a echoue)"
  - "Succes (action reussie)"
  - "Partiel (donnees incompletes)"
  - "Desactive (fonctionnalite non disponible)"

**Bloc 5 -- Tests et accessibilite** `[L+]`

**Q5.13** (L+) : "Prevoit-on des tests sur les maquettes avec de vrais utilisateurs ?"
- Options : "Oui, tests en personne", "Oui, tests a distance", "Non, le designer valide", "A voir selon le budget"
- Si oui -> noter : minimum 5 utilisateurs par segment, synthese et iterations

**Q5.14** (L+) : "L accessibilite est-elle une obligation legale ?"
- Options : "Oui (secteur public, EAA)", "Important mais pas obligatoire", "Pas une priorite V1", "Je ne sais pas"
- Si oui ou important -> noter : navigation clavier, compatibilite lecteur d ecran, ARIA, contrastes WCAG AA

**Bloc 6 -- Direction artistique** `[L+]` (descendu de XL a L)

**Q5.15** (L+) : "Faut-il definir une direction artistique ?"
- Options :
  - "Oui : moodboard, palette, typo, iconographie, style photo"
  - "Partiellement : juste palette + typo"
  - "Non, on a deja tout"
  - "A discuter avec le designer"

**Q5.16** (L+) : "Quel style de typographie ?"
- Options :
  - "Sans-serif moderne (clean, tech)"
  - "Serif classique (elegant, editorial)"
  - "Mix (serif pour les titres, sans-serif pour le texte)"
  - "Le designer decidera"
- Accompagner de : combien de fontes ? Licences necessaires ?

**Q5.17** (L+) : "Quel style d icones ?"
- Options :
  - "Outlined (traits fins, moderne)"
  - "Filled (pleines, plus visible)"
  - "Duotone (deux couleurs, tendance)"
  - "Le designer decidera"

**Bloc 7 -- Design system et composants** `[L+]`

**Q5.18** (L+) : "Quel niveau de systeme de design ?"
- Options :
  - "Basique : couleurs + typo + boutons"
  - "Standard : jetons de design + composants reutilisables + patterns"
  - "Complet : documentation interactive (Storybook) + guidelines + do/don t"
  - "A recommander"

**Q5.19** (L+) : "Comment se fait le passage maquettes vers code (handoff) ?"
- Options :
  - "Figma avec inspection + annotations"
  - "Outil de handoff dedie (Zeplin, etc.)"
  - "Le dev se debrouille avec les maquettes"
  - "A definir"
- Quelle que soit la reponse -> noter : reunion de handoff, canal de communication dedie pour questions design

**Bloc 8 -- Mode sombre et animations** `[XL]`

**Q5.20** (XL) : "Faut-il un mode sombre ?"
- Options : "Oui, des le depart", "Oui, mais en V2", "Non", "Si c est facile"

**Q5.21** (XL) : "Des animations ou micro-interactions speciales ?"
- Options :
  - "Transitions de page fluides"
  - "Micro-interactions (boutons, feedback, loaders)"
  - "Animations complexes (scroll, parallaxe, 3D)"
  - "Le minimum, pas de chichi"

**Bloc 9 -- Assets et livraison** `[XL]`

**Q5.22** (XL) : "Des maquettes d emails transactionnels a prevoir ?"
- Options : "Oui", "Non, on utilisera des templates standards", "A voir"

**Q5.23** (XL) : "Comment exporter les jetons de design (design tokens) ?"
- Options :
  - "JSON (universel)"
  - "CSS variables (web natif)"
  - "Tailwind config (si Tailwind)"
  - "Le designer decidera"

**Q5.24** (XL) : "Pipeline d optimisation des images ?"
- Options :
  - "WebP/AVIF auto + lazy loading + srcset responsive"
  - "Optimisation basique (compression)"
  - "A recommander"
  - "Pas besoin (peu d images)"

### Generation livrable

Generer `05-brief-ux-ui.md` structure en deux grandes parties :

**Partie 1 -- Brief UX** :
- Principes UX du projet
- User flows et diagrammes d interaction (si L+)
- Inventaire ecrans avec etats complets
- Parcours critiques (happy + error paths)
- Strategie responsive et breakpoints
- Strategie progressive disclosure et formulaires (si L+)
- Specs wireframing (si L+)
- Brief prototypage (si L+)
- Brief accessibilite (niveaux, navigation clavier, ARIA)
- Brief microcopy (labels, erreurs, empty states, CTA, ton/voix)
- Plan de tests utilisateurs (si prevu)

**Partie 2 -- Brief creatif et DA** :
- References visuelles (benchmarks captures)
- Direction artistique (moodboard textuel, ambiance, emotions)
- Palette de couleurs (primaire, secondaire, accent, semantique, neutres + contrastes WCAG)
- Typographie (choix, echelle, line-height, chargement fonts, licences)
- Style iconographique (outlined/filled/duotone, taille, coherence)
- Style photographique/illustratif
- Brief design system (niveau, tokens, composants, patterns, documentation)
- Specs animations et micro-interactions (si XL)
- Specs dark mode / themes (si XL)
- Maquettes emails (si XL)
- Pipeline assets (optimisation images, favicons, OG images, naming convention)
- Checklist handoff design -> dev (Figma structure, reunion, canal communication)

### Checkpoint
> "Brief UX/UI et creatif pret ! [N] ecrans identifies, [N] etats d interface a prevoir. On passe a l architecture technique ?"

"""

# Read existing skill file and replace Phase 5
skill_path = os.path.join(BASE, "commands", "project-architect.md")
with open(skill_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find Phase 5 boundaries
phase5_start = content.find("## Phase 5 : DESIGNER")
phase6_start = content.find("## Phase 6 : ARCHITECTURER")

if phase5_start == -1 or phase6_start == -1:
    print("ERROR: Could not find Phase 5 or Phase 6 markers")
    exit(1)

# Find the --- separator before Phase 6
separator_before_6 = content.rfind("---", phase5_start, phase6_start)

# Replace Phase 5 content (from Phase 5 header to the --- before Phase 6)
new_content = content[:phase5_start] + NEW_PHASE_5 + "---\n\n" + content[phase6_start:]

with open(skill_path, "w", encoding="utf-8") as f:
    f.write(new_content)
lines = new_content.count("\n") + 1
print(f"  project-architect.md: {lines} lines (Phase 5 enriched)")

# ============================================================
# 2. Update designer items in adaptation-matrix.json
# ============================================================

matrix_path = os.path.join(BASE, "data", "adaptation-matrix.json")
with open(matrix_path, "r", encoding="utf-8") as f:
    matrix = json.load(f)

matrix["phases"]["designer"]["items"] = {
    "S": [],
    "M": [
        "Principes UX du projet",
        "Parcours critiques (happy paths + error paths)",
        "Liste des ecrans/pages necessaires",
        "Etats d interface (vide, chargement, erreur, succes)",
        "References visuelles et benchmarking",
        "Couleurs de marque et preferences",
        "Style d images (photo, illustration, icones)",
        "Breakpoints responsive definis"
    ],
    "L": [
        "Principes UX du projet",
        "Parcours critiques (happy paths + error paths)",
        "Liste des ecrans/pages necessaires",
        "Etats d interface complets (vide, chargement, erreur, succes, partiel, desactive)",
        "References visuelles et benchmarking",
        "Breakpoints responsive definis",
        "User flows et diagrammes d interaction",
        "Strategie progressive disclosure et formulaires",
        "Specs wireframing (basse et haute fidelite)",
        "Prototypage interactif (Figma prototype)",
        "Plan de tests utilisateurs sur maquettes",
        "Accessibilite detaillee (clavier, ARIA, lecteur ecran, contrastes WCAG AA)",
        "Microcopy complet (labels, erreurs, empty states, CTA)",
        "Direction artistique (moodboard, ambiance, references)",
        "Palette de couleurs (primaire, secondaire, accent, semantique, neutres)",
        "Typographie (choix, echelle, line-height, chargement fonts, licences)",
        "Style iconographique (outlined/filled/duotone, taille)",
        "Style photographique / illustratif",
        "Specifications du design system (tokens, composants, patterns)",
        "Brief accessibilite (WCAG 2.1 AA)",
        "Checklist handoff design vers dev (Figma, reunion, canal comm)",
        "Benchmarking UX concurrentiel"
    ],
    "XL": [
        "Principes UX du projet",
        "Parcours critiques avec variantes",
        "Liste des ecrans/pages necessaires",
        "Etats d interface complets",
        "References visuelles et benchmarking",
        "Breakpoints responsive definis",
        "User flows et diagrammes d interaction",
        "Strategie progressive disclosure et formulaires",
        "Specs wireframing (basse et haute fidelite)",
        "Prototypage interactif (Figma prototype)",
        "Plan de tests utilisateurs (min 5 users par segment)",
        "Iterations post-tests documentees",
        "Accessibilite detaillee (clavier, ARIA, lecteur ecran, contrastes WCAG AA/AAA)",
        "Microcopy complet",
        "Direction artistique complete (moodboard, palette, typo, icones, photo)",
        "Palette de couleurs complete (+ verification contrastes WCAG AA/AAA)",
        "Typographie complete (heading/body/mono, echelle, line-height, chargement, licences)",
        "Style iconographique (selection ou creation, licences)",
        "Style photographique / illustratif (stock, custom, AI)",
        "Specifications du design system complet (tokens, composants atomiques/moleculaires/organismes, patterns)",
        "Documentation composants interactive (Storybook ou equivalent)",
        "Brief accessibilite (WCAG 2.1 AA/AAA)",
        "Checklist handoff design vers dev",
        "Benchmarking UX concurrentiel",
        "Specifications dark mode / themes",
        "Specifications animations et micro-interactions",
        "Specifications motion design (transitions pages/etats)",
        "Maquettes emails transactionnels",
        "Design tokens exportes (JSON / CSS variables / Tailwind config)",
        "Pipeline d optimisation assets (WebP/AVIF, srcset, lazy loading)",
        "Favicons et app icons (toutes tailles : 16, 32, 180, 192, 512px)",
        "OG images et social cards",
        "Convention de nommage des assets",
        "Figma structure avec inspect active"
    ]
}

with open(matrix_path, "w", encoding="utf-8") as f:
    json.dump(matrix, f, indent=2, ensure_ascii=False)

# Count items
for size in ["S", "M", "L", "XL"]:
    n = len(matrix["phases"]["designer"]["items"][size])
    print(f"  designer {size}: {n} items")

print("\nDone: Phase 5 enriched + matrix updated (V2.1 creative)")
