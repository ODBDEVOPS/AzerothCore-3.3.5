Voici un guide d'apprentissage très détaillé avec 20 chapitres précis pour maîtriser la gestion des DBC, MPQ et tables AzerothCore.

---

## GUIDE COMPLET EN 20 CHAPITRES

---

### CHAPITRE 1 : Les bases de World of Warcraft - Architecture des données

**Objectif :** Comprendre comment WoW stocke et organise ses données

**Ce que vous apprenez :**
- La séparation client/serveur dans WoW
- Les 3 types de stockage : MPQ (client), DBC (client), MySQL (serveur)
- Le flux de données : MPQ → DBC → Extraction → MySQL → Serveur

**Contenu détaillé :**
```
CLIENT (votre PC)                    SERVEUR (AzerothCore)
├── Data/                            ├── MySQL Database
│   ├── common.MPQ                   │   ├── acore_world
│   │   ├── CreatureModelData.dbc    │   │   ├── creature_template
│   │   ├── SkillLine.dbc            │   │   ├── skillline
│   │   └── Spell.dbc                │   │   ├── spell_dbc
│   └── patch-3.MPQ                  │   │   └── spell
│       └── CreatureModelData.dbc    │   └── acore_characters
└── Wow.exe                          └── worldserver.exe
```

**Exercice pratique :**
```sql
-- Observer la structure de la base AzerothCore
SHOW DATABASES;
USE acore_world;
SHOW TABLES LIKE '%skill%';
-- Résultat : skillline, skillline_dbc, skill_discovery_template, etc.
```

---

### CHAPITRE 2 : Comprendre le format MPQ en profondeur

**Objectif :** Maîtriser la structure des archives MPQ

**Ce que vous apprenez :**
- Le format Mo'PaQ (Mike O'Brien Pack)
- La table de hachage (hash table)
- La table des blocs (block table)
- Les méthodes de compression (zlib, bzip2, LZMA)
- Le chiffrement des noms de fichiers

**Structure interne d'un MPQ :**
```python
# Représentation simplifiée d'un MPQ
class MPQFile:
    def __init__(self):
        self.header = {
            'magic': 'MPQ\x1A',
            'header_size': 32,
            'archive_size': 1048576,
            'format_version': 1,
            'block_table_size': 100,
            'hash_table_offset': 512,
            'block_table_offset': 1024
        }
        self.hash_table = []  # Liste des fichiers indexés
        self.block_table = []  # Position des données
        self.files = {}  # nom_fichier -> données
```

**Les MPQ de WotLK 3.3.5 dans l'ordre :**
```python
ordre_lecture_mpq = [
    'common.MPQ',           # 1. Données de base
    'common-2.MPQ',         # 2. Suite des données communes
    'expansion.MPQ',        # 3. Données Burning Crusade
    'lichking.MPQ',         # 4. Données WotLK
    'patch.MPQ',            # 5. Premier patch
    'patch-2.MPQ',          # 6. Deuxième patch
    'patch-3.MPQ'           # 7. Dernier patch (priorité maximale)
]
# Règle : le dernier MPQ écrase les données des précédents
```

---

### CHAPITRE 3 : Le format DBC en détail

**Objectif :** Comprendre la structure binaire exacte d'un fichier DBC

**Ce que vous apprenez :**
- L'en-tête DBC (header) de 20 octets
- Les types de données stockés
- L'organisation en lignes et colonnes
- Le calcul des offsets

**Structure binaire d'un DBC :**
```python
# En-tête DBC - exactement 20 octets
class DBCHeader:
    def __init__(self, data):
        self.magic = data[0:4]      # 'WDBC' (4 octets)
        self.record_count = int.from_bytes(data[4:8], 'little')    # Nombre de lignes
        self.field_count = int.from_bytes(data[8:12], 'little')    # Nombre de colonnes
        self.record_size = int.from_bytes(data[12:16], 'little')   # Taille d'une ligne
        self.string_block_size = int.from_bytes(data[16:20], 'little')  # Taille du bloc texte

# Exemple : SkillLine.dbc
# record_count = 150 (150 compétences)
# field_count = 8 (8 colonnes par ligne)
# record_size = 32 (8 champs × 4 octets)
```

**Les types de données :**
```python
types_donnees_dbc = {
    'int32': 'Entier 32 bits - ID, index, valeurs numériques',
    'uint32': 'Entier non signé - IDs positifs',
    'float': 'Nombre décimal - échelles, coordonnées',
    'string': 'Référence vers le bloc de texte',
    'flags': 'Bitmask - options combinables',
    'locstring': 'Chaîne localisée (multi-langues)'
}
```

---

### CHAPITRE 4 : Les outils d'extraction

**Objectif :** Apprendre à utiliser les outils pour extraire les DBC des MPQ

**Ce que vous apprenez :**
- Installation et utilisation de MPQEditor
- Extraction avec StormLib
- Utilisation de libmpq en Python
- Extraction en ligne de commande

