# 🔍 SYSTÈME D'ANALYSE DE TABLES ET CORRESPONDANCES
## Guide Complet pour Achievement_Criteria

---

## 📋 TABLE DEMANDÉE : Achievement_Criteria

---

## 1. VUE D'ENSEMBLE

### Identification
- **Nom de la table** : Achievement_Criteria
- **Type** : Table DBC (fichier client)
- **Format** : Achievement_Criteria.dbc
- **Localisation** : DBFilesClient/Achievement_Criteria.dbc dans les MPQ

### Description
Cette table définit les **critères de complétion** des hauts faits (achievements). Chaque achievement peut avoir un ou plusieurs critères qui doivent être remplis pour le compléter. C'est le cœur du système de progression des achievements.

---

## 2. STRUCTURE DE LA TABLE

### Colonnes de Achievement_Criteria.dbc (WotLK 3.3.5)

```
+----------------------+------------+----------------------------------------------+
| Colonne              | Type       | Description                                  |
+----------------------+------------+----------------------------------------------+
| ID                   | INT (PK)   | Identifiant unique du critère                |
| AchievementID        | INT (FK)   | Achievement associé                          |
| Type                 | INT        | Type de critère (voir tableau des types)     |
| AssetID              | INT        | ID de l'asset (créature, objet, sort, etc.)  |
| Quantity             | INT        | Quantité requise                             |
| StartEvent           | INT        | Événement de début                           |
| StartAsset           | INT        | Asset de début                               |
| FailEvent            | INT        | Événement d'échec                            |
| FailAsset            | INT        | Asset d'échec                               |
| Description          | STRING     | Description du critère                       |
| Flags                | INT        | Drapeaux spéciaux                            |
| TimerStartEvent      | INT        | Événement de début du chronomètre            |
| TimerAssetID         | INT        | Asset du chronomètre                         |
| TimerTime            | INT        | Temps limite (en secondes)                   |
| UIOrder              | INT        | Ordre d'affichage dans l'interface           |
+----------------------+------------+----------------------------------------------+
```

### Exemple de données

```
ID    | AchievementID | Type | AssetID | Quantity | Description                    | Flags
------|---------------|------|---------|----------|--------------------------------|-------
1     | 6             | 11   | 0       | 10       | Reach level 10                 | 0
2     | 6             | 11   | 0       | 20       | Reach level 20                 | 0
3     | 6             | 11   | 0       | 30       | Reach level 30                 | 0
100   | 128           | 0    | 1234    | 1        | Kill Onyxia                   | 0
200   | 500           | 27   | 4567    | 100      | Collect 100 gold              | 0
300   | 750           | 36   | 7890    | 50       | Complete 50 quests            | 0
```

---

## 3. TYPES DE CRITÈRES

### Tableau complet des types de critères

