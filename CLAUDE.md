# project-architect — Plugin Claude Code

Plugin de preparation de projet de developpement, de la qualification initiale a la gate pre-dev.
Une seule commande `/project-architect`, workflow adaptatif S/M/L/XL.

## Architecture

**8 phases sequentielles** :
1. QUALIFIER — Taille du projet (S/M/L/XL)
2. COMPRENDRE — Contexte et contraintes
3. STRATEGISER — Strategie et positionnement
4. SPECIFIER — Cahier des charges fonctionnel
5. DESIGNER — Brief UX/UI et direction artistique (24 questions, 9 blocs)
6. ARCHITECTURER — Architecture technique
7. PLANIFIER — Planning et budget
8. VALIDER — Gate pre-dev + fichiers-pont (CLAUDE.md, implementation-roadmap.md)

**Matrice adaptative** : `data/adaptation-matrix.json` controle quelles questions/livrables s'appliquent selon la taille S/M/L/XL. Invariant : les items sont monotones (S <= M <= L <= XL).

## Fichiers cles

| Fichier | Role |
|---------|------|
| `commands/project-architect.md` | Skill principal (854 lignes, 82 questions) |
| `data/adaptation-matrix.json` | Matrice phases x tailles (308 items) |
| `agents/discovery-auditor.md` | Audit existant technique (sonnet) |
| `agents/spec-architect.md` | Cahier des charges (sonnet) |
| `agents/tech-architect.md` | Architecture technique (sonnet) |
| `agents/pre-dev-validator.md` | Validation pre-dev (haiku) |
| `templates/*.md` | 7 templates de livrables |
| `data/*.py` | Scripts de generation/test |

## Conventions

- Questions numerotees `Q{phase}.{num}` (ex: Q5.14)
- Phases en francais (QUALIFIER, COMPRENDRE, etc.)
- Items matrice monotones : S <= M <= L <= XL pour chaque phase
- Templates avec placeholders `{variable}`
- Agents references par path string dans plugin.json

## Workflow dev

1. Editer les fichiers source (commands/, templates/, data/, agents/)
2. Le hook PostToolUse sync automatiquement vers le cache plugin
3. Valider avec `python data/test-all.py` (10 tests)

## V2 (fichiers-pont)

Phase 8 genere deux fichiers-pont pour la phase de dev :
- `CLAUDE-project.md` : lu automatiquement par Claude Code a l'ouverture du projet
- `implementation-roadmap.md` : features ordonnees pour `/pipeline`
