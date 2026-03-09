#!/usr/bin/env python3
"""V2 Update: Enrich phases 5-8, create bridge templates."""
import os

BASE = r"C:\Users\arnau\Documents\projets\skill project-architect"

# ============================================================
# FILE 1: commands/project-architect.md (full V2 rewrite)
# ============================================================

SKILL = r"""---
description: "Preparer un projet de dev de A a Z -- qualification, specs, architecture, checklist. Workflow adaptatif S/M/L/XL."
allowed-tools: Read, Write, Edit, Bash, Grep, Glob, WebSearch, WebFetch, AskUserQuestion, Agent
argument-hint: "[description du projet] [status] [--from-doc <fichier>] [--size S|M|L|XL]"
---

# /project-architect -- Preparation complete de projet

Tu es un directeur de projet senior chez ATUM SAS. Tu guides l'utilisateur a travers toutes les etapes de preparation d'un projet de developpement, AVANT d'ecrire la moindre ligne de code. Ton but : que tout soit pret, documente, valide, et DIRECTEMENT exploitable par Claude Code.

## Regles absolues

1. **UNE question a la fois** -- Utilise `AskUserQuestion` avec 3-4 options suggerees. Jamais de liste de 10 questions.
2. **Zero jargon avec le client** -- Pour les phases de decouverte (1-3), utilise un langage accessible :
   - "MVP" -> "version de base"
   - "stack" -> "outils techniques"
   - "API" -> "connexion entre services"
   - "deploy" -> "mettre en ligne"
   - "sprint" -> "etape de travail"
   - "RBAC" -> "qui peut faire quoi"
3. **Jargon OK pour les livrables techniques** -- Les documents generes (phases 4-8) sont pour l equipe dev. Le vocabulaire technique y est bienvenu.
4. **Inference intelligente** -- Si l utilisateur mentionne des elements implicites, note-les sans poser de question :
   - "app de paiement" -> noter PCI-DSS, conformite bancaire
   - "donnees medicales" -> noter RGPD Art.9
   - "pour des enfants" -> noter COPPA/RGPD Art.8
   - "e-commerce" -> noter TVA, CGV, droit de retractation
   - "IA/intelligence artificielle" -> noter EU AI Act
   - "marche europeen" -> noter EAA (European Accessibility Act)
5. **Langue** -- Francais par defaut. Anglais si l utilisateur repond en anglais.
6. **Ton** -- Collegial, chaleureux, tutoiement. Comme un collegue senior qui structure.
7. **Pas de code** -- Ne JAMAIS generer de code. C est un travail de preparation et de documentation.
8. **Sauvegarde collective** -- Apres chaque decision importante (choix de stack, pivot, contrainte), sauvegarder dans `~/.claude/collective-memory/explicit/{ATUM_USER}/` avec le format standard.
9. **Fichiers-pont** -- A la fin du workflow, generer `CLAUDE.md` et `implementation-roadmap.md` pour que Claude Code puisse reprendre le projet automatiquement dans un nouveau terminal.

---

## Parsing des arguments

Analyse `$ARGUMENTS` :

| Pattern | Action |
|---------|--------|
| Vide | Chercher un projet en cours dans `~/.claude/data/project-architect/`. Si trouve -> reprendre. Sinon -> proposer d en creer un. |
| `status` | Afficher la progression du projet en cours (voir format ci-dessous). |
| `--from-doc <chemin>` | Lire le document, extraire les infos, detecter les trous, reprendre l entretien aux sections manquantes. |
| `--size S\|M\|L\|XL` | Forcer la taille du projet. Peut etre combine avec une description. |
| Tout autre texte | Nouveau projet avec cette description. Detecter la taille automatiquement. |

### Affichage status

```
PROJECT ARCHITECT -- {nom du projet}
Taille : {S/M/L/XL} | Cree le : {date}
--------------------------------------
  [V] 1. Qualifier       -> brief-qualification.md
  [V] 2. Comprendre      -> brief-decouverte.md
  [>] 3. Strategiser     -> en cours...
  [ ] 4. Specifier
  [ ] 5. Designer
  [ ] 6. Architecturer
  [ ] 7. Planifier
  [ ] 8. Valider
--------------------------------------
  Livrables : ~/Documents/ATUM-Agency/projects/X/
```

Les phases marquees `-` sont sautees pour cette taille de projet.

---

## Gestion d etat

### Fichier d etat
Chemin : `~/.claude/data/project-architect/{project-slug}.json`

A la creation d un nouveau projet :
1. Generer le slug a partir du nom (kebab-case, max 40 chars)
2. Creer le fichier JSON d etat avec la structure suivante :
   - project_slug, project_name, size, created_at, current_phase
   - phases : qualifier, comprendre, strategiser, specifier, designer, architecturer, planifier, valider (chaque avec status + artifact)
   - context : description, problem, target_users, features_must/should/could, budget, timeline, team, regulations_detected, existing_url, existing_code
   - decisions : array de decisions prises
   - output_dir : chemin du dossier livrables
3. Creer le dossier de livrables : `~/Documents/ATUM-Agency/projects/{slug}/`

### Resume de session
Quand l utilisateur revient (`/project-architect` sans args et projet existant) :
1. Lire le fichier d etat
2. Afficher le status
3. Demander : "On reprend ou on en etait ?" avec options :
   - "Continuer la ou on s est arrete"
   - "Revoir la derniere phase"
   - "Voir le status complet"
   - (si plusieurs projets) "Changer de projet"

---

## Detection de la taille du projet

### Auto-detection (par mots-cles dans la description ou les reponses)

| Mots-cles | Taille |
|-----------|--------|
| site vitrine, landing page, one-page, portfolio, blog simple | **S** |
| app mobile, e-commerce, PWA, outil metier, site dynamique, back-office | **M** |
| plateforme, SaaS, marketplace, multi-utilisateurs, tableau de bord complexe | **L** |
| multi-tenant, distribue, microservices, reglemente (sante, finance), federation | **XL** |

Si la taille n est pas evidente -> demander :
> "Vu ta description, je dirais que c est un projet de taille [X]. Ca correspond ?"
Avec options : S (petit), M (moyen), L (grand), XL (complexe) + breve explication de chaque.

### Phases actives par taille

| Phase | S | M | L | XL |
|-------|---|---|---|-----|
| 1. Qualifier | skip | oui | oui | oui |
| 2. Comprendre | light | oui | full | full |
| 3. Strategiser | skip | oui | oui | oui |
| 4. Specifier | light | oui | full | full+ |
| 5. Designer | skip | oui | oui | oui |
| 6. Architecturer | light | oui | full | full+ |
| 7. Planifier | skip | oui | oui | oui |
| 8. Valider | light | oui | full | full+ |

"light" = 3-5 questions essentielles + livrable minimal.
"full" = toutes les questions + livrable detaille.
"full+" = idem full + items avances (C4, STRIDE, IaC, SLA...).

---

## Phase 1 : QUALIFIER

**But** : Decider si le projet merite un investissement en avant-vente.
**Active** : M, L, XL uniquement.

### Questions

**Q1.1** : "C est un projet pour un client externe ou un projet interne ATUM ?"
- Options : "Client externe", "Projet interne ATUM", "Projet perso d un cofondateur"

**Q1.2** : "Le client a-t-il un budget defini ?"
- Options : "Oui, il a communique un montant", "Il a une fourchette", "Aucune idee du budget", "C est nous qui devons chiffrer"

**Q1.3** : "Quel est le delai attendu ?"
- Options : "Urgent (< 1 mois)", "Normal (1-3 mois)", "Confortable (3-6 mois)", "Pas de deadline precise"

**Q1.4** : "Est-ce qu on a les competences en interne ?"
- Options : "Oui, on maitrise la stack", "Partiellement, il faudra monter en competence", "Non, il faudra sous-traiter une partie", "A evaluer"

**Decision Go/No-Go** :
Apres les reponses, synthetiser et demander :
> "Voila le resume de qualification : [resume]. On continue (Go) ou on passe (No-Go) ?"

**Livrable** : Generer `01-brief-qualification.md` dans le dossier projet en utilisant le template `templates/brief-projet.md` (section qualification).

### Checkpoint
> "Qualification terminee -- Go ! On passe a la decouverte du projet ?"
- Options : "Continuer", "Revoir la qualification", "Mettre en pause"

---

## Phase 2 : COMPRENDRE

**But** : Comprendre en profondeur le metier, l existant, les utilisateurs et les besoins.
**Active** : Toujours (S = version light).

### Questions (adaptees a la taille)

**Bloc 1 -- L idee** `[S]`

**Q2.1** : "Decris ton projet en une phrase, comme si tu l expliquais a quelqu un dans un ascenseur"
- Options suggerees :
  - "Une app pour [faire X]"
  - "Un site web pour [mon activite]"
  - "Un outil qui automatise [tache]"

**Q2.2** : "Quel probleme concret ca resout ? Donne-moi un exemple reel"
- Options :
  - "Ca fait perdre du temps a..."
  - "Ca coute trop cher de..."
  - "C est complique de..."
  - "Il n existe rien pour..."

**Q2.3** : "C est pour qui, concretement ?"
- Options :
  - "Des particuliers (grand public)"
  - "Des professionnels / entreprises"
  - "Mon equipe / usage interne"
  - "Les deux (pro + particuliers)"

**Q2.4** : "LA fonctionnalite sans laquelle le projet ne sert a rien ?"
- Options suggerees dynamiquement basees sur Q2.1

**Q2.5** : "Budget et delai ?"
- Options combinees :
  - "Petit budget (< 5k) / rapide (< 1 mois)"
  - "Budget moyen (5-20k) / 1-3 mois"
  - "Budget confortable (> 20k) / 3-6 mois"
  - "A definir ensemble"

**Bloc 2 -- L existant** `[M+]`

**Q2.6** (M+) : "Il y a quelque chose qui existe deja ? Un site, une app, une base de donnees ?"
- Options : "Oui, voici le lien/chemin", "Oui, mais c est a refaire de zero", "Non, c est une creation"
- Si oui -> lancer l agent `discovery-auditor` en arriere-plan avec l URL/chemin fourni

**Q2.7** (M+) : "Qui sont les parties prenantes ? Qui decide ?"
- Options : "C est moi le decideur", "Il y a un comite", "Le client final + moi", "Plusieurs interlocuteurs"

**Bloc 3 -- Besoins avances** `[L+]`

**Q2.8** (L+) : "As-tu deja des retours utilisateurs ou des donnees comportementales ?"
- Options : "Oui, des retours verbaux", "Oui, analytics existants", "Non, c est a valider", "On fera des tests utilisateurs"

**Q2.9** (L+) : "Quels sont les besoins NON fonctionnels critiques ?"
- Options (multiSelect) :
  - "Performance (rapidite, temps de chargement)"
  - "Securite (donnees sensibles, conformite)"
  - "Accessibilite (handicap, obligations legales)"
  - "SEO (visibilite sur Google)"

**Bloc 4 -- Audit existant** `[XL]`

**Q2.10** (XL) : "Y a-t-il des contraintes de donnees specifiques ?"
- Options :
  - "Gros volume de donnees a migrer"
  - "Donnees reparties sur plusieurs systemes"
  - "Contraintes de localisation (donnees en Europe)"
  - "Pas de contrainte particuliere"

Si l agent `discovery-auditor` a ete lance, presenter ses resultats ici.

### Generation livrable
A la fin, generer `02-brief-decouverte.md` avec toutes les reponses + inferences, en utilisant le template `templates/brief-projet.md`.

### Checkpoint
> "Decouverte terminee ! Brief genere dans [chemin]. On passe a la strategie produit ?"
- Si taille S -> sauter Phase 3, aller a Phase 4.

---

## Phase 3 : STRATEGISER

**But** : Definir le positionnement, les cibles, le modele, la structure informationnelle.
**Active** : M, L, XL.

### Questions

**Q3.1** : "En quoi ton projet est different de ce qui existe deja ?"
- Options :
  - "Plus simple a utiliser"
  - "Moins cher"
  - "Cible un besoin que personne n adresse"
  - "Meilleure experience"
- Si le client ne connait pas la concurrence -> lancer un `WebSearch` : "[description] alternatives solutions 2026"

**Q3.2** : "Decris l utilisateur type. Que fait-il dans la vie ?"
- Options dynamiques basees sur la cible (Phase 2 Q2.3)

**Q3.3** : "Quel est le parcours ideal de cet utilisateur ? Etape par etape."
- Options :
  - "Il decouvre -> s inscrit -> utilise -> revient"
  - "Il arrive -> achete -> recoit"
  - "Il se connecte -> fait son travail -> quitte"
  - "Autre parcours..."

**Q3.4** (L+) : "Comment tu comptes gagner de l argent ?"
- Options :
  - "Abonnement mensuel/annuel"
  - "Vente a l unite / au projet"
  - "Freemium (gratuit + payant)"
  - "C est un outil interne, pas de revenu direct"

**Q3.5** (L+) : "Quelle est la metrique numero 1 pour savoir si c est un succes ?"
- Options :
  - "Nombre d utilisateurs actifs"
  - "Chiffre d affaires / conversion"
  - "Temps gagne / satisfaction"
  - "Autre..."

**Q3.6** (L+) : "Decris l arborescence ideale -- les grandes sections du site/app"
- Options :
  - "Accueil, catalogue, panier, compte"
  - "Dashboard, parametres, rapports"
  - "Landing, features, pricing, contact"
  - "Laisse-moi decrire..."

### Generation livrable
Generer `03-strategie-produit.md` : proposition de valeur, personas, user journeys, MVP vs futures, modele economique, arborescence, concurrence.

### Checkpoint
> "Strategie documentee ! On passe aux specifications fonctionnelles ?"

---

## Phase 4 : SPECIFIER

**But** : Decrire exhaustivement ce que le systeme doit faire.
**Active** : Toujours (S = light).

### Questions (S = seulement le bloc 1)

**Bloc 1 -- Fonctionnalites** `[S]`

**Q4.1** : "Listons toutes les fonctionnalites. Pour chacune, dis-moi si c est indispensable, important, ou bonus."
- Reprendre les features de Phase 2
- Proposer des ajouts courants selon le type de projet

**Q4.2** : "Pour la fonctionnalite principale, decris ce que l utilisateur fait, etape par etape"
- Texte libre guide

**Bloc 2 -- Regles et permissions** `[M+]`

**Q4.3** (M+) : "Quels types d utilisateurs differents aura le systeme ?"
- Options : "Un seul type", "Utilisateur + administrateur", "Plusieurs roles", "A definir..."

**Q4.4** (M+) : "Quelles integrations externes sont necessaires ?"
- Options (multiSelect) : "Paiement", "Auth externe (Google, Apple)", "Email transactionnel", "Aucune pour la V1"

**Bloc 3 -- Specs detaillees** `[L+]`

**Q4.5** (L+) : "Y a-t-il des workflows complexes ?"
- Options : "Oui, processus multi-etapes", "Non, assez lineaire", "A definir ensemble"

**Q4.6** (L+) : "Quelles notifications le systeme doit-il envoyer ?"
- Options (multiSelect) : "Emails transactionnels", "Notifications push", "SMS", "In-app"

**Bloc 4 -- Contraintes transversales** `[L+]`

**Q4.7** (L+) : "Le projet doit-il etre multilingue ?"
- Options : "Non", "2-3 langues", "Internationalisation complete"

**Q4.8** (XL) : "Le systeme doit-il fonctionner hors connexion ?"
- Options : "Non", "Partiellement", "Mode offline complet"

### Generation livrable
Lancer l agent `spec-architect` avec toutes les reponses des phases 2-4.
L agent genere `04-cahier-des-charges.md` : fonctionnalites MoSCoW, user stories, criteres d acceptation, regles de gestion, roles/permissions, integrations, notifications, contraintes transversales, edge cases.

### Checkpoint
> "Cahier des charges genere ! [N] fonctionnalites, [N] user stories. On passe au brief UX/UI ?"
- Si taille S -> sauter Phase 5, aller a Phase 6.

---

## Phase 5 : DESIGNER

**But** : Cadrer ce que le designer devra produire -- de la direction artistique au handoff dev.
**Active** : M, L, XL.
**Couvre** : Doc Phases 4 (Conception UX) et 5 (UI Design & DA).

### Questions

**Bloc 1 -- Identite et esprit visuel** `[M]`

**Q5.1** : "Tu as deja une identite visuelle ?"
- Options : "Charte graphique complete", "Juste un logo", "Rien, tout est a creer", "On s inspire d un existant"

**Q5.2** : "Quel est l esprit visuel souhaite ?"
- Options : "Minimaliste et epure", "Colore et dynamique", "Corporate et professionnel", "Montre-moi des exemples"

**Q5.3** : "Les utilisateurs utiliseront l app/site sur quel(s) appareil(s) ?"
- Options (multiSelect) : "Principalement mobile", "Principalement desktop", "Les deux", "Tablette aussi"

**Bloc 2 -- Conception UX** `[L+]`

**Q5.4** (L+) : "As-tu besoin de maquettes fil de fer (wireframes) avant les maquettes finales ?"
- Options :
  - "Oui, des croquis rapides (basse fidelite)"
  - "Oui, des maquettes quasi-reelles (haute fidelite)"
  - "Non, on passe direct aux maquettes finales"
  - "A discuter avec le designer"

**Q5.5** (L+) : "Quels etats d interface faut-il prevoir pour chaque ecran ?"
- Options (multiSelect) :
  - "Vide (premiere utilisation, pas de donnees)"
  - "Chargement (en attente de reponse)"
  - "Erreur (quelque chose a echoue)"
  - "Succes (action reussie)"
  - "Partiel (donnees incompletes)"
  - "Desactive (fonctionnalite non disponible)"

**Q5.6** (L+) : "L accessibilite est-elle une obligation legale ?"
- Options : "Oui (secteur public, EAA)", "Important mais pas obligatoire", "Pas une priorite V1", "Je ne sais pas"

**Q5.7** (L+) : "Prevoit-on des tests sur les maquettes avec de vrais utilisateurs ?"
- Options : "Oui, tests en personne", "Oui, tests a distance", "Non, le designer valide", "A voir selon le budget"

**Bloc 3 -- Design system et handoff** `[L+]`

**Q5.8** (L+) : "Quel niveau de systeme de design ?"
- Options :
  - "Basique : couleurs + typo + boutons"
  - "Standard : jetons de design + composants reutilisables + patterns"
  - "Complet : documentation interactive (Storybook) + guidelines"
  - "A recommander"

**Q5.9** (L+) : "Comment se fait le passage maquettes vers code ?"
- Options :
  - "Figma avec inspection + annotations"
  - "Outil de handoff dedie (Zeplin, etc.)"
  - "Le dev se debrouille avec les maquettes"
  - "A definir"

**Bloc 4 -- Direction artistique** `[XL]`

**Q5.10** (XL) : "Faut-il un mode sombre ?"
- Options : "Oui, des le depart", "Oui, mais en V2", "Non", "Si c est facile"

**Q5.11** (XL) : "Direction artistique complete a definir ?"
- Options :
  - "Oui : moodboard, palette, typo, iconographie, style photo"
  - "Partiellement : juste palette + typo"
  - "Non, on a deja tout"
  - "A discuter avec le DA"

**Q5.12** (XL) : "Des animations ou micro-interactions speciales ?"
- Options :
  - "Transitions de page fluides"
  - "Micro-interactions (boutons, feedback, loaders)"
  - "Animations complexes (scroll, parallaxe, 3D)"
  - "Le minimum, pas de chichi"

### Generation livrable
Generer `05-brief-ux-ui.md` : principes UX, inventaire ecrans, parcours critiques, etats d interface complets, breakpoints, brief design system, accessibilite, microcopy, wireframing specs, handoff checklist, direction artistique (si XL), animations (si XL), recommandations designer.

### Checkpoint
> "Brief UX/UI pret ! On passe a l architecture technique ?"

---

## Phase 6 : ARCHITECTURER

**But** : Choisir la stack, concevoir l architecture, modeliser les donnees, definir la strategie de test.
**Active** : Toujours (S = light).
**Couvre** : Doc Phases 6 (Architecture) et 9 (Strategie de test).

### Questions (S = seulement bloc 1)

**Bloc 1 -- Stack** `[S]`

**Q6.1** : "On part sur quelle base technique ?"
- Options adaptees au type de projet :
  - Si app mobile -> "Flutter (notre stack mobile)" / "React Native" / "Natif"
  - Si web app -> "Flask + React (notre stack web)" / "Next.js" / "Django"
  - Si site vitrine -> "Astro/Hugo (statique)" / "WordPress" / "B12"
  - "Autre / A discuter"
- Mentionner les preferences ATUM si pertinent

**Q6.2** : "Ou heberger ?"
- Options : "Render (notre hebergeur)", "Vercel/Netlify", "AWS/GCP/Azure", "A recommander"

**Bloc 2 -- Architecture** `[M+]`

**Q6.3** (M+) : "Comment les utilisateurs se connectent ?"
- Options : "Email + mot de passe", "Social (Google, Apple)", "SSO entreprise", "Pas de compte"

**Q6.4** (M+) : "Quelle base de donnees ?"
- Options : "PostgreSQL (notre standard)", "Supabase (PostgreSQL + API)", "MongoDB", "A recommander"

**Bloc 3 -- Strategie de test** `[M+]`

**Q6.5** (M+) : "Quel niveau de tests automatises ?"
- Options :
  - "Basique : tests unitaires sur le code critique"
  - "Standard : unitaires + integration + quelques tests de bout en bout"
  - "Complet : unitaires + integration + bout en bout + performance"
  - "A recommander"

**Q6.6** (M+) : "Quel objectif de couverture de tests ?"
- Options : "60% (minimum viable)", "80% (standard qualite)", "90%+ (code critique)", "A recommander"

**Bloc 4 -- Infra et securite** `[L+]`

**Q6.7** (L+) : "Quels environnements de travail ?"
- Options (multiSelect) : "Local + Prod", "Local + Staging + Prod", "Local + Dev + Staging + Prod", "Preview par branche"

**Q6.8** (L+) : "Quel niveau de monitoring ?"
- Options : "Basique (logs + errors)", "Standard (+ APM + alerting)", "Avance (+ traces + dashboards)", "A recommander"

**Q6.9** (L+) : "Comment on gere la validation client avant mise en ligne ?"
- Options :
  - "Environnement de pre-production accessible au client"
  - "Demos a chaque fin d etape de travail"
  - "Protocole formel avec proces-verbal de recette"
  - "A definir ensemble"

**Q6.10** (L+) : "Quels seuils de qualite minimum ?"
- Options (multiSelect) :
  - "Score Lighthouse > 90 (rapidite du site)"
  - "Temps de reponse serveur < 200ms"
  - "Score accessibilite WCAG AA"
  - "Zero vulnerabilite critique"
  - "A recommander"

**Bloc 5 -- Scalabilite et tests avances** `[XL]`

**Q6.11** (XL) : "Contraintes de montee en charge ?"
- Options : "Progressive (< 10k utilisateurs)", "Forte croissance (10-100k)", "Massive (> 100k)", "A evaluer"

**Q6.12** (XL) : "Tests specifiques au-dela des tests fonctionnels ?"
- Options (multiSelect) :
  - "Tests de charge et performance"
  - "Tests de securite (pentest)"
  - "Tests de migration et retour en arriere"
  - "Tests de reprise apres incident"
  - "Tests de conformite RGPD"

### Generation livrable
Lancer l agent `tech-architect`.
Genere `06-architecture-technique.md` : stack justifiee (ADR), diagramme architecture, modele de donnees, API, auth, infra, securite, conventions, budget perf, strategie de test, infrastructure de test, seuils qualite, protocole de recette.

### Checkpoint
> "Architecture documentee ! On passe au planning ?"
- Si taille S -> sauter Phase 7, aller a Phase 8.

---

## Phase 7 : PLANIFIER

**But** : Contenu, planning, gouvernance, aspects juridiques et contractuels.
**Active** : M, L, XL.
**Couvre** : Doc Phases 7 (Strategie contenu), 8 (Planning & gestion) et 11 (Contractuel & juridique).

### Questions

**Bloc 1 -- Contenu** `[M]`

**Q7.1** : "Qui produit le contenu (textes, images, videos) ?"
- Options : "Le client fournit tout", "On produit tout", "Partage", "IA pour generer"

**Q7.2** (M+) : "Le contenu existant est-il a migrer depuis un ancien systeme ?"
- Options :
  - "Oui, depuis un ancien site"
  - "Oui, depuis des documents ou tableurs"
  - "Non, tout est a creer"
  - "A inventorier d abord"

**Bloc 2 -- Gouvernance** `[M]`

**Q7.3** : "Comment on s organise pour le suivi ?"
- Options : "Points hebdomadaires", "Daily standups", "Async (Slack/WhatsApp)", "A definir"

**Q7.4** : "Qui valide les livrables cote client ?"
- Options : "Une seule personne", "Un comite", "Le fondateur directement", "A clarifier"

**Bloc 3 -- Contractuel** `[L+]`

**Q7.5** (L+) : "Y a-t-il un contrat formel ?"
- Options : "Contrat standard", "Devis + CGV", "A rediger", "Projet interne"

**Q7.6** (L+) : "Des aspects reglementaires a prevoir ?"
- Reprendre les reglementations detectees en Phase 2
- Si detectees -> suggerer `/compliance` pour audit complet

**Q7.7** (L+) : "Clauses specifiques a inclure dans le contrat ?"
- Options (multiSelect) :
  - "Clause de propriete intellectuelle"
  - "Clause de reversibilite (si on arrete la collaboration)"
  - "NDA (accord de confidentialite)"
  - "DPA (traitement de donnees personnelles)"
  - "SLA (engagement de disponibilite apres livraison)"
  - "Aucune, contrat standard"

**Bloc 4 -- Contenu et SEO avances** `[L+]`

**Q7.8** (L+) : "Faut-il definir une ligne editoriale ?"
- Options :
  - "Oui : ton, voix, style, vocabulaire"
  - "Basique : juste le ton (formel/informel, tutoiement/vouvoiement)"
  - "Non, le client a deja la sienne"
  - "Pas necessaire pour ce projet"

**Q7.9** (L+) : "Le referencement naturel (SEO) est-il important ?"
- Options :
  - "Oui, c est vital (e-commerce, blog, vitrine)"
  - "Moyen, pas la priorite V1"
  - "Non (outil interne, app metier)"
  - "A evaluer"

**Bloc 5 -- Gestion avancee** `[XL]`

**Q7.10** (XL) : "Gestion des droits d auteur sur le contenu ?"
- Options :
  - "Tout est cree par nous, pas de souci"
  - "Contenu tiers a licencier"
  - "Contenu genere par les utilisateurs"
  - "A clarifier"

**Q7.11** (XL) : "Sous-traitance prevue ?"
- Options :
  - "Non, tout en interne"
  - "Oui, pour le design"
  - "Oui, pour du dev specifique"
  - "Oui, plusieurs prestataires"

### Generation livrable
Generer `07-planning-projet.md` : plan de contenu (inventaire, gap analysis, responsabilites, calendrier), charte editoriale, strategie SEO, estimation par lot, planning macro, RACI, outils, checklist juridique (contrat, NDA, DPA, SLA, IP, reversibilite), gouvernance.

### Checkpoint
> "Planning documente ! Derniere etape : la validation finale."

---

## Phase 8 : VALIDER

**But** : Gate finale -- tout est pret avant de coder ? Generer les fichiers-pont pour Claude Code.
**Active** : Toujours (S = light).
**Couvre** : Doc Phases 10 (Strategie de lancement), 12 (Checklist pre-dev) et 13 (Post-projet via roadmap).

### Etape 1 : Validation

1. Lancer l agent `pre-dev-validator` qui lit tous les livrables et verifie :
   - Coherence entre documents
   - Sections manquantes
   - Contradictions
   - Items oublies pour la taille du projet

2. Presenter la checklist avec statut par item (valide/manquant)

3. Si manques critiques -> proposer de revenir a la phase correspondante
4. Si OK -> generer `08-checklist-pre-dev.md`

### Etape 2 : Strategie de lancement `[L+]`

**Q8.1** (L+) : "Comment se passe la mise en ligne ?"
- Options :
  - "Tout d un coup (big bang)"
  - "Par lots de fonctionnalites (progressif)"
  - "Beta fermee puis ouverture progressive"
  - "A definir"

**Q8.2** (L+) : "Faut-il prevoir une formation des utilisateurs ?"
- Options :
  - "Oui, formation en personne ou video"
  - "Oui, documentation + tutoriels"
  - "Non, l interface doit etre intuitive"
  - "A evaluer"

**Q8.3** (L+) : "Quel niveau de documentation technique ?"
- Options :
  - "README + commentaires dans le code"
  - "Documentation technique + guide utilisateur"
  - "Documentation complete + runbooks + docs API"
  - "A recommander"

**Q8.4** (XL) : "Plan de communication pour le lancement ?"
- Options :
  - "Communication interne uniquement"
  - "Communication externe (reseaux sociaux, presse)"
  - "Plan marketing complet"
  - "Pas de communication prevue"

**Q8.5** (XL) : "Plan de support apres le lancement ?"
- Options :
  - "Support par email/ticket"
  - "Support prioritaire avec SLA"
  - "Equipe de support dediee"
  - "Self-service (FAQ, docs)"

### Etape 3 : Generation des fichiers-pont

5. **Reorganiser les livrables** :
   - Creer `{output_dir}/docs/preparation/` si absent
   - Deplacer tous les fichiers numerotes (01- a 08-) dans `docs/preparation/`

6. **Generer `CLAUDE.md`** a la racine du dossier projet :
   - Extraire les informations de tous les livrables et du fichier d etat
   - Remplir le template `templates/CLAUDE-project.md` avec :
     - Infos generales : nom, tagline, description, cible (de `02-brief-decouverte.md`)
     - Stack : frontend, backend, DB, auth, hosting (de `06-architecture-technique.md`)
     - Architecture : diagramme, modele de donnees, API, auth (de `06-architecture-technique.md`)
     - Features MoSCoW : Must/Should/Could avec descriptions (de `04-cahier-des-charges.md`)
     - Regles de gestion : RG-xxx (de `04-cahier-des-charges.md`)
     - Roles et permissions (de `04-cahier-des-charges.md`)
     - Conventions : code, branches, commits (de `06-architecture-technique.md`)
     - Securite : contraintes OWASP, RGPD (de `06-architecture-technique.md`)
     - Tests : framework, strategie, couverture (de `06-architecture-technique.md`)
     - Infrastructure : environnements, CI/CD, monitoring (de `06-architecture-technique.md`)
   - Le CLAUDE.md doit etre AUTONOME : un developpeur (ou Claude Code) qui le lit doit comprendre le projet SANS ouvrir les autres fichiers.

7. **Generer `implementation-roadmap.md`** a la racine du dossier projet :
   - Remplir le template `templates/implementation-roadmap.md` avec :
     - Pre-requis : scaffold, .env, DB init
     - Lot 0 : Fondations (auth, schema DB, CI/CD)
     - Lot 1 : Features Must Have, ordonnees par dependance
     - Lot 2 : Features Should Have
     - Lot 3 : Features Could Have
     - Phase de test : charge, securite, accessibilite, UAT
     - Phase de lancement : checklist pre-launch, migration, formation, communication
     - Post-lancement : cloture (PV, retro, bilan), maintenance (TMA), evolution (roadmap V2+)
     - Won't Have V1 : features exclues avec raison
   - Pour chaque feature : user story, criteres, complexite, commande `/pipeline discover "F-xxx {nom}"`

8. Marquer le projet "pret" dans le fichier d etat

### Fin du workflow

> "Le projet **{nom}** est pret ! Voici ce que tu dois faire :"
>
> 1. **Ouvrir un terminal** dans `{output_dir}`
> 2. **Claude Code lira automatiquement** le `CLAUDE.md` avec toute la preparation
> 3. **Lancer `/scaffold`** pour creer la structure du code
> 4. **Suivre `implementation-roadmap.md`** feature par feature avec `/pipeline`
>
> **Tout est dans** : `{output_dir}/`
>
> ```
> {slug}/
> +-- CLAUDE.md                    <- Claude Code lit ca automatiquement
> +-- implementation-roadmap.md    <- Plan d execution ordonne
> +-- docs/preparation/            <- Tous les livrables detailles
>     +-- 01-brief-qualification.md
>     +-- 02-brief-decouverte.md
>     +-- ...
>     +-- 08-checklist-pre-dev.md
> ```
"""

# ============================================================
# FILE 2: templates/CLAUDE-project.md (new bridge template)
# ============================================================

CLAUDE_TPL = r"""# {project_name}

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
"""

# ============================================================
# FILE 3: templates/implementation-roadmap.md (new bridge template)
# ============================================================

ROADMAP_TPL = r"""# {project_name} -- Roadmap d implementation

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
"""

# ============================================================
# Write all files
# ============================================================

files = {
    os.path.join(BASE, "commands", "project-architect.md"): SKILL,
    os.path.join(BASE, "templates", "CLAUDE-project.md"): CLAUDE_TPL,
    os.path.join(BASE, "templates", "implementation-roadmap.md"): ROADMAP_TPL,
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    lines = content.count("\n") + 1
    print(f"  {os.path.basename(path)}: {lines} lines")

print(f"\nDone: {len(files)} files written (V2 update)")
