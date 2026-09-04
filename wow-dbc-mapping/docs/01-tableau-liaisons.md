# 📌 Tableau Synthétique des Liaisons DBC

> **Dernière mise à jour** : 2026-09-04  
> **Version WoW** : Retail 11.0.2 | Classic 1.15.4 | WotLK 3.4.3

---

## 🔮 Sorts et Compétences

### Liaisons Principales de Spell.dbc

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `Spell.dbc` | `SpellVisualID` (colonnes 132-133) | `SpellVisual.dbc` | N-1 | Association visuelle (impact + aura) | Pyroblast (ID 11366) → Visual 1234 (impact) + 1235 (aura) |
| `Spell.dbc` | `SpellIconID` | `SpellIcon.dbc` | N-1 | Icône affichée dans le grimoire | Éclair (ID 403) → Icon 188 |
| `Spell.dbc` | `SpellCastTimeID` | `SpellCastTimes.dbc` | N-1 | Temps d'incantation | Boule de feu (ID 133) → 3.5 secondes |
| `Spell.dbc` | `SpellDurationID` | `SpellDuration.dbc` | N-1 | Durée des effets appliqués | Mot de pouvoir : Bouclier (ID 17) → 30 secondes |
| `Spell.dbc` | `SpellRangeID` | `SpellRange.dbc` | N-1 | Portée du sort | Tir des arcanes (ID 5143) → 40 mètres |
| `Spell.dbc` | `SpellCooldownsID` | `SpellCooldowns.dbc` | N-1 | Temps de recharge | Blizzard (ID 10) → 8 secondes |
| `Spell.dbc` | `SpellCategoryID` | `SpellCategory.dbc` | N-1 | Catégorie de cooldown partagé | Tous les sorts de givre → Catégorie 133 |
| `Spell.dbc` | `SpellDescriptionVariablesID` | `SpellDescriptionVariables.dbc` | 1-1 | Variables pour la description | "Inflige $s1 points de dégâts" |
| `Spell.dbc` | `SpellEquippedItemsID` | `SpellEquippedItems.dbc` | N-1 | Item requis équipé | Tir mortel (ID 53351) → Arme à distance |
| `Spell.dbc` | `SpellInterruptsID` | `SpellInterrupts.dbc` | N-1 | Comportement d'interruption | Contre-sort (ID 2139) → Interrompt les sorts |
| `Spell.dbc` | `SpellLevelsID` | `SpellLevels.dbc` | N-1 | Niveau requis | Boule de feu → Niveau 1, 14, 22... |
| `Spell.dbc` | `SpellMissileID` | `SpellMissile.dbc` | N-1 | Projectile du sort | Flèche de givre (ID 116) → Missile 342 |
| `Spell.dbc` | `SpellRadiusID` | `SpellRadius.dbc` | N-1 | Rayon d'effet de zone | Nova de givre (ID 122) → 10 mètres |
| `Spell.dbc` | `SpellScalingID` | `SpellScaling.dbc` | N-1 | Échelle de dégâts | Frappe du héros (ID 78) → Scaling 145 |
| `Spell.dbc` | `SpellShapeshiftID` | `SpellShapeshift.dbc` | N-1 | Forme animale requise | Morsure féroce (ID 22568) → Forme de félin |
| `Spell.dbc` | `SpellVisualKitID` | `SpellVisualKit.dbc` | N-1 | Kit visuel détaillé | Nova de givre → Kit avec particules |
| `Spell.dbc` | `SpellAuraOptionsID` | `SpellAuraOptions.dbc` | N-1 | Options d'aura | Aura de vindicte → Options spécifiques |
| `Spell.dbc` | `SpellAuraRestrictionsID` | `SpellAuraRestrictions.dbc` | N-1 | Restrictions d'aura | Anathème → Restrictions de cumul |
| `Spell.dbc` | `SpellCastingRequirementsID` | `SpellCastingRequirements.dbc` | N-1 | Conditions d'incantation | Sorts de pêche → Besoin d'une canne |
| `Spell.dbc` | `SpellPowerID` | `SpellPower.dbc` | N-1 | Puissance des effets | Éclair de givre (ID 116) → Puissance 214 |
| `Spell.dbc` | `SpellRuneCostID` | `SpellRuneCost.dbc` | N-1 | Coût en runes (DK) | Frappe de givre → 1 rune de givre |
| `Spell.dbc` | `SpellTotemID_1..2` | `TotemCategory.dbc` | N-N | Totem requis | Totem de soins → Totem d'eau |
| `Spell.dbc` | `ReagentID_1..8` | `Item.dbc` | N-N | Composants consommés | Portail : Hurlevent (ID 3561) → Pierre de portail |
| `Spell.dbc` | `ReagentCount_1..8` | *(valeur numérique)* | N-N | Quantité de composants | Portail : Hurlevent → 1 pierre |
| `Spell.dbc` | `EffectItemID_1..3` | `Item.dbc` | N-N | Items créés par le sort | Invocation : Éclair de mana (ID 5504) → Item 17008 |
| `Spell.dbc` | `EffectSpellID_1..3` | `Spell.dbc` | N-1 | Sorts déclenchés | Métamorphose (ID 5484) → Aura de métamorphose |
| `Spell.dbc` | `EffectTriggerSpellID_1..3` | `Spell.dbc` | N-1 | Sorts sur déclencheur | Sceau du croisé → Jugement du croisé |
| `Spell.dbc` | `SpellCooldownGroupID` | `SpellCooldowns.dbc` | N-1 | Groupe de cooldown | Sorts de métamorphose → Groupe 87 |
| `Spell.dbc` | `RequiredTotemCategoryID_1..2` | `TotemCategory.dbc` | N-1 | Catégorie de totem requise | Totem de soins → Totem d'eau |

