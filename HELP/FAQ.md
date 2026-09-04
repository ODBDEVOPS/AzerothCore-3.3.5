Je vais tout expliquer simplement, étape par étape, comme si vous découvriez complètement le sujet.

## C'est quoi un DBC/DBFilesClient ?

Un DBC (DataBase Client) est un fichier qui contient des données de jeu World of Warcraft sous forme de tableau.

**Exemple concret :** Imaginez un fichier `CreatureModelData.dbc` qui contient les modèles 3D des créatures :

```
ID | ModelName        | Scale | MountHeight
---|------------------|-------|------------
1  | Wolf.m2          | 1.0   | 0.5
2  | Bear.m2          | 1.2   | 0.8
3  | Dragon.m2        | 2.5   | 1.5
```

Chaque ligne = un enregistrement (record)
Chaque colonne = un champ (field)
L'ID = identifiant unique (comme un numéro de sécurité sociale)

## Le problème que vous rencontrez

Les fichiers DBC sont stockés dans des MPQ (sortes de "boîtes" qui contiennent les fichiers du jeu). Le jeu a plusieurs MPQ :

```
wow-update-base-3.3.5.MPQ   (jeu de base)
wow-update-3.3.5.12345.MPQ  (patch 1)
wow-update-3.3.5.67890.MPQ  (patch 2)
```

**Problème :** Le même DBC peut exister dans plusieurs MPQ avec des différences !

Exemple concret :
- Dans le MPQ de base : `CreatureModelData.dbc` a Wolf avec Scale = 1.0
- Dans le patch 1 : `CreatureModelData.dbc` a Wolf avec Scale = 1.5 (modifié)
- Dans le patch 2 : `CreatureModelData.dbc` a Wolf avec Scale = 1.3 (re-modifié)

Quand vous lisez tous les MPQ, vous trouvez 3 versions de la ligne "Wolf" avec des valeurs différentes. C'est ça les "doublons" et "changements".

## Solutions expliquées simplement

### Solution 1 : Garder la dernière version (la plus simple)

```python
# Imaginez que vous avez 3 listes (une pour chaque MPQ)
mpq_base = [
    {'id': 1, 'name': 'Wolf', 'scale': 1.0},
    {'id': 2, 'name': 'Bear', 'scale': 1.2}
]

mpq_patch1 = [
    {'id': 1, 'name': 'Wolf', 'scale': 1.5}  # Wolf modifié
]

mpq_patch2 = [
    {'id': 1, 'name': 'Wolf', 'scale': 1.3}  # Wolf re-modifié
]

# On crée un dictionnaire pour stocker la version finale
final_data = {}

# On lit dans l'ordre (base d'abord, puis patchs)
for record in mpq_base + mpq_patch1 + mpq_patch2:
    # L'ID est la clé, le record écrase l'ancien
    final_data[record['id']] = record

# Résultat : Wolf aura scale = 1.3 (dernière version)
print(final_data)
# {1: {'id': 1, 'name': 'Wolf', 'scale': 1.3}, 
#  2: {'id': 2, 'name': 'Bear', 'scale': 1.2}}
```

**Explication simple :** C'est comme si vous aviez un classeur. Chaque fois que vous trouvez une nouvelle version d'une fiche, vous remplacez l'ancienne par la nouvelle.

### Solution 2 : Suivre les changements (pour comprendre ce qui a changé)

```python
# On garde l'historique
history = {}
final_data = {}

def add_record(record, source):
    record_id = record['id']
    
    if record_id in final_data:
        # Ce record existe déjà, on a un doublon !
        print(f"Doublon trouvé pour ID {record_id}")
        print(f"  Ancien: {final_data[record_id]}")
        print(f"  Nouveau: {record}")
        
        # On sauvegarde l'historique
        if record_id not in history:
            history[record_id] = []
        history[record_id].append({
            'ancien': final_data[record_id].copy(),
            'nouveau': record.copy(),
            'source': source
        })
    
    # On met à jour avec la nouvelle version
    final_data[record_id] = record

# Test
add_record({'id': 1, 'name': 'Wolf', 'scale': 1.0}, 'MPQ Base')
add_record({'id': 1, 'name': 'Wolf', 'scale': 1.5}, 'Patch 1')
add_record({'id': 1, 'name': 'Wolf', 'scale': 1.3}, 'Patch 2')

print("\nDonnées finales :")
for id, record in final_data.items():
    print(f"  ID {id}: {record}")

print("\nHistorique des changements :")
for id, changes in history.items():
    print(f"  ID {id}:")
    for change in changes:
        print(f"    Changé de {change['ancien']['scale']} à {change['nouveau']['scale']} ({change['source']})")
```