```
┌──────┬──────────────────────────────────────────────────────────┐
│ Type │ Description                                              │
├──────┼──────────────────────────────────────────────────────────┤
│ 0    │ Kill creature (tuer une créature)                        │
│ 1    │ Win battleground (gagner un champ de bataille)           │
│ 2    │ Reach level (atteindre un niveau)                        │
│ 3    │ Reach skill level (atteindre un niveau de compétence)    │
│ 4    │ Complete achievement (compléter un achievement)          │
│ 5    │ Complete quest count (compléter X quêtes)                │
│ 6    │ Complete daily quest (compléter une quête journalière)   │
│ 7    │ Complete quests in zone (quêtes dans une zone)           │
│ 8    │ Damage done (dégâts infligés)                            │
│ 9    │ Complete daily quest daily (quête journalière/jour)      │
│ 10   │ Complete battleground (compléter un champ de bataille)   │
│ 11   │ Death (mourir)                                           │
│ 12   │ Death in dungeon (mourir en donjon)                      │
│ 13   │ Death in raid (mourir en raid)                           │
│ 14   │ Fall without dying (tomber sans mourir)                  │
│ 15   │ Deaths from falling (morts par chute)                    │
│ 16   │ Complete quest (compléter une quête spécifique)          │
│ 17   │ Be spell target (être cible d'un sort)                   │
│ 18   │ Cast spell (lancer un sort)                              │
│ 19   │ Win arena (gagner en arène)                              │
│ 20   │ Play arena (jouer en arène)                              │
│ 21   │ Learn spell (apprendre un sort)                          │
│ 22   │ Win rated arena (gagner en arène cotée)                  │
│ 23   │ Own item (posséder un objet)                             │
│ 24   │ Win duel (gagner un duel)                                │
│ 25   │ Lose duel (perdre un duel)                               │
│ 26   │ Kill creature type (tuer type de créature)               │
│ 27   │ Gold earned (or gagné)                                   │
│ 28   │ Use item (utiliser un objet)                             │
│ 29   │ Loot item (butiner un objet)                             │
│ 30   │ Explore area (explorer une zone)                         │
│ 31   │ Own rank (obtenir un rang)                               │
│ 32   │ Buy bank slot (acheter un emplacement de banque)         │
│ 33   │ Gain reputation (gagner de la réputation)                │
│ 34   │ Gain exalted reputation (réputation exaltée)             │
│ 35   │ Visit barber shop (visiter le barbier)                   │
│ 36   │ Equip item (équiper un objet)                            │
│ 37   │ Roll need (jet de besoin)                                │
│ 38   │ Roll greed (jet de cupidité)                             │
│ 39   │ Hurt creature (blesser une créature)                     │
│ 40   │ Heal creature (soigner une créature)                     │
│ 41   │ Get loot by type (butin par type)                        │
│ 42   │ Land killing blow (coup fatal)                           │
│ 43   │ Use item on creature (objet sur créature)                │
│ 44   │ Complete dungeon (compléter un donjon)                   │
│ 45   │ Complete raid (compléter un raid)                        │
│ 46   │ Own mount (posséder une monture)                         │
│ 47   │ Learn spell type (apprendre type de sort)                │
│ 48   │ Own companion (posséder un familier)                     │
│ 49   │ Be in zone (être dans une zone)                          │
│ 50   │ Complete scenario (compléter un scénario)                │
└──────┴──────────────────────────────────────────────────────────┘
```

---

## 4. CORRESPONDANCES AVEC AUTRES TABLES

### Tableau des correspondances

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CORRESPONDANCES COMPLÈTES                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ACHIEVEMENT_CRITERIA.DBC (Client)                                  │
│  │                                                                  │
│  ├── ID ────────────────────► achievement_criteria_data.id          │
│  ├── AchievementID ─────────► achievement_dbc.id                    │
│  ├── Type ──────────────────► achievement_criteria_data.type        │
│  ├── AssetID ───────────────► achievement_criteria_data.value       │
│  ├── Quantity ──────────────► achievement_criteria_data.value       │
│  ├── Description ───────────► (texte dans le client)                │
│  └── Flags ─────────────────► (drapeaux spéciaux)                   │
│                                                                     │
│  TABLES LIÉES                                                       │
│  ├── Achievement.dbc → parent                                       │
│  ├── Achievement_Category.dbc → via Achievement.dbc                 │
│  ├── Creature.dbc → pour Type=0 (tuer créature)                     │
│  ├── Spell.dbc → pour Type=18 (lancer sort)                         │
│  ├── Item.dbc → pour Type=23 (posséder objet)                       │
│  ├── Quest.dbc → pour Type=16 (compléter quête)                     │
│  └── AreaTable.dbc → pour Type=30 (explorer zone)                   │
│                                                                     │
│  TABLES MYSQL AZEROTHCORE                                           │
│  ├── achievement_criteria_data                                      │
│  ├── achievement_dbc                                                │
│  ├── character_achievement_progress                                 │
│  └── character_achievement                                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. STRUCTURE BINAIRE DU FICHIER DBC

### Format détaillé