### Liaisons avec les Compétences

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `SkillLine.dbc` | `SkillLineID` | `SkillLineAbility.dbc` | 1-N | Compétence et ses capacités | Cuisine (185) → 200+ recettes |
| `SkillLineAbility.dbc` | `SpellID` | `Spell.dbc` | N-1 | Capacité apprise via la compétence | Ambidextrie (205) → Sort 674 |
| `SkillLineAbility.dbc` | `SkillLineID` | `SkillLine.dbc` | N-1 | Compétence parente | Recette de cuisine → Cuisine |
| `SkillLineAbility.dbc` | `RaceMask` | `ChrRaces.dbc` | N-N | Races pouvant apprendre | Ingénierie gnome → Gnome uniquement |
| `SkillLineAbility.dbc` | `ClassMask` | `ChrClasses.dbc` | N-N | Classes pouvant apprendre | Crochetage → Voleur uniquement |
| `SkillLine.dbc` | `CategoryID` | `SkillLineCategory.dbc` | N-1 | Catégorie de compétence | Cuisine → Métiers secondaires |
| `SkillLine.dbc` | `IconID` | `SpellIcon.dbc` | N-1 | Icône de la compétence | Alchimie → Icon 346 |

### Liaisons avec les Talents

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `Talent.dbc` | `SpellID` | `Spell.dbc` | N-1 | Sort conféré par le talent | Peau de givre → Sort amélioré |
| `Talent.dbc` | `TalentTabID` | `TalentTab.dbc` | N-1 | Arbre de talents | Élémentaire → Arbre du chaman |
| `Talent.dbc` | `RequiredSpellID` | `Spell.dbc` | N-1 | Sort prérequis | Amélioration → Sort de base |
| `Talent.dbc` | `Rank_1..5` | `Spell.dbc` | 1-N | Rangs du talent | Bouclier divin → 3 rangs |
| `TalentTab.dbc` | `SpellIconID` | `SpellIcon.dbc` | N-1 | Icône de l'arbre | Arbre Sacré → Icon 235 |

---

## 🎒 Items

