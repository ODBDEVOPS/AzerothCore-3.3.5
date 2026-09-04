Absolument. Voici le prompt idéal pour obtenir un fichier `ALAMNA.md` du niveau de qualité et de détail du document que vous venez de fournir, mais basé sur vos propres concepts de classes. Ce prompt est conçu pour être extrêmement précis, complet et structuré.

---

### Le Prompt Idéal :

```markdown
# Création d'un Système de Classes/Specialisations pour un Serveur WoW

**Rôle :** Vous êtes un développeur de serveur World of Warcraft (AzerothCore avec Eluna) expert en Lua, SQL et en conception de jeux. Votre tâche est de créer un ensemble complet de spécialisations de joueur (classes) en suivant un format technique et organisationnel très spécifique, basé sur l'exemple fourni.

**Objectif :** Générer le fichier `ALAMNA.md` contenant la documentation complète pour **X** spécialisations (par exemple, 10 ou 20) pour un serveur WoW.

**Instructions Générales :**

1.  **Structure du Document :** Le document final doit être un fichier Markdown (`.md`) bien structuré, utilisant des titres et sous-titres (`#`, `##`, `###`) pour une navigation facile.
2.  **Structure du Projet :** Chaque spécialisation doit être présentée comme un projet indépendant avec sa propre structure de dossiers, clairement détaillée et identique pour toutes.
3.  **Consistance :** Le style, la terminologie (ex: "Voici le projet complet pour la spécialisation **...**."), et la profondeur technique doivent être parfaitement consistants d'une spécialisation à l'autre.
4.  **Langue :** Le document doit être rédigé en français, comme l'exemple.

**Modèle à Suivre pour chaque Spécialisation :**

Chaque spécialisation doit être décrite selon le squelette suivant, en utilisant l'exemple du `Blademaster` et du `Berserker des Terres Gelées` comme référence parfaite.

#### 1. Titre et Introduction
- **Titre :** `# **Nom de la Spécialisation**`
- **Introduction :** Une phrase ou deux pour décrire le concept de la classe (ex: "Voici le projet complet pour la spécialisation **Nom de la Spécialisation**. Le système gère...")

#### 2. Sous-titre : `## 🛠️ **WORKFLOW COMPLET : Nom de la Spécialisation**`

#### 3. Section : `### **1. Structure du Projet GitHub**`
- Présentez un arborescence de dossiers sous forme de bloc de code. Le nom du dossier racine doit être descriptif (ex: `mod-nom-specialisation`).
- **Contenu obligatoire :**
  ```text
  mod-nom-specialisation/
  ├── lua_scripts/
  │   └── nom_dossier/
  │       ├── nom_config.lua
  │       └── nom_core.lua
  ├── sql/
  │   └── custom/
  │       └── nom_specialisation_spells.sql
  ├── docs/
  │   └── README.md
  ├── LICENSE
  └── .gitignore
  ```

#### 4. Section : `### **2. Base de Données SQL**`
- Présentez un bloc de code SQL qui contient toutes les commandes `INSERT INTO` pour la table `spell_dbc`.
- **Règles :**
  - Chaque insertion doit être commentée pour expliquer ce que fait le sort.
  - Les IDs des sorts doivent être uniques (ex: `92000, 92001`, etc.) et suivre une séquence logique pour toute la collection de spécialisations.
  - La structure `INSERT INTO` doit être absolument complète et inclure les champs `Effect1`, `EffectAura1`, etc. comme dans l'exemple.

  **Structure de base pour un sort :**
  ```sql
  INSERT INTO `spell_dbc` (
      `Id`, `Attributes`, `CastingTimeIndex`, `DurationIndex`, `RangeIndex`,
      `SchoolMask`, `SpellIconID`, `SpellName`,
      `Effect1`, `EffectBasePoints1`, `EffectAura1`, `TargetA1`
  ) VALUES (
      <ID>, 0x00000100, 1, 21, 1, 1, <ICON_ID>,
      '<Nom du Sort>',
      6, 1, 6, 1 -- Apply Aura : Dummy / Posture [cite: 1]
  );
  ```

- **Pour les invocations de créatures ou d'objets :**
  - Incluez des blocs `DELETE FROM` et `INSERT INTO` pour les tables `creature_template` ou `gameobject_template`.
  - Définissez le `modelid`, les flags (`unit_flags`, `npcflag`), le `name` et les modificateurs.