### Solution 3 : Détecter les vrais doublons (copies identiques)

```python
def analyze_records(all_records):
    """Analyse les records pour trouver les doublons"""
    
    # Grouper par ID
    by_id = {}
    for record in all_records:
        record_id = record['id']
        if record_id not in by_id:
            by_id[record_id] = []
        by_id[record_id].append(record)
    
    # Analyser chaque groupe
    results = {
        'uniques': [],      # Records qui n'apparaissent qu'une fois
        'doublons': [],     # Records identiques qui apparaissent plusieurs fois
        'modifiés': []      # Records qui ont changé
    }
    
    for record_id, versions in by_id.items():
        if len(versions) == 1:
            # Un seul exemplaire
            results['uniques'].append(versions[0])
        elif all(v == versions[0] for v in versions):
            # Tous identiques
            results['doublons'].append({
                'id': record_id,
                'record': versions[0],
                'nombre_copies': len(versions)
            })
        else:
            # Différentes versions
            results['modifiés'].append({
                'id': record_id,
                'versions': versions,
                'nombre_versions': len(versions)
            })
    
    return results

# Test
all_records = [
    {'id': 1, 'name': 'Wolf', 'scale': 1.0},
    {'id': 1, 'name': 'Wolf', 'scale': 1.0},  # Copie identique
    {'id': 1, 'name': 'Wolf', 'scale': 1.5},  # Version modifiée
    {'id': 2, 'name': 'Bear', 'scale': 1.2},  # Unique
    {'id': 3, 'name': 'Cat', 'scale': 0.8},
    {'id': 3, 'name': 'Cat', 'scale': 0.8}    # Doublon identique
]

resultats = analyze_records(all_records)

print("Uniques :")
for record in resultats['uniques']:
    print(f"  {record}")

print("\nDoublons identiques :")
for item in resultats['doublons']:
    print(f"  ID {item['id']}: {item['nombre_copies']} copies identiques")

print("\nModifiés :")
for item in resultats['modifiés']:
    print(f"  ID {item['id']}: {item['nombre_versions']} versions différentes")
    for i, version in enumerate(item['versions'], 1):
        print(f"    Version {i}: {version}")
```

## Solution complète simple pour débutant

```python
class SimpleDBCLoader:
    """
    Un chargeur simple qui :
    1. Lit tous les MPQ dans le bon ordre
    2. Garde la dernière version de chaque ligne
    3. Vous dit ce qui a changé
    """
    
    def __init__(self):
        self.data = {}  # Stockage final
        self.changements = []  # Liste des changements détectés
    
    def charger_mpq(self, nom_mpq, records):
        """Charge les records d'un MPQ"""
        print(f"\nChargement de {nom_mpq}...")
        
        for record in records:
            record_id = record['id']
            
            if record_id in self.data:
                # Ce record existe déjà
                if self.data[record_id] != record:
                    # Il a changé
                    self.changements.append({
                        'id': record_id,
                        'ancien': self.data[record_id].copy(),
                        'nouveau': record.copy(),
                        'source': nom_mpq
                    })
                    print(f"  ID {record_id} modifié !")
                else:
                    print(f"  ID {record_id} est un doublon identique")
            else:
                print(f"  ID {record_id} est nouveau")
            
            # Mettre à jour avec la dernière version
            self.data[record_id] = record
    
    def obtenir_donnees_finales(self):
        """Retourne les données uniques finales"""
        return list(self.data.values())
    
    def obtenir_resume(self):
        """Retourne un résumé simple"""
        return {
            'total_records': len(self.data),
            'nombre_changements': len(self.changements),
            'changements': self.changements
        }

# Utilisation
loader = SimpleDBCLoader()

# Simuler la lecture des MPQ dans l'ordre
loader.charger_mpq("MPQ Base", [
    {'id': 1, 'name': 'Wolf', 'scale': 1.0},
    {'id': 2, 'name': 'Bear', 'scale': 1.2},
    {'id': 3, 'name': 'Cat', 'scale': 0.8}
])

loader.charger_mpq("Patch 1", [
    {'id': 1, 'name': 'Wolf', 'scale': 1.5},  # Modifié
    {'id': 4, 'name': 'Dog', 'scale': 0.9}    # Nouveau
])

loader.charger_mpq("Patch 2", [
    {'id': 1, 'name': 'Wolf', 'scale': 1.3},  # Re-modifié
    {'id': 2, 'name': 'Bear', 'scale': 1.2}   # Identique (doublon)
])

# Obtenir les résultats
print("\n" + "="*50)
print("RÉSUMÉ FINAL")
print("="*50)

resume = loader.obtenir_resume()
print(f"Total records uniques : {resume['total_records']}")
print(f"Changements détectés : {resume['nombre_changements']}")

print("\nDonnées finales :")
for record in loader.obtenir_donnees_finales():
    print(f"  ID {record['id']}: {record['name']} (scale: {record['scale']})")
```