```python
class AchievementCriteriaDBC:
    """
    Structure de Achievement_Criteria.dbc
    Header : 20 octets
    Record Size : 60 octets (15 champs × 4 octets)
    """
    
    def __init__(self):
        self.header = {
            'magic': b'WDBC',           # 4 octets - Signature
            'record_count': 0,          # 4 octets - Nombre de lignes
            'field_count': 15,          # 4 octets - Nombre de colonnes
            'record_size': 60,          # 4 octets - Taille d'une ligne
            'string_block_size': 0      # 4 octets - Taille du bloc texte
        }
        
        self.fields = [
            {'name': 'ID', 'type': 'uint32', 'offset': 0},
            {'name': 'AchievementID', 'type': 'uint32', 'offset': 4},
            {'name': 'Type', 'type': 'uint32', 'offset': 8},
            {'name': 'AssetID', 'type': 'uint32', 'offset': 12},
            {'name': 'Quantity', 'type': 'uint32', 'offset': 16},
            {'name': 'StartEvent', 'type': 'uint32', 'offset': 20},
            {'name': 'StartAsset', 'type': 'uint32', 'offset': 24},
            {'name': 'FailEvent', 'type': 'uint32', 'offset': 28},
            {'name': 'FailAsset', 'type': 'uint32', 'offset': 32},
            {'name': 'Description', 'type': 'string_ref', 'offset': 36},
            {'name': 'Flags', 'type': 'uint32', 'offset': 40},
            {'name': 'TimerStartEvent', 'type': 'uint32', 'offset': 44},
            {'name': 'TimerAssetID', 'type': 'uint32', 'offset': 48},
            {'name': 'TimerTime', 'type': 'uint32', 'offset': 52},
            {'name': 'UIOrder', 'type': 'uint32', 'offset': 56}
        ]
```

### Parsing en Python

