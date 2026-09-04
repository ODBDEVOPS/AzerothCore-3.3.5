Voici une liste exhaustive et structurée des DBC (Database Client) pour World of Warcraft 3.3.5a (Wrath of the Lich King), organisée par catégories avec leurs dépendances principales.

---

## **LISTE EXHAUSTIVE DES DBC WOW 3.3.5a**

### **1. DBC PRINCIPAUX (CORE)**

#### **Achievement.dbc**
```
├── Achievement_Category.dbc
├── Achievement_Criteria.dbc
├── Spell.dbc
├── Item.dbc
├── Map.dbc
├── Creature.dbc (référence via CreatureEntry)
├── GameObject.dbc (référence via GameObjectEntry)
├── Faction.dbc
└── Icon (via Achievement_Criteria)
```
#### **Spell.dbc (234 champs - Le plus important)**
```
├── SpellIcon.dbc
├── SpellVisual.dbc
├── SpellVisualKit.dbc
├── SpellCastTimes.dbc
├── SpellDuration.dbc
├── SpellRange.dbc
├── SpellRadius.dbc
├── SpellItemEnchantment.dbc
├── SpellItemEnchantmentCondition.dbc
├── SpellShapeshiftForm.dbc
├── SpellDescriptionVariables.dbc
├── SpellDifficulty.dbc
├── SpellAuraRestrictions.dbc
├── SpellCastingRequirements.dbc
├── SpellCategories.dbc
├── SpellCategory.dbc
├── SpellClassOptions.dbc
├── SpellCooldowns.dbc
├── SpellEquippedItems.dbc
├── SpellInterrupts.dbc
├── SpellLevels.dbc
├── SpellPower.dbc
├── SpellReagents.dbc
├── SpellRuneCost.dbc
├── SpellScaling.dbc
├── SpellShapeshift.dbc
├── SpellTargetRestrictions.dbc
├── SpellTotems.dbc
├── SpellMissile.dbc
├── SkillLineAbility.dbc
├── Item.dbc (pour SpellReagents)
├── Faction.dbc (pour SpellTargetRestrictions)
└── AreaTable.dbc (pour SpellTargetRestrictions)
```

### **2. DBC DES COMPÉTENCES ET MÉTIERS**

```
SkillLine.dbc
├── SkillLineAbility.dbc
│   ├── Spell.dbc
│   ├── SkillLine.dbc
│   ├── ChrRaces.dbc (RaceMask)
│   ├── ChrClasses.dbc (ClassMask)
│   ├── Item.dbc (ItemSubClassMask)
│   └── SkillTiers.dbc (via SkillLine)
├── SkillLineCategory.dbc
├── SkillTiers.dbc
├── SkillCostsData.dbc
├── SkillRaceClassInfo.dbc
│   ├── SkillLine.dbc
│   ├── ChrRaces.dbc
│   └── ChrClasses.dbc
└── SkillLineAbilitySortedSpell.dbc
    └── Spell.dbc
```

### **3. DBC DES ITEMS ET ÉQUIPEMENT**

```
Item.dbc
├── ItemDisplayInfo.dbc
│   ├── ItemVisuals.dbc
│   ├── ItemVisualEffects.dbc
│   ├── TextureFileData.dbc
│   └── ItemDisplayInfo.dbc (pour les modèles)
├── ItemExtendedCost.dbc
│   ├── Item.dbc (ItemID1-5)
│   └── CurrencyTypes.dbc (via Item)
├── ItemRandomProperties.dbc
│   └── SpellItemEnchantment.dbc
├── ItemRandomSuffix.dbc
├── ItemSet.dbc
│   ├── Item.dbc (ItemID1-17)
│   └── Spell.dbc (SetSpellID1-8)
├── ItemGroupSounds.dbc
│   └── SoundEntries.dbc
├── ItemBagFamily.dbc
├── ItemCondExtCosts.dbc
│   ├── ItemExtendedCost.dbc
│   └── Item.dbc
├── ItemLimitCategory.dbc
├── ItemPurchaseGroup.dbc
│   └── Item.dbc
├── ItemReforge.dbc
├── ItemSearchName.dbc
├── ItemSubClass.dbc
│   ├── ItemClass.dbc
│   └── ItemSubClassMask.dbc
├── ItemSubClassMask.dbc
└── ItemClass.dbc

ItemDisplayInfo.dbc
├── ItemVisuals.dbc
├── ItemVisualEffects.dbc
├── TextureFileData.dbc
├── ItemDisplayInfo.dbc (ressources de modèle)
└── SoundEntries.dbc (sons d'équipement)
```

