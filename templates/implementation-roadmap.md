# {project_name} -- Roadmap d implementation

**Date** : {date}
**Taille** : {size}
**Auteur** : {author}

---

## Pre-requis

Avant de commencer le developpement :

1. **Scaffolding** : Lancer `/scaffold` pour creer la structure du projet
2. **Variables d environnement** : Creer le fichier `.env` avec les cles necessaires
3. **Base de donnees** : Initialiser le schema ({database})
4. **Depot** : Initialiser Git, configurer les branches ({branch_naming})
5. **CI/CD** : Configurer le pipeline ({cicd})

---

## Lot 0 : Fondations

> Mettre en place l infrastructure technique de base.

### F-000 : Setup projet et CI/CD
- **Description** : Configurer la structure du projet, linter, formatter, pipeline CI/CD, environnements
- **Complexite** : Medium
- **Dependances** : Aucune (premier lot)
- **Commande** : `/pipeline discover "F-000 Setup projet et CI/CD"`

### F-001 : Schema de base de donnees
- **Description** : Creer les tables/collections de base : {core_entities}
- **Complexite** : {db_complexity}
- **Dependances** : F-000
- **Commande** : `/pipeline discover "F-001 Schema de base de donnees"`

### F-002 : Authentification
- **Description** : {auth_description}
- **Complexite** : {auth_complexity}
- **Dependances** : F-001
- **Commande** : `/pipeline discover "F-002 Authentification"`

---

## Lot 1 : Must Have (fonctionnalites indispensables)

> Version de base -- le minimum pour que le produit fonctionne.

{must_have_features_with_details}

---

## Lot 2 : Should Have (fonctionnalites importantes)

> Ameliorations significatives -- a faire si le temps le permet.

{should_have_features_with_details}

---

## Lot 3 : Could Have (bonus)

> Nice to have -- si tout le reste est fait.

{could_have_features_with_details}

---

## Phase de test

> Valider la qualite avant la mise en ligne.

### Tests fonctionnels
- [ ] Tests unitaires : couverture >= {coverage_target}
- [ ] Tests d integration : API, base de donnees, auth
- [ ] Tests de bout en bout : parcours critiques

### Tests non fonctionnels
- [ ] Tests de charge : {load_test_targets}
- [ ] Tests de securite : scan OWASP, pentest si prevu
- [ ] Tests d accessibilite : score WCAG {wcag_target}
- [ ] Tests de compatibilite : navigateurs et appareils cibles

### Recette client (UAT)
- [ ] Environnement de recette accessible
- [ ] Scenarios de recette prepares
- [ ] Proces-verbal de recette signe

---

## Phase de lancement

> Tout ce qui doit etre fait avant, pendant et juste apres la mise en ligne.

### Checklist pre-lancement
- [ ] DNS configure
- [ ] SSL/HTTPS actif
- [ ] Redirections 301 en place (si migration)
- [ ] robots.txt et sitemap.xml
- [ ] Analytics et tracking configures
- [ ] Consent management (cookies RGPD)
- [ ] Backups automatises et testes
- [ ] Monitoring et alertes actifs
- [ ] Documentation technique a jour
- [ ] Documentation utilisateur prete

### Deploiement
- **Strategie** : {deployment_strategy}
- **Plan de rollback** : {rollback_plan}
- **Fenetre de deploiement** : {deployment_window}

### Formation
- {training_plan}

### Communication
- {launch_communication}

---

## Post-lancement

> Activites de cloture et de maintenance continue.

### Cloture du projet
- [ ] Proces-verbal de livraison signe
- [ ] Retrospective interne (ce qui a marche, ce qui peut etre ameliore)
- [ ] Bilan financier (budget prevu vs reel)
- [ ] Enquete de satisfaction client

### Maintenance evolutive
- **TMA (maintenance corrective)** : {tma_plan}
- **Montee en version des dependances** : {dependency_update_plan}
- **Monitoring continu** : {monitoring_plan}
- **Revue de securite periodique** : {security_review_plan}

### Evolution future
- **Roadmap V2** : {v2_roadmap_summary}
- **Features Won't Have reportees** : {deferred_features}

### Fin de vie (si applicable)
- {end_of_life_plan}

---

## Won't Have V1 (hors perimetre)

| Feature | Raison | Report prevu |
|---------|--------|--------------|
{wont_have_table}

---

> Roadmap generee par `/project-architect` -- ATUM SAS