### Liaisons Principales de Item.dbc

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `Item.dbc` | `DisplayInfoID` | `ItemDisplayInfo.dbc` | N-1 | Apparence 3D de l'item | Ashbringer (ID 13262) → Modèle unique |
| `Item.dbc` | `SpellID_1..5` | `Spell.dbc` | N-N | Sorts conférés | Cœur de Ragnaros (ID 17782) → Fureur de Ragnaros |
| `Item.dbc` | `SpellTrigger_1..5` | *(valeur numérique)* | N-N | Type de déclenchement | Épée runique → Sur coup (trigger 1) |
| `Item.dbc` | `SpellCharges_1..5` | *(valeur numérique)* | N-N | Charges du sort | Pierre de soins → 3 charges |
| `Item.dbc` | `ItemSetID` | `ItemSet.dbc` | N-1 | Ensemble d'items | Heaume de Tranche-Mort (ID 34345) → Ensemble 817 |
| `Item.dbc` | `RandomPropertiesID` | `ItemRandomProperties.dbc` | N-1 | Propriétés aléatoires | Lame runique → "de l'Ours" |
| `Item.dbc` | `RandomSuffixID` | `ItemRandomSuffix.dbc` | N-1 | Suffixe aléatoire | Lame runique → "de l'Ours" (suffixe 164) |
| `Item.dbc` | `RequiredReputationFaction` | `Faction.dbc` | N-1 | Réputation requise | Épée du croisé → Croisade d'argent |
| `Item.dbc` | `RequiredReputationRank` | *(valeur numérique)* | N-1 | Rang de réputation | Épée du croisé → Exalté (rang 7) |
| `Item.dbc` | `RequiredSkillID` | `SkillLine.dbc` | N-1 | Compétence requise | Minerai de thorium → Minage (186) |
| `Item.dbc` | `RequiredSkillRank` | *(valeur numérique)* | N-1 | Niveau de compétence | Minerai de thorium → Minage 245 |
| `Item.dbc` | `RequiredLevel` | *(valeur numérique)* | N-1 | Niveau requis | Ashbringer → Niveau 60 |
| `Item.dbc` | `ContainerSlots` | *(valeur numérique)* | N-1 | Nombre d'emplacements | Sac de voyageur → 6 emplacements |
| `Item.dbc` | `LockID` | `Lock.dbc` | N-1 | Mécanisme de verrouillage | Coffre verrouillé → Lock 48 |
| `Item.dbc` | `GroupID` | `ItemGroupSounds.dbc` | N-1 | Sons de l'item | Épée longue → Son de métal |
| `Item.dbc` | `MaterialID` | `Material.dbc` | N-1 | Matériau de l'item | Épée → Métal (matériau 1) |
| `Item.dbc` | `TotemCategoryID` | `TotemCategory.dbc` | N-1 | Catégorie de totem | Totem de terre → Catégorie 47 |
| `Item.dbc` | `PageTextID` | `PageTextMaterial.dbc` | N-1 | Texte de la page | Journal de quête → Texte unique |
| `Item.dbc` | `FactionID` | `Faction.dbc` | N-1 | Faction autorisée | Monture tauren → Tauren uniquement |
| `Item.dbc` | `Flags` | *(bitfield)* | N-N | Drapeaux d'objets | Lié quand équipé → Bit 1 |
| `Item.dbc` | `BuyPrice` | *(valeur numérique)* | N-1 | Prix d'achat | Petit sac → 4 pièces d'argent |
| `Item.dbc` | `ItemLevel` | *(valeur numérique)* | N-1 | Niveau d'objet | Ashbringer → Ilvl 74 |

### Liaisons avec ItemDisplayInfo.dbc

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `ItemDisplayInfo.dbc` | `ModelID_1..2` | `ModelFileData.dbc` | N-1 | Modèle 3D de l'item | Épée → Modèle .m2 |
| `ItemDisplayInfo.dbc` | `TextureID_1..10` | `TextureFileData.dbc` | N-1 | Textures de l'item | Armure → Texture .blp |
| `ItemDisplayInfo.dbc` | `IconID` | `ItemDisplayInfo.dbc` | N-1 | Icône d'inventaire | Potion → Icon 348 |
| `ItemDisplayInfo.dbc` | `ParticleColorID` | `ParticleColor.dbc` | N-1 | Couleur des particules | Épée enchantée → Lueur rouge |
| `ItemDisplayInfo.dbc` | `SoundID` | `ItemGroupSounds.dbc` | N-1 | Sons de l'item | Bâton → Son de bois |

### Liaisons avec ItemSet.dbc

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `ItemSet.dbc` | `ItemID_1..8` | `Item.dbc` | 1-N | Items de l'ensemble | Tranche-Mort → 8 pièces |
| `ItemSet.dbc` | `SetSpellID_1..8` | `Spell.dbc` | N-N | Bonus de set | Tranche-Mort → Bonus 4 pièces |
| `ItemSet.dbc` | `SkillLineID` | `SkillLine.dbc` | N-1 | Compétence associée | Ensemble de forgeron → Forge |