**Outils essentiels :**
```python
# 1. MPQEditor (Interface graphique)
# - Ouvrir un MPQ : File > Open
# - Naviguer dans DBFilesClient/
# - Extraire : clic droit > Extract

# 2. Python avec stormlib
import stormlib

# Ouvrir un MPQ
mpq = stormlib.open_archive('common.MPQ')

# Lister les DBC
for file in mpq.files:
    if file.endswith('.dbc'):
        print(f"Trouvé : {file}")

# Extraire un DBC
data = mpq.read_file('DBFilesClient/SkillLine.dbc')
with open('SkillLine.dbc', 'wb') as f:
    f.write(data)

# 3. Extraction en masse
def extraire_tous_les_dbc(mpq_path, output_folder):
    mpq = stormlib.open_archive(mpq_path)
    count = 0
    for file in mpq.files:
        if 'DBFilesClient' in file and file.endswith('.dbc'):
            data = mpq.read_file(file)
            filename = file.split('/')[-1]
            with open(f'{output_folder}/{filename}', 'wb') as f:
                f.write(data)
            count += 1
    print(f"{count} DBC extraits")
```

---

### CHAPITRE 5 : Parser un DBC en Python - Partie 1 (Base)

**Objectif :** Créer un parseur DBC simple

**Ce que vous apprenez :**
- Lire le header
- Extraire les lignes
- Convertir les données binaires en valeurs Python
- Gérer les types de base

**Code complet d'un parseur simple :**
```python
import struct

class DBCParser:
    def __init__(self, filepath):
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.parse_header()
        self.parse_records()
    
    def parse_header(self):
        """Lit les 20 premiers octets"""
        self.magic = self.data[0:4]
        self.record_count = struct.unpack('<I', self.data[4:8])[0]
        self.field_count = struct.unpack('<I', self.data[8:12])[0]
        self.record_size = struct.unpack('<I', self.data[12:16])[0]
        self.string_block_size = struct.unpack('<I', self.data[16:20])[0]
        
        print(f"Magic: {self.magic}")
        print(f"Records: {self.record_count}")
        print(f"Fields: {self.field_count}")
        print(f"Record size: {self.record_size}")
    
    def parse_records(self):
        """Extrait toutes les lignes"""
        self.records = []
        offset = 20  # Après le header
        
        for i in range(self.record_count):
            record_data = self.data[offset:offset + self.record_size]
            
            # Diviser en champs de 4 octets
            fields = []
            for j in range(0, self.record_size, 4):
                field = struct.unpack('<I', record_data[j:j+4])[0]
                fields.append(field)
            
            self.records.append(fields)
            offset += self.record_size
    
    def get_record(self, index):
        """Retourne une ligne spécifique"""
        if 0 <= index < len(self.records):
            return self.records[index]
        return None

# Utilisation
parser = DBCParser('SkillLine.dbc')
print(f"\nPremière ligne : {parser.get_record(0)}")
```

---

### CHAPITRE 6 : Parser un DBC en Python - Partie 2 (Avancé)

**Objectif :** Gérer les types complexes et les chaînes de caractères

**Ce que vous apprenez :**
- Lire les chaînes du bloc de texte
- Gérer les floats
- Gérer les flags
- Créer des objets Python structurés

**Code avancé avec gestion des types :**
```python
import struct
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class DBCField:
    name: str
    type: str  # 'int', 'float', 'string', 'flags'

class AdvancedDBCParser:
    def __init__(self, filepath, schema):
        self.schema = schema  # Liste de DBCField
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.parse()
    
    def parse(self):
        # Header
        self.record_count = struct.unpack('<I', self.data[4:8])[0]
        self.field_count = struct.unpack('<I', self.data[8:12])[0]
        self.record_size = struct.unpack('<I', self.data[12:16])[0]
        self.string_block_size = struct.unpack('<I', self.data[16:20])[0]
        
        # Position du bloc de texte
        self.string_block_offset = 20 + (self.record_count * self.record_size)
        self.string_block = self.data[self.string_block_offset:]
        
        # Parser les records
        self.records = []
        offset = 20
        
        for i in range(self.record_count):
            record = {}
            for j, field in enumerate(self.schema):
                field_offset = offset + (j * 4)
                raw_value = struct.unpack('<I', self.data[field_offset:field_offset+4])[0]
                
                if field.type == 'int':
                    record[field.name] = raw_value
                elif field.type == 'float':
                    record[field.name] = struct.unpack('<f', 
                        self.data[field_offset:field_offset+4])[0]
                elif field.type == 'string':
                    record[field.name] = self.read_string(raw_value)
                elif field.type == 'flags':
                    record[field.name] = self.parse_flags(raw_value)
            
            self.records.append(record)
            offset += self.record_size
    
    def read_string(self, offset):
        """Lit une chaîne depuis le bloc de texte"""
        if offset >= len(self.string_block):
            return ""
        end = self.string_block.find(b'\x00', offset)
        if end == -1:
            return ""
        return self.string_block[offset:end].decode('utf-8', errors='ignore')
    
    def parse_flags(self, value):
        """Convertit un entier en liste de flags"""
        flags = []
        for i in range(32):
            if value & (1 << i):
                flags.append(i)
        return flags

# Schéma pour SkillLine.dbc
skillline_schema = [
    DBCField('ID', 'int'),
    DBCField('CategoryID', 'int'),
    DBCField('SkillCostsID', 'int'),
    DBCField('DisplayName', 'string'),
    DBCField('Description', 'string'),
    DBCField('SpellIconID', 'int'),
    DBCField('AlternateVerb', 'string'),
    DBCField('CanLink', 'flags')
]

parser = AdvancedDBCParser('SkillLine.dbc', skillline_schema)
print(f"Première compétence : {parser.records[0]}")
```