```python
import struct
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AchievementCriteria:
    ID: int
    AchievementID: int
    Type: int
    AssetID: int
    Quantity: int
    StartEvent: int
    StartAsset: int
    FailEvent: int
    FailAsset: int
    Description: str
    Flags: int
    TimerStartEvent: int
    TimerAssetID: int
    TimerTime: int
    UIOrder: int

class AchievementCriteriaParser:
    """Parser pour Achievement_Criteria.dbc"""
    
    CRITERIA_TYPES = {
        0: "Kill creature",
        1: "Win battleground",
        2: "Reach level",
        3: "Reach skill level",
        4: "Complete achievement",
        5: "Complete quest count",
        6: "Complete daily quest",
        7: "Complete quests in zone",
        8: "Damage done",
        9: "Complete daily quest daily",
        10: "Complete battleground",
        11: "Death",
        12: "Death in dungeon",
        13: "Death in raid",
        14: "Fall without dying",
        15: "Deaths from falling",
        16: "Complete quest",
        17: "Be spell target",
        18: "Cast spell",
        19: "Win arena",
        20: "Play arena",
        21: "Learn spell",
        22: "Win rated arena",
        23: "Own item",
        24: "Win duel",
        25: "Lose duel",
        26: "Kill creature type",
        27: "Gold earned",
        28: "Use item",
        29: "Loot item",
        30: "Explore area",
        31: "Own rank",
        32: "Buy bank slot",
        33: "Gain reputation",
        34: "Gain exalted reputation",
        35: "Visit barber shop",
        36: "Equip item",
        37: "Roll need",
        38: "Roll greed",
        39: "Hurt creature",
        40: "Heal creature",
        41: "Get loot by type",
        42: "Land killing blow",
        43: "Use item on creature",
        44: "Complete dungeon",
        45: "Complete raid",
        46: "Own mount",
        47: "Learn spell type",
        48: "Own companion",
        49: "Be in zone",
        50: "Complete scenario"
    }
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.criteria = []
        self.parse()
    
    def parse(self):
        """Parse le fichier DBC"""
        with open(self.filepath, 'rb') as f:
            data = f.read()
        
        # Header
        record_count = struct.unpack('<I', data[4:8])[0]
        field_count = struct.unpack('<I', data[8:12])[0]
        record_size = struct.unpack('<I', data[12:16])[0]
        string_block_size = struct.unpack('<I', data[16:20])[0]
        
        print(f"Records: {record_count}")
        print(f"Fields: {field_count}")
        print(f"Record Size: {record_size}")
        
        # String block
        string_block_offset = 20 + (record_count * record_size)
        string_block = data[string_block_offset:]
        
        # Parse records
        offset = 20
        for i in range(record_count):
            record_data = data[offset:offset + record_size]
            
            crit = AchievementCriteria(
                ID=struct.unpack('<I', record_data[0:4])[0],
                AchievementID=struct.unpack('<I', record_data[4:8])[0],
                Type=struct.unpack('<I', record_data[8:12])[0],
                AssetID=struct.unpack('<I', record_data[12:16])[0],
                Quantity=struct.unpack('<I', record_data[16:20])[0],
                StartEvent=struct.unpack('<I', record_data[20:24])[0],
                StartAsset=struct.unpack('<I', record_data[24:28])[0],
                FailEvent=struct.unpack('<I', record_data[28:32])[0],
                FailAsset=struct.unpack('<I', record_data[32:36])[0],
                Description=self.read_string(string_block, 
                    struct.unpack('<I', record_data[36:40])[0]),
                Flags=struct.unpack('<I', record_data[40:44])[0],
                TimerStartEvent=struct.unpack('<I', record_data[44:48])[0],
                TimerAssetID=struct.unpack('<I', record_data[48:52])[0],
                TimerTime=struct.unpack('<I', record_data[52:56])[0],
                UIOrder=struct.unpack('<I', record_data[56:60])[0]
            )
            
            self.criteria.append(crit)
            offset += record_size
    
    def read_string(self, string_block, offset):
        """Lit une chaîne depuis le bloc de texte"""
        if offset >= len(string_block):
            return ""
        end = string_block.find(b'\x00', offset)
        if end == -1:
            return ""
        return string_block[offset:end].decode('utf-8', errors='ignore')
    
    def get_criteria_for_achievement(self, achievement_id):
        """Retourne tous les critères d'un achievement"""
        return [c for c in self.criteria if c.AchievementID == achievement_id]
    
    def get_criteria_by_type(self, criteria_type):
        """Retourne tous les critères d'un type donné"""
        return [c for c in self.criteria if c.Type == criteria_type]
    
    def get_type_name(self, criteria_type):
        """Retourne le nom lisible d'un type"""
        return self.CRITERIA_TYPES.get(criteria_type, f"Unknown ({criteria_type})")
    
    def print_summary(self):
        """Affiche un résumé des critères"""
        print(f"\n{'='*60}")
        print("RÉSUMÉ DES CRITÈRES")
        print(f"{'='*60}")
        print(f"Total critères : {len(self.criteria)}")
        
        # Par type
        types_count = {}
        for c in self.criteria:
            type_name = self.get_type_name(c.Type)
            types_count[type_name] = types_count.get(type_name, 0) + 1
        
        print("\nRépartition par type :")
        for type_name, count in sorted(types_count.items(), key=lambda x: -x[1]):
            print(f"  {type_name:<40} : {count}")
    
    def export_to_json(self, output_file):
        """Exporte les critères en JSON"""
        import json
        
        data = []
        for c in self.criteria:
            data.append({
                'ID': c.ID,
                'AchievementID': c.AchievementID,
                'Type': c.Type,
                'TypeName': self.get_type_name(c.Type),
                'AssetID': c.AssetID,
                'Quantity': c.Quantity,
                'Description': c.Description,
                'Flags': c.Flags,
                'TimerTime': c.TimerTime,
                'UIOrder': c.UIOrder
            })
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Exporté vers {output_file}")
```

---

## 6. CORRESPONDANCE AVEC MYSQL AZEROTHCORE

### Table achievement_criteria_data

```sql
-- Structure de achievement_criteria_data dans acore_world
DESCRIBE acore_world.achievement_criteria_data;

-- Colonnes typiques :
-- criteria_id    : Référence Achievement_Criteria.ID
-- type           : Type de données supplémentaires
-- value1         : Première valeur
-- value2         : Deuxième valeur
-- ScriptName     : Script associé
```

### Requêtes de correspondance