### **4. DBC DES CRÉATURES ET PNJ**

```
CreatureFamily.dbc
├── CreatureType.dbc
├── CreatureDisplayInfo.dbc
│   ├── CreatureDisplayInfoExtra.dbc
│   ├── CreatureModelData.dbc
│   └── TextureFileData.dbc
├── CreatureSpellData.dbc
│   └── Spell.dbc
└── CreatureSoundData.dbc
    └── SoundEntries.dbc

CreatureDisplayInfo.dbc
├── CreatureDisplayInfoExtra.dbc
├── CreatureModelData.dbc
├── CreatureSoundData.dbc
├── TextureFileData.dbc
└── CreatureDisplayInfo.dbc (variations)

CreatureType.dbc
└── Aucune dépendance (table de référence)

CreatureModelData.dbc
└── TextureFileData.dbc

CreatureDisplayInfoExtra.dbc
├── CreatureDisplayInfo.dbc
├── TextureFileData.dbc
└── ItemDisplayInfo.dbc (équipement)
```
### **5. DBC DES ZONES ET CARTES**

```
Map.dbc
├── MapDifficulty.dbc
│   ├── Map.dbc
│   └── MapDifficulty.dbc (difficultés liées)
├── AreaTable.dbc
│   ├── AreaGroup.dbc
│   │   └── AreaTable.dbc
│   ├── AreaPOI.dbc
│   │   └── AreaTable.dbc
│   ├── AreaTrigger.dbc
│   │   └── Map.dbc
│   ├── ZoneIntroMusicTable.dbc
│   │   └── SoundEntries.dbc
│   └── AreaTable.dbc (Zone parent)
├── Light.dbc
│   ├── LightParams.dbc
│   └── LightSkybox.dbc
├── LightParams.dbc
├── LightSkybox.dbc
├── LiquidType.dbc
│   └── Spell.dbc (SpellID)
├── LoadingScreens.dbc
└── WorldMapArea.dbc
    ├── Map.dbc
    └── AreaTable.dbc

MapDifficulty.dbc
├── Map.dbc
├── MapDifficulty.dbc (référence croisée)
└── LoadingScreens.dbc (écran de chargement)
```

### **6. DBC DES QUÊTES**

```
QuestInfo.dbc
├── QuestSort.dbc
├── QuestXP.dbc
├── QuestFactionReward.dbc
│   └── Faction.dbc
├── QuestPOIBlob.dbc
│   └── Map.dbc
└── QuestPOIPoint.dbc
    └── QuestPOIBlob.dbc

QuestSort.dbc
└── Aucune dépendance

QuestXP.dbc
└── Aucune dépendance (table de valeurs)
```

### **7. DBC DES GRAPHIQUES ET EFFETS**

```
AnimationData.dbc
├── AnimKit.dbc
│   ├── AnimKitBoneSet.dbc
│   └── AnimKitSegment.dbc
├── AnimReplacement.dbc
├── AnimSet.dbc
└── CameraShakes.dbc

ParticleColor.dbc
├── ParticleShader.dbc
└── ParticleTexture.dbc

SoundEntries.dbc
├── SoundEntriesAdvanced.dbc
├── SoundFilter.dbc
├── SoundProviderPreferences.dbc
├── SoundSamplePreferences.dbc
├── SoundWaterType.dbc
└── ZoneMusic.dbc
    └── SoundEntries.dbc

AnimKit.dbc
├── AnimKitBoneSet.dbc
└── AnimKitSegment.dbc

AnimKitBoneSet.dbc
└── Aucune dépendance

AnimKitSegment.dbc
└── AnimKit.dbc

CameraShakes.dbc
└── Aucune dépendance

FootstepTerrainLookup.dbc
└── Aucune dépendance

Footprints.dbc
├── TextureFileData.dbc
└── Spell.dbc

GroundEffectDoodad.dbc
├── Spell.dbc
└── TextureFileData.dbc

GroundEffectTexture.dbc
├── GroundEffectDoodad.dbc
└── TextureFileData.dbc
```

### **8. DBC DES INTERFACES**

```
Interface\AddOns.dbc (non standard, généralement en Lua/XML)
├── Interface\FrameXML.dbc (pas un vrai DBC, fichiers XML)
├── Interface\GlueXML.dbc (pas un vrai DBC, fichiers XML)
└── Interface\UIScale.dbc (pas un vrai DBC)

CharSections.dbc
├── ChrRaces.dbc
├── TextureFileData.dbc
└── CharSections.dbc (sections parentes)

CharTitles.dbc
├── Faction.dbc (MaskID)
└── Aucune autre dépendance

CharVariations.dbc
├── ChrRaces.dbc
└── TextureFileData.dbc

CharacterFacialHairStyles.dbc
├── ChrRaces.dbc
└── TextureFileData.dbc

CharacterHairGeosets.dbc
├── ChrRaces.dbc
└── TextureFileData.dbc
```