---

### CHAPITRE 7 : Extraire les DBC de plusieurs MPQ

**Objectif :** Lire les DBC depuis tous les MPQ dans le bon ordre

**Ce que vous apprenez :**
- Parcourir tous les MPQ d'un dossier WoW
- Trier les MPQ par priorité
- Extraire le même DBC de plusieurs MPQ
- Fusionner les résultats

**Code complet :**
```python
import os
import stormlib
from pathlib import Path

class MultiMPQExtractor:
    def __init__(self, wow_data_folder):
        self.wow_folder = Path(wow_data_folder)
        self.mpq_files = self.find_mpq_files()
        self.sort_mpq_by_priority()
    
    def find_mpq_files(self):
        """Trouve tous les MPQ dans le dossier"""
        mpq_files = []
        for file in self.wow_folder.glob('*.MPQ'):
            mpq_files.append(str(file))
        return mpq_files
    
    def sort_mpq_by_priority(self):
        """Trie les MPQ : patch > base"""
        priority = {
            'common': 1,
            'common-2': 2,
            'expansion': 3,
            'lichking': 4,
            'patch': 5,
            'patch-2': 6,
            'patch-3': 7
        }
        
        def get_priority(mpq_path):
            name = os.path.basename(mpq_path).lower()
            for key, prio in priority.items():
                if name.startswith(key):
                    return prio
            return 0
        
        self.mpq_files.sort(key=get_priority)
        print("Ordre de lecture des MPQ :")
        for mpq in self.mpq_files:
            print(f"  {os.path.basename(mpq)}")
    
    def extract_dbc_from_all(self, dbc_name):
        """Extrait un DBC de tous les MPQ"""
        versions = []
        
        for mpq_path in self.mpq_files:
            try:
                mpq = stormlib.open_archive(mpq_path)
                file_path = f'DBFilesClient/{dbc_name}'
                
                if mpq.has_file(file_path):
                    data = mpq.read_file(file_path)
                    versions.append({
                        'mpq': os.path.basename(mpq_path),
                        'data': data,
                        'size': len(data)
                    })
                    print(f"Trouvé dans {os.path.basename(mpq_path)} : {len(data)} octets")
            except Exception as e:
                print(f"Erreur avec {mpq_path}: {e}")
        
        return versions

# Utilisation
extractor = MultiMPQExtractor('C:/WoW/Data')
versions = extractor.extract_dbc_from_all('SkillLine.dbc')
print(f"\n{len(versions)} versions trouvées")
```

---

### CHAPITRE 8 : Détecter les doublons et changements

**Objectif :** Identifier les différences entre les versions d'un même DBC

**Ce que vous apprenez :**
- Comparer les versions extraites
- Identifier les doublons identiques
- Détecter les lignes modifiées
- Créer un rapport de changements

**Code de détection :**
```python
class DuplicateDetector:
    def __init__(self):
        self.records_by_id = {}
        self.duplicates = []
        self.changes = []
    
    def add_records(self, records, source):
        """Ajoute des records d'une source"""
        for record in records:
            record_id = record['ID']
            
            if record_id not in self.records_by_id:
                # Nouveau record
                self.records_by_id[record_id] = [{
                    'record': record,
                    'source': source
                }]
            else:
                # Record existant - vérifier si identique
                existing = self.records_by_id[record_id][-1]['record']
                
                if existing == record:
                    # Doublon identique
                    self.duplicates.append({
                        'id': record_id,
                        'source': source,
                        'record': record
                    })
                else:
                    # Changement détecté
                    self.changes.append({
                        'id': record_id,
                        'old': existing,
                        'new': record,
                        'source': source,
                        'differences': self.compare_records(existing, record)
                    })
                
                self.records_by_id[record_id].append({
                    'record': record,
                    'source': source
                })
    
    def compare_records(self, old, new):
        """Compare deux records et retourne les différences"""
        differences = {}
        for key in set(old.keys()) | set(new.keys()):
            if old.get(key) != new.get(key):
                differences[key] = {
                    'old': old.get(key),
                    'new': new.get(key)
                }
        return differences
    
    def get_report(self):
        """Génère un rapport complet"""
        total_ids = len(self.records_by_id)
        total_duplicates = len(self.duplicates)
        total_changes = len(self.changes)
        
        # Compter les records avec plusieurs versions
        records_with_versions = sum(1 for versions in self.records_by_id.values() 
                                   if len(versions) > 1)
        
        return {
            'total_unique_ids': total_ids,
            'total_duplicates': total_duplicates,
            'total_changes': total_changes,
            'records_with_multiple_versions': records_with_versions,
            'duplicates': self.duplicates,
            'changes': self.changes
        }
    
    def print_report(self):
        """Affiche un rapport lisible"""
        report = self.get_report()
        print("="*60)
        print("RAPPORT D'ANALYSE DES DOUBLONS")
        print("="*60)
        print(f"IDs uniques : {report['total_unique_ids']}")
        print(f"Doublons identiques : {report['total_duplicates']}")
        print(f"Changements détectés : {report['total_changes']}")
        print(f"Records avec versions multiples : {report['records_with_multiple_versions']}")
        
        if report['changes']:
            print("\nChangements détaillés :")
            for change in report['changes'][:5]:  # Afficher les 5 premiers
                print(f"\n  ID {change['id']} :")
                for field, diff in change['differences'].items():
                    print(f"    {field}: {diff['old']} → {diff['new']}")
```

