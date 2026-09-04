Parfait ! Je vais tout vous expliquer de A à Z, comme si vous n'aviez jamais utilisé GitHub de votre vie. Pas de panique, on va y aller très doucement ! 🎓

## 📚 **PARTIE 1 : COMPRENDRE LES BASES**

### **C'est quoi GitHub ?**
Imaginez GitHub comme un **Google Drive pour codeurs** :
- Vous stockez vos fichiers en ligne
- Vous pouvez revenir en arrière si erreur
- Plusieurs personnes peuvent travailler ensemble
- Des robots peuvent faire des tâches automatiquement

### **C'est quoi un MPQ ?**
C'est comme un **fichier ZIP** utilisé par World of Warcraft. Dedans, il y a les fichiers DBC (les données du jeu).

### **C'est quoi un DBC ?**
C'est un fichier qui contient les **données du jeu** (sorts, objets, quêtes...). Comme un tableau Excel mais en format spécial.

### **C'est quoi GitHub Actions ?**
C'est un **robot automatique** qui travaille pour vous sur les serveurs de GitHub. Vous lui dites quoi faire, il le fait tout seul.

---

## 🚀 **PARTIE 2 : CRÉER VOTRE PREMIER PROJET**

### **Étape 1 : Créer un compte GitHub**

1. Allez sur [github.com](https://github.com)
2. Cliquez sur **"Sign up"** (S'inscrire)
3. Remplissez :
   - Email : votre email
   - Password : un mot de passe
   - Username : votre pseudo
4. Vérifiez votre email
5. C'est fait ! 🎉

### **Étape 2 : Créer un nouveau projet (repository)**

1. Cliquez sur le **"+"** en haut à droite
2. Choisissez **"New repository"**

![Création repo](https://docs.github.com/assets/cb-20363/images/help/repository/repo-create.png)

3. Remplissez :
   - **Repository name** : `azerothcore-dbc` (ou ce que vous voulez)
   - **Description** : "Extraction des DBC de WoW 3.3.5"
   - **Public/Private** : Choisissez **Private** si c'est personnel
   - Cochez **"Add a README file"**
4. Cliquez sur **"Create repository"**

---

## 📁 **PARTIE 3 : CRÉER LES FICHIERS NÉCESSAIRES**

### **Étape 1 : Créer le dossier pour les MPQ**

1. Dans votre repo, cliquez sur **"Add file"** → **"Create new file"**
2. Dans le champ du nom, tapez : `mpq/README.md`
3. Dans le contenu, écrivez :
```markdown
# Dossier MPQ

Placez vos fichiers MPQ ici :
- common.MPQ
- common-2.MPQ
- expansion.MPQ
- lichking.MPQ
- patch.MPQ
- patch-2.MPQ
```
4. Cliquez sur **"Commit new file"** (bouton vert en bas)

### **Étape 2 : Créer le script d'extraction**

1. Cliquez sur **"Add file"** → **"Create new file"**
2. Nom du fichier : `tools/extract_dbc.py`
3. Copiez-collez ce code SIMPLIFIÉ :

```python
#!/usr/bin/env python3
"""
Script SIMPLE pour extraire les DBC des MPQ
Pour les débutants - AzerothCore 3.3.5
"""

import os
import hashlib
from pathlib import Path
import subprocess
import json

print("=" * 60)
print("🚀 DÉMARRAGE DE L'EXTRACTION DES FICHIERS DBC")
print("=" * 60)

# 1. Vérifier si le dossier MPQ existe
mpq_folder = Path("mpq")
if not mpq_folder.exists():
    print("❌ ERREUR : Le dossier 'mpq' n'existe pas !")
    print("👉 Créez un dossier 'mpq' et mettez vos fichiers MPQ dedans")
    exit(1)

# 2. Trouver tous les fichiers MPQ
mpq_files = list(mpq_folder.glob("*.MPQ")) + list(mpq_folder.glob("*.mpq"))

if not mpq_files:
    print("❌ ERREUR : Aucun fichier MPQ trouvé !")
    print("👉 Mettez vos fichiers MPQ dans le dossier 'mpq'")
    exit(1)

print(f"✅ {len(mpq_files)} fichiers MPQ trouvés :")
for mpq in mpq_files:
    print(f"   📦 {mpq.name}")

# 3. Créer le dossier de sortie
output_folder = Path("dbc_extracted")
output_folder.mkdir(exist_ok=True)

# 4. Extraire les DBC de chaque MPQ
all_dbc_files = []

for mpq_file in mpq_files:
    print(f"\n📂 Traitement de {mpq_file.name}...")
    
    # Créer un sous-dossier pour ce MPQ
    mpq_output = output_folder / mpq_file.stem
    mpq_output.mkdir(exist_ok=True)
    
    try:
        # Essayer d'extraire avec 7z
        result = subprocess.run(
            ["7z", "e", str(mpq_file), "*.dbc", f"-o{mpq_output}", "-y"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"   ✅ Extraction réussie pour {mpq_file.name}")
            
            # Compter les fichiers extraits
            extracted = list(mpq_output.glob("*.dbc"))
            print(f"   📊 {len(extracted)} fichiers DBC extraits")
            all_dbc_files.extend(extracted)
        else:
            print(f"   ⚠️ Problème avec {mpq_file.name}")
            print(f"   Erreur : {result.stderr[:200]}")
            
    except Exception as e:
        print(f"   ❌ Erreur : {str(e)}")

# 5. Vérifier les doublons
print("\n" + "=" * 60)
print("🔍 RECHERCHE DES DOUBLONS")
print("=" * 60)

file_hashes = {}
duplicates = []

for dbc_file in all_dbc_files:
    # Calculer le hash MD5 (empreinte unique du fichier)
    hash_md5 = hashlib.md5()
    with open(dbc_file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    file_hash = hash_md5.hexdigest()
    
    if file_hash in file_hashes:
        # C'est un doublon !
        print(f"   🔄 DOUBLON : {dbc_file.name}")
        print(f"      Original : {file_hashes[file_hash].name}")
        duplicates.append({
            "duplicate": str(dbc_file),
            "original": str(file_hashes[file_hash]),
            "hash": file_hash
        })
    else:
        file_hashes[file_hash] = dbc_file

# 6. Créer un rapport
print("\n" + "=" * 60)
print("📊 RÉSUMÉ FINAL")
print("=" * 60)
print(f"✅ Fichiers DBC uniques : {len(file_hashes)}")
print(f"🔄 Fichiers en double : {len(duplicates)}")

# 7. Sauvegarder le rapport
report = {
    "total_mpq": len(mpq_files),
    "total_dbc_unique": len(file_hashes),
    "total_duplicates": len(duplicates),
    "duplicates_list": duplicates
}

report_file = output_folder / "rapport_extraction.json"
with open(report_file, "w") as f:
    json.dump(report, f, indent=2)

print(f"\n📄 Rapport sauvegardé : {report_file}")
print("\n✅ EXTRACTION TERMINÉE !")
```

4. Cliquez sur **"Commit new file"**

---

## 🤖 **PARTIE 4 : CRÉER LE WORKFLOW GITHUB ACTIONS**

### **Étape 1 : Créer le fichier de workflow**

1. Cliquez sur **"Add file"** → **"Create new file"**
2. Nom du fichier : `.github/workflows/import-dbc.yml`
3. Copiez-collez ce code :

```yaml
name: Extraire les DBC des MPQ

# Quand lancer ce workflow ?
on:
  # Manuellement (bouton)
  workflow_dispatch:
    inputs:
      message:
        description: 'Message pour ce lancement'
        required: false
        default: 'Extraction manuelle'
  
  # Automatiquement quand on ajoute des MPQ
  push:
    paths:
      - 'mpq/**'

# Ce que le robot doit faire
jobs:
  extraction:
    runs-on: ubuntu-latest
    
    steps:
      # Étape 1 : Récupérer votre code
      - name: 📥 Récupérer le code
        uses: actions/checkout@v3
      
      # Étape 2 : Installer Python
      - name: 🐍 Installer Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      # Étape 3 : Installer 7zip
      - name: 📦 Installer 7zip
        run: |
          sudo apt-get update
          sudo apt-get install -y p7zip-full
      
      # Étape 4 : Vérifier les fichiers
      - name: 🔍 Vérifier les fichiers MPQ
        run: |
          echo "Fichiers dans le dossier mpq :"
          ls -la mpq/
          if [ ! -d "mpq" ] || [ -z "$(ls -A mpq/)" ]; then
            echo "⚠️ Aucun fichier MPQ trouvé !"
            exit 1
          fi
      
      # Étape 5 : Lancer l'extraction
      - name: 🚀 Extraire les DBC
        run: |
          python tools/extract_dbc.py
      
      # Étape 6 : Sauvegarder les résultats
      - name: 💾 Sauvegarder les DBC extraits
        uses: actions/upload-artifact@v3
        with:
          name: dbc-extraits
          path: dbc_extracted/
      
      # Étape 7 : Afficher le résumé
      - name: 📊 Afficher le rapport
        run: |
          if [ -f "dbc_extracted/rapport_extraction.json" ]; then
            cat dbc_extracted/rapport_extraction.json
          else
            echo "Pas de rapport trouvé"
          fi
```

4. Cliquez sur **"Commit new file"**

---

## 🎯 **PARTIE 5 : UTILISER VOTRE WORKFLOW**

### **Étape 1 : Ajouter vos fichiers MPQ**

**Méthode simple (pour les petits fichiers) :**

1. Cliquez sur le dossier `mpq`
2. Cliquez sur **"Add file"** → **"Upload files"**
3. Glissez-déposez vos fichiers MPQ
4. Cliquez sur **"Commit changes"**

**Méthode pour les gros fichiers (>25 Mo) :**

1. Installez [GitHub Desktop](https://desktop.github.com/)
2. Connectez votre compte
3. Clonez votre repository
4. Copiez les MPQ dans le dossier local
5. Faites un commit et push

### **Étape 2 : Lancer l'extraction**

**Méthode 1 : Automatique**
- Dès que vous ajoutez des MPQ, le workflow se lance tout seul !

**Méthode 2 : Manuelle**
1. Allez dans l'onglet **"Actions"** en haut
2. Cliquez sur **"Extraire les DBC des MPQ"**
3. Cliquez sur **"Run workflow"**
4. Cliquez sur le bouton vert **"Run workflow"**

### **Étape 3 : Voir les résultats**

1. Dans l'onglet **"Actions"**, cliquez sur le workflow en cours
2. Vous verrez les étapes s'exécuter en direct
3. Quand c'est fini (vert ✅) :
   - Cliquez sur le workflow terminé
   - En bas, dans **"Artifacts"**, téléchargez `dbc-extraits`

---

## 🛠️ **PARTIE 6 : DÉPANNAGE SIMPLE**

### **Problème 1 : "Aucun fichier MPQ trouvé"**

**Solution :**
- Vérifiez que vos fichiers sont bien dans le dossier `mpq/`
- Vérifiez l'extension : `.MPQ` ou `.mpq` (majuscules ou minuscules)

### **Problème 2 : Le workflow échoue**

**Solution :**
1. Cliquez sur le workflow qui a échoué
2. Lisez le message d'erreur en rouge
3. Prenez une capture d'écran
4. Cherchez l'erreur sur Google

### **Problème 3 : Fichiers trop gros**

**Solution :**
- Utilisez [Git LFS](https://git-lfs.com/) pour les gros fichiers
- Ou scindez vos MPQ en plus petits morceaux

---

## 📋 **PARTIE 7 : CHECKLIST RAPIDE**

✅ **Avant de commencer :**
- [ ] J'ai un compte GitHub
- [ ] J'ai créé un repository
- [ ] J'ai mes fichiers MPQ prêts

✅ **Fichiers à créer :**
- [ ] `mpq/README.md`
- [ ] `tools/extract_dbc.py`
- [ ] `.github/workflows/import-dbc.yml`

✅ **Après le lancement :**
- [ ] Le workflow est vert ✅
- [ ] J'ai téléchargé les artefacts
- [ ] J'ai vérifié le rapport des doublons

---

## 🎓 **PARTIE 8 : POUR ALLER PLUS LOIN**

### **Commandes Git de base (si vous utilisez Git en local)**

```bash
# Copier votre repo en local
git clone https://github.com/votre-pseudo/azerothcore-dbc.git

# Ajouter des fichiers
git add .
git commit -m "Ajout des MPQ"
git push

# Mettre à jour
git pull
```

### **Modifier le script pour vos besoins**

Dans `extract_dbc.py`, vous pouvez :
- Changer le nom du dossier de sortie
- Ajouter des filtres (ex: extraire seulement certains DBC)
- Modifier le format du rapport

---

## ❓ **QUESTIONS FRÉQUENTES**

**Q : C'est gratuit ?**
R : Oui ! Pour les projets publics, et même privés (avec limites).

**Q : Mes MPQ sont-ils en sécurité ?**
R : Si votre repo est privé, oui. En public, tout le monde peut les voir.

**Q : Puis-je supprimer les doublons automatiquement ?**
R : Oui, modifiez le script pour ajouter `os.remove(fichier_doublon)`.

**Q : Combien de temps ça prend ?**
R : Quelques minutes selon la taille des MPQ.

**Q : Puis-je traiter plusieurs MPQ en même temps ?**
R : Oui, le script les traite tous automatiquement.

---

## 🎯 **RÉSUMÉ VISUEL**

```
VOTRE PARCOURS :
1. Créer compte GitHub (5 min)
2. Créer repository (2 min)
3. Créer les 3 fichiers (10 min)
4. Ajouter les MPQ (5 min)
5. Lancer le workflow (1 min)
6. Récupérer les résultats (2 min)
```

**TOTAL : ~25 minutes pour la première fois !**

---

Est-ce que c'est plus clair maintenant ? Voulez-vous que je vous guide sur une étape en particulier ? Dites-moi où vous en êtes et je vous aide ! 😊