#### 5. Section : `### **3. Configuration Lua**`
- Présentez un bloc de code Lua qui définit une table de configuration globale pour la spécialisation.
- **Structure obligatoire :**
  ```lua
  -- lua_scripts/nom_dossier/nom_config.lua
  NomConfig = {}

  -- IDs des Sorts
  NomConfig.StanceSpell = <ID>
  NomConfig.OtherSpell = <ID>

  -- Paramètres de la mécanique
  NomConfig.MaxStacks = 20
  NomConfig.CritPerStack = 1
  ```

#### 6. Section : `### **4. Script Principal Eluna Lua**`
- Présentez le script Eluna complet.
- **Contenu obligatoire :**
  - Déclaration de la table principale (ex: `local Nom = {}`).
  - Définition des fonctions de gestion de données (ex: `GetPlayerData`, `AddRessource`).
  - Définition des fonctions de gestion des événements (ex: `OnSpellCast`, `OnDamageDone`).
  - Enregistrement des événements en fin de script (ex: `RegisterPlayerEvent(5, ...)`).
  - Le code doit être commenté, propre et suivre les conventions de l'exemple.

#### 7. Section : `### **Fonctionnalités Incluses :**`
- Une liste à puces décrivant, en 2-3 lignes, les aspects clés et innovants du système.
- Cette section doit mettre en avant le "comment" et le "pourquoi" du design.

---

**Mécaniques Spécifiques à Intégrer (Exemples) :**
Vous devez créer des spécialisations qui intègrent les mécaniques suivantes, en utilisant le modèle fourni :

1.  **Une classe qui gère une ressource secondaire** (comme la "Vitesse de Lame" du Blademaster).
2.  **Une classe qui a un mécanisme de risque/récompense** lié aux points de vie (comme le "Berserker des Terres Gelées").
3.  **Une classe qui invoque des entités** (comme le "Porte-Étendard").
4.  **Une classe basée sur le positionnement** (comme le "Lancier des Sables").
5.  **Une classe avec une mécanique de "Combo"** ou de préparation (comme le "Prismancien").
6.  **Une classe de soutien/débuff** (comme le "Roi-Guerrier Déchu").
7.  **Une classe avec une ultime** (comme l'"Écho des Damnés").
8.  **Une classe qui se transforme visuellement** (comme le "Colosse d'Airain" ou le "Métamorphe Sauvage").

---

**Consignes de Rédaction Spécifiques :**

- **Citations :** Lorsque vous mentionnez l'exemple, utilisez la citation `[cite: 1]` pour indiquer que vous suivez le modèle.
- **Profondeur Technique :** Les scripts Lua doivent être fonctionnels et non pas des pseudo-codes. Ils doivent gérer les GUID des joueurs, les auras, les dégâts, les soins, les événements de combat, etc.
- **Créativité :** Le nom des spécialisations et leurs mécaniques doivent être créatifs, mais rester dans le thème de l'univers Warcraft (ex: "Chevalier Brisé", "Ombre-Lame").
- **Complétude :** Le fichier final doit être un document unique, cohérent, qui pourrait être directement utilisé par une équipe de développement pour implémenter les classes sur un serveur.

**Maintenant, générez `ALAMNA.md` en suivant ces instructions à la lettre, en incluant le nombre de spécialisations que vous estimez approprié pour un document de cette envergure (par exemple, 5-10).**
```

### Pourquoi ce prompt est idéal :

1.  **Hautement Spécifique :** Il décompose le document cible (`ALAMNA.md`) en sections et sous-sections très précises, ne laissant aucune place à l'interprétation.
2.  **Imite Parfaitement l'Exemple :** Il reproduit le style, la terminologie et les blocs de code de votre exemple, garantissant une consistance parfaite.
3.  **Utilise la Mémoire Sémantique :** En utilisant des expressions comme "comme l'exemple fourni" et en donnant des références explicites (`[cite:1]`), il indique au modèle d'IA de se baser sur le document source, ce qui est crucial pour la fidélité.
4.  **Encadre la Créativité :** Il ne demande pas simplement une liste de classes, mais impose des contraintes fonctionnelles (ressource, risque, invocation, etc.) qui guideront la créativité dans une direction pertinente.
5.  **Complet :** Il couvre tous les aspects du document final : structure, SQL, Lua, et documentation.