---

### CHAPITRE 9 : Stratégies de résolution des doublons

**Objectif :** Choisir la meilleure stratégie pour vos besoins

**Ce que vous apprenez :**
- Les 5 stratégies principales
- Quand utiliser chaque stratégie
- Implémenter chaque stratégie
- Combiner les stratégies

**Les stratégies :**
```python
class ResolutionStrategies:
    @staticmethod
    def last_wins(versions):
        """Stratégie 1 : La dernière version gagne"""
        return versions[-1] if versions else None
    
    @staticmethod
    def first_wins(versions):
        """Stratégie 2 : La première version gagne (données de base)"""
        return versions[0] if versions else None
    
    @staticmethod
    def merge_fields(versions):
        """Stratégie 3 : Fusionner les champs (prendre les non-nuls)"""
        if not versions:
            return None
        
        merged = {}
        for version in versions:
            for key, value in version.items():
                if value is not None and value != "":
                    merged[key] = value
        return merged
    
    @staticmethod
    def priority_based(versions, priorities):
        """Stratégie 4 : Basée sur la priorité des sources"""
        if not versions:
            return None
        
        best_version = versions[0]
        best_priority = -1
        
        for version in versions:
            source = version.get('_source', '')
            priority = priorities.get(source, 0)
            if priority > best_priority:
                best_priority = priority
                best_version = version
        
        return best_version
    
    @staticmethod
    def manual_review(versions):
        """Stratégie 5 : Revue manuelle des conflits"""
        conflicts = []
        for i, version in enumerate(versions):
            print(f"Version {i+1}: {version}")
        
        choice = input("Choisissez la version (1-N) ou 'f' pour fusionner : ")
        if choice.lower() == 'f':
            return ResolutionStrategies.merge_fields(versions)
        else:
            return versions[int(choice) - 1]

# Exemple d'utilisation
priorities = {
    'common.MPQ': 1,
    'expansion.MPQ': 2,
    'lichking.MPQ': 3,
    'patch.MPQ': 4,
    'patch-2.MPQ': 5,
    'patch-3.MPQ': 6
}
```

---

### CHAPITRE 10 : Créer un système de versionnage

**Objectif :** Suivre l'historique complet des modifications

**Ce que vous apprenez :**
- Créer un système de versionnage
- Enregistrer l'historique
- Restaurer des versions antérieures
- Analyser l'évolution des données

**Code complet :**
```python
import hashlib
import json
from datetime import datetime

class DBCVersionControl:
    def __init__(self):
        self.versions = {}  # id -> liste de versions
        self.current = {}   # id -> version actuelle
        self.history_log = []
    
    def add_version(self, record, source, timestamp=None):
        """Ajoute une nouvelle version d'un record"""
        record_id = record['ID']
        
        if timestamp is None:
            timestamp = datetime.now()
        
        # Calculer un hash pour identifier la version
        record_hash = self.hash_record(record)
        
        version = {
            'record': record.copy(),
            'source': source,
            'timestamp': timestamp,
            'hash': record_hash,
            'version_number': len(self.versions.get(record_id, [])) + 1
        }
        
        # Ajouter à l'historique
        if record_id not in self.versions:
            self.versions[record_id] = []
        self.versions[record_id].append(version)
        
        # Mettre à jour la version actuelle
        self.current[record_id] = record.copy()
        
        # Journaliser
        self.history_log.append({
            'action': 'add',
            'id': record_id,
            'source': source,
            'timestamp': timestamp,
            'hash': record_hash
        })
        
        return version['version_number']
    
    def hash_record(self, record):
        """Crée un hash unique pour un record"""
        record_str = json.dumps(record, sort_keys=True)
        return hashlib.md5(record_str.encode()).hexdigest()
    
    def get_version(self, record_id, version_number):
        """Récupère une version spécifique"""
        if record_id in self.versions:
            for version in self.versions[record_id]:
                if version['version_number'] == version_number:
                    return version['record']
        return None
    
    def get_history(self, record_id):
        """Retourne l'historique complet d'un record"""
        return self.versions.get(record_id, [])
    
    def rollback(self, record_id, version_number):
        """Revient à une version antérieure"""
        old_record = self.get_version(record_id, version_number)
        if old_record:
            self.current[record_id] = old_record.copy()
            return True
        return False
    
    def get_changes_over_time(self, record_id):
        """Analyse l'évolution d'un record"""
        history = self.get_history(record_id)
        changes = []
        
        for i in range(1, len(history)):
            old = history[i-1]['record']
            new = history[i]['record']
            
            differences = {}
            for key in set(old.keys()) | set(new.keys()):
                if old.get(key) != new.get(key):
                    differences[key] = {
                        'from': old.get(key),
                        'to': new.get(key),
                        'at': history[i]['timestamp']
                    }
            
            if differences:
                changes.append({
                    'version': i,
                    'changes': differences
                })
        
        return changes
```

