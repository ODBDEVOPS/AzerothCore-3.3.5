# 🔍 SYSTÈME D'ANALYSE DE TABLES ET CORRESPONDANCES
## Guide Complet pour Achievement_Category

---

## 📋 TABLE DEMANDÉE : Achievement_Category

---

## 1. VUE D'ENSEMBLE

### Identification
- **Nom de la table** : Achievement_Category
- **Type** : Table DBC (fichier client)
- **Format** : Achievement_Category.dbc
- **Localisation** : DBFilesClient/Achievement_Category.dbc dans les MPQ

### Description
Cette table définit les **catégories et sous-catégories** dans lesquelles sont organisés les hauts faits (achievements). Elle structure l'interface des hauts faits dans le jeu.

---

## 2. STRUCTURE DE LA TABLE

### Colonnes de Achievement_Category.dbc

```
+------------------+------------+------------------------------------------+
| Colonne          | Type       | Description                              |
+------------------+------------+------------------------------------------+
| ID               | INT (PK)   | Identifiant unique de la catégorie       |
| ParentID         | INT (FK)   | Catégorie parente (-1 si racine)         |
| Name             | STRING     | Nom de la catégorie                      |
| UIOrder          | INT        | Ordre d'affichage dans l'interface       |
+------------------+------------+------------------------------------------+
```

### Exemple de données

```
ID  | ParentID | Name              | UIOrder
----|----------|-------------------|--------
1   | -1       | Statistics        | 1
2   | -1       | General           | 2
3   | -1       | Quests            | 3
4   | -1       | Exploration       | 4
5   | -1       | Player vs Player  | 5
6   | -1       | Dungeons & Raids  | 6
7   | -1       | Professions       | 7
8   | -1       | Reputation        | 8
9   | -1       | World Events      | 9
10  | -1       | Feats of Strength | 10
11  | -1       | Guild             | 11
81  | 1        | Wealth            | 1
82  | 1        | Gear              | 2
83  | 1        | Character         | 3
```

---

## 3. CORRESPONDANCES AVEC AUTRES TABLES

### Tableau des correspondances

```
┌─────────────────────────┬──────────────────────────────────────┐
│ Table liée              │ Relation                             │
├─────────────────────────┼──────────────────────────────────────┤
│ Achievement.dbc         │ Achievement.CategoryID → Category.ID │
│ Achievement_Criteria    │ Via Achievement.dbc                  │
│ CriteriaTree.dbc        │ Via Achievement.dbc                  │
│ achievement_dbc (MySQL) │ Copie SQL de Achievement.dbc         │
└─────────────────────────┴──────────────────────────────────────┘
```

### Détail des relations

#### A) Relation avec Achievement.dbc
```sql
-- Achievement.dbc contient un champ CategoryID
-- qui référence Achievement_Category.ID

SELECT 
    ac.ID AS CategoryID,
    ac.Name AS CategoryName,
    ac.ParentID AS ParentCategory,
    a.ID AS AchievementID,
    a.Title AS AchievementTitle
FROM Achievement_Category ac
LEFT JOIN Achievement a ON a.CategoryID = ac.ID
ORDER BY ac.UIOrder, a.ID;
```

#### B) Hiérarchie Parent-Enfant
```sql
-- Achievement_Category a une auto-référence
-- ParentID pointe vers une autre catégorie

SELECT 
    parent.ID AS ParentID,
    parent.Name AS ParentName,
    child.ID AS ChildID,
    child.Name AS ChildName
FROM Achievement_Category parent
INNER JOIN Achievement_Category child ON child.ParentID = parent.ID
ORDER BY parent.ID, child.UIOrder;
```

---

## 4. STRUCTURE BINAIRE DU FICHIER DBC

### Format détaillé

```python
class AchievementCategoryDBC:
    """
    Structure de Achievement_Category.dbc
    Header : 20 octets
    Record Size : 16 octets (4 champs × 4 octets)
    """
    
    def __init__(self):
        self.header = {
            'magic': b'WDBC',           # 4 octets - Signature
            'record_count': 0,          # 4 octets - Nombre de lignes
            'field_count': 4,           # 4 octets - Nombre de colonnes
            'record_size': 16,          # 4 octets - Taille d'une ligne
            'string_block_size': 0      # 4 octets - Taille du bloc texte
        }
        
        self.fields = [
            {'name': 'ID', 'type': 'uint32', 'offset': 0},
            {'name': 'ParentID', 'type': 'int32', 'offset': 4},
            {'name': 'Name', 'type': 'string_ref', 'offset': 8},
            {'name': 'UIOrder', 'type': 'uint32', 'offset': 12}
        ]
```

### Parsing en Python