### **9. DBC DE COMBAT ET STATISTIQUES**

```
AttackAnimKits.dbc
├── AttackAnimTypes.dbc
└── AnimKit.dbc

AttackAnimTypes.dbc
└── Aucune dépendance

CombatRating.dbc
└── Aucune dépendance

RandPropPoints.dbc
├── Item.dbc (ItemLevel)
└── ItemRandomProperties.dbc

gtCombatRatings.dbc
└── CombatRating.dbc

ArmorLocation.dbc
└── Aucune dépendance

BankBagSlotPrices.dbc
└── Aucune dépendance

BarberShopStyle.dbc
├── ChrRaces.dbc
├── ChrClasses.dbc
├── CharSections.dbc
└── TextureFileData.dbc

BattlemasterList.dbc
├── Map.dbc
└── SoundEntries.dbc

Cfg_Categories.dbc
├── Cfg_Configs.dbc
└── Localization (via locale)
```

### **10. DBC DES CLASSES ET RACES**

```
ChrClasses.dbc
├── ChrRaces.dbc (via ClassRace)
├── ChrSpecialization.dbc
├── ClassFamily.dbc
├── ClassSkillLines.dbc
│   └── SkillLine.dbc
├── ClassRace.dbc
│   ├── ChrClasses.dbc
│   └── ChrRaces.dbc
└── Spell.dbc (SpellFamily)

ChrRaces.dbc
├── CharBaseInfo.dbc
│   ├── ChrRaces.dbc
│   └── ChrClasses.dbc
├── CharStartOutfit.dbc
│   ├── ChrRaces.dbc
│   ├── ChrClasses.dbc
│   ├── Item.dbc (ItemID1-24)
│   └── Spell.dbc (SpellID1-10)
├── CharTitles.dbc (TitleID)
├── Faction.dbc
├── FactionGroup.dbc
├── FactionTemplate.dbc
│   └── Faction.dbc
└── PlayerCondition.dbc
    ├── ChrRaces.dbc
    ├── ChrClasses.dbc
    └── Spell.dbc

CharBaseInfo.dbc
├── ChrRaces.dbc
├── ChrClasses.dbc
└── Aucune autre dépendance

CharStartOutfit.dbc
├── ChrRaces.dbc
├── ChrClasses.dbc
├── Item.dbc (ItemID1-24)
└── Spell.dbc (SpellID1-10)
```

### **11. DBC DES FACTIONS ET RÉPUTATIONS**

```
Faction.dbc
├── FactionGroup.dbc
├── FactionTemplate.dbc
│   └── Faction.dbc
├── CharTitles.dbc
└── QuestFactionReward.dbc

FactionGroup.dbc
├── Faction.dbc
└── SoundEntries.dbc (sons)

FactionTemplate.dbc
├── Faction.dbc (FactionID1-4)
└── FactionTemplate.dbc (référence croisée)
```

### **12. DBC DES DONJONS ET RAIDS**

```
DungeonEncounter.dbc
├── Map.dbc
├── Creature.dbc (CreatureEntry)
├── Spell.dbc (SpellID)
└── DungeonEncounter.dbc (encounters liés)

DungeonMap.dbc
├── Map.dbc
└── AreaTable.dbc

DungeonMapChunk.dbc
└── DungeonMap.dbc

LFGDungeons.dbc
├── Map.dbc
├── DungeonEncounter.dbc
├── Faction.dbc
└── LFGDungeonGroup.dbc

LFGDungeonGroup.dbc
└── LFGDungeons.dbc
```

### **13. DBC DES SORTS ET AURAS SPÉCIFIQUES**