## En résumé très simple :

1. **Un DBC** = Un tableau avec des lignes et des colonnes
2. **Un MPQ** = Une boîte qui contient des DBC

Je vais vous expliquer la différence entre les tables `skillline` et `skillline_dbc` dans AzerothCore, et comment gérer leurs données.

## La différence entre les deux tables

Dans AzerothCore, il y a souvent **deux versions de la même donnée** :

### 1. `skillline_dbc` - Les données originales du jeu
```sql
-- Cette table contient les données EXACTES des fichiers DBC
-- C'est une copie directe de SkillLine.dbc
SELECT * FROM skillline_dbc LIMIT 5;
```
- **Source** : Extraite directement des fichiers DBC du client WoW
- **Contenu** : Données brutes, non modifiées
- **Usage** : Référence, ne doit PAS être modifiée
- **Colonnes** : Souvent avec des noms techniques (ID, CategoryID, SkillCostsID, etc.)

### 2. `skillline` - Les données modifiées par le serveur
```sql
-- Cette table est utilisée par le serveur, peut être modifiée
SELECT * FROM skillline LIMIT 5;
```
- **Source** : Basée sur les DBC mais peut être modifiée
- **Contenu** : Données potentiellement modifiées pour le serveur
- **Usage** : Utilisée activement par le serveur
- **Colonnes** : Peut avoir des noms plus lisibles ou des colonnes supplémentaires

## Comment voir les différences

### Comparer les deux tables
```sql
-- Vérifier si les tables sont identiques
SELECT 
    (SELECT COUNT(*) FROM skillline) as count_skillline,
    (SELECT COUNT(*) FROM skillline_dbc) as count_skillline_dbc;

-- Trouver les différences
SELECT 'Dans skillline mais pas dans skillline_dbc' as type, ID, DisplayName
FROM skillline
WHERE ID NOT IN (SELECT ID FROM skillline_dbc)

UNION ALL

SELECT 'Dans skillline_dbc mais pas dans skillline' as type, ID, DisplayName
FROM skillline_dbc
WHERE ID NOT IN (SELECT ID FROM skillline);
```

### Structure typique des tables

```sql
-- Structure de skillline_dbc (données DBC brutes)
DESCRIBE skillline_dbc;
-- ID, CategoryID, SkillCostsID, DisplayName, Description, 
-- SpellIconID, AlternateVerb, CanLink

-- Structure de skillline (données serveur)
DESCRIBE skillline;
-- ID, CategoryID, SkillCostID, DisplayName, Description, 
-- SpellIconID, AlternateVerb, CanLink
-- (peut avoir des colonnes supplémentaires ou noms différents)
```

## Solution pour fusionner/dédoublonner

### 1. Créer une vue unifiée
```sql
-- Créer une vue qui combine les deux tables
CREATE OR REPLACE VIEW skillline_unified AS
SELECT 
    ID,
    CategoryID,
    SkillCostID,
    DisplayName,
    Description,
    SpellIconID,
    AlternateVerb,
    CanLink,
    'dbc' as source
FROM skillline_dbc
UNION
SELECT 
    ID,
    CategoryID,
    SkillCostID,
    DisplayName,
    Description,
    SpellIconID,
    AlternateVerb,
    CanLink,
    'server' as source
FROM skillline
WHERE ID NOT IN (SELECT ID FROM skillline_dbc);
```

### 2. Trouver les doublons et différences
```sql
-- Trouver les IDs présents dans les deux tables avec des valeurs différentes
SELECT 
    s.ID,
    s.DisplayName as server_name,
    d.DisplayName as dbc_name,
    CASE 
        WHEN s.DisplayName != d.DisplayName THEN 'NOM DIFFERENT'
        ELSE 'IDENTIQUE'
    END as statut
FROM skillline s
INNER JOIN skillline_dbc d ON s.ID = d.ID
WHERE s.DisplayName != d.DisplayName
   OR s.CategoryID != d.CategoryID
   OR s.SkillCostID != d.SkillCostID;
```