```python
import struct

def parse_achievement_category(filepath):
    """Parse Achievement_Category.dbc"""
    
    with open(filepath, 'rb') as f:
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
    
    categories = []
    offset = 20
    
    for i in range(record_count):
        record_data = data[offset:offset + record_size]
        
        # Parse fields
        category_id = struct.unpack('<I', record_data[0:4])[0]
        parent_id = struct.unpack('<i', record_data[4:8])[0]
        name_offset = struct.unpack('<I', record_data[8:12])[0]
        ui_order = struct.unpack('<I', record_data[12:16])[0]
        
        # Read string
        name = read_string(string_block, name_offset)
        
        categories.append({
            'ID': category_id,
            'ParentID': parent_id,
            'Name': name,
            'UIOrder': ui_order
        })
        
        offset += record_size
    
    return categories

def read_string(string_block, offset):
    """Lit une chaîne depuis le bloc de texte"""
    if offset >= len(string_block):
        return ""
    end = string_block.find(b'\x00', offset)
    if end == -1:
        return ""
    return string_block[offset:end].decode('utf-8', errors='ignore')
```

---

## 5. CORRESPONDANCE AVEC MYSQL AZEROTHCORE

### Tables MySQL équivalentes

Dans AzerothCore, il n'y a **pas de table MySQL directe** pour Achievement_Category. Les catégories sont gérées via :

```sql
-- 1. achievement_dbc contient la référence à la catégorie
SELECT * FROM acore_world.achievement_dbc LIMIT 5;
-- Colonne categoryId référence Achievement_Category.ID

-- 2. Les catégories sont "en dur" dans le client
-- via Achievement_Category.dbc

-- 3. Vérification des relations
SELECT 
    a.id,
    a.title,
    a.categoryId as category_id
FROM acore_world.achievement_dbc a
ORDER BY a.categoryId, a.id;
```

### Requêtes utiles

```sql
-- Lister les achievements par catégorie
SELECT 
    a.categoryId,
    COUNT(*) as achievement_count,
    MIN(a.id) as first_achievement,
    MAX(a.id) as last_achievement
FROM acore_world.achievement_dbc a
GROUP BY a.categoryId
ORDER BY a.categoryId;

-- Catégories avec le plus d'achievements
SELECT 
    a.categoryId,
    COUNT(*) as total
FROM acore_world.achievement_dbc a
GROUP BY a.categoryId
ORDER BY total DESC;

-- Achievements sans catégorie valide
SELECT 
    a.id,
    a.title,
    a.categoryId
FROM acore_world.achievement_dbc a
WHERE a.categoryId NOT IN (1,2,3,4,5,6,7,8,9,10,11,81,82,83);
```

---

## 6. TABLEAU COMPLET DES CORRESPONDANCES

### Mapping DBC → MySQL

```
┌─────────────────────────────────────────────────────────────────┐
│                    CORRESPONDANCES COMPLÈTES                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ACHIEVEMENT_CATEGORY.DBC (Client)                              │
│  ├── ID ────────────────────► achievement_dbc.categoryId        │
│  ├── ParentID ──────────────► (auto-référence dans le DBC)      │
│  ├── Name ──────────────────► (texte affiché dans le client)    │
│  └── UIOrder ───────────────► (ordre dans l'interface)          │
│                                                                 │
│  ACHIEVEMENT.DBC (Client)                                       │
│  ├── ID ────────────────────► achievement_dbc.id                │
│  ├── CategoryID ────────────► achievement_dbc.categoryId        │
│  ├── Title ─────────────────► achievement_dbc.title             │
│  ├── Description ───────────► achievement_dbc.description       │
│  ├── Points ────────────────► achievement_dbc.points            │
│  ├── Flags ─────────────────► achievement_dbc.flags             │
│  └── IconID ────────────────► achievement_dbc.icon              │
│                                                                 │
│  ACHIEVEMENT_CRITERIA.DBC (Client)                              │
│  ├── ID ────────────────────► achievement_criteria_data.id      │
│  ├── AchievementID ─────────► achievement_dbc.id                │
│  └── Quantity ──────────────► achievement_criteria_data.value   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. OUTIL DE RECHERCHE AUTOMATIQUE

### Script Python pour analyser n'importe quelle table

```python
import mysql.connector
import json