---

### CHAPITRE 11 : Structure de la base de données AzerothCore

**Objectif :** Comprendre l'organisation des tables dans acore_world

**Ce que vous apprenez :**
- Les catégories de tables
- La convention de nommage
- Les relations entre tables
- Le rôle des tables _dbc

**Catégories de tables :**
```sql
-- Tables de gameplay (modifiables)
SELECT TABLE_NAME FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'acore_world' 
AND TABLE_NAME NOT LIKE '%_dbc' 
AND TABLE_NAME NOT LIKE '%_template%'
LIMIT 20;

-- Tables template (modèles)
-- creature_template, gameobject_template, item_template
SELECT TABLE_NAME FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'acore_world' 
AND TABLE_NAME LIKE '%_template'
LIMIT 20;

-- Tables DBC (données client brutes)
SELECT TABLE_NAME FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'acore_world' 
AND TABLE_NAME LIKE '%_dbc'
LIMIT 20;

-- Compter les tables par type
SELECT 
    SUM(CASE WHEN TABLE_NAME LIKE '%_dbc' THEN 1 ELSE 0 END) as tables_dbc,
    SUM(CASE WHEN TABLE_NAME LIKE '%_template' THEN 1 ELSE 0 END) as tables_template,
    SUM(CASE WHEN TABLE_NAME NOT LIKE '%_dbc' AND TABLE_NAME NOT LIKE '%_template' 
        THEN 1 ELSE 0 END) as tables_autres
FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'acore_world';
```

---

### CHAPITRE 12 : Comprendre les tables jumelles (_dbc vs serveur)

**Objectif :** Maîtriser la différence entre skillline et skillline_dbc

**Ce que vous apprenez :**
- Pourquoi il y a deux tables pour la même donnée
- Le flux de synchronisation
- Quand utiliser l'une ou l'autre
- Les risques de modification

**Analyse détaillée :**
```sql
-- Comparer les structures
DESCRIBE skillline;
DESCRIBE skillline_dbc;

-- Différences typiques
-- skillline : peut avoir des colonnes modifiées
-- skillline_dbc : reflète exactement le fichier DBC

-- Exemple de comparaison
SELECT 
    s.ID,
    s.DisplayName as serveur_name,
    d.DisplayName as dbc_name,
    CASE 
        WHEN s.DisplayName = d.DisplayName THEN 'IDENTIQUE'
        ELSE 'DIFFERENT'
    END as statut
FROM skillline s
LEFT JOIN skillline_dbc d ON s.ID = d.ID
WHERE s.DisplayName != d.DisplayName OR d.DisplayName IS NULL;

-- Tables jumelles courantes
SELECT TABLE_NAME 
FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'acore_world' 
AND TABLE_NAME LIKE '%\_dbc'
AND SUBSTRING_INDEX(TABLE_NAME, '_dbc', 1) IN (
    SELECT TABLE_NAME 
    FROM information_schema.TABLES 
    WHERE TABLE_SCHEMA = 'acore_world'
);
```

---

### CHAPITRE 13 : Comparer et synchroniser les tables

**Objectif :** Créer un système de synchronisation entre tables jumelles

**Ce que vous apprenez :**
- Comparer les données entre tables
- Identifier les divergences
- Synchroniser dans les deux sens
- Sauvegarder avant modification

**Code SQL de synchronisation :**
```sql
-- 1. Sauvegarde de sécurité
CREATE TABLE skillline_backup AS SELECT * FROM skillline;

-- 2. Trouver les différences
CREATE TEMPORARY TABLE differences AS
SELECT 
    COALESCE(s.ID, d.ID) as ID,
    s.ID as serveur_id,
    d.ID as dbc_id,
    s.DisplayName as serveur_name,
    d.DisplayName as dbc_name
FROM skillline s
LEFT JOIN skillline_dbc d ON s.ID = d.ID
WHERE s.ID IS NULL OR d.ID IS NULL OR s.DisplayName != d.DisplayName;

-- 3. Synchroniser serveur → dbc
UPDATE skillline_dbc d
INNER JOIN skillline s ON d.ID = s.ID
SET 
    d.DisplayName = s.DisplayName,
    d.Description = s.Description,
    d.SpellIconID = s.SpellIconID;

-- 4. Synchroniser dbc → serveur
UPDATE skillline s
INNER JOIN skillline_dbc d ON s.ID = d.ID
SET 
    s.DisplayName = d.DisplayName,
    s.Description = d.Description,
    s.SpellIconID = d.SpellIconID;

-- 5. Insérer les manquants
INSERT INTO skillline (ID, DisplayName, Description)
SELECT d.ID, d.DisplayName, d.Description
FROM skillline_dbc d
LEFT JOIN skillline s ON d.ID = s.ID
WHERE s.ID IS NULL;
```

