# {project_name} -- Architecture Technique

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
