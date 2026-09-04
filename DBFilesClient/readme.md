# DBFilesClient - World of Warcraft 3.3.5a Database Files

<div align="center">

![Version](https://img.shields.io/badge/version-3.3.5a-blue.svg)
![Build](https://img.shields.io/badge/build-12340-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![DBC Count](https://img.shields.io/badge/dbc%20files-250%2B-red.svg)

**Collection complète des fichiers DBC (Database Client) pour World of Warcraft Wrath of the Lich King**

[Structure](#-structure) • [Installation](#-installation) • [Documentation](#-documentation) • [Contributions](#-contributions) • [Licence](#-licence)

</div>

---

## 📋 Table des matières

- [Aperçu](#-aperçu)
- [Structure](#-structure)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Documentation](#-documentation)
- [Dépendances](#-dépendances)
- [Outils](#-outils)
- [Contributions](#-contributions)
- [Crédits](#-crédits)
- [Licence](#-licence)

---

## 🔍 Aperçu

Ce repository contient l'ensemble des fichiers **DBC (Database Client)** extraits de World of Warcraft version **3.3.5a** (build 12340), également connu sous le nom de **Wrath of the Lich King**.

Les fichiers DBC sont des bases de données client utilisées par le jeu pour stocker des informations sur les sorts, les objets, les créatures, les zones, et bien plus encore. Ils sont essentiels pour :

- 🎮 **Développement de serveurs privés** (TrinityCore, AzerothCore, MaNGOS)
- 🛠️ **Création d'outils et d'éditeurs**
- 📊 **Analyse de données du jeu**
- 🔧 **Modding et personnalisation**

### Caractéristiques

- ✅ **250+ fichiers DBC** couvrant tous les aspects du jeu
- ✅ **Structure complète** avec toutes les dépendances documentées
- ✅ **Format binaire original** compatible avec les outils standard
- ✅ **Documentation exhaustive** pour chaque fichier
- ✅ **Organisation par catégories** logiques

---

## 📁 Structure

```
DBFilesClient/
├── 📂 Core/
│   ├── Achievement.dbc
│   ├── Achievement_Category.dbc
│   ├── Achievement_Criteria.dbc
│   ├── Spell.dbc
│   ├── Item.dbc
│   └── Map.dbc
│
├── 📂 Skills/
│   ├── SkillLine.dbc
│   ├── SkillLineAbility.dbc
│   ├── SkillLineCategory.dbc
│   ├── SkillTiers.dbc
│   └── SkillRaceClassInfo.dbc
│
├── 📂 Items/
│   ├── ItemDisplayInfo.dbc
│   ├── ItemExtendedCost.dbc
│   ├── ItemRandomProperties.dbc
│   ├── ItemSet.dbc
│   └── ItemClass.dbc
│
├── 📂 Creatures/
│   ├── CreatureFamily.dbc
│   ├── CreatureType.dbc
│   ├── CreatureDisplayInfo.dbc
│   ├── CreatureModelData.dbc
│   └── CreatureSpellData.dbc
│
├── 📂 World/
│   ├── AreaTable.dbc
│   ├── AreaTrigger.dbc
│   ├── MapDifficulty.dbc
│   ├── Light.dbc
│   └── WorldMapArea.dbc
│
├── 📂 Quests/
│   ├── QuestInfo.dbc
│   ├── QuestSort.dbc
│   ├── QuestXP.dbc
│   └── QuestFactionReward.dbc
│
├── 📂 Graphics/
│   ├── AnimationData.dbc
│   ├── AnimKit.dbc
│   ├── ParticleColor.dbc
│   └── SoundEntries.dbc
│
├── 📂 Interface/
│   ├── CharSections.dbc
│   ├── CharTitles.dbc
│   └── CharacterFacialHairStyles.dbc
│
├── 📂 Combat/
│   ├── CombatRating.dbc
│   ├── RandPropPoints.dbc
│   └── gtCombatRatings.dbc
│
├── 📂 Classes/
│   ├── ChrClasses.dbc
│   ├── ChrRaces.dbc
│   ├── CharBaseInfo.dbc
│   └── CharStartOutfit.dbc
│
├── 📂 Factions/
│   ├── Faction.dbc
│   ├── FactionGroup.dbc
│   └── FactionTemplate.dbc
│
├── 📂 Dungeons/
│   ├── DungeonEncounter.dbc
│   ├── DungeonMap.dbc
│   └── LFGDungeons.dbc
│
├── 📂 Spells/
│   ├── SpellAuraOptions.dbc
│   ├── SpellCooldowns.dbc
│   ├── SpellReagents.dbc
│   └── SpellTargetRestrictions.dbc
│
├── 📂 Cinematics/
│   ├── CinematicCamera.dbc
│   ├── CinematicSequences.dbc
│   └── Movie.dbc
│
├── 📂 Environment/
│   ├── Weather.dbc
│   ├── ZoneMusic.dbc
│   └── ZoneLight.dbc
│
├── 📂 Events/
│   ├── CalendarHolidays.dbc
│   ├── GameEvents.dbc
│   └── WorldStateUI.dbc
│
├── 📂 Transport/
│   ├── TransportAnimation.dbc
│   ├── Vehicle.dbc
│   └── VehicleSeat.dbc
│
├── 📂 Localization/
│   ├── Languages.dbc
│   └── LanguagesWords.dbc
│
└── 📂 Misc/
    ├── TaxiNodes.dbc
    ├── TaxiPath.dbc
    └── WorldSafeLocs.dbc
```

---

## 💾 Installation

### Prérequis

- World of Warcraft 3.3.5a installé (build 12340)
- Espace disque : ~100 MB
- Outils d'extraction (optionnel)

### Méthode 1 : Téléchargement direct

```bash
# Cloner le repository
git clone https://github.com/votre-username/DBFilesClient.git

# Accéder au dossier
cd DBFilesClient
```

### Méthode 2 : Extraction depuis le client

```bash
# Utiliser un extracteur DBC (ex: TrinityCore Tools)
./mapextractor -i /chemin/vers/wow -o /chemin/vers/output

# Les fichiers DBC seront dans le dossier "dbc"
```

---

## 🚀 Utilisation

### Pour les développeurs de serveurs

```cpp
// Exemple : Lecture d'un fichier DBC avec TrinityCore
#include "DBCFileLoader.h"

DBCFileLoader loader;
loader.Load("Spell.dbc");

for (uint32 i = 0; i < loader.GetNumRows(); ++i)
{
    char* row = loader.AutoProduceData(i);
    uint32 spellId = *(uint32*)row;
    // Traitement des données...
}
```

### Pour l'analyse de données

```python
# Exemple : Analyse avec Python (via python-dbc)
from dbc import DBCFile

spells = DBCFile("Spell.dbc")
for spell in spells:
    print(f"Spell ID: {spell.id}, Name: {spell.name}")
```

### Outils compatibles

| Outil | Description | Lien |
|-------|-------------|------|
| **DBC Editor** | Éditeur graphique de fichiers DBC | [Télécharger](https://github.com/wowdev/DBCEditor) |
| **WDBX Editor** | Éditeur moderne avec support 3.3.5 | [Télécharger](https://github.com/WowDevTools/WDBXEditor) |
| **DBC Viewer** | Visualiseur rapide en ligne de commande | [Télécharger](https://github.com/TrinityCore/dbcviewer) |
| **SpellWork** | Analyseur spécialisé pour Spell.dbc | [Télécharger](https://github.com/TrinityCore/SpellWork) |

---

## 📖 Documentation

### Structure d'un fichier DBC

Chaque fichier DBC contient :

```
┌─────────────────────────────────────┐
│            Header (20 bytes)        │
├─────────────────────────────────────┤
│  Magic Number ('WDBC') - 4 bytes    │
│  Record Count - 4 bytes             │
│  Field Count - 4 bytes              │
│  Record Size - 4 bytes              │
│  String Block Size - 4 bytes        │
├─────────────────────────────────────┤
│         Data Records                │
├─────────────────────────────────────┤
│         String Block                │
└─────────────────────────────────────┘
```

### Catégories principales

| Catégorie | Nombre de fichiers | Description |
|-----------|-------------------|-------------|
| **Core** | 15+ | Fichiers fondamentaux (Spell, Item, Map) |
| **Skills** | 10+ | Compétences et métiers |
| **Items** | 20+ | Équipement et objets |
| **Creatures** | 15+ | PNJ et créatures |
| **World** | 20+ | Zones, cartes et environnement |
| **Quests** | 10+ | Quêtes et récompenses |
| **Graphics** | 20+ | Effets visuels et sons |
| **Interface** | 15+ | Éléments d'interface |
| **Combat** | 10+ | Statistiques de combat |
| **Classes** | 15+ | Classes et races |
| **Factions** | 5+ | Système de réputation |
| **Dungeons** | 10+ | Donjons et raids |
| **Spells** | 25+ | Sorts et auras |
| **Autres** | 50+ | Divers et utilitaires |

### Dépendances principales

```
Spell.dbc
├── SpellIcon.dbc
├── SpellVisual.dbc
├── SpellDuration.dbc
├── SpellRange.dbc
└── SpellCooldowns.dbc

Item.dbc
├── ItemDisplayInfo.dbc
├── ItemClass.dbc
└── ItemSet.dbc

CreatureDisplayInfo.dbc
├── CreatureModelData.dbc
└── CreatureSoundData.dbc
```

---

## 🔗 Dépendances

### Dépendances entre fichiers DBC

Les fichiers DBC ont de nombreuses interdépendances. Les plus importantes sont :

| Fichier principal | Dépendances directes |
|------------------|---------------------|
| `Spell.dbc` | SpellIcon, SpellVisual, SpellDuration, SpellRange |
| `Item.dbc` | ItemDisplayInfo, ItemClass, ItemSet |
| `Creature.dbc` | CreatureDisplayInfo, CreatureType |
| `Map.dbc` | MapDifficulty, AreaTable |
| `QuestInfo.dbc` | QuestSort, QuestXP, Faction |

### Dépendances logicielles

- **Client WoW 3.3.5a** (build 12340)
- **Système d'exploitation** : Windows, Linux, macOS
- **Outils compatibles** : voir section [Outils](#-outils)

---

## 🛠️ Outils

### Extraction

| Outil | Plateforme | Description |
|-------|------------|-------------|
| **TrinityCore Extractor** | Multi-plateforme | Extracteur officiel TrinityCore |
| **AzerothCore Extractor** | Multi-plateforme | Extracteur AzerothCore |
| **Casc Storage** | Windows | Utilitaire d'extraction moderne |

### Édition

| Outil | Plateforme | Description |
|-------|------------|-------------|
| **WDBX Editor** | Windows | Éditeur complet avec interface graphique |
| **DBC Editor** | Windows | Éditeur simple et rapide |
| **DBCUtil** | CLI | Outil en ligne de commande |

### Analyse

| Outil | Plateforme | Description |
|-------|------------|-------------|
| **SpellWork** | Windows | Analyse des sorts |
| **DBC Viewer** | CLI | Visualisation rapide |
| **WoWDevTools** | Multi-plateforme | Suite d'outils de développement |

---

## 🤝 Contributions

Les contributions sont les bienvenues ! Voici comment vous pouvez aider :

### Comment contribuer

1. **Fork** le repository
2. **Créer** une branche (`git checkout -b feature/AmazingFeature`)
3. **Commit** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrir** une Pull Request

### Types de contributions

- 🐛 **Correction de bugs** : Fichiers DBC corrompus ou incorrects
- 📝 **Documentation** : Amélioration de la documentation
- 🗂️ **Organisation** : Meilleure structure des fichiers
- 🛠️ **Outils** : Nouveaux outils pour manipuler les DBC
- 📊 **Analyse** : Nouvelles analyses ou recherches

### Règles de contribution

- ✅ Vérifier l'intégrité des fichiers avant de commit
- ✅ Documenter tout changement
- ✅ Suivre la structure existante
- ✅ Tester avec les outils compatibles
- ❌ Ne pas inclure de fichiers protégés par copyright

---

## 👥 Crédits

### Contributeurs principaux

- **Blizzard Entertainment** - Créateurs de World of Warcraft
- **TrinityCore Team** - Documentation et outils
- **AzerothCore Team** - Documentation et outils
- **Communauté WoW Modding** - Recherche et documentation

### Remerciements spéciaux

- Merci à la communauté **WowDev** pour la documentation
- Merci aux développeurs de **WDBX Editor**
- Merci aux contributeurs de **TrinityCore** et **AzerothCore**

---

## 📄 Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
MIT License

Copyright (c) 2024 DBFilesClient Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## ⚠️ Avertissement

Ce repository est fourni à des fins éducatives et de recherche uniquement. Les fichiers DBC sont la propriété de Blizzard Entertainment. L'utilisation de ces fichiers doit respecter les conditions d'utilisation de Blizzard.

**World of Warcraft** et **Wrath of the Lich King** sont des marques déposées de Blizzard Entertainment.

---

## 📞 Contact

- **Issues** : [GitHub Issues](https://github.com/votre-username/DBFilesClient/issues)
- **Discussions** : [GitHub Discussions](https://github.com/votre-username/DBFilesClient/discussions)
- **Wiki** : [GitHub Wiki](https://github.com/votre-username/DBFilesClient/wiki)

---

## 🔄 Mises à jour

### Version 1.0.0 (2024)

- ✅ Publication initiale
- ✅ 250+ fichiers DBC inclus
- ✅ Documentation complète
- ✅ Structure organisée par catégories

### Prochaines versions

- 📋 Ajout d'outils d'analyse
- 📋 Support pour d'autres versions de WoW
- 📋 Documentation des champs détaillée
- 📋 Scripts d'extraction automatisés

---

<div align="center">

**[⬆ Retour en haut](#dbfilesclient---world-of-warcraft-335a-database-files)**

**Made with ❤️ by the WoW Modding Community**

</div>
```

Ce README.md est :
- ✅ **Complet** : Couvre tous les aspects importants
- ✅ **Professionnel** : Structure claire et organisée
- ✅ **Informatif** : Documentation détaillée
- ✅ **Visuellement attrayant** : Utilisation d'emojis et de badges
- ✅ **Pratique** : Instructions d'installation et d'utilisation
- ✅ **Conforme** : Respecte les standards GitHub

Vous pouvez personnaliser les liens GitHub, le nom d'utilisateur, et ajuster le contenu selon vos besoins spécifiques.
