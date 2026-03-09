# {project_name}

> {tagline}

**Genere par** : `/project-architect` -- ATUM SAS
**Date** : {date}
**Taille projet** : {size}

---

## Stack technique

| Composant | Technologie | Version | Justification |
|-----------|-------------|---------|---------------|
| Frontend | {frontend} | {frontend_version} | {frontend_why} |
| Backend | {backend} | {backend_version} | {backend_why} |
| Base de donnees | {database} | {database_version} | {database_why} |
| Auth | {auth} | - | {auth_why} |
| Hosting | {hosting} | - | {hosting_why} |

## Architecture

{architecture_diagram}

### Modele de donnees

{data_model}

### API (endpoints principaux)

| Methode | Endpoint | Description | Auth requise |
|---------|----------|-------------|--------------|
{api_endpoints}

### Authentification

- **Mecanisme** : {auth_mechanism}
- **Stockage tokens** : {token_storage}
- **Refresh** : {refresh_strategy}
- **Roles** : {roles_list}

## Conventions

- **Langue du code** : Anglais
- **Langue de l interface** : {ui_language}
- **Linter** : {linter}
- **Formatter** : {formatter}
- **Commits** : {commit_convention}
- **Branches** : {branch_naming}
- **Code review** : {code_review_process}
- **Structure dossiers** : {folder_structure}

## Fonctionnalites

### Must Have (V1 -- indispensable)

{must_have_features}

### Should Have (important)

{should_have_features}

### Could Have (bonus)

{could_have_features}

### Won't Have V1 (hors perimetre)

{wont_have_features}

## Regles de gestion

{business_rules}

## Roles et permissions

{roles_permissions_matrix}

## Securite

- **OWASP** : {owasp_coverage}
- **Secrets** : {secrets_management}
- **Chiffrement** : {encryption}
- **Conformite** : {compliance}
- **Audit trail** : {audit_trail}

## Tests

- **Framework** : {test_framework}
- **Strategie** : {test_strategy}
- **Couverture cible** : {coverage_target}
- **Infrastructure de test** : {test_infrastructure}
- **Protocole de recette** : {uat_protocol}

## Infrastructure

- **Environnements** : {environments}
- **CI/CD** : {cicd_pipeline}
- **Monitoring** : {monitoring}
- **Backups** : {backups}
- **Strategie de deploiement** : {deployment_strategy}

## Budget de performance

| Route/Page | Temps cible | Taille max |
|------------|-------------|------------|
{perf_budget}

## Cible utilisateurs

- **Cible principale** : {primary_target}
- **Utilisateur type** : {user_persona}
- **Parcours principal** : {main_user_journey}

## Specs completes

Les livrables detailles sont dans `docs/preparation/` :
- `01-brief-qualification.md` -- Qualification et Go/No-Go
- `02-brief-decouverte.md` -- Brief de decouverte complet
- `03-strategie-produit.md` -- Strategie produit et positionnement
- `04-cahier-des-charges.md` -- Cahier des charges fonctionnel
- `05-brief-ux-ui.md` -- Brief UX/UI et design system
- `06-architecture-technique.md` -- Architecture technique detaillee
- `07-planning-projet.md` -- Planning et gouvernance
- `08-checklist-pre-dev.md` -- Checklist pre-developpement

## Implementation

Suivre `implementation-roadmap.md` pour l ordre de developpement.
Pour chaque feature : `/pipeline discover "F-xxx {nom_feature}"`

---

> CLAUDE.md genere par `/project-architect` -- ATUM SAS