```sql
-- 1. Lier les critères aux achievements
SELECT 
    ac.ID as criteria_id,
    ac.AchievementID,
    ac.Type,
    ac.AssetID,
    ac.Quantity,
    ac.Description,
    a.Title as achievement_title,
    a.CategoryID
FROM Achievement_Criteria ac
JOIN Achievement a ON ac.AchievementID = a.ID
ORDER BY a.CategoryID, a.ID, ac.UIOrder;

-- 2. Critères par type dans MySQL
SELECT 
    acd.criteria_id,
    acd.type,
    acd.value1,
    acd.value2,
    a.id as achievement_id,
    a.title as achievement_title
FROM acore_world.achievement_criteria_data acd
JOIN acore_world.achievement_dbc a ON a.id = acd.criteria_id
ORDER BY acd.type, acd.criteria_id;

-- 3. Progression des joueurs
SELECT 
    c.name as character_name,
    a.id as achievement_id,
    a.title as achievement_title,
    cap.counter as progress,
    acd.value1 as required
FROM acore_characters.character_achievement_progress cap
JOIN acore_characters.characters c ON cap.guid = c.guid
JOIN acore_world.achievement_dbc a ON cap.criteria = a.id
JOIN acore_world.achievement_criteria_data acd ON acd.criteria_id = cap.criteria
WHERE cap.counter < acd.value1
LIMIT 20;
```

### Tableau de correspondance MySQL

```
┌─────────────────────────────────────────────────────────────────────┐
│              CORRESPONDANCE DBC → MYSQL                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Achievement_Criteria.dbc                                          │
│  ├── ID ──────────────────► achievement_criteria_data.criteria_id  │
│  ├── AchievementID ───────► achievement_dbc.id                     │
│  ├── Type ────────────────► (interprété par le serveur)            │
│  ├── AssetID ─────────────► achievement_criteria_data.value1       │
│  ├── Quantity ────────────► achievement_criteria_data.value2       │
│  └── Description ─────────► (texte client uniquement)              │
│                                                                     │
│  Progression des personnages :                                     │
│  ├── character_achievement_progress.criteria                        │
│  │   └── Référence Achievement_Criteria.ID                         │
│  ├── character_achievement_progress.counter                        │
│  │   └── Progression actuelle                                      │
│  └── character_achievement.achievement                             │
│      └── Référence Achievement.ID                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 7. OUTIL DE RECHERCHE AUTOMATIQUE

### Script Python complet pour analyser n'importe quelle table

```python
import mysql.connector
import json
import re