---

## 🐉 Créatures

### Liaisons Principales de CreatureDisplayInfo.dbc

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `CreatureDisplayInfo.dbc` | `ModelID` | `CreatureModelData.dbc` | N-1 | Modèle 3D de la créature | Ragnaros → Géant de feu |
| `CreatureDisplayInfo.dbc` | `TextureID_1..3` | `TextureFileData.dbc` | N-1 | Textures du modèle | Onyxia → Cuir noir |
| `CreatureDisplayInfo.dbc` | `SoundID` | `CreatureSoundData.dbc` | 1-1 | Sons de la créature | Murloc → Cri spécifique |
| `CreatureDisplayInfo.dbc` | `ExtraDisplayInfoID` | `CreatureDisplayInfoExtra.dbc` | N-1 | Apparence supplémentaire | Dragon → Ailes et cornes |
| `CreatureDisplayInfo.dbc` | `CreatureModelScale` | *(valeur numérique)* | N-1 | Échelle du modèle | Ogre → 1.25x |
| `CreatureDisplayInfo.dbc` | `NPCSoundID` | `NPCSounds.dbc` | N-1 | Sons du PNJ | Vendeur → Sons de vendeur |
| `CreatureDisplayInfo.dbc` | `PortraitTextureID` | `TextureFileData.dbc` | N-1 | Texture de portrait | Roi-liche → Portrait unique |

### Liaisons avec CreatureModelData.dbc

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `CreatureModelData.dbc` | `ModelPathID` | `ModelFileData.dbc` | N-1 | Chemin du modèle .m2 | Loup → Models/wolf.m2 |
| `CreatureModelData.dbc` | `SizeClass` | *(valeur numérique)* | N-1 | Classe de taille | Ogre → Classe 3 (grand) |
| `CreatureModelData.dbc` | `CollisionWidth` | *(valeur numérique)* | N-1 | Largeur de collision | Dragon → 5 mètres |
| `CreatureModelData.dbc` | `MountHeight` | *(valeur numérique)* | N-1 | Hauteur de monture | Cheval → 1.8 mètres |

### Liaisons avec CreatureSoundData.dbc

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `CreatureSoundData.dbc` | `SoundID_1..4` | `SoundEntries.dbc` | N-N | Sons d'action | Murloc → Cri, mort, attaque |
| `CreatureSoundData.dbc` | `NPCSoundID` | `NPCSounds.dbc` | N-1 | Sons du PNJ | Garde → Sons de garde |

---

## 🗺️ Zones et Cartes

### Liaisons Principales de Map.dbc

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `Map.dbc` | `AreaTableID` | `AreaTable.dbc` | 1-N | Zones d'une carte | Kalimdor (1) → Durotar (14) |
| `Map.dbc` | `LoadingScreenID` | `LoadingScreens.dbc` | N-1 | Écran de chargement | Kalimdor → Écran spécifique |
| `Map.dbc` | `MapType` | *(valeur numérique)* | N-1 | Type de carte | Azeroth → Continent (type 0) |
| `Map.dbc` | `Directory` | *(valeur texte)* | N-1 | Dossier des fichiers | Kalimdor → "Kalimdor" |
| `Map.dbc` | `MapName` | *(valeur texte)* | N-1 | Nom de la carte | 1 → "Kalimdor" |
| `Map.dbc` | `MinimapIconScale` | *(valeur numérique)* | N-1 | Échelle de la minimap | Kalimdor → 0.5 |

### Liaisons avec AreaTable.dbc

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `AreaTable.dbc` | `ZoneMusicID` | `ZoneMusic.dbc` | N-1 | Musique de la zone | Durotar → Musique unique |
| `AreaTable.dbc` | `LoadingScreenID` | `LoadingScreens.dbc` | N-1 | Écran de chargement | Mulgore → Écran unique |
| `AreaTable.dbc` | `ParentAreaID` | `AreaTable.dbc` | N-1 | Zone parente | Durotar → Kalimdor |
| `AreaTable.dbc` | `MapID` | `Map.dbc` | N-1 | Carte parente | Durotar → Kalimdor (1) |
| `AreaTable.dbc` | `FactionGroupID` | `FactionGroup.dbc` | N-1 | Groupe de faction | Durotar → Horde |
| `AreaTable.dbc` | `ZoneIntroMusicID` | `ZoneMusic.dbc` | N-1 | Musique d'intro | Mulgore → Musique d'entrée |
| `AreaTable.dbc` | `AreaType` | *(valeur numérique)* | N-1 | Type de zone | Durotar → Zone extérieure (type 1) |