```
SpellAuraOptions.dbc
├── Spell.dbc
└── SpellAuraRestrictions.dbc

SpellAuraRestrictions.dbc
├── Spell.dbc
└── SpellCastingRequirements.dbc

SpellCastingRequirements.dbc
├── Spell.dbc
└── ChrClasses.dbc (ClassMask)

SpellCategories.dbc
├── Spell.dbc
└── SpellCategory.dbc

SpellCategory.dbc
└── SpellCategories.dbc

SpellClassOptions.dbc
├── Spell.dbc
└── ChrClasses.dbc

SpellCooldowns.dbc
├── Spell.dbc
└── SpellCategory.dbc

SpellEquippedItems.dbc
├── Spell.dbc
└── Item.dbc (ItemClass/SubClass)

SpellInterrupts.dbc
├── Spell.dbc
└── Spell.dbc (InterruptSpellID)

SpellLevels.dbc
├── Spell.dbc
└── ChrClasses.dbc

SpellPower.dbc
├── Spell.dbc
└── ChrClasses.dbc

SpellReagents.dbc
├── Spell.dbc
└── Item.dbc (ReagentID1-8)

SpellRuneCost.dbc
├── Spell.dbc
└── Item.dbc (RuneID)

SpellScaling.dbc
├── Spell.dbc
└── gtCombatRatings.dbc

SpellShapeshift.dbc
├── Spell.dbc
└── SpellShapeshiftForm.dbc

SpellTargetRestrictions.dbc
├── Spell.dbc
├── CreatureType.dbc
└── AreaTable.dbc

SpellTotems.dbc
├── Spell.dbc
└── Item.dbc (TotemID1-2)
```

### **14. DBC DES CINÉMATIQUES ET EFFETS SPÉCIAUX**

```
CinematicCamera.dbc
├── CinematicSequences.dbc
└── CameraShakes.dbc

CinematicSequences.dbc
├── CinematicCamera.dbc
└── SoundEntries.dbc

Movie.dbc
└── Aucune dépendance

MovieFileData.dbc
└── Movie.dbc

MovieVariation.dbc
├── Movie.dbc
└── MovieFileData.dbc
```

### **15. DBC DES ENVIRONNEMENTS ET EFFETS MÉTÉO**

```
Weather.dbc
├── SoundEntries.dbc
└── TextureFileData.dbc

ZoneIntroMusicTable.dbc
├── SoundEntries.dbc
├── AreaTable.dbc
└── ZoneMusic.dbc

ZoneMusic.dbc
├── SoundEntries.dbc
└── ZoneIntroMusicTable.dbc

ZoneLight.dbc
├── LightParams.dbc
└── AreaTable.dbc

ZoneLightPoint.dbc
├── ZoneLight.dbc
└── Map.dbc
```
### **16. DBC DES ÉVÉNEMENTS ET CALENDRIER**

```
CalendarHolidays.dbc
├── CalendarEventType.dbc
└── QuestInfo.dbc

CalendarEventType.dbc
└── Aucune dépendance

HolidayDescriptions.dbc
├── CalendarHolidays.dbc
└── Localization

HolidayNames.dbc
├── CalendarHolidays.dbc
└── Localization

GameEvents.dbc
├── CalendarHolidays.dbc
└── QuestInfo.dbc

WorldStateUI.dbc
├── Map.dbc
├── AreaTable.dbc
└── SoundEntries.dbc

WorldStateZoneSounds.dbc
├── WorldStateUI.dbc
├── AreaTable.dbc
└── SoundEntries.dbc
```

### **17. DBC DES MÉTIERS ET PROFESSIONS**

```
CraftingData.dbc (pas un DBC standard, géré côté serveur)
└── Référence à Spell.dbc pour les recettes

SpellItemEnchantment.dbc
├── Spell.dbc
├── Item.dbc (pour les gemmes)
└── SpellItemEnchantmentCondition.dbc

SpellItemEnchantmentCondition.dbc
├── Item.dbc
└── Spell.dbc

ItemEnchantment.dbc (alias de SpellItemEnchantment)
└── Même structure que SpellItemEnchantment
```


### **18. DBC DES TRANSPORTS ET VÉHICULES**

```
TransportAnimation.dbc
├── TransportPhysics.dbc
└── AnimKit.dbc

TransportPhysics.dbc
└── Aucune dépendance

Vehicle.dbc
├── Spell.dbc (SpellID)
├── Creature.dbc (via CreatureEntry)
└── VehicleSeat.dbc

VehicleSeat.dbc
├── Vehicle.dbc
├── Spell.dbc (SpellID)
└── Item.dbc (ItemID)
```

### **19. DBC DES RÉSEAUX ET BATTLE.NET**

```
BattlemasterList.dbc
├── Map.dbc
├── SoundEntries.dbc
└── BattlemasterList.dbc (référence croisée)

BattlemasterList.dbc (alias)
└── Même structure que ci-dessus

ServerMessages.dbc
└── Localization

WardenChecks.dbc (sécurité, non documenté publiquement)
└── Aucune dépendance
```


### **20. DBC DE LOCALISATION ET LANGAGE**

