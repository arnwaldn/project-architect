#!/usr/bin/env python3
"""Generate README.md for GitHub publication."""
import os

BASE = r"C:\Users\arnau\Documents\projets\skill project-architect"

content = r"""# project-architect

Plugin Claude Code pour la preparation complete de projets de developpement -- de la qualification initiale a la gate pre-dev.

Une seule commande, un workflow adaptatif S/M/L/XL, 82 questions, 8 livrables + 2 fichiers-pont.

## Installation

```bash
claude plugin add https://github.com/arnwaldn/project-architect
```

## Usage

```bash
# Nouveau projet
/project-architect une marketplace de services locaux

# Reprendre un projet en cours
/project-architect

# Voir la progression
/project-architect status

# Importer depuis un document existant
/project-architect --from-doc specs.pdf

# Forcer la taille
/project-architect mon app --size L
```

## Ce que ca fait

Le plugin guide un entretien structure en **8 phases** pour produire toute la documentation de preparation avant d'ecrire la moindre ligne de code :

| Phase | Nom | But |
|-------|-----|-----|
| 1 | QUALIFIER | Go/No-Go -- le projet vaut-il l'investissement ? |
| 2 | COMPRENDRE | Decouverte du projet, de l'existant, des utilisateurs |
| 3 | STRATEGISER | Positionnement, personas, parcours utilisateurs, MVP |
| 4 | SPECIFIER | Cahier des charges fonctionnel (user stories, regles de gestion) |
| 5 | DESIGNER | Brief UX/UI complet (24 questions, 9 blocs) |
| 6 | ARCHITECTURER | Stack, modele de donnees, API, securite, tests |
| 7 | PLANIFIER | Planning, gouvernance, contenu, aspects juridiques |
| 8 | VALIDER | Gate pre-dev + generation des fichiers-pont |

### Adaptation automatique

Le workflow s'adapte a la taille du projet :

- **S** (site vitrine) : 4 phases actives, ~15 questions, ~3 livrables
- **M** (app mobile, e-commerce) : 8 phases, ~50 questions, 8 livrables
- **L** (plateforme SaaS) : 8 phases completes, ~70 questions, 8 livrables detailles
- **XL** (systeme distribue, reglemente) : 8 phases exhaustives, ~82 questions, 8 livrables + items avances

### Fichiers-pont (V2)

A la fin du workflow, le plugin genere 2 fichiers-pont :

- **CLAUDE.md** : lu automatiquement par Claude Code a l'ouverture du projet. Contient toute la preparation (stack, archi, features, regles, conventions).
- **implementation-roadmap.md** : plan d'execution ordonne par lots de dependances, avec commandes `/pipeline` pour chaque feature.

## 4 agents specialises

| Agent | Role | Modele |
|-------|------|--------|
| discovery-auditor | Audit de l'existant (perf, SEO, securite, dette) | Sonnet |
| spec-architect | Cahier des charges (user stories, regles de gestion) | Sonnet |
| tech-architect | Architecture technique (ADR, modele de donnees, API) | Sonnet |
| pre-dev-validator | Validation pre-dev (coherence entre livrables) | Haiku |

## Structure du plugin

```
project-architect/
├── .claude-plugin/
│   └── plugin.json              # Manifeste du plugin
├── commands/
│   ├── project-architect.md     # Skill principal (854 lignes)
│   └── test-plugin.md           # Tests du plugin
├── agents/
│   ├── discovery-auditor.md     # Audit existant
│   ├── spec-architect.md        # Specs fonctionnelles
│   ├── tech-architect.md        # Architecture technique
│   └── pre-dev-validator.md     # Validation pre-dev
├── templates/
│   ├── brief-projet.md          # Template brief
│   ├── cahier-des-charges.md    # Template specs
│   ├── architecture-doc.md      # Template archi
│   ├── planning-projet.md       # Template planning
│   ├── checklist-pre-dev.md     # Template checklist
│   ├── CLAUDE-project.md        # Template fichier-pont CLAUDE.md
│   └── implementation-roadmap.md # Template fichier-pont roadmap
├── data/
│   └── adaptation-matrix.json   # Matrice phases x tailles (308 items)
├── CLAUDE.md                    # Context pour le dev du plugin
└── README.md
```

## Sortie

A la fin du workflow, le dossier projet contient :

```
mon-projet/
├── CLAUDE.md                    # Claude Code lit ca automatiquement
├── implementation-roadmap.md    # Plan d'execution ordonne
└── docs/preparation/
    ├── 01-brief-qualification.md
    ├── 02-brief-decouverte.md
    ├── 03-strategie-produit.md
    ├── 04-cahier-des-charges.md
    ├── 05-brief-ux-ui.md
    ├── 06-architecture-technique.md
    ├── 07-planning-projet.md
    └── 08-checklist-pre-dev.md
```

## Auteur

**ATUM SAS** -- Agence de developpement web et mobile.

## Licence

MIT
"""

readme_path = os.path.join(BASE, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
print("README.md written (%d bytes)" % len(content))
