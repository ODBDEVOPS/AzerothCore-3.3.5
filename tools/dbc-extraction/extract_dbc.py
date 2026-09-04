#!/usr/bin/env python3
"""
🎮 Script d'extraction DBC pour AzerothCore 3.3.5
📝 Adapté au repository ODBDEVOPS/AzerothCore-3.3.5
"""

import os
import hashlib
from pathlib import Path
import subprocess
import json
from datetime import datetime
import shutil

# ============================================
# CONFIGURATION
# ============================================
MPQ_FOLDER = Path("mpq")                    # Dossier des MPQ
OUTPUT_FOLDER = Path("resultats_dbc")       # Dossier de sortie
RAW_FOLDER = OUTPUT_FOLDER / "bruts"        # DBC bruts extraits
UNIQUE_FOLDER = OUTPUT_FOLDER / "uniques"   # DBC uniques
DOUBLONS_FOLDER = OUTPUT_FOLDER / "doublons" # DBC en double

# Liste des DBC importants pour AzerothCore
DBC_IMPORTANTS = [
    "Achievement.dbc",
    "AreaTable.dbc",
    "CreatureDisplayInfo.dbc",
    "CreatureFamily.dbc",
    "Faction.dbc",
    "FactionTemplate.dbc",
    "Item.dbc",
    "ItemDisplayInfo.dbc",
    "Map.dbc",
    "Quest.dbc",
    "SkillLine.dbc",
    "SkillLineAbility.dbc",
    "SoundEntries.dbc",
    "Spell.dbc",
    "SpellIcon.dbc",
    "TaxiNodes.dbc",
    "WorldMapArea.dbc",
    "WorldSafeLocs.dbc"
]

# ============================================
# FONCTIONS UTILITAIRES
# ============================================
def afficher_titre(message):
    """Affiche un titre formaté"""
    print("\n" + "=" * 60)
    print(f"  {message}")
    print("=" * 60)

def calculer_hash(fichier):
    """Calcule le hash MD5 d'un fichier"""
    hash_md5 = hashlib.md5()
    try:
        with open(fichier, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"⚠️ Erreur hash {fichier.name}: {e}")
        return None

def copier_fichier(source, destination):
    """Copie un fichier avec gestion des noms en double"""
    if not destination.exists():
        shutil.copy2(source, destination)
        return destination
    
    # Si le fichier existe déjà, ajouter un suffixe
    compteur = 1
    while True:
        nouveau_nom = f"{destination.stem}_{compteur}{destination.suffix}"
        nouveau_dest = destination.parent / nouveau_nom
        if not nouveau_dest.exists():
            shutil.copy2(source, nouveau_dest)
            return nouveau_dest
        compteur += 1

# ============================================
# ÉTAPE 1 : VÉRIFICATION DES MPQ
# ============================================
afficher_titre("📦 ÉTAPE 1 : RECHERCHE DES FICHIERS MPQ")

if not MPQ_FOLDER.exists():
    print("❌ ERREUR : Le dossier 'mpq' n'existe pas !")
    print("👉 Créez le dossier 'mpq' à la racine de votre repo")
    exit(1)

# Trouver tous les fichiers MPQ
mpq_files = []
for extension in ["*.MPQ", "*.mpq", "*.MPQ.part", "*.mpq.part"]:
    mpq_files.extend(list(MPQ_FOLDER.glob(extension)))

# Filtrer les fichiers .part (upload incomplet)
mpq_files = [f for f in mpq_files if not f.name.endswith('.part')]

if not mpq_files:
    print("❌ ERREUR : Aucun fichier MPQ trouvé dans 'mpq/'")
    print("👉 Uploadez vos fichiers MPQ (common.MPQ, expansion.MPQ, etc.)")
    exit(1)

print(f"✅ {len(mpq_files)} fichier(s) MPQ trouvé(s) :")
for mpq in mpq_files:
    taille_mo = mpq.stat().st_size / (1024 * 1024)
    print(f"   📦 {mpq.name} ({taille_mo:.1f} Mo)")