class TableSearchSystem:
    """Système de recherche et d'analyse de tables"""
    
    def __init__(self, db_config):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor(dictionary=True)
        
        # Cache des métadonnées
        self.table_cache = {}
        self.relation_cache = {}
    
    def search_table(self, search_term):
        """Recherche une table par nom partiel"""
        self.cursor.execute("""
            SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS
            FROM information_schema.TABLES
            WHERE TABLE_SCHEMA = 'acore_world'
            AND TABLE_NAME LIKE %s
            ORDER BY 
                CASE 
                    WHEN TABLE_NAME = %s THEN 0
                    WHEN TABLE_NAME LIKE %s THEN 1
                    ELSE 2
                END,
                TABLE_NAME
        """, (
            f'%{search_term}%',
            search_term,
            f'{search_term}%'
        ))
        
        return self.cursor.fetchall()
    
    def get_table_structure(self, table_name):
        """Récupère la structure complète d'une table"""
        if table_name in self.table_cache:
            return self.table_cache[table_name]
        
        self.cursor.execute(f"DESCRIBE {table_name}")
        structure = self.cursor.fetchall()
        
        self.table_cache[table_name] = structure
        return structure
    
    def get_table_relations(self, table_name):
        """Trouve toutes les relations de la table"""
        if table_name in self.relation_cache:
            return self.relation_cache[table_name]
        
        # Relations sortantes
        self.cursor.execute("""
            SELECT 
                COLUMN_NAME,
                REFERENCED_TABLE_NAME,
                REFERENCED_COLUMN_NAME
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE TABLE_SCHEMA = 'acore_world'
            AND TABLE_NAME = %s
            AND REFERENCED_TABLE_NAME IS NOT NULL
        """, (table_name,))
        outgoing = self.cursor.fetchall()
        
        # Relations entrantes
        self.cursor.execute("""
            SELECT 
                TABLE_NAME,
                COLUMN_NAME,
                REFERENCED_COLUMN_NAME
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE TABLE_SCHEMA = 'acore_world'
            AND REFERENCED_TABLE_NAME = %s
        """, (table_name,))
        incoming = self.cursor.fetchall()
        
        relations = {
            'outgoing': outgoing,
            'incoming': incoming
        }
        
        self.relation_cache[table_name] = relations
        return relations
    
    def find_corresponding_tables(self, table_name):
        """Trouve les tables correspondantes"""
        # Nettoyer le nom (enlever _dbc, _template, etc.)
        base_name = re.sub(r'_(dbc|template|locale|addon|data)$', '', table_name)
        
        correspondences = []
        
        # Rechercher les variantes
        self.cursor.execute("""
            SELECT TABLE_NAME
            FROM information_schema.TABLES
            WHERE TABLE_SCHEMA = 'acore_world'
            AND (
                TABLE_NAME LIKE %s
                OR TABLE_NAME LIKE %s
                OR %s LIKE CONCAT('%%', TABLE_NAME, '%%')
            )
            ORDER BY TABLE_NAME
        """, (
            f'{base_name}%',
            f'%{base_name}%',
            base_name
        ))
        
        for row in self.cursor.fetchall():
            correspondences.append(row['TABLE_NAME'])
        
        return correspondences
    
    def generate_full_report(self, table_name):
        """Génère un rapport complet pour une table"""
        print(f"\n{'='*70}")
        print(f"📊 RAPPORT COMPLET : {table_name}")
        print(f"{'='*70}")
        
        # 1. Structure
        print(f"\n📋 STRUCTURE DE LA TABLE :")
        print("-"*50)
        structure = self.get_table_structure(table_name)
        for field in structure:
            key_info = f" [PK]" if field['Key'] == 'PRI' else f" [FK]" if field['Key'] == 'MUL' else ""
            print(f"  {field['Field']:<35} {field['Type']:<20} {field['Null']:<5}{key_info}")
        
        # 2. Relations
        print(f"\n🔗 RELATIONS :")
        print("-"*50)
        relations = self.get_table_relations(table_name)
        
        if relations['outgoing']:
            print("  Relations sortantes :")
            for rel in relations['outgoing']:
                print(f"    → {rel['COLUMN_NAME']} → {rel['REFERENCED_TABLE_NAME']}.{rel['REFERENCED_COLUMN_NAME']}")
        else:
            print("  Aucune relation sortante")
        
        if relations['incoming']:
            print("  Relations entrantes :")
            for rel in relations['incoming']:
                print(f"    ← {rel['TABLE_NAME']}.{rel['COLUMN_NAME']} → {rel['REFERENCED_COLUMN_NAME']}")
        else:
            print("  Aucune relation entrante")
        
        # 3. Tables correspondantes
        print(f"\n📑 TABLES CORRESPONDANTES :")
        print("-"*50)
        correspondences = self.find_corresponding_tables(table_name)
        for table in correspondences:
            if table != table_name:
                print(f"  • {table}")
        
        # 4. Exemples de données
        print(f"\n🔍 EXEMPLES DE DONNÉES (5 premiers) :")
        print("-"*50)
        self.cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
        examples = self.cursor.fetchall()
        for i, example in enumerate(examples, 1):
            print(f"  {i}. {example}")
        
        # 5. Statistiques
        print(f"\n📈 STATISTIQUES :")
        print("-"*50)
        self.cursor.execute(f"SELECT COUNT(*) as count FROM {table_name}")
        count = self.cursor.fetchone()['count']
        print(f"  Nombre total d'enregistrements : {count}")
        
        return {
            'table_name': table_name,
            'structure': structure,
            'relations': relations,
            'correspondences': correspondences,
            'examples': examples,
            'count': count
        }
    
    def interactive_mode(self):
        """Mode interactif de recherche"""
        print("🔍 SYSTÈME DE RECHERCHE DE TABLES")
        print("Entrez un nom de table (ou 'quit' pour quitter)")
        print("Exemples : Achievement, Criteria, Creature, Quest, Spell, Item")
        print()
        
        while True:
            search = input("> ").strip()
            
            if search.lower() == 'quit':
                break
            
            if not search:
                continue
            
            results = self.search_table(search)
            
            if not results:
                print(f"❌ Aucune table trouvée pour '{search}'")
                continue
            
            print(f"\n📊 {len(results)} table(s) trouvée(s) :")
            for i, row in enumerate(results, 1):
                rows_info = f" (~{row['TABLE_ROWS']} lignes)" if row['TABLE_ROWS'] else ""
                print(f"  {i}. {row['TABLE_NAME']}{rows_info}")
            
            choice = input("\nSélectionnez un numéro pour analyser (ou Entrée pour continuer) : ")
            
            if choice.isdigit() and 1 <= int(choice) <= len(results):
                selected = results[int(choice) - 1]['TABLE_NAME']
                self.generate_full_report(selected)
            elif choice.strip():
                print("❌ Sélection invalide")