```
Languages.dbc
└── Aucune dépendance

LanguagesWords.dbc
├── Languages.dbc
└── Localization

Locales (fichiers de localisation)
├── Achievement.dbc (localisé)
├── Spell.dbc (localisé)
├── Item.dbc (localisé)
└── Tous les DBC avec des champs texte
```


### **21. DBC DIVERS ET UTILITAIRES**

```
AccountData.dbc (pas un vrai DBC, géré côté serveur)
└── Aucune dépendance

Cfg_Configs.dbc
├── Cfg_Categories.dbc
└── Localization

ChatChannels.dbc
├── Faction.dbc
└── Localization

ChatProfanity.dbc
└── Localization

DeclinedWord.dbc
├── Languages.dbc
└── Localization

DeclinedWordCases.dbc
├── DeclinedWord.dbc
└── Localization

GameObjectDisplayInfo.dbc
├── TextureFileData.dbc
├── SoundEntries.dbc
└── GameObjectDisplayInfo.dbc (modèles)

GameObjectArtKit.dbc
├── TextureFileData.dbc
└── GameObjectDisplayInfo.dbc

NameGen.dbc
├── ChrRaces.dbc
└── Localization

NamesProfanity.dbc
├── ChrRaces.dbc
└── Localization

NamesReserved.dbc
└── Aucune dépendance

PetPersonality.dbc
└── Aucune dépendance

PetLoyalty.dbc
└── Aucune dépendance

ScalingStatDistribution.dbc
├── ChrClasses.dbc
└── Item.dbc

ScalingStatValues.dbc
├── ScalingStatDistribution.dbc
└── ChrClasses.dbc

StableSlotPrices.dbc
└── Aucune dépendance

TaxiNodes.dbc
├── Map.dbc
└── TaxiPath.dbc

TaxiPath.dbc
├── TaxiNodes.dbc
└── Map.dbc

TaxiPathNode.dbc
├── TaxiPath.dbc
└── Map.dbc

TotemCategory.dbc
├── Item.dbc
└── Spell.dbc

UnitBlood.dbc
├── CreatureDisplayInfo.dbc
└── TextureFileData.dbc

UnitBloodLevels.dbc
├── UnitBlood.dbc
└── TextureFileData.dbc

WMOAreaTable.dbc
├── AreaTable.dbc
├── Map.dbc
└── WMOAreaTable.dbc (référence croisée)

WorldMapOverlay.dbc
├── Map.dbc
├── AreaTable.dbc
└── TextureFileData.dbc

WorldMapTransforms.dbc
├── Map.dbc
└── WorldMapArea.dbc

WorldSafeLocs.dbc
├── Map.dbc
└── AreaTable.dbc

WorldStateUI.dbc
├── Map.dbc
├── AreaTable.dbc
└── SoundEntries.dbc
```

### **RÉSUMÉ STATISTIQUE**

| Catégorie | Nombre approximatif de DBC |
|-----------|---------------------------|
| Core | 15-20 |
| Compétences/Métiers | 10-15 |
| Items/Équipement | 20-25 |
| Créatures/PNJ | 10-15 |
| Zones/Cartes | 15-20 |
| Quêtes | 5-10 |
| Graphiques/Effets | 15-20 |
| Interfaces | 10-15 |
| Combat/Stats | 10-15 |
| Classes/Races | 15-20 |
| Factions | 5-10 |
| Donjons/Raids | 5-10 |
| Sorts/Auras | 20-25 |
| Cinématiques | 5-10 |
| Environnement/Météo | 5-10 |
| Événements/Calendrier | 5-10 |
| Transports/Véhicules | 5-10 |
| Localisation | 10-15 |
| Divers | 30-40 |
| **TOTAL** | **~250-300 DBC** |

---

### **STRUCTURE GÉNÉRALE DES DÉPENDANCES**

```
                    ┌─────────────────────────────┐
                    │      CORE (Spell, Item)     │
                    └─────────────┬───────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
┌───────▼────────┐    ┌───────────▼──────────┐    ┌────────▼────────┐
│   Compétences   │    │      Créatures        │    │      Zones      │
└───────┬────────┘    └───────────┬──────────┘    └────────┬────────┘
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  │
                    ┌─────────────▼───────────────┐
                    │   RÉFÉRENCES CROISÉES        │
                    │   (Classes, Races, Factions) │
                    └─────────────────────────────┘
```

Cette liste exhaustive couvre l'ensemble des DBC présents dans World of Warcraft 3.3.5a (Wrath of the Lich King), avec leurs dépendances principales et leurs interconnexions.