# ============================================
# ÉTAPE 2 : CRÉATION DES DOSSIERS
# ============================================
afficher_titre("📂 ÉTAPE 2 : CRÉATION DES DOSSIERS")

for dossier in [OUTPUT_FOLDER, RAW_FOLDER, UNIQUE_FOLDER, DOUBLONS_FOLDER]:
    dossier.mkdir(exist_ok=True, parents=True)
    print(f"   ✅ {dossier}")

# ============================================
# ÉTAPE 3 : EXTRACTION DES DBC
# ============================================
afficher_titre("🔧 ÉTAPE 3 : EXTRACTION DES DBC")

total_extraits = 0
log_extraction = []

for mpq_file in mpq_files:
    print(f"\n   📦 Traitement de {mpq_file.name}...")
    
    # Dossier pour ce MPQ
    mpq_output = RAW_FOLDER / mpq_file.stem.replace('.', '_')
    mpq_output.mkdir(exist_ok=True, parents=True)
    
    try:
        # Commande 7z pour extraire les DBC
        commande = [
            "7z", "e",           # extraire
            str(mpq_file),       # depuis ce MPQ
            "*.dbc",             # seulement les fichiers DBC
            f"-o{mpq_output}",   # vers ce dossier
            "-y",                # répondre oui à tout
            "-bso0", "-bsp0"     # silence
        ]
        
        print(f"   🔄 Extraction en cours...")
        resultat = subprocess.run(
            commande,
            capture_output=True,
            text=True,
            timeout=600  # 10 minutes max
        )
        
        if resultat.returncode == 0:
            fichiers_extraits = list(mpq_output.glob("*.dbc"))
            nb_extraits = len(fichiers_extraits)
            total_extraits += nb_extraits
            
            print(f"   ✅ {nb_extraits} fichiers DBC extraits")
            
            log_extraction.append({
                "mpq": mpq_file.name,
                "fichiers_extraits": nb_extraits,
                "statut": "succes"
            })
        else:
            print(f"   ⚠️ Erreur avec {mpq_file.name}")
            print(f"   Message : {resultat.stderr[:200]}")
            
            log_extraction.append({
                "mpq": mpq_file.name,
                "fichiers_extraits": 0,
                "statut": "echec",
                "erreur": resultat.stderr[:200]
            })
            
    except subprocess.TimeoutExpired:
        print(f"   ⏰ Timeout pour {mpq_file.name} (trop long)")
        log_extraction.append({
            "mpq": mpq_file.name,
            "statut": "timeout"
        })
    except Exception as e:
        print(f"   ❌ Erreur : {str(e)}")
        log_extraction.append({
            "mpq": mpq_file.name,
            "statut": "erreur",
            "erreur": str(e)
        })

print(f"\n   📊 Total extraits : {total_extraits} fichiers DBC")

# ============================================
# ÉTAPE 4 : DÉTECTION DES DOUBLONS
# ============================================
afficher_titre("🔍 ÉTAPE 4 : DÉTECTION DES DOUBLONS")

tous_les_dbc = list(RAW_FOLDER.rglob("*.dbc"))
print(f"   📄 {len(tous_les_dbc)} fichiers DBC à analyser")

hash_des_fichiers = {}
liste_doublons = []
fichiers_uniques = []
dbc_importants_trouves = []

for dbc_file in tous_les_dbc:
    file_hash = calculer_hash(dbc_file)
    
    if file_hash is None:
        continue
    
    # Vérifier si c'est un DBC important
    if dbc_file.name in DBC_IMPORTANTS:
        dbc_importants_trouves.append(dbc_file.name)
    
    if file_hash in hash_des_fichiers:
        # C'est un doublon !
        print(f"   🔄 Doublon : {dbc_file.name}")
        print(f"      → Original : {hash_des_fichiers[file_hash].name}")
        
        # Copier vers le dossier doublons
        copier_fichier(dbc_file, DOUBLONS_FOLDER / dbc_file.name)
        
        liste_doublons.append({
            "fichier": dbc_file.name,
            "source": str(dbc_file),
            "original": str(hash_des_fichiers[file_hash]),
            "hash": file_hash
        })
    else:
        # C'est unique
        hash_des_fichiers[file_hash] = dbc_file
        fichiers_uniques.append(dbc_file)
        
        # Copier vers le dossier uniques
        copier_fichier(dbc_file, UNIQUE_FOLDER / dbc_file.name)