### Liaisons avec ZoneMusic.dbc

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `ZoneMusic.dbc` | `SoundID_1..2` | `SoundEntries.dbc` | N-1 | Fichiers audio | Durotar → Musique d'ambiance |
| `ZoneMusic.dbc` | `Volume` | *(valeur numérique)* | N-1 | Volume de la musique | Durotar → 0.8 |
| `ZoneMusic.dbc` | `MinDelay` | *(valeur numérique)* | N-1 | Délai minimum | Durotar → 10 secondes |
| `ZoneMusic.dbc` | `MaxDelay` | *(valeur numérique)* | N-1 | Délai maximum | Durotar → 30 secondes |

---

## 🎭 Modèles et Textures

### Chaîne de Dépendances des Modèles

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `ModelFileData.dbc` | `FileDataID` | *(valeur numérique)* | N-1 | ID du fichier modèle | Wolf.m2 → FileID 12345 |
| `ModelFileData.dbc` | `Flags` | *(bitfield)* | N-1 | Drapeaux du modèle | Animated → Bit 3 |
| `TextureFileData.dbc` | `FileDataID` | *(valeur numérique)* | N-1 | ID du fichier texture | Wolf.blp → FileID 67890 |
| `TextureFileData.dbc` | `TexturePath` | *(valeur texte)* | N-1 | Chemin de la texture | "Creature/Wolf/Wolf.blp" |
| `TextureFileData.dbc` | `Flags` | *(bitfield)* | N-1 | Drapeaux de texture | Mipmap → Bit 0 |

### Liaisons avec les Effets Visuels

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `SpellVisualKit.dbc` | `FileDataID` | `TextureFileData.dbc` | N-1 | Texture des particules | Nova de givre → Texture de glace |
| `SpellVisualKit.dbc` | `ModelID_1..3` | `ModelFileData.dbc` | N-1 | Modèles des effets | Boule de feu → Modèle de feu |
| `SpellVisualKit.dbc` | `SoundID` | `SoundEntries.dbc` | N-1 | Son de l'effet | Éclair → Son de foudre |
| `SpellVisual.dbc` | `SpellVisualKitID` | `SpellVisualKit.dbc` | N-1 | Kit visuel principal | Boule de feu → Kit de projectile |
| `SpellVisual.dbc` | `SpellVisualKitID_2` | `SpellVisualKit.dbc` | N-1 | Kit visuel d'impact | Boule de feu → Kit d'explosion |

---

## 🎵 Sons et Audio

### Liaisons avec les Sons

| Source | Champ(s) | Cible | Cardinalité | Description | Exemple Concret |
|--------|----------|-------|-------------|-------------|-----------------|
| `SoundEntries.dbc` | `FileDataID_1..10` | `SoundFiles.dbc` | 1-N | Fichiers audio | Cri de murloc → 3 variations |
| `SoundEntries.dbc` | `SoundType` | *(valeur numérique)* | N-1 | Type de son | Ambiance → Type 2 |
| `SoundFiles.dbc` | `FileDataID` | *(valeur numérique)* | N-1 | ID du fichier audio | Murloc_cry.ogg → FileID |
| `SoundFiles.dbc` | `Path` | *(valeur texte)* | N-1 | Chemin du fichier | "Sound/Creature/Murloc/Cry.ogg" |

---

## 📊 Statistiques Globales des Liaisons