# Utilisation
if __name__ == '__main__':
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'votre_mdp',
        'database': 'acore_world'
    }
    
    system = TableSearchSystem(config)
    system.interactive_mode()
```

---

## 8. ANALYSE SPÉCIFIQUE POUR Achievement_Criteria

### Résumé des correspondances

```python
def analyze_achievement_criteria_specific():
    """Analyse spécifique pour Achievement_Criteria"""
    
    correspondences = {
        'DBC_File': 'Achievement_Criteria.dbc',
        'MySQL_Tables': [
            'achievement_criteria_data',
            'achievement_dbc',
            'character_achievement_progress',
            'character_achievement'
        ],
        'Related_DBC': [
            'Achievement.dbc',           # Parent
            'Achievement_Category.dbc',  # Grand-parent via Achievement
            'Creature.dbc',              # Pour Type=0
            'Spell.dbc',                 # Pour Type=18
            'Item.dbc',                  # Pour Type=23
            'Quest.dbc',                 # Pour Type=16
            'AreaTable.dbc'              # Pour Type=30
        ],
        'Key_Relations': {
            'AchievementID → Achievement.ID': 'Chaque critère appartient à un achievement',
            'AssetID → Variable selon Type': 'Référence créature, sort, objet, etc.',
            'ID → achievement_criteria_data.criteria_id': 'Correspondance MySQL',
            'ID → character_achievement_progress.criteria': 'Progression des joueurs'
        }
    }
    
    print("ANALYSE SPÉCIFIQUE : Achievement_Criteria")
    print("="*60)
    print("\n📁 FICHIER DBC :")
    print(f"  {correspondences['DBC_File']}")
    
    print("\n🗄️ TABLES MYSQL :")
    for table in correspondences['MySQL_Tables']:
        print(f"  • {table}")
    
    print("\n🔗 DBC LIÉS :")
    for dbc in correspondences['Related_DBC']:
        print(f"  • {dbc}")
    
    print("\n🔑 RELATIONS CLÉS :")
    for relation, description in correspondences['Key_Relations'].items():
        print(f"  • {relation}")
        print(f"    {description}")

analyze_achievement_criteria_specific()
```

---

## 9. RÉSUMÉ POUR Achievement_Criteria

### Points clés
1. **Achievement_Criteria** est un DBC client qui définit les critères de complétion
2. Chaque critère appartient à un achievement (AchievementID)
3. Il existe 50+ types de critères différents
4. Dans MySQL, les données sont dans `achievement_criteria_data`
5. La progression des joueurs est suivie dans `character_achievement_progress`

### Flux de données
```
Achievement.dbc
    ↓ AchievementID
Achievement_Criteria.dbc
    ↓ ID
achievement_criteria_data (MySQL)
    ↓ criteria_id
character_achievement_progress (MySQL)
    ↓ achievement
character_achievement (MySQL)
```

### Exemple concret
```
Achievement : "Niveau 10" (ID=6)
    ↓
Critère : "Atteindre le niveau 10" (ID=1)
    - Type = 2 (Reach level)
    - Quantity = 10
    - AssetID = 0
    ↓
MySQL : achievement_criteria_data
    - criteria_id = 1
    - value1 = 10
    ↓
Joueur atteint niveau 10
    ↓
character_achievement_progress
    - criteria = 1
    - counter = 10
    ↓
Achievement complété !
```