print(f"\n   ✅ Fichiers uniques : {len(fichiers_uniques)}")
print(f"   🔄 Doublons trouvés : {len(liste_doublons)}")
print(f"   ⭐ DBC importants trouvés : {len(set(dbc_importants_trouves))}/{len(DBC_IMPORTANTS)}")

# ============================================
# ÉTAPE 5 : CRÉATION DU RAPPORT
# ============================================
afficher_titre("📊 ÉTAPE 5 : CRÉATION DU RAPPORT")

rapport = {
    "date_extraction": datetime.now().isoformat(),
    "repository": "ODBDEVOPS/AzerothCore-3.3.5",
    "fichiers_mpq": [mpq.name for mpq in mpq_files],
    "total_extraits": total_extraits,
    "total_uniques": len(fichiers_uniques),
    "total_doublons": len(liste_doublons),
    "dbc_importants": {
        "trouves": len(set(dbc_importants_trouves)),
        "total": len(DBC_IMPORTANTS),
        "liste": sorted(set(dbc_importants_trouves))
    },
    "details_extraction": log_extraction,
    "liste_doublons": liste_doublons,
    "liste_fichiers_uniques": sorted([f.name for f in fichiers_uniques])
}

# Sauvegarder en JSON
rapport_json = OUTPUT_FOLDER / "rapport_extraction.json"
with open(rapport_json, "w", encoding="utf-8") as f:
    json.dump(rapport, f, indent=2, ensure_ascii=False)

# Sauvegarder en texte lisible
rapport_txt = OUTPUT_FOLDER / "rapport_extraction.txt"
with open(rapport_txt, "w", encoding="utf-8") as f:
    f.write("=" * 60 + "\n")
    f.write("RAPPORT D'EXTRACTION DBC - AZEROTHCORE 3.3.5\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"Date : {rapport['date_extraction']}\n")
    f.write(f"Repository : {rapport['repository']}\n\n")
    
    f.write("FICHIERS MPQ TRAITÉS :\n")
    for mpq in mpq_files:
        f.write(f"  • {mpq.name}\n")
    
    f.write(f"\nSTATISTIQUES :\n")
    f.write(f"  • Total extraits : {total_extraits}\n")
    f.write(f"  • Fichiers uniques : {len(fichiers_uniques)}\n")
    f.write(f"  • Doublons : {len(liste_doublons)}\n")
    
    f.write(f"\nDBC IMPORTANTS :\n")
    f.write(f"  • Trouvés : {len(set(dbc_importants_trouves))}/{len(DBC_IMPORTANTS)}\n")
    for dbc in sorted(set(dbc_importants_trouves)):
        f.write(f"    ✓ {dbc}\n")
    
    if liste_doublons:
        f.write(f"\nLISTE DES DOUBLONS :\n")
        f.write("-" * 40 + "\n")
        for d in liste_doublons:
            f.write(f"  • {d['fichier']}\n")

print(f"   ✅ Rapport JSON : {rapport_json}")
print(f"   ✅ Rapport texte : {rapport_txt}")

# ============================================
# RÉSUMÉ FINAL
# ============================================
afficher_titre("🎉 EXTRACTION TERMINÉE !")

print(f"""
📊 RÉSUMÉ :
  • MPQ traités : {len(mpq_files)}
  • DBC extraits : {total_extraits}
  • Fichiers uniques : {len(fichiers_uniques)}
  • Doublons : {len(liste_doublons)}
  
📂 RÉSULTATS :
  • DBC uniques : {UNIQUE_FOLDER}/
  • DBC doublons : {DOUBLONS_FOLDER}/
  • Rapports : {OUTPUT_FOLDER}/
  
🎯 PROCHAINE ÉTAPE :
  • Téléchargez les DBC depuis l'onglet Actions
  • Ou utilisez-les pour votre base de données
""")