| Domaine | DBC Source | DBC Cible | Nombre de Liaisons | Type Principal |
|---------|-----------|-----------|-------------------|----------------|
| 🔮 Sorts | Spell.dbc | 25+ DBC différents | 50+ | N-1 (majoritaire) |
| 🎒 Items | Item.dbc | 15+ DBC différents | 30+ | N-1 et N-N |
| 🐉 Créatures | CreatureDisplayInfo.dbc | 8+ DBC différents | 15+ | N-1 |
| 🗺️ Zones | Map.dbc / AreaTable.dbc | 6+ DBC différents | 15+ | 1-N et N-1 |
| 🎭 Modèles | Divers | ModelFileData.dbc | 20+ | N-1 |
| 🎵 Sons | Divers | SoundEntries.dbc | 15+ | N-N |

### Répartition des Cardinalités

| Cardinalité | Nombre | Pourcentage | Exemple |
|-------------|--------|------------|---------|
| **1-1** | 5 | 5% | SpellDescriptionVariables |
| **N-1** | 65 | 65% | Spell → SpellVisual |
| **1-N** | 15 | 15% | Map → AreaTable |
| **N-N** | 15 | 15% | Spell ↔ Item |

### DBC les Plus Référencés (Cibles)

| DBC Cible | Nombre de Références | Domaines |
|-----------|---------------------|----------|
| `TextureFileData.dbc` | 12 | Sorts, Items, Créatures |
| `Spell.dbc` | 10 | Items, Talents, Compétences |
| `SoundEntries.dbc` | 8 | Sorts, Créatures, Zones |
| `ModelFileData.dbc` | 6 | Items, Créatures, Sorts |
| `SpellVisualKit.dbc` | 5 | Sorts uniquement |

### DBC les Plus Référençants (Sources)

| DBC Source | Nombre de Sorties | Domaines |
|-----------|------------------|----------|
| `Spell.dbc` | 50+ | Sorts |
| `Item.dbc` | 30+ | Items |
| `CreatureDisplayInfo.dbc` | 15+ | Créatures |
| `AreaTable.dbc` | 10+ | Zones |
| `SpellVisualKit.dbc` | 8+ | Effets visuels |

---

## 🔗 Matrice des Liaisons Croisées

| Source \ Cible | Spell.dbc | Item.dbc | TextureFileData.dbc | SoundEntries.dbc | ModelFileData.dbc |
|----------------|-----------|----------|---------------------|------------------|-------------------|
| **Spell.dbc** | ✅ (auto-réf) | ✅ (N-N) | ❌ (indirect) | ❌ (indirect) | ❌ (indirect) |
| **Item.dbc** | ✅ (N-N) | ✅ (via ItemSet) | ❌ (indirect) | ✅ (direct) | ❌ (indirect) |
| **CreatureDisplayInfo.dbc** | ❌ (indirect) | ❌ (indirect) | ✅ (direct) | ✅ (direct) | ✅ (direct) |
| **AreaTable.dbc** | ❌ (indirect) | ❌ (indirect) | ❌ (indirect) | ✅ (direct) | ❌ (indirect) |
| **SpellVisualKit.dbc** | ❌ (indirect) | ❌ (indirect) | ✅ (direct) | ✅ (direct) | ✅ (direct) |

---

## 📝 Notes et Observations

### 🔍 Points Importants

1. **Spell.dbc est le hub central** avec plus de 50 liaisons sortantes
2. **Item.dbc est le second hub** avec 30+ liaisons
3. **TextureFileData.dbc est la feuille terminale** de nombreuses chaînes
4. **Les liaisons N-N sont rares** mais importantes (Spell ↔ Item)
5. **Les auto-références existent** (Spell → Spell via EffectSpellID, AreaTable → AreaTable via ParentAreaID)

### ⚠️ Champs Ambigus

- `Spell.dbc::SpellVisualID` : Contient en réalité 2 IDs (impact + aura) dans les versions modernes
- `Item.dbc::SpellID_1..5` : Peut référencer des sorts inexistants (dépréciés)
- `CreatureDisplayInfo.dbc::TextureID_1..3` : Peut contenir des IDs invalides (0 = pas de texture)

### 🔄 Changements par Version

| Version | Changement |
|---------|-----------|
| Classic | Structure simple, moins de DBC |
| TBC | Ajout de SpellDescriptionVariables |
| WotLK | Ajout de SpellScaling, SpellRuneCost |
| Retail | Séparation en plus de DBC spécialisés |

---

*Ce tableau est maintenu à jour régulièrement. Dernière révision : 4 septembre 2026*