---

### CHAPITRE 14 : Créer un outil d'analyse complet en Python

**Objectif :** Combiner tout ce qu'on a appris dans un outil unique

**Ce que vous apprenez :**
- Architecture d'un outil complet
- Gestion des erreurs
- Journalisation
- Export de rapports

**Code complet :**
```python
import os
import json
import logging
from datetime import datetime
import mysql.connector
import stormlib

class WoWDataAnalyzer:
    def __init__(self, wow_folder, db_config):
        self.wow_folder = wow_folder
        self.db_config = db_config
        self.setup_logging()
        self.results = {}
    
    def setup_logging(self):
        """Configure la journalisation"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('wow_analyzer.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def analyze_dbc_from_mpq(self, dbc_name):
        """Analyse un DBC depuis tous les MPQ"""
        self.logger.info(f"Analyse de {dbc_name} depuis les MPQ...")
        
        mpq_files = self.find_mpq_files()
        versions = []
        
        for mpq_path in mpq_files:
            try:
                mpq = stormlib.open_archive(mpq_path)
                file_path = f'DBFilesClient/{dbc_name}'
                
                if mpq.has_file(file_path):
                    data = mpq.read_file(file_path)
                    versions.append({
                        'source': os.path.basename(mpq_path),
                        'data': data
                    })
                    self.logger.info(f"  Trouvé dans {os.path.basename(mpq_path)}")
            except Exception as e:
                self.logger.error(f"  Erreur avec {mpq_path}: {e}")
        
        return versions
    
    def analyze_database_tables(self, table_name):
        """Analyse une table dans la base de données"""
        self.logger.info(f"Analyse de la table {table_name}...")
        
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Table normale
        cursor.execute(f"SELECT COUNT(*) as count FROM {table_name}")
        normal_count = cursor.fetchone()['count']
        
        # Table _dbc
        dbc_table = f"{table_name}_dbc"
        cursor.execute(f"SELECT COUNT(*) as count FROM {dbc_table}")
        dbc_count = cursor.fetchone()['count']
        
        cursor.close()
        conn.close()
        
        return {
            'normal_table': {'name': table_name, 'count': normal_count},
            'dbc_table': {'name': dbc_table, 'count': dbc_count}
        }
    
    def generate_report(self):
        """Génère un rapport complet"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'results': self.results
        }
        
        with open('analysis_report.json', 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        self.logger.info("Rapport généré : analysis_report.json")
        return report

# Utilisation
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'votre_mdp',
    'database': 'acore_world'
}

analyzer = WoWDataAnalyzer('C:/WoW/Data', config)
analyzer.results['skillline'] = analyzer.analyze_database_tables('skillline')
analyzer.generate_report()
```

---

### CHAPITRE 15 : Gérer les gros volumes de données

**Objectif :** Optimiser pour des millions d'enregistrements

**Ce que vous apprenez :**
- Traitement par lots (batch)
- Mémoire efficace
- Indexation
- Parallélisation

**Code optimisé :**
```python
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

class BatchProcessor:
    def __init__(self, batch_size=1000):
        self.batch_size = batch_size
    
    def process_in_batches(self, records, process_func):
        """Traite les records par lots"""
        results = []
        
        for i in range(0, len(records), self.batch_size):
            batch = records[i:i + self.batch_size]
            batch_results = process_func(batch)
            results.extend(batch_results)
            
            print(f"Traité : {i + len(batch)}/{len(records)}")
        
        return results
    
    def parallel_process(self, records, process_func, max_workers=4):
        """Traite les records en parallèle"""
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            
            for i in range(0, len(records), self.batch_size):
                batch = records[i:i + self.batch_size]
                future = executor.submit(process_func, batch)
                futures.append(future)
            
            results = []
            for future in futures:
                results.extend(future.result())
            
            return results

# Utilisation
def process_batch(batch):
    """Fonction de traitement d'un lot"""
    results = []
    for record in batch:
        # Traitement ici
        results.append(record)
    return results

processor = BatchProcessor(batch_size=500)
results = processor.parallel_process(all_records, process_batch)
```

---

### CHAPITRE 16 : Créer une base de données propre et optimisée

**Objectif :** Fusionner les données DBC et serveur dans une nouvelle structure

**Ce que vous apprenez :**
- Concevoir un schéma de base de données
- Créer des tables optimisées
- Indexer correctement
- Gérer les relations

