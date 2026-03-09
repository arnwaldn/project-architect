#!/usr/bin/env python3
"""Write all 5 template files for project-architect plugin."""
import os

base = r"C:\Users\arnau\Documents\projets\skill project-architect\templates"

templates = {
    "brief-projet.md": """# {project_name} -- Brief Projet

> {tagline}

**Date** : {date}
**Auteur** : {author}
**Taille** : {size}
**Statut** : Brief initial

---

## 1. Le probleme

{problem_description}

### Comment les gens font aujourd hui
{current_alternatives}

## 2. La solution

{solution_description}

### Parcours utilisateur
1. {step_1}
2. {step_2}
3. {step_3}

## 3. Pour qui ?

- **Cible principale** : {primary_target}
- **Utilisateur type** : {user_persona}

## 4. Fonctionnalites

### Indispensable (version de base)
- [ ] {must_have_1}
- [ ] {must_have_2}

### Important
- [ ] {should_have_1}
- [ ] {should_have_2}

### Bonus (plus tard)
- [ ] {could_have_1}

## 5. Marche et concurrence

| Concurrent | Ce qu il fait bien | Ce qui manque |
|------------|-------------------|---------------|
| {competitor_1} | {strength_1} | {weakness_1} |

**Differentiation** : {differentiation}
**Modele economique** : {business_model}

## 6. Contraintes

- **Budget** : {budget}
- **Delai** : {timeline}
- **Equipe** : {team}
- **Reglementation** : {regulations}

## 7. Criteres de succes

| Horizon | Critere | Objectif |
|---------|---------|----------|
| 6 mois | {metric_6m} | {target_6m} |
| 2 ans | {metric_2y} | {target_2y} |

## 8. Qualification (si applicable)

- **Type** : {project_type} (client externe / interne / perso)
- **Go/No-Go** : {go_nogo}
- **Risques identifies** : {risks}

## 9. Audit de l existant (si applicable)

{audit_summary}

---

> Document genere par `/project-architect` -- ATUM SAS
""",

    "cahier-des-charges.md": """# {project_name} -- Cahier des Charges Fonctionnel

**Version** : 1.0
**Date** : {date}
**Auteur** : {author}
**Statut** : Draft

---

## 1. Contexte et objectifs

### Contexte
{context}

### Objectifs
{objectives}

### Perimetre
- **Inclus** : {in_scope}
- **Exclus** : {out_of_scope}

---

## 2. Fonctionnalites

### 2.1 Indispensable (Must Have)

#### F-001 : {feature_name}
**Description** : {feature_description}
**User Story** : En tant que {role}, je veux {action}, afin de {benefit}.
**Criteres d acceptation** :
- Etant donne {context_1}, quand {action_1}, alors {result_1}
- Etant donne {context_2}, quand {action_2}, alors {result_2}
**Priorite** : Must Have

### 2.2 Important (Should Have)
{should_have_features}

### 2.3 Bonus (Could Have)
{could_have_features}

### 2.4 Hors perimetre V1 (Won't Have)
{wont_have_features}

---

## 3. Regles de gestion

| ID | Regle | Condition | Action |
|----|-------|-----------|--------|
| RG-001 | {rule_name} | {condition} | {action} |

---

## 4. Roles et permissions

| Action | {role_1} | {role_2} | {role_3} |
|--------|----------|----------|----------|
| {action_1} | oui/non | oui/non | oui/non |

---

## 5. Integrations

### 5.1 {integration_name}
- **Service** : {service}
- **Usage** : {usage}
- **Donnees echangees** : {data}
- **Gestion d erreur** : {error_handling}

---

## 6. Notifications

| Declencheur | Canal | Destinataire | Template |
|-------------|-------|-------------|----------|
| {trigger} | {channel} | {recipient} | {template} |

---

## 7. Contraintes transversales

- **Accessibilite** : {accessibility}
- **Multilingue** : {i18n}
- **Conformite** : {compliance}
- **Performance** : {performance}
- **Compatibilite** : {compatibility}

---

## 8. Cas d erreur et edge cases

| Scenario | Comportement attendu |
|----------|---------------------|
| {error_scenario_1} | {expected_behavior_1} |

---

> Document genere par `/project-architect` -- ATUM SAS
""",

    "architecture-doc.md": """# {project_name} -- Architecture Technique

**Version** : 1.0
**Date** : {date}
**Auteur** : {author}

---

## 1. Decisions d architecture (ADR)

### ADR-001 : {decision_title}
- **Contexte** : {context}
- **Decision** : {decision}
- **Justification** : {rationale}
- **Alternatives** : {alternatives}
- **Consequences** : {consequences}

---

## 2. Stack technique

| Couche | Technologie | Version | Justification |
|--------|-------------|---------|---------------|
| Frontend | {frontend} | {version} | {why} |
| Backend | {backend} | {version} | {why} |
| Base de donnees | {database} | {version} | {why} |
| Hebergement | {hosting} | - | {why} |

---

## 3. Architecture globale

```
{architecture_diagram}
```

---

## 4. Modele de donnees

### Entites

#### {entity_name}
| Champ | Type | Contraintes | Description |
|-------|------|-------------|-------------|
| id | UUID | PK | Identifiant unique |
| {field} | {type} | {constraints} | {description} |

### Relations
- {entity_a} -> {entity_b} : {cardinality} ({description})

---

## 5. Architecture API

| Methode | Endpoint | Description | Auth |
|---------|----------|-------------|------|
| GET | /api/{resource} | {description} | {auth} |
| POST | /api/{resource} | {description} | {auth} |

---

## 6. Authentification et autorisation

- **Mecanisme** : {auth_mechanism}
- **Stockage tokens** : {token_storage}
- **Refresh strategy** : {refresh}
- **Permissions** : {permissions_model}

---

## 7. Infrastructure

- **Hebergement** : {hosting_details}
- **Environnements** : {environments}
- **CI/CD** : {cicd}
- **Monitoring** : {monitoring}
- **Backups** : {backups}

---

## 8. Securite

- **OWASP Top 10** : {owasp_coverage}
- **Gestion des secrets** : {secrets}
- **Chiffrement** : {encryption}
- **Audit trail** : {audit}

---

## 9. Conventions

- **Nommage branches** : {branch_naming}
- **Nommage commits** : {commit_convention}
- **Linter/Formatter** : {linter}
- **Structure dossiers** : {folder_structure}

---

## 10. Budget de performance

| Route/Page | TTI cible | LCP cible | Bundle max |
|------------|-----------|-----------|------------|
| {route} | {tti} | {lcp} | {bundle} |

---

> Document genere par `/project-architect` -- ATUM SAS
""",

    "planning-projet.md": """# {project_name} -- Planning Projet

**Date** : {date}
**Chef de projet** : {pm}

---

## 1. Plan de contenu

| Contenu | Responsable | Echeance | Statut |
|---------|-------------|----------|--------|
| {content_item} | {responsible} | {deadline} | A faire |

---

## 2. Estimation par lot

| Lot | Description | Complexite | Estimation |
|-----|-------------|-----------|------------|
| Lot 1 | {description} | {complexity} | {estimate} |

**Buffer technique** : +25% pour imprevisibles

---

## 3. Planning macro

| Jalon | Date | Livrable | Validation |
|-------|------|----------|-----------|
| Kick-off | {date} | - | - |
| {milestone} | {date} | {deliverable} | {validator} |
| Mise en ligne | {date} | Production | Client |

---

## 4. RACI

| Activite | {person_1} | {person_2} | {person_3} |
|----------|-----------|-----------|-----------|
| {activity} | R/A/C/I | R/A/C/I | R/A/C/I |

R = Responsable, A = Approbateur, C = Consulte, I = Informe

---

## 5. Gouvernance

- **Points de suivi** : {meeting_cadence}
- **Outils** : {tools}
- **Canal de communication** : {channels}
- **Process de changement** : {change_process}
- **Circuit de validation** : {validation_circuit}

---

## 6. Checklist juridique

- [ ] Contrat de prestation signe
- [ ] Conditions de paiement definies
- [ ] Clause de propriete intellectuelle
- [ ] NDA si necessaire
- [ ] DPA si donnees personnelles
- [ ] CGU/CGV si plateforme
- [ ] Mentions legales
- [ ] Politique de confidentialite
- [ ] Conformite RGPD verifiee

---

> Document genere par `/project-architect` -- ATUM SAS
""",

    "checklist-pre-dev.md": """# {project_name} -- Checklist Pre-Developpement

**Date** : {date}
**Taille** : {size}
**Verdict** : {verdict}

---

## Livrables strategiques

- [{status}] Brief valide et objectifs clairs
- [{status}] Personas et parcours utilisateurs
- [{status}] MVP defini
- [{status}] Strategie de croissance documentee
- [{status}] Arborescence et architecture de l information

## Livrables fonctionnels

- [{status}] Cahier des charges fonctionnel complet
- [{status}] User stories avec criteres d acceptation
- [{status}] Backlog priorise et estime
- [{status}] Specifications des integrations
- [{status}] Regles de gestion documentees

## Livrables UX/UI

- [{status}] Brief UX/UI
- [{status}] Inventaire des ecrans
- [{status}] Etats d interface specifies
- [{status}] Microcopy valide
- [{status}] Design system brief

## Livrables techniques

- [{status}] Architecture technique documentee
- [{status}] ADR rediges
- [{status}] Stack choisie et justifiee
- [{status}] Modele de donnees
- [{status}] Architecture API
- [{status}] Strategie de test definie
- [{status}] Pipeline CI/CD planifie

## Livrables organisationnels

- [{status}] Planning macro valide
- [{status}] RACI defini
- [{status}] Equipe staffee
- [{status}] Outils de gestion configures
- [{status}] Calendrier de livraison contenu

## Livrables contractuels

- [{status}] Contrat signe
- [{status}] Premier jalon paye
- [{status}] NDA signe (si applicable)
- [{status}] DPA signe (si applicable)

---

## Incoherences detectees

{inconsistencies}

## Manques critiques

{critical_gaps}

---

**Score** : {score_valid}/{score_total} items valides ({score_percent}%)

**Prochaines etapes** :
1. {next_step_1}
2. {next_step_2}
3. {next_step_3}

---

> Document genere par `/project-architect` -- ATUM SAS
"""
}

for filename, content in templates.items():
    filepath = os.path.join(base, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    lines = content.count("\n") + 1
    print(f"  {filename}: {lines} lines")

print(f"\nDone: {len(templates)} templates written")