### 3. Synchroniser les tables (si nécessaire)
```sql
-- Mettre à jour skillline avec les données de skillline_dbc
UPDATE skillline s
INNER JOIN skillline_dbc d ON s.ID = d.ID
SET 
    s.CategoryID = d.CategoryID,
    s.SkillCostID = d.SkillCostID,
    s.DisplayName = d.DisplayName,
    s.Description = d.Description,
    s.SpellIconID = d.SpellIconID,
    s.AlternateVerb = d.AlternateVerb,
    s.CanLink = d.CanLink;
```

### 4. Créer une table de référence unique
```sql
-- Créer une table propre qui contient les données finales
CREATE TABLE IF NOT EXISTS skillline_final AS
SELECT 
    COALESCE(s.ID, d.ID) as ID,
    -- Priorité aux données serveur si elles existent
    COALESCE(s.CategoryID, d.CategoryID) as CategoryID,
    COALESCE(s.SkillCostID, d.SkillCostID) as SkillCostID,
    COALESCE(s.DisplayName, d.DisplayName) as DisplayName,
    COALESCE(s.Description, d.Description) as Description,
    COALESCE(s.SpellIconID, d.SpellIconID) as SpellIconID,
    COALESCE(s.AlternateVerb, d.AlternateVerb) as AlternateVerb,
    COALESCE(s.CanLink, d.CanLink) as CanLink
FROM skillline s
LEFT JOIN skillline_dbc d ON s.ID = d.ID;
```

## Script Python pour analyser les deux tables

```python
import mysql.connector

def comparer_skillline():
    """Compare les tables skillline et skillline_dbc"""
    
    # Connexion à la base
    conn = mysql.connector.connect(
        host="localhost",
        user="votre_user",
        password="votre_password",
        database="acore_world"
    )
    cursor = conn.cursor(dictionary=True)
    
    # Lire les deux tables
    cursor.execute("SELECT * FROM skillline")
    skillline = {row['ID']: row for row in cursor.fetchall()}
    
    cursor.execute("SELECT * FROM skillline_dbc")
    skillline_dbc = {row['ID']: row for row in cursor.fetchall()}
    
    print(f"skillline: {len(skillline)} enregistrements")
    print(f"skillline_dbc: {len(skillline_dbc)} enregistrements")
    
    # Analyser les différences
    tous_ids = set(skillline.keys()) | set(skillline_dbc.keys())
    
    identiques = 0
    differents = 0
    seulement_skillline = []
    seulement_dbc = []
    
    for id in tous_ids:
        if id in skillline and id in skillline_dbc:
            # Comparer les enregistrements
            if skillline[id] == skillline_dbc[id]:
                identiques += 1
            else:
                differents += 1
                print(f"\nDifférence pour ID {id}:")
                for champ in skillline[id]:
                    if skillline[id][champ] != skillline_dbc[id].get(champ):
                        print(f"  {champ}: {skillline[id][champ]} vs {skillline_dbc[id].get(champ)}")
        elif id in skillline:
            seulement_skillline.append(id)
        else:
            seulement_dbc.append(id)
    
    print(f"\nRésumé:")
    print(f"  Identiques: {identiques}")
    print(f"  Différents: {differents}")
    print(f"  Seulement dans skillline: {len(seulement_skillline)}")
    print(f"  Seulement dans skillline_dbc: {len(seulement_dbc)}")
    
    cursor.close()
    conn.close()

# Exécuter
comparer_skillline()
```

## En résumé simple :

1. **`skillline_dbc`** = Copie exacte des données du client WoW (fichiers DBC)
2. **`skillline`** = Version utilisée par le serveur, peut être modifiée
3. **Le doublon est normal** : c'est le design d'AzerothCore
4. **Ne supprimez pas** ces tables sans comprendre leur usage
5. **Pour vos besoins** : utilisez `skillline` si vous voulez modifier, `skillline_dbc` comme référence

Quelle table devez-vous utiliser pour votre projet ? Ça dépend de ce que vous voulez faire :
- **Lecture seule** : utilisez `skillline_dbc` (données originales)
- **Modification** : utilisez `skillline` (données du serveur)
- **Comparaison** : utilisez les deux pour voir ce qui a été changé
4. **Plusieurs MPQ** = Plusieurs versions du même DBC
5. **Le problème** = Quand on lit tout, on trouve des lignes dupliquées ou modifiées
6. **La solution simple** = Garder la dernière version de chaque ligne (par ID)
7. **La solution avancée** = En plus, suivre ce qui a changé

La clé est l'**ID** : chaque ligne a un numéro unique. Si vous trouvez deux lignes avec le même ID, c'est la même donnée dans deux versions différentes. Il faut décider laquelle garder (généralement la dernière).