**Code SQL :**
```sql
-- Créer une base de données propre
CREATE DATABASE IF NOT EXISTS wow_data_clean;
USE wow_data_clean;

-- Table unifiée pour les compétences
CREATE TABLE skillline_unified (
    ID INT PRIMARY KEY,
    CategoryID INT,
    SkillCostID INT,
    DisplayName VARCHAR(255),
    Description TEXT,
    SpellIconID INT,
    AlternateVerb VARCHAR(255),
    CanLink INT,
    source VARCHAR(50),
    version INT DEFAULT 1,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_category (CategoryID),
    INDEX idx_name (DisplayName)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table d'historique
CREATE TABLE skillline_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_id INT,
    field_name VARCHAR(50),
    old_value TEXT,
    new_value TEXT,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_by VARCHAR(50),
    FOREIGN KEY (skill_id) REFERENCES skillline_unified(ID),
    INDEX idx_skill (skill_id),
    INDEX idx_changed_at (changed_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

---

### CHAPITRE 17 : Interface en ligne de commande (CLI)

**Objectif :** Créer un outil utilisable en ligne de commande

**Ce que vous apprenez :**
- Créer des commandes CLI
- Gérer les arguments
- Interface interactive
- Affichage formaté

**Code complet :**
```python
import argparse
import sys
from rich.console import Console
from rich.table import Table

console = Console()

def main():
    parser = argparse.ArgumentParser(description='Analyseur de données WoW')
    subparsers = parser.add_subparsers(dest='command')
    
    # Commande analyze
    analyze_parser = subparsers.add_parser('analyze', help='Analyser un DBC')
    analyze_parser.add_argument('dbc_name', help='Nom du DBC à analyser')
    analyze_parser.add_argument('--mpq-folder', required=True, help='Dossier des MPQ')
    
    # Commande compare
    compare_parser = subparsers.add_parser('compare', help='Comparer deux tables')
    compare_parser.add_argument('table_name', help='Nom de la table')
    
    # Commande report
    report_parser = subparsers.add_parser('report', help='Générer un rapport')
    report_parser.add_argument('--output', default='report.json', help='Fichier de sortie')
    
    args = parser.parse_args()
    
    if args.command == 'analyze':
        analyze_dbc(args.dbc_name, args.mpq_folder)
    elif args.command == 'compare':
        compare_tables(args.table_name)
    elif args.command == 'report':
        generate_report(args.output)

def analyze_dbc(dbc_name, mpq_folder):
    """Analyse un DBC et affiche les résultats"""
    console.print(f"[bold green]Analyse de {dbc_name}[/bold green]")
    
    table = Table(title=f"Résultats pour {dbc_name}")
    table.add_column("MPQ Source", style="cyan")
    table.add_column("Taille", justify="right")
    table.add_column("Records", justify="right")
    
    # Analyse ici...
    table.add_row("common.MPQ", "1.2 MB", "150")
    table.add_row("patch.MPQ", "1.3 MB", "155")
    
    console.print(table)

if __name__ == '__main__':
    main()
```

---

### CHAPITRE 18 : Interface graphique simple avec Tkinter

**Objectif :** Créer une application avec interface graphique

**Ce que vous apprenez :**
- Créer une fenêtre
- Ajouter des boutons et listes
- Gérer les événements
- Afficher les résultats

**Code complet :**
```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class WoWDataManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WoW Data Manager")
        self.geometry("800x600")
        
        self.setup_ui()
    
    def setup_ui(self):
        # Menu
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Ouvrir MPQ...", command=self.open_mpq)
        file_menu.add_command(label="Ouvrir DBC...", command=self.open_dbc)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit)
        
        # Panneau principal
        main_panel = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        main_panel.pack(fill=tk.BOTH, expand=True)
        
        # Liste des fichiers
        left_frame = ttk.Frame(main_panel)
        main_panel.add(left_frame, weight=1)
        
        self.file_list = tk.Listbox(left_frame)
        self.file_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Zone de détails
        right_frame = ttk.Frame(main_panel)
        main_panel.add(right_frame, weight=2)
        
        self.detail_text = tk.Text(right_frame, wrap=tk.WORD)
        self.detail_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Barre de statut
        self.status_bar = ttk.Label(self, text="Prêt", relief=tk.SUNKEN)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    
    def open_mpq(self):
        """Ouvre un fichier MPQ"""
        filename = filedialog.askopenfilename(
            title="Sélectionner un MPQ",
            filetypes=[("MPQ files", "*.MPQ"), ("All files", "*.*")]
        )
        
        if filename:
            self.status_bar.config(text=f"Ouverture de {filename}...")
            # Charger le MPQ ici
            messagebox.showinfo("Succès", f"MPQ ouvert : {filename}")
    
    def open_dbc(self):
        """Ouvre un fichier DBC"""
        filename = filedialog.askopenfilename(
            title="Sélectionner un DBC",
            filetypes=[("DBC files", "*.dbc"), ("All files", "*.*")]
        )
        
        if filename:
            self.status_bar.config(text=f"Chargement de {filename}...")
            # Charger le DBC ici

if __name__ == '__main__':
    app = WoWDataManager()
    app.mainloop()
```

---

### CHAPITRE 19 : Tests et validation

**Objectif :** Garantir la fiabilité de votre outil

**Ce que vous apprenez :**
- Écrire des tests unitaires
- Valider les données
- Gérer les erreurs
- Déboguer

**Code de tests :**
```python
import unittest
import tempfile
import os

