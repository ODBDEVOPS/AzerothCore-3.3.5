# 🗺️ Cartographie des Liaisons DBC - World of Warcraft

![Version](https://img.shields.io/badge/Version-1.0-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![WoW](https://img.shields.io/badge/WoW-Retail%20%7C%20Classic%20%7C%20WotLK-orange)

## 📖 Description

Analyse exhaustive des liaisons, dépendances et hiérarchies entre les fichiers DBC (Database Client) de World of Warcraft. Cette cartographie couvre les relations fonctionnelles, les cardinalités et les cas particuliers.

## 🗂️ Structure du Projet

- **[📌 Tableau des Liaisons](docs/01-tableau-liaisons.md)** - Vue d'ensemble des relations
- **[🗺️ Schéma des Dépendances](docs/02-schema-dependances.md)** - Graphes et visualisations
- **[🔎 Analyse par Domaine](docs/03-analyse-domaines.md)** - Sorts, Items, Créatures, Zones
- **[⚠️ Cas Particuliers](docs/04-cas-particuliers.md)** - Edge cases et exceptions

## 🚀 Démarrage Rapide

### Visualiser le Schéma Mermaid

```bash
# Avec Mermaid CLI
npm install -g @mermaid-js/mermaid-cli
mmdc -i diagrams/dbc-dependencies.mmd -o images/schema.png
```
### Importer les Données CSV
```python
import pandas as pd

# Charger les liaisons
df = pd.read_csv('data/dbc-links.csv')
print(df.head())
```