class TableAnalyzer:
    """Analyse une table et trouve ses correspondances"""
    
    def __init__(self, db_config):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor(dictionary=True)
    
    def analyze_table(self, table_name):
        """Analyse complète d'une table"""
        result = {
            'table_name': table_name,
            'structure': self.get_structure(table_name),
            'relations': self.get_relations(table_name),
            'correspondences': self.find_correspondences(table_name),
            'examples': self.get_examples(table_name)
        }
        return result
    
    def get_structure(self, table_name):
        """Récupère la structure de la table"""
        self.cursor.execute(f"DESCRIBE {table_name}")
        return self.cursor.fetchall()
    
    def get_relations(self, table_name):
        """Trouve les relations avec d'autres tables"""
        self.cursor.execute("""
            SELECT 
                TABLE_NAME,
                COLUMN_NAME,
                REFERENCED_TABLE_NAME,
                REFERENCED_COLUMN_NAME
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE TABLE_SCHEMA = 'acore_world'
            AND TABLE_NAME = %s
            AND REFERENCED_TABLE_NAME IS NOT NULL
        """, (table_name,))
        return self.cursor.fetchall()
    
    def find_correspondences(self, table_name):
        """Trouve les tables correspondantes"""
        correspondences = []
        
        # Chercher les tables avec des noms similaires
        self.cursor.execute("""
            SELECT TABLE_NAME
            FROM information_schema.TABLES
            WHERE TABLE_SCHEMA = 'acore_world'
            AND (TABLE_NAME LIKE %s OR TABLE_NAME LIKE %s)
        """, (f'%{table_name}%', f'%{table_name.replace("_", "")}%'))
        
        for row in self.cursor.fetchall():
            correspondences.append(row['TABLE_NAME'])
        
        return correspondences
    
    def get_examples(self, table_name, limit=5):
        """Récupère des exemples de données"""
        self.cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit}")
        return self.cursor.fetchall()
    
    def generate_report(self, table_name):
        """Génère un rapport complet"""
        analysis = self.analyze_table(table_name)
        
        print("="*70)
        print(f"ANALYSE DE LA TABLE : {table_name}")
        print("="*70)
        
        print("\n1. STRUCTURE :")
        print("-"*50)
        for field in analysis['structure']:
            print(f"  {field['Field']:<30} {field['Type']:<20} {field['Null']:<5} {field['Key']}")
        
        print("\n2. RELATIONS :")
        print("-"*50)
        if analysis['relations']:
            for rel in analysis['relations']:
                print(f"  → {rel['REFERENCED_TABLE_NAME']}.{rel['REFERENCED_COLUMN_NAME']}")
        else:
            print("  Aucune relation directe trouvée")
        
        print("\n3. TABLES CORRESPONDANTES :")
        print("-"*50)
        for table in analysis['correspondences']:
            print(f"  • {table}")
        
        print("\n4. EXEMPLES DE DONNÉES :")
        print("-"*50)
        for example in analysis['examples']:
            print(f"  {example}")
        
        return analysis

# Utilisation
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'votre_mdp',
    'database': 'acore_world'
}

analyzer = TableAnalyzer(config)
analyzer.generate_report('achievement_dbc')
```

---

## 8. RECHERCHE INTERACTIVE

### Script interactif

```python
def interactive_search():
    """Recherche interactive de tables"""
    print("🔍 Système de recherche de tables")
    print("Entrez un nom de table (ou 'quit' pour quitter)")
    print("Exemples : Achievement, Category, Creature, Quest, Spell")
    
    while True:
        search_term = input("\n> ").strip()
        
        if search_term.lower() == 'quit':
            break
        
        if not search_term:
            continue
        
        # Recherche dans la base
        results = search_tables(search_term)
        
        if results:
            print(f"\n📊 Tables trouvées pour '{search_term}':")
            for i, table in enumerate(results, 1):
                print(f"  {i}. {table}")
            
            choice = input("\nSélectionnez un numéro pour analyser (ou Entrée pour continuer) : ")
            if choice.isdigit() and 1 <= int(choice) <= len(results):
                table_name = results[int(choice) - 1]
                analyze_specific_table(table_name)
        else:
            print(f"❌ Aucune table trouvée pour '{search_term}'")

def search_tables(term):
    """Recherche des tables dans la base"""
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT TABLE_NAME
        FROM information_schema.TABLES
        WHERE TABLE_SCHEMA = 'acore_world'
        AND TABLE_NAME LIKE %s
        ORDER BY TABLE_NAME
    """, (f'%{term}%',))
    
    results = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    
    return results

def analyze_specific_table(table_name):
    """Analyse une table spécifique"""
    print(f"\n{'='*70}")
    print(f"ANALYSE DÉTAILLÉE : {table_name}")
    print(f"{'='*70}")
    
    # Structure
    print(f"\n📋 STRUCTURE :")
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"DESCRIBE {table_name}")
    for field in cursor.fetchall():
        print(f"  • {field['Field']} ({field['Type']})")
    
    # Données
    cursor.execute(f"SELECT COUNT(*) as count FROM {table_name}")
    count = cursor.fetchone()['count']
    print(f"\n📊 Nombre d'enregistrements : {count}")
    
    # Exemples
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
    examples = cursor.fetchall()
    print(f"\n🔍 Exemples :")
    for ex in examples:
        print(f"  {ex}")
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    interactive_search()
```

---

## 9. RÉSUMÉ POUR Achievement_Category

### Points clés
1. **Achievement_Category** est un DBC client, pas une table MySQL
2. Elle organise les achievements en catégories
3. Elle a une structure hiérarchique (ParentID)
4. Elle est référencée par Achievement.dbc via CategoryID
5. Dans MySQL, la relation se fait via achievement_dbc.categoryId

### Structure hiérarchique
```
Racine (-1)
├── Statistics (1)
│   ├── Wealth (81)
│   ├── Gear (82)
│   └── Character (83)
├── General (2)
├── Quests (3)
├── Exploration (4)
├── Player vs Player (5)
├── Dungeons & Raids (6)
├── Professions (7)
├── Reputation (8)
├── World Events (9)
├── Feats of Strength (10)
└── Guild (11)
```