class TestDBCParser(unittest.TestCase):
    def setUp(self):
        """Préparation des tests"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_dbc = self.create_test_dbc()
    
    def create_test_dbc(self):
        """Crée un DBC de test"""
        import struct
        
        # Header
        record_count = 2
        field_count = 3
        record_size = 12
        string_block_size = 20
        
        header = struct.pack('<4sIIII',
            b'WDBC',
            record_count,
            field_count,
            record_size,
            string_block_size
        )
        
        # Records
        records = b''
        for i in range(record_count):
            record = struct.pack('<III', i, i*10, i*100)
            records += record
        
        # String block
        strings = b'Test String\x00Another\x00'
        
        return header + records + strings
    
    def test_parse_header(self):
        """Teste le parsing du header"""
        parser = DBCParser(self.test_dbc)
        self.assertEqual(parser.record_count, 2)
        self.assertEqual(parser.field_count, 3)
        self.assertEqual(parser.record_size, 12)
    
    def test_parse_records(self):
        """Teste le parsing des records"""
        parser = DBCParser(self.test_dbc)
        self.assertEqual(len(parser.records), 2)
        self.assertEqual(parser.records[0], [0, 0, 0])
        self.assertEqual(parser.records[1], [1, 10, 100])
    
    def test_invalid_file(self):
        """Teste la gestion des fichiers invalides"""
        with self.assertRaises(Exception):
            DBCParser("fichier_inexistant.dbc")

if __name__ == '__main__':
    unittest.main()
```

---

### CHAPITRE 20 : Projet final - Outil complet intégré

**Objectif :** Combiner tout en un outil professionnel

**Ce que vous apprenez :**
- Architecture complète
- Intégration de toutes les fonctionnalités
- Documentation
- Distribution

**Structure du projet final :**
```
wow_data_manager/
├── README.md
├── requirements.txt
├── setup.py
├── wow_manager/
│   ├── __init__.py
│   ├── main.py
│   ├── parsers/
│   │   ├── __init__.py
│   │   ├── dbc_parser.py
│   │   └── mpq_parser.py
│   ├── analyzers/
│   │   ├── __init__.py
│   │   ├── duplicate_detector.py
│   │   └── change_tracker.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connector.py
│   │   └── sync_manager.py
│   ├── gui/
│   │   ├── __init__.py
│   │   └── main_window.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── config.py
└── tests/
    ├── __init__.py
    ├── test_dbc_parser.py
    └── test_duplicate_detector.py
```

**Code principal (main.py) :**
```python
#!/usr/bin/env python3
"""
WoW Data Manager - Outil complet de gestion des données WoW
"""

import argparse
import sys
from pathlib import Path

from wow_manager.parsers import DBCParser, MPQParser
from wow_manager.analyzers import DuplicateDetector, ChangeTracker
from wow_manager.database import DatabaseConnector, SyncManager
from wow_manager.utils import setup_logger

def main():
    """Point d'entrée principal"""
    parser = argparse.ArgumentParser(
        description='WoW Data Manager - Gestion complète des données',
        epilog='Exemple: wow_manager analyze SkillLine.dbc --folder C:/WoW/Data'
    )
    
    # Sous-commandes
    subparsers = parser.add_subparsers(dest='command', help='Commandes disponibles')
    
    # Commande analyze
    analyze = subparsers.add_parser('analyze', help='Analyser un DBC')
    analyze.add_argument('dbc_name', help='Nom du DBC')
    analyze.add_argument('--folder', required=True, help='Dossier WoW Data')
    analyze.add_argument('--output', help='Fichier de sortie')
    
    # Commande sync
    sync = subparsers.add_parser('sync', help='Synchroniser les tables')
    sync.add_argument('table', help='Nom de la table')
    sync.add_argument('--direction', choices=['to_dbc', 'to_server', 'both'],
                     default='both', help='Direction de synchronisation')
    
    # Commande report
    report = subparsers.add_parser('report', help='Générer un rapport')
    report.add_argument('--format', choices=['json', 'html', 'pdf'],
                       default='json', help='Format du rapport')
    
    args = parser.parse_args()
    
    # Logger
    logger = setup_logger('wow_manager')
    
    try:
        if args.command == 'analyze':
            logger.info(f"Analyse de {args.dbc_name}")
            # Logique d'analyse ici
            
        elif args.command == 'sync':
            logger.info(f"Synchronisation de {args.table}")
            # Logique de synchronisation ici
            
        elif args.command == 'report':
            logger.info("Génération du rapport")
            # Logique de rapport ici
            
        else:
            parser.print_help()
            
    except Exception as e:
        logger.error(f"Erreur : {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```

---

## RÉSUMÉ DU PARCOURS D'APPRENTISSAGE

| Chapitre | Compétence acquise | Niveau |
|----------|-------------------|---------|
| 1-4 | Comprendre les formats | Débutant |
| 5-7 | Parser les données | Intermédiaire |
| 8-10 | Gérer les doublons | Avancé |
| 11-13 | Travailler avec MySQL | Intermédiaire |
| 14-18 | Créer des outils | Avancé |
| 19-20 | Professionnaliser | Expert |

Ce parcours vous amène de débutant complet à capable de créer un outil professionnel de gestion des données WoW !
